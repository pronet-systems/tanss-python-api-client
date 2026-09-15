"""Die drei Token-Ablaeufe der Schnittstelle: anmelden, erneuern, fuer ein externes Programm praegen."""

from __future__ import annotations

import json
import logging
from dataclasses import dataclass, replace
from datetime import datetime, timedelta, timezone
from typing import Any
from urllib.parse import quote

import httpx

from .errors import TanssApiError
from .tokens import API_TOKEN_HEADER, MutableTokenProvider, TokenProvider, bearer_header_value

_logger = logging.getLogger(__name__)

LOGIN_PATH = "/api/v1/user/login"
"""Der gemessene Anmeldepfad: ``POST /api/v1/user/login`` mit den Zugangsdaten in Kopfzeilen (gegen
TANSS 10.10 gemessen).

Auf einer 10.10-Instanz ist die Anmeldung kein Handler, sondern eine vorgeschaltete Pruefung auf
diesem Pfad. Sie nimmt Zugangsdaten ausschliesslich aus Kopfzeilen und akzeptiert ``user`` +
``password``, ``user`` + ``logintoken`` oder ``dbapikey``. Der dokumentierte Pfad
:data:`DOCUMENTED_LOGIN_PATH` antwortet dort mit 404.
"""

DOCUMENTED_LOGIN_PATH = "/api/v1/login"
"""Der Anmeldepfad, wie ihn die Schnittstellenbeschreibung fuehrt: ``POST /api/v1/login`` mit dem Rumpf
``TnsLoginCredentials``.

Auf 10.10 gibt es ihn nicht - gemessen 404. :meth:`TanssSession.login` weicht deshalb erst nach einer
404 auf :data:`LOGIN_PATH` hierher aus; neuere Fassungen bedienen ihn.
"""

USER_HEADER = "user"
"""Die Kopfzeile mit dem Anmeldenamen (gegen TANSS 10.10 gemessen)."""

PASSWORD_HEADER = "password"
"""Die Kopfzeile mit dem Kennwort (gegen TANSS 10.10 gemessen)."""

LOGIN_TOKEN_HEADER = "logintoken"
"""Die Kopfzeile mit dem anwendungsspezifischen Anmeldetoken; sie tritt an die Stelle von
:data:`PASSWORD_HEADER` (gegen TANSS 10.10 gemessen)."""

DASHBOARD_KEY_HEADER = "dbapikey"
"""Die Kopfzeile des dritten Anmeldewegs: der Dashboard-Schluessel, der Benutzername **und** Kennwort
ersetzt (gegen TANSS 10.10 gemessen).

Traegt eine Anmeldeanfrage **nur** diese Kopfzeile, nimmt der Server ausschliesslich diesen Zweig;
:meth:`TanssSession.login_with_dashboard_key` schickt genau das.
"""

REFRESH_TOKEN_HEADER = "refreshToken"
"""Die Kopfzeile, in der das Erneuerungstoken reist (gegen TANSS 10.10 gemessen).

Die Schreibweise ist gleichgueltig: Gemessen antworten ``refreshToken``, ``refreshtoken`` und
``RefreshToken`` gleichermassen mit 200 - HTTP-Kopfzeilen sind unabhaengig von Gross- und
Kleinschreibung. Geschickt wird die Schreibweise der Messung.
"""

REFRESH_PATH = "/api/v1/employees/ownState"
"""Der Pfad, ueber den :meth:`TanssSession.refresh` erneuert.

Erneuert wird laut Dokumentation ueber jede Route ausser den beiden Anmeldepfaden, und gemessen ist
genau das: Das Erneuerungstoken in der Kopfzeile :data:`REFRESH_TOKEN_HEADER` auf einer beliebigen
Nicht-Anmelderoute liefert ein volles Anmeldeergebnis (gegen TANSS 10.10 gemessen). Gewaehlt ist eine
kleine lesende Route mit der Rolle ``USER``, die sowohl dokumentiert ist als auch auf 10.10 wirklich
existiert und auf dem Server nichts hinterlaesst.
"""

MINT_PATH = "/api/v1/jwts"
"""Der Pfad des Praegens ohne den Programmnamen: ``/api/v1/jwts/{ext_program}``."""


def _text_of(owner: Any, name: str) -> str | None:
    """Der Wert eines Feldes, wenn es eine Zeichenkette ist; sonst ``None``."""
    if isinstance(owner, dict):
        value = owner.get(name)
        if isinstance(value, str):
            return value
    return None


def _number_of(owner: Any, name: str) -> int:
    """Der Wert eines Feldes als ganze Zahl; 0, wenn es fehlt oder keine Zahl ist."""
    if isinstance(owner, dict):
        value = owner.get(name)
        if isinstance(value, bool):
            return 0
        if isinstance(value, (int, float)):
            return int(value)
    return 0


