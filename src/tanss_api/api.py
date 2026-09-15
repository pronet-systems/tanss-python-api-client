"""Der Einstieg: eine Verbindungsschicht, darauf der vollstaendige erzeugte Client und die Sitzung."""

from __future__ import annotations

import asyncio
import logging
from types import TracebackType
from typing import Any

import httpx
from kiota_abstractions.authentication import AuthenticationProvider
from kiota_abstractions.request_information import RequestInformation
from kiota_bundle.default_request_adapter import DefaultRequestAdapter
from kiota_http.kiota_client_factory import KiotaClientFactory
from kiota_http.middleware import (
    BaseMiddleware,
    ParametersNameDecodingHandler,
    RedirectHandler,
    UrlReplaceHandler,
    UserAgentHandler,
)

from . import _paths, token_roles
from .options import TanssApiOptions
from .rest.tanss_rest_client import TanssRestClient
from .session import TanssSession
from .tokens import API_TOKEN_HEADER, TokenProvider, bearer_header_value

_logger = logging.getLogger(__name__)

LOGGED_IN_USER_ID_PARAMETER = "loggedInUserId"
"""Der Parametername, so wie TANSS ihn erwartet."""

MINT_PREFIX = "/api/v1/jwts"
"""Der Pfad, unter dem jeder Aufruf ein Token praegt und deshalb nie wiederholt wird."""

RETRY_STATUS_CODES = frozenset({429, 503, 504})
"""Die Statuscodes, nach denen ueberhaupt wiederholt wird."""


class TanssApiTokenAuthenticationProvider(AuthenticationProvider):
    """Setzt auf jede Anfrage des erzeugten Clients die Kopfzeile ``apiToken``.

    **Die Kopfzeile heisst ``apiToken``, nicht ``Authorization``.** So steht es in der
    Schnittstellenbeschreibung, und die Beschreibung der Anmeldung sagt es noch einmal ausdruecklich.
    Dieselbe Kopfzeile tragen auch alle Modul-Verfahren.

    **Das Praefix ``Bearer`` gehoert zum Wert** - und zwar genau einmal; das besorgt
    :func:`tanss_api.tokens.bearer_header_value`.

    **Kein Token, keine Kopfzeile.** Liefert der Anbieter ``None`` oder Leerraum, geht die Anfrage ohne
    ``apiToken`` hinaus. Das ist fuer die tokenfreien Routen richtig, und fuer alle anderen antwortet
    TANSS mit 403, was :class:`tanss_api.errors.TanssApiError` sauber ausweist.

    **Gelesen wird bei jeder Anfrage neu.** Ein Sitzungstoken laeuft nach vier Stunden ab; ein
    gemerkter Wert erzeugte nach jeder Erneuerung reihenweise 403.
    """

    def __init__(self, tokens: TokenProvider) -> None:
        """Baut den Anbieter.

        :param tokens: Woher das Token kommt. Wird bei jeder Anfrage befragt.
        """
        if tokens is None:
            raise TypeError("Der Token-Anbieter darf nicht None sein.")
        self._tokens = tokens

    async def authenticate_request(
        self,
        request: RequestInformation,
        additional_authentication_context: dict[str, Any] = {},
    ) -> None:
        """Setzt die Kopfzeile ``apiToken``, wenn ein Token vorliegt.

        :param request: Die Anfrage des erzeugten Clients.
        :param additional_authentication_context: Von Kiota vorgesehen, hier ohne Bedeutung.
        """
        if request is None:
            raise TypeError("Die Anfrage darf nicht None sein.")

        request.headers.remove(API_TOKEN_HEADER)
        value = bearer_header_value(self._tokens.get_token())
        if value is not None:
            request.headers.add(API_TOKEN_HEADER, value)


