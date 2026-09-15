"""Woher der Wert der Kopfzeile ``apiToken`` kommt."""

from __future__ import annotations

import threading
from typing import Protocol, runtime_checkable


@runtime_checkable
class TokenProvider(Protocol):
    """Die Quelle des Tokens.

    Die Schnittstellenbeschreibung beschreibt im Abschnitt ``securitySchemes.ApiTokenAuth`` ein
    ``apiKey``-Verfahren mit ``in: header`` und ``name: apiToken``: Der Wert traegt das Praefix
    ``Bearer`` bereits und wird unveraendert in der Kopfzeile ``apiToken`` geschickt. Mehr als diese
    eine Zeichenkette braucht die Bibliothek nicht zu wissen.

    Gefragt wird vor **jeder** Anfrage. Ein Token laeuft nach vier Stunden ab, und ein einmal gemerkter
    Wert erzeugte nach jeder Erneuerung reihenweise 403. Eine Umsetzung muss deshalb billig und
    nebenlaeufig aufrufbar sein.

    ``None`` oder leer heisst: kein Token. Der Authentifizierungsanbieter setzt dann keine Kopfzeile —
    richtig fuer die Anmeldung selbst, die mit ``security: []`` als tokenfrei ausgewiesen ist.
    """

    def get_token(self) -> str | None:
        """Das aktuelle Token, mit oder ohne ``Bearer``; ``None``, wenn keines vorliegt."""
        ...


class StaticTokenProvider:
    """Ein unveraenderlicher Wert — fuer ein in der Konfiguration hinterlegtes Modul-Token.

    Modul-Token (ERP, PHONE, REMOTE_SUPPORT, TIMESTAMP, ...) werden in der TANSS-Verwaltung erzeugt und
    laufen typischerweise erst nach einem Jahr ab (``GET /api/v1/jwts/{ext_program}``, Vorgabe von
    ``duration``: 31536000000 ms). Fuer sie genuegt ein fester Wert; ein Sitzungstoken gehoert in den
    :class:`MutableTokenProvider`.
    """

    __slots__ = ("_token",)

    def __init__(self, token: str | None = None) -> None:
        """Baut den Anbieter.

        :param token: Das Token, mit oder ohne ``Bearer``; ``None`` fuer "keines".
        """
        self._token = token

    def get_token(self) -> str | None:
        """Das hinterlegte Token."""
        return self._token


class MutableTokenProvider:
    """Ein Wert, der sich aendern darf — der Platz fuer das Sitzungstoken aus der Anmeldung.

    Lesen und Schreiben sind nebenlaeufig sicher: Ein Schloss schuetzt beide Seiten, sodass ein Leser
    entweder das alte oder das neue Token sieht, nie einen halben Wert.

    :class:`tanss_api.session.TanssSession` schreibt hier nach Anmeldung und Erneuerung den Wert aus
    ``content.apiKey`` hinein, sodass alle laufenden Clients ohne Neubau weiterarbeiten.
    """

    __slots__ = ("_lock", "_token")

    def __init__(self, token: str | None = None) -> None:
        """Baut den Anbieter, wahlweise mit einem Anfangswert.

        :param token: Das erste Token; ``None``, solange noch keine Anmeldung erfolgt ist.
        """
        self._lock = threading.Lock()
        self._token = token

    @property
    def token(self) -> str | None:
        """Das aktuelle Token. Schreiben wirkt sofort auf alle Clients, die diesen Anbieter halten."""
        with self._lock:
            return self._token

    @token.setter
    def token(self, value: str | None) -> None:
        with self._lock:
            self._token = value

    def set_token(self, value: str | None) -> None:
        """Setzt das Token. Gleichbedeutend mit der Zuweisung an :attr:`token`.

        :param value: Das neue Token; ``None`` leert den Speicher.
        """
        self.token = value

    def get_token(self) -> str | None:
        """Das aktuelle Token."""
        return self.token


API_TOKEN_HEADER = "apiToken"
"""Die Kopfzeile, die TANSS liest.

Sie heisst ``apiToken``, nicht ``Authorization``. So steht es in der Schnittstellenbeschreibung
(``securitySchemes.ApiTokenAuth``: ``type: apiKey``, ``in: header``, ``name: apiToken``), und die
Beschreibung der Anmeldung sagt es noch einmal ausdruecklich. Dieselbe Kopfzeile tragen auch alle
Modul-Verfahren.
"""

BEARER_PREFIX = "Bearer "
"""Das Praefix, das der Wert genau einmal traegt."""


def bearer_header_value(token: str | None) -> str | None:
    """Der Wert der Kopfzeile: das Token mit genau einem ``Bearer`` davor.

    ``None``, wenn gar kein Token vorliegt; der Aufrufer setzt die Kopfzeile dann nicht.

    Das Praefix gehoert zum Wert, und zwar genau einmal. Ein Token aus der Anmeldung bringt es mit und
    wird unveraendert gesendet. Fehlt es (etwa bei einem von Hand kopierten JWT), wird es
    vorangestellt: Der Server schneidet das Praefix ab, bevor er das Token prueft; ohne Praefix
    schlaegt die Pruefung fehl, und die 403 ist von der eines abgelaufenen Tokens nicht zu
    unterscheiden (vom Server so umgesetzt, gegen 10.10 geprueft).

    :param token: Das gespeicherte Token, mit oder ohne Praefix, mit oder ohne Leerraum.
    """
    raw = (token or "").strip()
    if not raw or raw.lower() == BEARER_PREFIX.strip().lower():
        # "Bearer" ohne Token dahinter ist kein Token, sondern ein leerer Speicher.
        return None

    if raw.startswith(BEARER_PREFIX):
        return raw

    # Ein von Hand eingetragenes "bearer ..." zaehlt als vorhandenes Praefix, wird aber auf die
    # woertliche Schreibweise gebracht: Der Server schneidet "Bearer " ab, nicht irgendeine
    # Schreibweise davon.
    if raw[: len(BEARER_PREFIX)].lower() == BEARER_PREFIX.lower():
        return BEARER_PREFIX + raw[len(BEARER_PREFIX):].lstrip()

    return BEARER_PREFIX + raw