def encode_credential_header(value: str, parameter_name: str) -> bytes:
    """Bringt eine Zugangsangabe in die Form, in der der Server sie erwartet: als UTF-8-Bytes.

    **Vom Server so umgesetzt, gegen 10.10 geprueft:** Der Server liest jede Zugangsdaten-Kopfzeile -
    ``user``, ``password``, ``logintoken``, ``dbapikey`` -, nimmt deren **ISO-8859-1-Bytes** und
    dekodiert sie als **UTF-8**. Der Server rechnet also damit, dass auf der Leitung UTF-8 steht,
    obwohl HTTP-Kopfzeilen byteweise als Latin-1 gelesen werden.

    **Folge fuer einen Python-Client:** httpx kodiert einen Kopfzeilenwert, der als ``str`` uebergeben
    wird, als ASCII und weist alles darueber ab. Ein Wert, der schon als ``bytes`` uebergeben wird,
    geht dagegen Byte fuer Byte auf die Leitung. Diese Funktion liefert deshalb
    ``value.encode("utf-8")``: Aus ``ae`` (U+00E4) werden die Bytes ``C3 A4``, und genau die rechnet
    der Server zurueck. Ein Kennwort mit Umlauten kommt so unveraendert an.

    **Das Eurozeichen laesst sich nicht uebertragen.** Der Server ersetzt nach dem Dekodieren jedes
    ``EUR``-Zeichen (U+20AC) durch U+0080 - das Byte, unter dem Windows-1252 das Eurozeichen fuehrt.
    Ein Kennwort damit kommt also selbst bei richtiger Kodierung veraendert an; es taugt fuer diese
    Anmeldung nicht.

    :param value: Die Zugangsangabe, wie der Aufrufer sie kennt.
    :param parameter_name: Der Name des Parameters, fuer die Fehlermeldung.
    :raises ValueError: Der Wert traegt ein Steuerzeichen. HTTP-Kopfzeilen koennen keines tragen; hier
        wird es gemeldet, solange noch zu sehen ist, welche Angabe gemeint war.
    """
    for character in value:
        if character < " " or character == "\x7f":
            raise ValueError(
                f"Die Zugangsangabe {parameter_name} enthaelt das Steuerzeichen "
                f"U+{ord(character):04X} und kann deshalb nicht als HTTP-Kopfzeile uebertragen "
                "werden. TANSS nimmt Zugangsdaten ausschliesslich in Kopfzeilen entgegen (gegen "
                "TANSS 10.10 gemessen)."
            )

    return value.encode("utf-8")