class LoggedInUserIdHandler(BaseMiddleware):
    """Haengt ``loggedInUserId`` an, wo TANSS daran den Mitarbeiter erkennt - und nur dort.

    **Die Regel ist Verhalten des Servers, keine Vermutung.** Vom Server so umgesetzt: Ein Token vom
    Typ ``TANSS_APP`` bekommt die Rolle ``ROLE_USER`` nur dann zugesprochen, wenn die Anfrage den
    Abfrageparameter ``loggedInUserId`` traegt - er benennt den Mitarbeiter, in dessen Kontext
    gearbeitet wird. Ohne ihn fehlt dieser Kontext, und jede Route mit der Rolle ``USER`` antwortet 403
    (vom Server so umgesetzt, gegen 10.10 geprueft). Ein Login-Token (``ACCESS``) fuehrt den
    Mitarbeiter im Anspruch ``sub`` mit; dort ist der Parameter ueberfluessig, aber unschaedlich.

    **Gefragt wird die Rollentabelle, nicht der Pfadanfang.** Angehaengt wird genau dort, wo
    :func:`tanss_api.token_roles.required_for` eine Rolle nennt, die ``USER`` einschliesst - also auf
    den USER-Modulen unter ``/api/v1`` samt der gemischten Zeilen. Die Modul-Praefixe
    (``/api/erp/v1``, ``/api/tanss.x/v1``, ``/api/remoteSupports/v1``, ...) bekommen ihn nie: Ihre
    Token kennen keinen Mitarbeiter.

    **Nichts wird ueberschrieben.** Steht ``loggedInUserId`` schon in der Abfrage - in welcher
    Schreibweise auch immer -, bleibt der Wert des Aufrufers stehen. Wer ihn selbst angibt, meint einen
    anderen Mitarbeiter.

    **Ohne Mitarbeiter-Id geschieht nichts.** Ist :attr:`tanss_api.options.TanssApiOptions.employee_id`
    ``None``, haengt der Handler nirgends etwas an - richtig fuer Modul-Token.

    Der Handler sitzt am Ende der Kette, unmittelbar vor der Verbindungsschicht. Er sieht damit die
    fertige Adresse und nicht die Vorlage mit Platzhaltern. Als Middleware und nicht als
    httpx-Ereignishaken umgesetzt, weil nur eine Middleware die Adresse noch aendern darf.
    """

    def __init__(self, employee_id: int | None, base_path: str = "") -> None:
        """Baut den Handler aus den Einzelwerten.

        :param employee_id: Die Mitarbeiter-Id, die angehaengt wird; ``None`` schaltet den Handler
            still.
        :param base_path: Der Pfadanteil der Basisadresse, etwa ``/backend``; leer, wenn keiner.
        """
        super().__init__()
        self._employee_id = str(employee_id) if employee_id is not None else None
        self._base_path = (base_path or "").rstrip("/")

    async def send(
        self, request: httpx.Request, transport: httpx.AsyncBaseTransport
    ) -> httpx.Response:
        """Haengt den Parameter an, wo die Rollentabelle ihn verlangt, und reicht weiter."""
        if self._employee_id is not None:
            path = _paths.below_base(request.url.path, self._base_path)
            if token_roles.includes_user(token_roles.required_for(path)) and not _has_parameter(
                request.url, LOGGED_IN_USER_ID_PARAMETER
            ):
                request.url = request.url.copy_add_param(
                    LOGGED_IN_USER_ID_PARAMETER, self._employee_id
                )
                _logger.debug(
                    "%s %s: %s=%s angehaengt.",
                    request.method,
                    path,
                    LOGGED_IN_USER_ID_PARAMETER,
                    self._employee_id,
                )

        return await super().send(request, transport)


