"""Anmelden, erneuern, praegen - die Kopfzeilen, die Erfolgsbedingung und der Ausweichweg."""

from __future__ import annotations

import json

import httpx
import pytest

from tanss_api import MutableTokenProvider, TanssApiError
from tanss_api.session import DOCUMENTED_LOGIN_PATH, LOGIN_PATH, TanssLoginResult

from .conftest import BASE, headers_of, make_api

ERFOLG = {
    "meta": {"text": "Welcome, your ApiToken is 4 hours valid."},
    "content": {
        "employeeId": 42,
        "apiKey": "Bearer sitzung",
        "expire": 1563963819,
        "refresh": "Bearer erneuerung",
        "employeeType": "COMPANY_ADMIN",
        "warning": "Kennwort laeuft ab",
    },
}
"""Die Antwort einer gelungenen Anmeldung, wie eine 10.10-Instanz sie gemessen liefert."""


def _erfolg(_: httpx.Request) -> httpx.Response:
    return httpx.Response(200, json=ERFOLG)


async def test_anmeldung_schickt_die_zugangsdaten_in_kopfzeilen_und_ohne_rumpf() -> None:
    halter = MutableTokenProvider()
    api, gesehen = make_api(_erfolg, halter)
    async with api:
        ergebnis = await api.session.login("benutzer", "kennwörtchen")

    anfrage = gesehen[-1]
    kopf = headers_of(anfrage)
    assert anfrage.method == "POST"
    assert str(anfrage.url).startswith(BASE + LOGIN_PATH)
    assert anfrage.content == b""
    assert kopf[b"user"] == "benutzer".encode("utf-8")
    assert kopf[b"password"] == "kennwörtchen".encode("utf-8")
    # Die Anmeldung traegt security: [] - kein Token, keine Kopfzeile.
    assert b"apitoken" not in kopf
    assert ergebnis.employee_id == 42
    assert ergebnis.api_key == "Bearer sitzung"
    assert ergebnis.refresh == "Bearer erneuerung"
    assert ergebnis.warning == "Kennwort laeuft ab"
    assert ergebnis.login_path == LOGIN_PATH
    assert ergebnis.expires_at.isoformat() == "2019-07-24T10:23:39+00:00"
    assert halter.token == "Bearer sitzung"


async def test_anmeldetoken_tritt_an_die_stelle_des_kennworts() -> None:
    api, gesehen = make_api(_erfolg, MutableTokenProvider())
    async with api:
        await api.session.login("benutzer", login_token="zweiterFaktor")

    kopf = headers_of(gesehen[-1])
    assert kopf[b"logintoken"] == b"zweiterFaktor"
    assert b"password" not in kopf


async def test_dashboard_anmeldung_schickt_nur_dbapikey() -> None:
    api, gesehen = make_api(_erfolg, MutableTokenProvider())
    async with api:
        ergebnis = await api.session.login_with_dashboard_key("schluessel")

    kopf = headers_of(gesehen[-1])
    assert kopf[b"dbapikey"] == b"schluessel"
    # Steht user oder password daneben, nimmt der Server einen anderen Zweig.
    assert b"user" not in kopf and b"password" not in kopf
    assert ergebnis.api_key == "Bearer sitzung"


async def test_404_weicht_auf_den_dokumentierten_weg_aus() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        if request.url.path.endswith(LOGIN_PATH):
            return httpx.Response(404)
        return httpx.Response(200, json=ERFOLG)

    api, gesehen = make_api(handler, MutableTokenProvider())
    async with api:
        ergebnis = await api.session.login("benutzer", "kennwort")

    assert ergebnis.login_path == DOCUMENTED_LOGIN_PATH
    assert str(gesehen[-1].url).startswith(BASE + DOCUMENTED_LOGIN_PATH)
    assert json.loads(gesehen[-1].read()) == {
        "username": "benutzer",
        "password": "kennwort",
        "token": "",
    }


async def test_abgelehnte_anmeldung_kommt_mit_200_und_traegt_den_code() -> None:
    abgelehnt = {
        "meta": {"text": "Unsuccesful login attempt"},
        "content": {"detailMessage": "LOGIN_ERROR_INVALID_USERNAME_OR_PASSWORD"},
    }
    api, _ = make_api(lambda _: httpx.Response(200, json=abgelehnt), MutableTokenProvider())
    async with api:
        with pytest.raises(TanssApiError) as fehler:
            await api.session.login("benutzer", "falsch")

    assert fehler.value.error_code == "LOGIN_ERROR_INVALID_USERNAME_OR_PASSWORD"
    assert fehler.value.status_code == 200
    assert str(fehler.value) == "Unsuccesful login attempt"


async def test_leere_antwort_meldet_den_eigenen_code() -> None:
    api, _ = make_api(lambda _: httpx.Response(200, content=b""), MutableTokenProvider())
    async with api:
        with pytest.raises(TanssApiError) as fehler:
            await api.session.login("benutzer", "kennwort")

    assert fehler.value.error_code == TanssLoginResult.EMPTY_RESPONSE_CODE
    assert fehler.value.status_code == 200


async def test_steuerzeichen_in_den_zugangsdaten_wird_abgewiesen() -> None:
    api, gesehen = make_api(_erfolg, MutableTokenProvider())
    async with api:
        with pytest.raises(ValueError):
            await api.session.login("benutzer", "kenn\nwort")

    assert gesehen == []


async def test_erneuerung_schickt_refreshtoken_und_kein_apitoken() -> None:
    halter = MutableTokenProvider("Bearer alt")
    api, gesehen = make_api(_erfolg, halter)
    async with api:
        ergebnis = await api.session.refresh("Bearer erneuerung")

    kopf = headers_of(gesehen[-1])
    assert gesehen[-1].method == "GET"
    assert kopf[b"refreshtoken"] == b"Bearer erneuerung"
    # Dasselbe Token in apiToken antwortet 403 (gegen TANSS 10.10 gemessen).
    assert b"apitoken" not in kopf
    assert ergebnis.login_path is None
    assert halter.token == "Bearer sitzung"


async def test_praegen_reicht_die_parameter_durch_und_liefert_das_token() -> None:
    antwort = {"meta": {}, "content": {"apiToken": "Bearer gepraegt"}}
    api, gesehen = make_api(
        lambda _: httpx.Response(200, json=antwort), MutableTokenProvider("sitzung")
    )
    async with api:
        token = await api.session.mint("tanss_app", duration=1000, info="Test", is_for_testing=True)

    adresse = str(gesehen[-1].url)
    assert token == "Bearer gepraegt"
    assert "/api/v1/jwts/tanss_app?" in adresse
    assert "duration=1000" in adresse
    assert "info=Test" in adresse
    assert "isForTesting=true" in adresse
    # Gepraegt wird mit dem Sitzungstoken; die Route verlangt die Rolle USER.
    assert gesehen[-1].headers["apiToken"] == "Bearer sitzung"
