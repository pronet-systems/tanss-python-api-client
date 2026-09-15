"""Beweist an einer echten Verbindung, dass Zugangsdaten mit Umlauten unveraendert ankommen.

Der Server liest jede Zugangsdaten-Kopfzeile als ISO-8859-1-Bytes und dekodiert sie als UTF-8 (vom
Server so umgesetzt, gegen 10.10 geprueft). Auf der Leitung muessen also die UTF-8-Bytes stehen;
``tanss_api.session.encode_credential_header`` sorgt dafuer, indem es den Wert als ``bytes`` uebergibt -
httpx wuerde einen ``str`` als ASCII kodieren und jedes Zeichen darueber abweisen.

Die Probe haengt an keinem fremden Rechner: Sie hoert selbst auf einem Anschluss der Rueckschleife,
liest die rohen Bytes und antwortet mit einer festen Anmeldeantwort.
"""

from __future__ import annotations

import asyncio
import json

from tanss_api import MutableTokenProvider, TanssApi, TanssApiOptions

ANMELDEANTWORT = {
    "meta": {"text": "Welcome, your ApiToken is 4 hours valid."},
    "content": {
        "employeeId": 7,
        "apiKey": "Bearer abc",
        "expire": 1789477324,
        "refresh": "Bearer def",
        "employeeType": "TECHNICAN",
    },
}


async def _anschluss() -> tuple[asyncio.Server, int, list[bytes]]:
    """Oeffnet einen Anschluss auf 127.0.0.1, der genau eine Anfrage beantwortet.

    :returns: Der Anschluss, seine Nummer und die Liste, in der die rohen Bytes landen.
    """
    empfangen: list[bytes] = []

    async def bediene(reader: asyncio.StreamReader, writer: asyncio.StreamWriter) -> None:
        # Der Kopf endet mit einer Leerzeile; einen Rumpf schickt die Anmeldung nicht.
        roh = await reader.readuntil(b"\r\n\r\n")
        empfangen.append(roh)

        rumpf = json.dumps(ANMELDEANTWORT).encode("utf-8")
        kopf = (
            b"HTTP/1.1 200 OK\r\nContent-Type: application/json\r\nContent-Length: "
            + str(len(rumpf)).encode("ascii")
            + b"\r\nConnection: close\r\n\r\n"
        )
        writer.write(kopf + rumpf)
        await writer.drain()
        writer.close()

    server = await asyncio.start_server(bediene, "127.0.0.1", 0)
    port = server.sockets[0].getsockname()[1]
    return server, port, empfangen


async def test_ein_kennwort_mit_umlauten_kommt_als_utf8_auf_der_leitung_an() -> None:
    server, port, empfangen = await _anschluss()
    async with server:
        optionen = TanssApiOptions(base_url=f"http://127.0.0.1:{port}/backend", employee_id=7)
        async with TanssApi.create(optionen, MutableTokenProvider()) as api:
            ergebnis = await api.session.login("müller", "Paßwortäöü")

    roh = empfangen[0]
    assert ergebnis.employee_id == 7

    # Die Kopfzeilen muessen die UTF-8-Bytes tragen: ae = C3 A4, ss = C3 9F, ue = C3 BC.
    assert b"user: " + "müller".encode("utf-8") in roh
    assert b"password: " + "Paßwortäöü".encode("utf-8") in roh

    # Und eben nicht die Latin-1-Bytes (ae = E4), die ein unbedachter Client schicken wuerde.
    assert b"user: " + "müller".encode("latin-1") not in roh
    assert b"password: " + "Paßwortäöü".encode("latin-1") not in roh


async def test_auch_der_dashboard_schluessel_reist_unveraendert() -> None:
    server, port, empfangen = await _anschluss()
    async with server:
        optionen = TanssApiOptions(base_url=f"http://127.0.0.1:{port}/backend")
        async with TanssApi.create(optionen, MutableTokenProvider()) as api:
            await api.session.login_with_dashboard_key("schlüssel-äöü")

    roh = empfangen[0]
    assert b"dbapikey: " + "schlüssel-äöü".encode("utf-8") in roh
    assert b"dbapikey: " + "schlüssel-äöü".encode("latin-1") not in roh

    # Der Dashboard-Weg schickt weder Benutzer noch Kennwort (gegen TANSS 10.10 gemessen).
    klein = roh.lower()
    assert b"\r\npassword:" not in klein
    assert b"\r\nuser:" not in klein