class ReadOnlyRetryHandler(BaseMiddleware):
    """Wiederholt nur Lesendes: ``GET``, nur 429, 503 und 504, nie unter ``/api/v1/jwts``.

    Kiota bringt einen eigenen Wiederholungs-Handler mit, der bei diesen Statuscodes jede Anfrage
    erneut schickt - auch ``POST``. Seine Einstellungen kennen nur einen Schalter ``should_retry``
    (wahr oder falsch) und keine Bedingung je Anfrage; die Regel dieser Bibliothek laesst sich damit
    nicht ausdruecken. Deshalb steht sie hier als eigene Middleware, und Kiotas Handler wird nicht in
    die Kette aufgenommen.

    **Warum nur Lesendes.** TANSS dedupliziert schreibende Aufrufe nicht: Ein wiederholtes ``POST``
    legt einen zweiten Datensatz an. Und unter ``/api/v1/jwts`` praegt jeder Aufruf ein neues Token und
    schreibt es in das Token-Protokoll; ein zweiter Versuch hinterliesse ein zweites Token.
    """

    RETRY_ATTEMPT_HEADER = "Retry-Attempt"
    """Die Kopfzeile, in der die Zahl der bisherigen Versuche mitlaeuft - so wie Kiota sie fuehrt."""

    def __init__(
        self,
        base_path: str = "",
        max_retries: int = 3,
        backoff_factor: float = 0.5,
        backoff_max: float = 120.0,
    ) -> None:
        """Baut den Handler.

        :param base_path: Der Pfadanteil der Basisadresse, etwa ``/backend``.
        :param max_retries: Die Zahl der Versuche nach dem ersten.
        :param backoff_factor: Der Faktor der Wartezeit: ``backoff_factor * 2 ** versuch`` Sekunden.
        :param backoff_max: Die obere Grenze einer einzelnen Wartezeit in Sekunden.
        """
        super().__init__()
        self._base_path = (base_path or "").rstrip("/")
        self._max_retries = max(0, max_retries)
        self._backoff_factor = backoff_factor
        self._backoff_max = backoff_max

    async def send(
        self, request: httpx.Request, transport: httpx.AsyncBaseTransport
    ) -> httpx.Response:
        """Schickt die Anfrage und wiederholt sie, solange die Regel es zulaesst."""
        response = await super().send(request, transport)

        attempt = 0
        while attempt < self._max_retries and self.is_repeatable_read(request, response):
            delay = self._delay(attempt, response)
            await response.aclose()
            await asyncio.sleep(delay)
            attempt += 1
            request.headers[self.RETRY_ATTEMPT_HEADER] = str(attempt)
            _logger.debug(
                "%s %s: Versuch %s nach HTTP %s.",
                request.method,
                request.url.path,
                attempt + 1,
                response.status_code,
            )
            response = await super().send(request, transport)

        return response

    def is_repeatable_read(self, request: httpx.Request, response: httpx.Response) -> bool:
        """Darf diese Antwort zu einer Wiederholung fuehren?

        Nur bei 429, 503 oder 504 und auch dann nur auf ein ``GET`` ausserhalb von
        :data:`MINT_PREFIX`.

        :param request: Die Anfrage, die zu der Antwort gefuehrt hat.
        :param response: Die Antwort.
        """
        if response.status_code not in RETRY_STATUS_CODES or request.method.upper() != "GET":
            return False

        path = _paths.below_base(request.url.path, self._base_path)
        return path != MINT_PREFIX and not path.startswith(MINT_PREFIX + "/")

    def _delay(self, attempt: int, response: httpx.Response) -> float:
        """Die Wartezeit vor dem naechsten Versuch: ``Retry-After``, sonst wachsender Abstand."""
        header = response.headers.get("Retry-After")
        if header:
            try:
                seconds = float(header)
            except ValueError:
                seconds = -1.0
            if seconds >= 0:
                return min(seconds, self._backoff_max)

        return min(self._backoff_factor * (2**attempt), self._backoff_max)


def _has_parameter(url: httpx.URL, name: str) -> bool:
    """Steht der Parameter - in irgendeiner Schreibweise - schon in der Abfrage?

    Verglichen wird ohne Ruecksicht auf Gross- und Kleinschreibung, sonst stuenden zwei nebeneinander.

    :param url: Die vollstaendige Adresse.
    :param name: Der gesuchte Name.
    """
    wanted = name.lower()
    return any(key.lower() == wanted for key in url.params.keys())


