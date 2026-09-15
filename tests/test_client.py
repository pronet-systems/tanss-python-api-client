"""Was die Verbindungsschicht an jede Anfrage haengt: Kopfzeile, Parameter, Wiederholung."""

from __future__ import annotations

import httpx
import pytest

from tanss_api import MutableTokenProvider, StaticTokenProvider, TanssApi, TanssApiOptions

from .conftest import BASE, make_api


def _leer(_: httpx.Request) -> httpx.Response:
    return httpx.Response(200, json={"meta": {}, "content": []})


async def test_das_praefix_bearer_steht_genau_einmal() -> None:
    api, gesehen = make_api(_leer, StaticTokenProvider("rohesJwt"))
    async with api:
        await api.rest.api.v1.tickets.own.get()

    wert = gesehen[-1].headers["apiToken"]
    assert wert == "Bearer rohesJwt"
    assert wert.count("Bearer") == 1


async def test_ein_mitgebrachtes_praefix_wird_nicht_verdoppelt() -> None:
    api, gesehen = make_api(_leer, StaticTokenProvider("Bearer ausDerAnmeldung"))
    async with api:
        await api.rest.api.v1.tickets.own.get()

    assert gesehen[-1].headers["apiToken"] == "Bearer ausDerAnmeldung"
    assert gesehen[-1].headers["apiToken"].count("Bearer") == 1


async def test_ohne_token_keine_kopfzeile() -> None:
    api, gesehen = make_api(_leer, StaticTokenProvider(None))
    async with api:
        await api.rest.api.v1.tickets.own.get()

    assert "apiToken" not in gesehen[-1].headers


async def test_user_route_traegt_loggedinuserid() -> None:
    api, gesehen = make_api(_leer, StaticTokenProvider("t"))
    async with api:
        await api.rest.api.v1.tickets.own.get()

    assert str(gesehen[-1].url) == f"{BASE}/api/v1/tickets/own?loggedInUserId=42"


async def test_ein_modul_praefix_bekommt_keinen_parameter() -> None:
    # /api/tanss.x/v1/... verlangt ein TANSS_APP-Token; dessen Traeger kennt keinen Mitarbeiter,
    # den der Parameter benennen koennte. Gesendet wird ueber die Verbindungsschicht der
    # Bibliothek, damit die Middleware-Kette dieselbe ist wie beim erzeugten Client.
    api, gesehen = make_api(_leer, StaticTokenProvider("t"))
    async with api:
        await api.http.get(f"{BASE}/api/tanss.x/v1/supports")
        await api.rest.api.erp.v1.customers.get()

    assert "loggedInUserId" not in str(gesehen[0].url)
    assert "loggedInUserId" not in str(gesehen[1].url)


async def test_ein_eigener_wert_bleibt_stehen() -> None:
    # Wer loggedInUserId selbst angibt, meint einen anderen Mitarbeiter.
    api, gesehen = make_api(_leer, StaticTokenProvider("t"))
    async with api:
        await api.http.get(f"{BASE}/api/v1/tickets/own?loggedInUserId=99")

    adresse = str(gesehen[-1].url)
    assert "loggedInUserId=99" in adresse
    assert "loggedInUserId=42" not in adresse


async def test_ohne_mitarbeiter_id_haengt_nichts_an() -> None:
    api, gesehen = make_api(_leer, StaticTokenProvider("t"), employee_id=None)
    async with api:
        await api.rest.api.v1.tickets.own.get()

    assert "loggedInUserId" not in str(gesehen[-1].url)


async def test_ein_lesender_aufruf_wird_wiederholt(monkeypatch: pytest.MonkeyPatch) -> None:
    async def sofort(_: float) -> None:
        return None

    monkeypatch.setattr("tanss_api.api.asyncio.sleep", sofort)

    antworten = [httpx.Response(503), httpx.Response(200, json={"meta": {}, "content": []})]
    api, gesehen = make_api(lambda _: antworten.pop(0), StaticTokenProvider("t"))
    async with api:
        await api.rest.api.v1.tickets.own.get()

    assert len(gesehen) == 2


async def test_das_praegen_wird_nie_wiederholt(monkeypatch: pytest.MonkeyPatch) -> None:
    async def sofort(_: float) -> None:
        return None

    monkeypatch.setattr("tanss_api.api.asyncio.sleep", sofort)

    api, gesehen = make_api(lambda _: httpx.Response(503), MutableTokenProvider("t"))
    async with api:
        with pytest.raises(Exception):
            await api.session.mint("tanss_app")

    assert len(gesehen) == 1


async def test_eine_uebergebene_verbindungsschicht_bleibt_offen() -> None:
    api, _ = make_api(_leer, StaticTokenProvider("t"))
    async with api:
        pass

    assert not api.http.is_closed
    await api.http.aclose()


async def test_eine_verbindungsschicht_ohne_basisadresse_bekommt_sie() -> None:
    gesehen: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        gesehen.append(request)
        return httpx.Response(200, json={"meta": {}, "content": []})

    client = httpx.AsyncClient(transport=httpx.MockTransport(handler))
    optionen = TanssApiOptions(base_url=BASE, employee_id=7)

    async with TanssApi.create(optionen, StaticTokenProvider("t"), http_client=client) as api:
        assert str(api.http.base_url).rstrip("/") == BASE
        await api.rest.api.v1.todos.get()

    assert str(gesehen[-1].url) == f"{BASE}/api/v1/todos?loggedInUserId=7"
    await client.aclose()


def test_die_basisadresse_muss_absolut_sein() -> None:
    with pytest.raises(ValueError):
        TanssApiOptions(base_url="tanss.example.de/backend")


def test_der_veraenderliche_anbieter_gibt_den_neuen_wert_heraus() -> None:
    anbieter = MutableTokenProvider()
    assert anbieter.get_token() is None
    anbieter.token = "Bearer neu"
    assert anbieter.get_token() == "Bearer neu"
