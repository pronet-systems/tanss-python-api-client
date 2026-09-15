# =============================================================================================
# **WARNUNG: DIESE PROBEN DUERFEN NIEMALS SCHREIBEND AUF EINE TANSS-INSTANZ ZUGREIFEN.** Sie laufen
# gegen eine **echte, produktive** Instanz. Erlaubt sind ausschliesslich lesende Aufrufe: GET, der
# Anmelde-POST auf dem Anmeldepfad und die PUT-Routen, die in Wahrheit Abfragen sind (etwa
# PUT /api/v1/tickets mit einem Filter). Jeder Aufruf, der Daten anlegt, aendert oder loescht - POST,
# PUT, PATCH, DELETE auf Nutzdaten -, hat hier nichts zu suchen, auch nicht "nur zum Ausprobieren" und
# auch nicht hinter einem Schalter. Wer das aendern will, legt eine eigene Sammlung gegen eine
# Testinstanz an. Grundlage: die gegen TANSS 10.10 gemessenen Befunde, alle lesend.
# =============================================================================================
"""Haelt die gemessenen Befunde gegen eine laufende Instanz fest.

Jede Probe meldet sich selbst an und gibt ihren Zugang wieder frei; die Proben sind damit voneinander
unabhaengig. Ohne ``TANSS_BASE_URL``, ``TANSS_USER`` und ``TANSS_PASSWORD`` werden sie uebersprungen.
"""

from __future__ import annotations

import os
import uuid
from datetime import datetime, timezone
from urllib.parse import urlsplit

import httpx
import pytest
from kiota_abstractions.api_error import APIError

from tanss_api import (
    MutableTokenProvider,
    StaticTokenProvider,
    TanssApi,
    TanssApiError,
    TanssApiOptions,
    TokenRole,
    required_for,
)
from tanss_api.rest.models.ticket_configuration import TicketConfiguration
from tanss_api.session import LOGIN_PATH
from tanss_api.tokens import API_TOKEN_HEADER, BEARER_PREFIX

BASE_URL_VARIABLE = "TANSS_BASE_URL"
"""Die vollstaendige Basis der Schnittstelle, etwa ``https://tanss.example.de/backend``."""

USER_VARIABLE = "TANSS_USER"
"""Der Anmeldename."""

PASSWORD_VARIABLE = "TANSS_PASSWORD"
"""Das Kennwort."""

DASHBOARD_KEY_VARIABLE = "TANSS_DBAPIKEY"
"""Der Dashboard-Schluessel eines Mitarbeiters - **zusaetzlich** und **freiwillig**.

Die Schnittstelle gibt ihn nicht heraus; er wird in der TANSS-Verwaltung gepflegt. Ohne ihn wird nur
die eine Probe uebersprungen, die einen gueltigen Schluessel braucht.
"""


def _wert(name: str) -> str | None:
    """Eine Umgebungsvariable ohne Randleerraum; ``None``, wenn sie leer ist."""
    wert = (os.environ.get(name) or "").strip()
    return wert or None


BASE_URL = _wert(BASE_URL_VARIABLE)
USER = _wert(USER_VARIABLE)
PASSWORD = _wert(PASSWORD_VARIABLE)
DASHBOARD_KEY = _wert(DASHBOARD_KEY_VARIABLE)


def _brauchbar() -> bool:
    """Sind alle drei Variablen gesetzt und ist die Adresse absolut?"""
    if not BASE_URL or not USER or not PASSWORD:
        return False
    teile = urlsplit(BASE_URL)
    return teile.scheme in ("http", "https") and bool(teile.netloc)


KONFIGURIERT = _brauchbar()

UEBERSPRUNGEN = pytest.mark.skipif(
    not KONFIGURIERT,
    reason=(
        f"Live-Probe: setze {BASE_URL_VARIABLE}, {USER_VARIABLE} und {PASSWORD_VARIABLE}, um sie "
        "laufen zu lassen."
    ),
)

OHNE_SCHLUESSEL = pytest.mark.skipif(
    not KONFIGURIERT or not DASHBOARD_KEY,
    reason=(
        f"Live-Probe: setze zusaetzlich {DASHBOARD_KEY_VARIABLE} (der Dashboard-Schluessel aus der "
        "TANSS-Verwaltung), um sie laufen zu lassen."
    ),
)