class TanssApi:
    """Die ganze Schnittstelle und die drei Token-Ablaeufe auf einer Verbindungsschicht.

    :attr:`rest` ist die ganze Schnittstelle - jede Operation, typisiert. Es gibt daneben keine
    Kurzwege, keine Repositories und keine Bequemlichkeiten: Was TANSS anbietet, steht in der
    Schnittstellenbeschreibung, und was darueber hinaus nuetzlich ist, entscheidet die aufrufende
    Anwendung, nicht diese Bibliothek.

    :attr:`session` deckt ab, was der erzeugte Client nicht kann, weil die Schnittstellenbeschreibung
    dafuer kein Schema fuehrt: Anmelden, Erneuern, Praegen.

    Beide senden ueber **eine** Verbindungsschicht mit denselben Regeln - Kopfzeile ``apiToken``,
    ``loggedInUserId`` auf USER-Routen, Wiederholung nur fuer lesende Aufrufe ausserhalb von
    ``/api/v1/jwts``.

    Das Objekt haelt eine offene Verbindungsschicht und gehoert deshalb geschlossen: entweder ueber
    ``async with`` oder ueber :meth:`aclose`.
    """

    __slots__ = ("_http", "_options", "_owns_http", "_rest", "_session", "_tokens")

    def __init__(
        self,
        options: TanssApiOptions,
        tokens: TokenProvider,
        http: httpx.AsyncClient,
        rest: TanssRestClient,
        session: TanssSession,
        owns_http: bool,
    ) -> None:
        """Nimmt die fertigen Teile entgegen. Gebaut wird ueber :meth:`create`."""
        self._options = options
        self._tokens = tokens
        self._http = http
        self._rest = rest
        self._session = session
        self._owns_http = owns_http

    @classmethod
    def create(
        cls,
        options: TanssApiOptions,
        tokens: TokenProvider,
        *,
        http_client: httpx.AsyncClient | None = None,
    ) -> "TanssApi":
        """Baut den Zugang.

        Die Basisadresse wird unveraendert vorangestellt: Die Vorlagen des erzeugten Clients beginnen
        mit ``{+baseurl}``, und dort steht die Adresse aus den Einstellungen. Aus
        ``https://tanss.example.de/backend`` und ``{+baseurl}/api/v1/tickets/own`` wird so
        ``https://tanss.example.de/backend/api/v1/tickets/own``.

        :param options: Adresse, Mitarbeiter-Id, Zeitgrenze, Proxy, TLS-Pruefung.
        :param tokens: Woher das Token kommt. Ein :class:`tanss_api.tokens.MutableTokenProvider` nimmt
            das Ergebnis von :meth:`tanss_api.session.TanssSession.login` selbsttaetig auf.
        :param http_client: Wahlweise eine fertige Verbindungsschicht - fuer Tests mit einer Attrappe
            (``httpx.MockTransport``) oder fuer einen Wirt, der seine Verbindungen selbst verwaltet.
            Sie wird um die Middleware-Kette dieser Bibliothek ergaenzt, aber nicht geschlossen; ohne
            Angabe baut diese Methode eine eigene aus ``options`` (Zeitgrenze, Proxy, TLS-Pruefung).
        :raises TypeError: Einstellungen oder Token-Anbieter fehlen.
        """
        if options is None:
            raise TypeError("Die Einstellungen duerfen nicht None sein.")
        if tokens is None:
            raise TypeError("Der Token-Anbieter darf nicht None sein.")

        base_url = options.normalised_base_url
        base_path = options.base_path

        owns_http = http_client is None
        if http_client is None:
            if not options.verify_tls:
                # NOTBEHELF: Schaltet die Zertifikatspruefung vollstaendig ab und macht die
                # Verbindung gegen einen Angreifer in der Mitte wertlos.
                _logger.warning(
                    "TLS-Pruefung fuer %s abgeschaltet: Die Verbindung ist gegen einen Angreifer in "
                    "der Mitte wertlos.",
                    base_url,
                )
            http_client = httpx.AsyncClient(
                base_url=base_url,
                timeout=options.timeout,
                proxy=options.proxy,
                verify=options.verify_tls,
                follow_redirects=False,
            )
        elif not str(http_client.base_url):
            # httpx.URL ist auch leer immer wahr; gefragt ist die Zeichenkette.
            http_client.base_url = base_url

        # Kiotas eigene Kette ohne dessen Wiederholungs-Handler, dafuer mit der Regel dieser
        # Bibliothek, und dahinter - unmittelbar vor der Leitung - die loggedInUserId-Regel.
        middleware: list[BaseMiddleware] = [
            RedirectHandler(),
            ReadOnlyRetryHandler(base_path),
            ParametersNameDecodingHandler(),
            UrlReplaceHandler(),
            UserAgentHandler(),
            LoggedInUserIdHandler(options.employee_id, base_path),
        ]
        http = KiotaClientFactory.create_with_custom_middleware(middleware, http_client)

        adapter = DefaultRequestAdapter(
            authentication_provider=TanssApiTokenAuthenticationProvider(tokens),
            http_client=http,
        )
        adapter.base_url = base_url

        _logger.debug(
            "Kiota-Client fuer %s gebaut: Mitarbeiter %s, Zeitgrenze %s s.",
            base_url,
            options.employee_id,
            options.timeout,
        )

        return cls(
            options=options,
            tokens=tokens,
            http=http,
            rest=TanssRestClient(adapter),
            session=TanssSession(http, tokens, base_url),
            owns_http=owns_http,
        )

    @property
    def options(self) -> TanssApiOptions:
        """Die Einstellungen, mit denen dieser Zugang gebaut wurde."""
        return self._options

    @property
    def tokens(self) -> TokenProvider:
        """Der Token-Anbieter, den jede Anfrage befragt."""
        return self._tokens

    @property
    def rest(self) -> TanssRestClient:
        """Der erzeugte Client: jede Operation der Schnittstellenbeschreibung, typisiert."""
        return self._rest

    @property
    def session(self) -> TanssSession:
        """Anmelden, Erneuern, Praegen."""
        return self._session

    @property
    def http(self) -> httpx.AsyncClient:
        """Die Verbindungsschicht, ueber die erzeugter Client und Sitzung senden."""
        return self._http

    async def aclose(self) -> None:
        """Schliesst die Verbindungsschicht.

        Eine von :meth:`create` selbst gebaute wird geschlossen; eine uebergebene bleibt offen - sie
        gehoert dem Aufrufer.
        """
        if self._owns_http:
            await self._http.aclose()

    async def __aenter__(self) -> "TanssApi":
        """Gibt den Zugang zurueck; geschlossen wird beim Verlassen des Blocks."""
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        """Schliesst die Verbindungsschicht."""
        await self.aclose()
