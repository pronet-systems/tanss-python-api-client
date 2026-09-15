"""Gemeinsames Handwerkszeug der Proben: ein Zugang auf einer Attrappe statt auf dem Netz.

Die Proben dieses Verzeichnisses sprechen mit keiner TANSS-Instanz. Gesendet wird ueber
``httpx.MockTransport``: Der Aufruf durchlaeuft die vollstaendige Middleware-Kette der Bibliothek -
Kopfzeile ``apiToken``, ``loggedInUserId``, Wiederholungsregel -, endet aber in einer Funktion im
Testlauf statt auf der Leitung. Die einzige Ausnahme ist ``test_credential_wire.py``: Dort ist gerade
die Leitung der Gegenstand, und der Gegenueber ist ein eigener Anschluss auf der Rueckschleife.
"""

from __future__ import annotations

from collections.abc import Callable

import httpx

from tanss_api import TanssApi, TanssApiOptions, TokenProvider

BASE = "https://tanss.example.de/backend"
"""Die Basisadresse der Proben - ein Platzhalter, keine Instanz."""


def make_api(
    handler: Callable[[httpx.Request], httpx.Response],
    tokens: TokenProvider,
    employee_id: int | None = 42,
) -> tuple[TanssApi, list[httpx.Request]]:
    """Baut einen Zugang auf einer Attrappe und gibt ihn samt der Liste der gesehenen Anfragen zurueck.

    :param handler: Die Antwort auf jede Anfrage.
    :param tokens: Der Token-Anbieter, den der Zugang befragt.
    :param employee_id: Die Mitarbeiter-Id fuer ``loggedInUserId``; ``None`` schaltet den Parameter ab.
    :returns: Der Zugang und die Liste, in der jede gesendete Anfrage steht.
    """
    seen: list[httpx.Request] = []

    def record(request: httpx.Request) -> httpx.Response:
        seen.append(request)
        return handler(request)

    client = httpx.AsyncClient(transport=httpx.MockTransport(record), base_url=BASE)
    options = TanssApiOptions(base_url=BASE, employee_id=employee_id)
    return TanssApi.create(options, tokens, http_client=client), seen


def headers_of(request: httpx.Request) -> dict[bytes, bytes]:
    """Die Kopfzeilen einer Anfrage als Bytes, die Namen in Kleinschreibung.

    Gefragt sind die rohen Bytes: Zugangsdaten gehen als UTF-8-Bytes hinaus, und genau das soll die
    Probe sehen und nicht die Rueckuebersetzung durch httpx.

    :param request: Die gesendete Anfrage.
    """
    return {name.lower(): value for name, value in request.headers.raw}