def _optionen() -> TanssApiOptions:
    """Die Einstellungen fuer den Zugang - bewusst **ohne** Mitarbeiter-Id.

    Ein Anmeldetoken fuehrt den Mitarbeiter im Anspruch ``sub``; ``loggedInUserId`` ist dann weder
    noetig noch wirksam (gegen TANSS 10.10 gemessen). Die Live-Proben lassen ihn deshalb weg und
    pruefen damit zugleich, dass es ohne ihn geht.
    """
    return TanssApiOptions(base_url=BASE_URL or "", employee_id=None, timeout=30.0)


async def _angemeldet():
    """Meldet sich an und liefert den fertigen Zugang samt Anmeldeergebnis."""
    api = TanssApi.create(_optionen(), MutableTokenProvider())
    try:
        anmeldung = await api.session.login(USER or "", PASSWORD or "")
    except BaseException:
        await api.aclose()
        raise
    return api, anmeldung


class _OhnePraefix(httpx.AsyncBaseTransport):
    """Schneidet das Praefix ``Bearer`` aus der Kopfzeile ``apiToken`` - nur, um die Ablehnung
    nachzustellen. Die Schicht sitzt unter der Middleware-Kette und sieht die fertige Anfrage."""

    def __init__(self, inner: httpx.AsyncBaseTransport) -> None:
        self._inner = inner

    async def handle_async_request(self, request: httpx.Request) -> httpx.Response:
        wert = request.headers.get(API_TOKEN_HEADER)
        if wert:
            request.headers[API_TOKEN_HEADER] = wert.replace(BEARER_PREFIX, "")
        return await self._inner.handle_async_request(request)

    async def aclose(self) -> None:
        await self._inner.aclose()


@UEBERSPRUNGEN
async def test_die_anmeldung_liefert_ein_bearer_token_und_eine_mitarbeiter_id() -> None:
    # POST auf den gemessenen Anmeldepfad mit den Kopfzeilen user und password antwortet 200;
    # apiKey und refresh tragen beide das Praefix "Bearer ".
    api, anmeldung = await _angemeldet()
    async with api:
        assert anmeldung.api_key.startswith(BEARER_PREFIX)
        assert anmeldung.refresh.startswith(BEARER_PREFIX)
        assert anmeldung.employee_id > 0
        assert anmeldung.expires_at > datetime.now(timezone.utc)
        # Auf 10.10 traegt der gemessene Weg; der dokumentierte Pfad ist dort 404.
        assert anmeldung.login_path == LOGIN_PATH


@UEBERSPRUNGEN
async def test_der_erzeugte_client_erreicht_ownstate() -> None:
    # apiToken mit Praefix -> 200, und ohne loggedInUserId, weil ein ACCESS-Token den Mitarbeiter
    # im Anspruch sub traegt.
    api, anmeldung = await _angemeldet()
    async with api:
        zustand = await api.rest.api.v1.employees.own_state.get()

        assert zustand is not None
        assert zustand.content is not None
        assert zustand.content.logged_in_user is not None
        assert zustand.content.logged_in_user.id == anmeldung.employee_id


@UEBERSPRUNGEN
async def test_ohne_das_praefix_bearer_antwortet_tanss_mit_403() -> None:
    # "apiToken: <jwt>" ohne Praefix -> 403 mit leerem Rumpf. Die Bibliothek setzt das Praefix von
    # sich aus; um die Messung nachzustellen, wird es unmittelbar vor der Leitung abgeschnitten.
    api, anmeldung = await _angemeldet()
    async with api:
        roh = anmeldung.api_key[len(BEARER_PREFIX):]
        transport = _OhnePraefix(httpx.AsyncHTTPTransport())
        client = httpx.AsyncClient(transport=transport, base_url=BASE_URL or "", timeout=30.0)
        async with TanssApi.create(_optionen(), StaticTokenProvider(roh), http_client=client) as ohne:
            with pytest.raises(APIError) as fehler:
                await ohne.rest.api.v1.employees.own_state.get()

            assert fehler.value.response_status_code == 403
        await client.aclose()


@UEBERSPRUNGEN
async def test_ein_modul_praefix_bleibt_dem_anmeldetoken_verschlossen() -> None:
    # Mit dem Anmeldetoken antworten alle modulgebundenen Praefixe 403 - hier /api/erp/v1/customers,
    # das ein ERP-Token verlangt.
    api, _ = await _angemeldet()
    async with api:
        assert required_for("/api/erp/v1/customers") is TokenRole.ERP_OR_CENTRON

        with pytest.raises(APIError) as fehler:
            await api.rest.api.erp.v1.customers.get()

        assert fehler.value.response_status_code == 403