@dataclass(frozen=True, slots=True)
class TanssLoginResult:
    """Das Ergebnis einer Anmeldung: Sitzungs- und Erneuerungstoken samt Mitarbeiter und Ablauf.

    **Nachgebildet, nicht abgeleitet.** Die Schnittstellenbeschreibung gibt der 200-Antwort der
    Anmeldung kein Schema, sondern nur ein Beispiel: ``meta.text`` und darunter ``content`` mit
    ``employeeId``, ``apiKey``, ``expire``, ``refresh`` und ``employeeType``.

    **Gegen TANSS 10.10 gemessen** antwortet eine Instanz mit genau diesem Umschlag und **einem Feld
    mehr**: ``content.warning``. Es steht in keinem Beispiel der Schnittstellenbeschreibung und ist
    hier als :attr:`warning` aufgenommen. Beide Token tragen das Praefix ``Bearer`` schon im Wert.

    **Der Statuscode taugt nicht zur Fehlererkennung** (gegen TANSS 10.10 gemessen): Eine
    fehlgeschlagene Anmeldung antwortet ebenfalls mit HTTP 200 - entweder mit ``meta.text`` =
    ``Unsuccesful login attempt`` und ``content.detailMessage`` =
    ``LOGIN_ERROR_INVALID_USERNAME_OR_PASSWORD`` oder, bei einer Anfrage ohne die erwarteten
    Kopfzeilen, mit einem **leeren** Rumpf. Massgeblich ist deshalb allein, ob ``content.apiKey``
    vorhanden ist; :meth:`parse` wirft sonst einen :class:`tanss_api.errors.TanssApiError` mit dem Code
    aus ``content.detailMessage`` beziehungsweise :attr:`EMPTY_RESPONSE_CODE`.
    """

    employee_id: int
    """Die Mitarbeiter-Id aus ``content.employeeId`` - der Wert fuer ``loggedInUserId``."""

    api_key: str
    """Das Sitzungstoken aus ``content.apiKey``, einschliesslich ``Bearer``; vier Stunden gueltig."""

    expire: int
    """Der Ablauf aus ``content.expire`` als Unix-Zeit in Sekunden."""

    refresh: str
    """Das Erneuerungstoken aus ``content.refresh``; fuenf Tage gueltig."""

    employee_type: str | None = None
    """Die Art des Kontos aus ``content.employeeType``, gemessen ``COMPANY_ADMIN``."""

    warning: str | None = None
    """Der Warnhinweis aus ``content.warning`` - gegen TANSS 10.10 gemessen, in der
    Schnittstellenbeschreibung nicht beschrieben; ``None``, wenn die Instanz keinen mitschickt."""

    login_path: str | None = None
    """Der Pfad, ueber den diese Anmeldung zustande kam: :data:`LOGIN_PATH` (der gemessene Weg mit
    Kopfzeilen) oder :data:`DOCUMENTED_LOGIN_PATH` (der dokumentierte Weg mit JSON-Rumpf, auf den die
    Sitzung nach einer 404 ausweicht). :meth:`parse` laesst das Feld ``None``; gesetzt wird es von
    :meth:`TanssSession.login`. Nach einer Erneuerung bleibt es ``None``."""

    EMPTY_RESPONSE_CODE = "LOGIN_EMPTY_RESPONSE"
    """Der Code, unter dem eine Anmeldung mit **leerem** Rumpf gemeldet wird.

    TANSS 10.10 beantwortet eine Anmeldeanfrage ohne die erwarteten Kopfzeilen mit HTTP 200 und ohne
    jeden Inhalt (gegen TANSS 10.10 gemessen). Der Wert stammt nicht von TANSS, sondern ist die Kennung
    dieser Bibliothek fuer genau diesen Fall.
    """

    @property
    def expires_at(self) -> datetime:
        """Der Ablauf als Zeitpunkt (UTC), abgeleitet aus :attr:`expire` (Unix-Sekunden)."""
        return datetime.fromtimestamp(self.expire, tz=timezone.utc)

    @classmethod
    def parse(cls, body: str) -> "TanssLoginResult":
        """Liest die Antwort einer Anmeldung oder Erneuerung - den Umschlag ``{ meta, content }``.

        **Erfolg heisst: ``content.apiKey`` ist da.** Der Statuscode sagt nichts (gegen TANSS 10.10
        gemessen); fehlt der Schluessel, wirft diese Methode einen
        :class:`tanss_api.errors.TanssApiError`, dessen ``error_code`` der gemessene Wert aus
        ``content.detailMessage`` ist (etwa ``LOGIN_ERROR_INVALID_USERNAME_OR_PASSWORD``) und dessen
        Meldung ``meta.text`` traegt. Ist der Rumpf leer, ist der Code :attr:`EMPTY_RESPONSE_CODE`.

        :param body: Der Rumpf der Antwort.
        :raises tanss_api.errors.TanssApiError: Der Rumpf ist leer, kein JSON-Objekt oder traegt kein
            ``content.apiKey``.
        """
        if body is None:
            raise TypeError("Der Rumpf darf nicht None sein.")

        if not body.strip():
            raise cls._empty(body)

        try:
            root = json.loads(body)
        except ValueError as cause:
            raise TanssApiError(
                "Die Antwort auf die Anmeldung war kein JSON. Erwartet wird der Umschlag "
                "{ meta, content } mit apiKey, refresh, expire und employeeId.",
                raw_body=body,
            ) from cause

        content = root.get("content") if isinstance(root, dict) else None
        api_key = _text_of(content, "apiKey")
        if not api_key:
            raise cls._rejected(body, root, content)

        return cls(
            employee_id=_number_of(content, "employeeId"),
            api_key=api_key,
            expire=_number_of(content, "expire"),
            refresh=_text_of(content, "refresh") or "",
            employee_type=_text_of(content, "employeeType"),
            warning=_text_of(content, "warning"),
        )

    @classmethod
    def _empty(cls, body: str) -> TanssApiError:
        return TanssApiError(
            "Die Anmeldung kam mit leerem Rumpf und HTTP 200 zurueck. So beantwortet TANSS 10.10 eine "
            "Anmeldeanfrage, die die Zugangsdaten nicht in den Kopfzeilen user/password "
            "beziehungsweise user/logintoken traegt (gegen TANSS 10.10 gemessen).",
            status_code=200,
            error_code=cls.EMPTY_RESPONSE_CODE,
            raw_body=body,
        )

    @classmethod
    def _rejected(cls, body: str, root: Any, content: Any) -> TanssApiError:
        code = _text_of(content, "detailMessage")
        meta = _text_of(root.get("meta"), "text") if isinstance(root, dict) else None
        message = meta or (
            "Die Antwort auf die Anmeldung trug kein content.apiKey und damit kein Token (gegen "
            "TANSS 10.10 gemessen)."
        )
        return TanssApiError(
            message,
            status_code=200,
            error_code=code,
            localized_text=meta,
            raw_body=body,
        )