@UEBERSPRUNGEN
async def test_eine_gesperrte_route_bleibt_gesperrt() -> None:
    # /api/v1/sla antwortet 403, obwohl die offizielle Schnittstellenbeschreibung die Route
    # beschreibt: Die Sicherheitskonfiguration zaehlt die USER-Module einzeln auf und endet mit
    # denyAll.
    api, _ = await _angemeldet()
    async with api:
        assert required_for("/api/v1/sla") is TokenRole.DENIED

        with pytest.raises(APIError) as fehler:
            await api.rest.api.v1.sla.get()

        assert fehler.value.response_status_code == 403


@UEBERSPRUNGEN
async def test_die_route_todos_antwortet_wie_modelliert() -> None:
    # GET /api/v1/todos -> 200, content = {id, employeeId, choosenListId, lists[]} - genau so setzt
    # der Server es um (gegen 10.10 geprueft), obwohl die Route nicht dokumentiert ist.
    api, anmeldung = await _angemeldet()
    async with api:
        todos = await api.rest.api.v1.todos.get()

        assert todos is not None
        assert todos.content is not None
        assert todos.content.id is not None
        assert todos.content.employee_id == anmeldung.employee_id
        assert todos.content.lists is not None


@UEBERSPRUNGEN
async def test_die_erneuerung_laeuft_ueber_die_kopfzeile_refreshtoken() -> None:
    # Erneuerungstoken in refreshToken, ohne apiToken, auf einer beliebigen Nicht-Anmelderoute
    # -> 200 mit vollstaendigem Anmeldeergebnis.
    api, anmeldung = await _angemeldet()
    async with api:
        erneuert = await api.session.refresh(anmeldung.refresh)

        assert erneuert.api_key.startswith(BEARER_PREFIX)
        assert erneuert.refresh.startswith(BEARER_PREFIX)
        assert erneuert.employee_id == anmeldung.employee_id
        assert erneuert.expire >= anmeldung.expire

        # Der veraenderliche Anbieter traegt danach das neue Token; ein Aufruf damit geht.
        zustand = await api.rest.api.v1.employees.own_state.get()
        assert zustand is not None and zustand.content is not None


@UEBERSPRUNGEN
async def test_eine_listenabfrage_ist_ein_put_und_trotzdem_lesend() -> None:
    # PUT /api/v1/tickets mit einem Filter antwortet 200. Das PUT ist hier die Abfrage - es legt
    # nichts an und aendert nichts; deshalb ist es der einzige Nicht-GET neben der Anmeldung, der
    # hier stehen darf.
    api, anmeldung = await _angemeldet()
    async with api:
        filter_ = TicketConfiguration()
        filter_.staff = [anmeldung.employee_id]
        filter_.items_per_page = 3
        filter_.page = 0

        assert await api.rest.api.v1.tickets.put(filter_) is not None


@UEBERSPRUNGEN
async def test_ein_erfundener_dashboard_schluessel_meldet_no_user_for_dashboard() -> None:
    # Allein mit der Kopfzeile dbapikey nimmt der Server den Dashboard-Zweig. Ein Schluessel, den
    # kein Mitarbeiter traegt, antwortet mit HTTP 200 und LOGIN_ERROR_NO_USER_FOR_DASHBOARD - genau
    # das beweist, dass der Weg bedient wird. Ein echter Schluessel ist dafuer nicht noetig.
    async with TanssApi.create(_optionen(), MutableTokenProvider()) as api:
        with pytest.raises(TanssApiError) as fehler:
            await api.session.login_with_dashboard_key(
                "kein-mitarbeiter-hat-diesen-schluessel-" + uuid.uuid4().hex
            )

    assert fehler.value.error_code == "LOGIN_ERROR_NO_USER_FOR_DASHBOARD"
    assert fehler.value.status_code == 200
    assert str(fehler.value) == "Unsuccesful login attempt"


@OHNE_SCHLUESSEL
async def test_ein_gueltiger_dashboard_schluessel_meldet_an() -> None:
    # Mit einem Schluessel aus der TANSS-Verwaltung kommt ein gewoehnliches ACCESS-Token heraus -
    # nur mit dem Anspruch dashboardLogin = true.
    async with TanssApi.create(_optionen(), MutableTokenProvider()) as api:
        anmeldung = await api.session.login_with_dashboard_key(DASHBOARD_KEY or "")

    assert anmeldung.api_key.startswith(BEARER_PREFIX)
    assert anmeldung.employee_id > 0
    assert anmeldung.login_path == LOGIN_PATH