class TanssSession:
    """Anmelden, erneuern, praegen.

    Die Sitzung schickt ihre Anfragen ueber denselben ``httpx.AsyncClient`` wie der erzeugte Client -
    mit derselben Basisadresse, derselben Zeitgrenze, demselben Proxy, derselben TLS-Einstellung,
    derselben ``loggedInUserId``-Regel und derselben Wiederholungsregel. Die Kopfzeilen setzt sie
    allerdings selbst, weil jeder der drei Ablaeufe andere braucht: die Anmeldung die Zugangsdaten
    (``user``/``password`` oder ``dbapikey``), die Erneuerung ``refreshToken`` und **kein**
    ``apiToken``, das Praegen das Sitzungstoken in ``apiToken``.

    **Drei Anmeldewege, ein Filter.** Hinter :data:`LOGIN_PATH` steht kein Handler, sondern die
    Anmeldepruefung des Servers. Sie nimmt ``user`` + ``password``, ``user`` + ``logintoken`` (beides
    :meth:`login`) oder allein ``dbapikey`` (:meth:`login_with_dashboard_key`). Alle Zugangsdaten
    reisen in Kopfzeilen, und zwar in der Kodierung, die :func:`encode_credential_header` beschreibt.

    **Anmeldung und Erneuerung tragen nie das Token des Anbieters.** Die Anmeldung ist mit
    ``security: []`` ausgewiesen, und die Erneuerung schlaegt mit gesetztem ``apiToken`` gemessen fehl
    (gegen TANSS 10.10 gemessen). Der Token-Anbieter wird fuer beide gar nicht erst gefragt.

    **Die Anmeldung wird nicht wiederholt.** Sie ist ein ``POST``, und die Wiederholungsregel der
    Bibliothek laesst nur ``GET`` in die Wiederholung nach 429, 503 und 504.

    Der erzeugte Client taugt fuer diese drei Ablaeufe nicht: Die 200-Antwort der Anmeldung hat kein
    Schema, sondern nur ein Beispiel - es gaebe also nichts zu typisieren -, und den gemessenen Weg
    ``POST /api/v1/user/login`` kennt die Schnittstellenbeschreibung ueberhaupt nicht.
    """

    __slots__ = ("_base_url", "_http", "_tokens")

    def __init__(
        self,
        http: httpx.AsyncClient,
        tokens: TokenProvider | None = None,
        base_url: str | None = None,
    ) -> None:
        """Baut die Sitzung auf einer fertigen Verbindungsschicht.

        :param http: Der Client, den :meth:`tanss_api.api.TanssApi.create` gebaut hat: mit
            Basisadresse, Zeitgrenze, Proxy und der Middleware-Kette.
        :param tokens: Der Token-Anbieter. Ein :class:`tanss_api.tokens.MutableTokenProvider` bekommt
            nach Anmeldung und Erneuerung den neuen ``apiKey`` eingetragen; jeder andere Anbieter
            bleibt unberuehrt. Gefragt wird er nur beim Praegen.
        :param base_url: Die Basisadresse; ohne Angabe die des Clients.
        :raises ValueError: Weder der Client noch der Aufrufer nennen eine Basisadresse.
        """
        # httpx.URL ist auch leer immer wahr; gefragt ist die Zeichenkette.
        address = (base_url or str(http.base_url)).strip().rstrip("/")
        if not address:
            raise ValueError(
                "Die Sitzung braucht eine Basisadresse; TanssApi.create setzt sie auf dem "
                "httpx.AsyncClient."
            )

        self._base_url = address
        self._http = http
        self._tokens = tokens

    async def login(
        self,
        username: str,
        password: str | None = None,
        login_token: str | None = None,
    ) -> TanssLoginResult:
        """Meldet einen Benutzer an und liefert das Paar aus Sitzungs- und Erneuerungstoken.

        **Der Weg ist gemessen** (gegen TANSS 10.10): ``POST`` auf :data:`LOGIN_PATH` **ohne Rumpf**,
        die Zugangsdaten in den Kopfzeilen ``user`` und ``password``. Ist ``login_token`` gesetzt,
        tritt ``logintoken`` an die Stelle des Kennworts: Der Server nimmt ``user`` + ``password``,
        ``user`` + ``logintoken`` oder ``dbapikey`` - sonst nichts. Ein JSON-Rumpf ohne Kopfzeilen
        fuehrt gemessen zu HTTP 200 mit leerem Inhalt.

        **Ausweichweg.** Antwortet :data:`LOGIN_PATH` mit 404 - auf 10.10 tut er das nicht, auf einer
        kuenftigen Fassung womoeglich -, wiederholt diese Methode die Anmeldung auf dem dokumentierten
        :data:`DOCUMENTED_LOGIN_PATH` mit dem Rumpf ``TnsLoginCredentials`` (genau drei Felder:
        ``username``, ``password``, ``token``). Welcher Weg getragen hat, steht danach in
        :attr:`TanssLoginResult.login_path`.

        **Erfolg erkennt man nicht am Statuscode** (gegen TANSS 10.10 gemessen): Eine falsche
        Zugangsangabe antwortet mit HTTP 200 und ``content.detailMessage`` =
        ``LOGIN_ERROR_INVALID_USERNAME_OR_PASSWORD``, eine unvollstaendige Anfrage mit HTTP 200 und
        leerem Rumpf. Massgeblich ist ``content.apiKey``; fehlt es, wirft
        :meth:`TanssLoginResult.parse` einen :class:`tanss_api.errors.TanssApiError` mit diesem Code
        beziehungsweise mit :attr:`TanssLoginResult.EMPTY_RESPONSE_CODE`.

        **Ohne ``apiToken``.** Die Operation traegt ``security: []``; der Token-Anbieter wird hier nicht
        gefragt. War ein :class:`tanss_api.tokens.MutableTokenProvider` uebergeben, steht danach
        :attr:`TanssLoginResult.api_key` darin, und alle Clients daran arbeiten ohne Neubau weiter.

        Die Antwort traegt zwei Token: ``content.apiKey`` (vier Stunden) und ``content.refresh`` (fuenf
        Tage), beide mit dem Praefix ``Bearer``. Zusaetzlich gilt laut Dokumentation eine Leerlaufgrenze
        von zwei Minuten.

        **Umlaute.** Name, Kennwort und Anmeldetoken gehen als UTF-8-Bytes hinaus, siehe
        :func:`encode_credential_header`. Der dokumentierte Ausweichweg schickt sie unveraendert, denn
        sein Rumpf ist JSON und damit ohnehin UTF-8.

        :param username: Der Anmeldename; geht als Kopfzeile ``user`` hinaus.
        :param password: Das Kennwort; geht als Kopfzeile ``password`` hinaus. Ist ``login_token``
            gesetzt, bleibt diese Kopfzeile weg, und der Wert wird nur noch fuer den dokumentierten
            Ausweichweg gebraucht.
        :param login_token: Das anwendungsspezifische Anmeldetoken (zweiter Faktor) fuer die Kopfzeile
            ``logintoken``; ``None``, wenn mit Kennwort angemeldet wird.
        :raises ValueError: Weder Kennwort noch Anmeldetoken sind angegeben, oder eine der Angaben
            traegt ein Steuerzeichen.
        :raises tanss_api.errors.TanssApiError: Die Antwort trug kein ``content.apiKey`` (abgelehnte
            oder unvollstaendige Anmeldung), oder TANSS hat mit einem Fehlerstatus geantwortet.
        """
        if username is None:
            raise TypeError("Der Anmeldename darf nicht None sein.")
        if password is None and login_token is None:
            raise ValueError(
                "Die Anmeldung braucht ein Kennwort oder ein Anmeldetoken: Der Server nimmt "
                "user+password, user+logintoken oder dbapikey (gegen TANSS 10.10 gemessen)."
            )

        # Kein Rumpf, Zugangsdaten ausschliesslich in Kopfzeilen, und entweder password oder
        # logintoken - nie beides.
        headers: dict[str, bytes] = {USER_HEADER: encode_credential_header(username, "username")}
        if login_token is None:
            headers[PASSWORD_HEADER] = encode_credential_header(password or "", "password")
        else:
            headers[LOGIN_TOKEN_HEADER] = encode_credential_header(login_token, "login_token")

        path = LOGIN_PATH
        status, body = await self._send("POST", LOGIN_PATH, headers=headers)

        if status == 404:
            # Der gemessene Weg fehlt: dann die dokumentierte Route mit dem JSON-Rumpf.
            path = DOCUMENTED_LOGIN_PATH
            status, body = await self._send(
                "POST",
                DOCUMENTED_LOGIN_PATH,
                json_body={
                    "username": username,
                    "password": password or "",
                    "token": login_token or "",
                },
            )

        if status < 200 or status >= 300:
            raise TanssApiError.from_response(status, body)

        result = replace(TanssLoginResult.parse(body), login_path=path)
        self._store(result)
        _logger.info(
            "Anmeldung ueber %s erfolgreich: Mitarbeiter %s, Token gueltig bis %s.",
            path,
            result.employee_id,
            result.expires_at.isoformat(),
        )
        return result

    async def login_with_dashboard_key(self, dashboard_api_key: str) -> TanssLoginResult:
        """Meldet eine Dashboard-Anzeige an - der dritte Anmeldeweg, allein ueber ``dbapikey``.

        **Vom Server so umgesetzt, gegen 10.10 geprueft:** Traegt die Anfrage **nur** die Kopfzeile
        ``dbapikey`` - kein ``user``, kein ``password`` -, nimmt der Server ausschliesslich diesen
        Zweig: Er sucht den einen aktiven Mitarbeiter, dessen Dashboard-Schluessel dem uebergebenen
        Wert gleicht, prueft, dass dieser Mitarbeiter zur eigenen Firma gehoert, und gibt ein
        gewoehnliches Zugangstoken aus.

        **Was dabei herauskommt**, ist ein Token vom Typ ``ACCESS`` wie nach :meth:`login` - mit dem
        einen Unterschied, dass der Server darin den Anspruch ``dashboardLogin`` = ``true`` sieht. Das
        Ergebnis ist dasselbe :class:`TanssLoginResult`. Erneuert wird danach wie sonst auch ueber
        :meth:`refresh`.

        **Woher der Schluessel kommt.** Er haengt am einzelnen Mitarbeiter und wird in der
        TANSS-Verwaltung gepflegt. Die Schnittstelle gibt ihn nicht heraus - gemessen traegt die
        Antwort von ``GET /api/v1/employees/{id}`` dieses Feld nicht. Wer ihn braucht, holt ihn also
        aus der Verwaltung, nicht ueber die API.

        **Fehlschlaege kommen wie jede abgelehnte Anmeldung als HTTP 200** mit ``meta.text`` =
        ``Unsuccesful login attempt`` und dem Code in ``content.detailMessage``; er steht danach in
        ``error_code``. Drei Codes gehoeren zu diesem Weg:

        * ``LOGIN_ERROR_NO_USER_FOR_DASHBOARD`` - kein aktiver Mitarbeiter traegt diesen Schluessel
          (mit einem erfundenen Schluessel gegen TANSS 10.10 gemessen).
        * ``LOGIN_ERROR_TOO_MANY_USER_FOR_DASHBOARD`` - mehr als ein Mitarbeiter traegt ihn; der
          Anbieter verlangt genau einen.
        * ``LOGIN_ERROR_DASHBOARD_USER_NOT_WITHIN_OWN_COMPANY`` - der Treffer gehoert nicht zur eigenen
          Firma.

        **Ausweichweg.** Antwortet :data:`LOGIN_PATH` mit 404 - auf 10.10 tut er das nicht -,
        wiederholt diese Methode die Anmeldung auf dem dokumentierten :data:`DOCUMENTED_LOGIN_PATH` mit
        dem Rumpf ``{"dbapikey": ...}``: Der Server nimmt dort neben ``username``, ``password`` und
        ``token`` auch ``dbapikey`` entgegen - anders als die offizielle Schnittstellenbeschreibung,
        die nur die ersten drei kennt.

        :param dashboard_api_key: Der Dashboard-Schluessel des Mitarbeiters; geht - kodiert wie in
            :func:`encode_credential_header` beschrieben - als Kopfzeile ``dbapikey`` hinaus.
        :raises ValueError: Der Schluessel ist leer oder traegt ein Steuerzeichen.
        :raises tanss_api.errors.TanssApiError: Die Antwort trug kein ``content.apiKey``, oder TANSS
            hat mit einem Fehlerstatus geantwortet.
        """
        if not dashboard_api_key or not dashboard_api_key.strip():
            raise ValueError("Der Dashboard-Schluessel darf nicht leer sein.")

        # Nur dbapikey - kein Rumpf, kein user, kein password. Steht eine der beiden anderen
        # Kopfzeilen daneben, nimmt der Server einen anderen Zweig.
        headers = {DASHBOARD_KEY_HEADER: encode_credential_header(dashboard_api_key, "dashboard_api_key")}

        path = LOGIN_PATH
        status, body = await self._send("POST", LOGIN_PATH, headers=headers)

        if status == 404:
            path = DOCUMENTED_LOGIN_PATH
            status, body = await self._send(
                "POST",
                DOCUMENTED_LOGIN_PATH,
                json_body={DASHBOARD_KEY_HEADER: dashboard_api_key},
            )

        if status < 200 or status >= 300:
            raise TanssApiError.from_response(status, body)

        result = replace(TanssLoginResult.parse(body), login_path=path)
        self._store(result)
        _logger.info(
            "Dashboard-Anmeldung ueber %s erfolgreich: Mitarbeiter %s, Token gueltig bis %s.",
            path,
            result.employee_id,
            result.expires_at.isoformat(),
        )
        return result

    async def refresh(self, refresh_token: str, path: str = REFRESH_PATH) -> TanssLoginResult:
        """Tauscht das Erneuerungstoken gegen ein frisches Paar - ueber die Kopfzeile ``refreshToken``.

        **Gegen TANSS 10.10 gemessen:** Das Erneuerungstoken in der Kopfzeile ``apiToken`` antwortet
        **403**. Dasselbe Token in der Kopfzeile ``refreshToken``, und zwar **ohne** jede Kopfzeile
        ``apiToken``, antwortet 200 mit einem vollstaendigen Anmeldeergebnis - neues ``apiKey`` und
        neues ``refresh``. Genau so schickt diese Methode die Anfrage: ein ``GET`` auf ``path``,
        ``refreshToken`` gesetzt, ``apiToken`` weggelassen. Die eigentliche Nutzlast der Route wird
        verworfen.

        Die Schreibweise der Kopfzeile ist gleichgueltig (``refreshToken``, ``refreshtoken``,
        ``RefreshToken`` - alle gemessen mit 200); HTTP-Kopfzeilen sind unabhaengig von Gross- und
        Kleinschreibung.

        **Einen Erneuerungspfad gibt es nicht.** Die offizielle Schnittstellenbeschreibung erwaehnt im
        Fliesstext einen eigenen Pfad dafuer. Auf 10.10 existiert er nicht (gegen TANSS 10.10
        gemessen), und er steht weder in der offiziellen Schnittstellenbeschreibung als Operation noch
        unter den Routen, die 10.10 bedient. Wer auf einer Instanz mit einem eigenen Pfad arbeitet,
        gibt ihn in ``path`` an.

        Das Praefix ``Bearer`` gehoert zum Wert und wird - wie bei ``apiToken`` - genau einmal gesetzt;
        ohne Praefix lehnt der Filter ab (gegen TANSS 10.10 gemessen).

        :param refresh_token: Das Erneuerungstoken aus :attr:`TanssLoginResult.refresh`.
        :param path: Die Route, ueber die erneuert wird - jede ausser den beiden Anmeldepfaden;
            Vorgabe :data:`REFRESH_PATH`.
        :raises ValueError: Token oder Pfad sind leer.
        :raises tanss_api.errors.TanssApiError: Das Erneuerungstoken ist abgelaufen oder die Antwort
            trug kein Paar.
        """
        if not refresh_token or not refresh_token.strip():
            raise ValueError("Das Erneuerungstoken darf nicht leer sein.")
        if not path or not path.strip():
            raise ValueError("Der Pfad darf nicht leer sein.")

        # refreshToken ja, apiToken nein - mit apiToken kommt 403.
        headers: dict[str, str] = {}
        value = bearer_header_value(refresh_token)
        if value is not None:
            headers[REFRESH_TOKEN_HEADER] = value

        status, body = await self._send("GET", path, headers=headers)
        if status < 200 or status >= 300:
            raise TanssApiError.from_response(status, body)

        result = TanssLoginResult.parse(body)
        self._store(result)
        _logger.info("Token ueber %s erneuert: gueltig bis %s.", path, result.expires_at.isoformat())
        return result

    async def mint(
        self,
        ext_program: str,
        duration: timedelta | int | None = None,
        info: str | None = None,
        is_for_testing: bool | None = None,
    ) -> str:
        """Praegt ein Token fuer ein externes Programm: ``GET /api/v1/jwts/{ext_program}``.

        Beschreibung der Operation: Sie praegt ein JWT, mit dem ein externes Programm (etwa ein
        Fernwartungs-Agent, eine App oder ein Integrationsdienst) sich gegen diese Schnittstelle
        anmeldet. Die Lebensdauer ist ``duration`` (Millisekunden, Vorgabe ein Jahr), ``info`` wird im
        Token-Protokoll abgelegt, sodass das ausgegebene Token nachverfolgt und zurueckgezogen werden
        kann, und ``isForTesting=true`` laesst diesen Protokolleintrag weg. Fuer
        ``REMOTE_SUPPORT``-Programme muss ``info`` ein Zahlencode >= 1000 sein. Vorausgesetzt wird das
        Recht ``CREATE_JWT_TOKENS_FOR_EXTERNAL_PROGRAMMS``, und das Programm muss lizenziert sein.

        **Jeder Aufruf praegt ein neues Token und wird serverseitig protokolliert.** Genau deshalb
        nimmt die Wiederholungsregel des Clients :data:`MINT_PATH` aus: Eine Wiederholung nach 429, 503
        oder 504 hinterliesse ein zweites Token im Protokoll. Wer nur ausprobiert, setzt
        ``is_for_testing``.

        Die Route verlangt die Rolle ``USER``; die Kopfzeile traegt also das Sitzungstoken aus
        :meth:`login`, nicht das gepraegte.

        :param ext_program: Die Kennung des Programms, etwa ``tanss_app``, ``remote_support`` oder
            ``erp`` (Pfadparameter ``ext_program``; welche Kennungen eine Instanz fuehrt, haengt an
            ihren lizenzierten Programmen).
        :param duration: Die Gueltigkeitsdauer, als :class:`datetime.timedelta` oder als ganze Zahl in
            Millisekunden; ``None`` ueberlaesst dem Server seine Vorgabe von einem Jahr.
        :param info: Der Eintrag fuer das Token-Protokoll; bei ``REMOTE_SUPPORT`` ein Zahlencode
            >= 1000.
        :param is_for_testing: Bei ``True`` wird kein Protokolleintrag geschrieben.
        :returns: Das gepraegte Token aus ``content.apiToken``.
        :raises ValueError: Die Programmkennung ist leer.
        :raises tanss_api.errors.TanssApiError: Recht oder Lizenz fehlen (403), oder die Antwort trug
            kein Token.
        """
        if not ext_program or not ext_program.strip():
            raise ValueError("Die Programmkennung darf nicht leer sein.")

        query: list[str] = []
        if duration is not None:
            milliseconds = (
                int(duration.total_seconds() * 1000) if isinstance(duration, timedelta) else int(duration)
            )
            query.append("duration=" + str(milliseconds))
        if info is not None:
            query.append("info=" + quote(info, safe=""))
        if is_for_testing is not None:
            query.append("isForTesting=" + ("true" if is_for_testing else "false"))

        path = MINT_PATH + "/" + quote(ext_program, safe="")
        if query:
            path += "?" + "&".join(query)

        headers: dict[str, str] = {}
        value = bearer_header_value(self._tokens.get_token() if self._tokens else None)
        if value is not None:
            headers[API_TOKEN_HEADER] = value

        status, body = await self._send("GET", path, headers=headers)
        if status < 200 or status >= 300:
            raise TanssApiError.from_response(status, body)

        minted = self._token_of(body)
        _logger.info(
            "Token fuer %s gepraegt; Protokolleintrag: %s.",
            ext_program,
            "nein" if is_for_testing else "ja",
        )
        return minted

    @staticmethod
    def _token_of(body: str) -> str:
        try:
            document = json.loads(body)
        except ValueError as cause:
            raise TanssApiError("Die Antwort auf das Praegen war kein JSON.", raw_body=body) from cause

        if isinstance(document, dict):
            token = _text_of(document.get("content"), "apiToken")
            if token:
                return token

        raise TanssApiError(
            "Die Antwort auf das Praegen trug kein Token. Dokumentiert ist eine Map mit dem gepraegten "
            "JWT unter dem Schluessel apiToken, also { meta, content: { apiToken } }.",
            status_code=200,
            raw_body=body,
        )

    def _store(self, result: TanssLoginResult) -> None:
        """Traegt das neue Sitzungstoken ein, wenn der Anbieter ein veraenderlicher ist.

        Jeder andere Anbieter bleibt unberuehrt: Ein fest hinterlegtes Modul-Token darf eine Anmeldung
        nicht ueberschreiben.
        """
        if isinstance(self._tokens, MutableTokenProvider):
            self._tokens.token = result.api_key

    def _address(self, path: str) -> str:
        """Die vollstaendige Adresse zu einem Pfad unterhalb der Basisadresse."""
        return self._base_url + "/" + path.lstrip("/")

    async def _send(
        self,
        method: str,
        path: str,
        headers: dict[str, Any] | None = None,
        json_body: dict[str, Any] | None = None,
    ) -> tuple[int, str]:
        """Schickt die Anfrage und liefert Status und Rumpf roh zurueck.

        Ueber Erfolg entscheidet bei der Anmeldung nicht der Status, sondern ``content.apiKey`` (gegen
        TANSS 10.10 gemessen). Deshalb wird hier nichts geworfen.
        """
        response = await self._http.request(
            method,
            self._address(path),
            headers=headers,
            json=json_body,
        )
        return response.status_code, response.text
