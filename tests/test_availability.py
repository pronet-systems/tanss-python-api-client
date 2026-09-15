"""Der mitgelieferte Endpunkt-Index: dokumentiert, vorhanden, erreichbar - oder gar nicht gefuehrt."""

from __future__ import annotations

import json
from importlib import resources

from tanss_api import ApiAvailability


def _packaged_index() -> dict:
    """Der Index, wie er im Paket liegt - dieselbe Quelle, die die Klasse liest."""
    raw = resources.files("tanss_api").joinpath(ApiAvailability.RESOURCE_NAME).read_text(encoding="utf-8")
    return json.loads(raw)


def test_die_zahl_der_eintraege_stimmt_mit_dem_paket_ueberein() -> None:
    index = _packaged_index()

    assert ApiAvailability.count() == index["count"]
    assert ApiAvailability.count() == len(index["operations"])
    assert ApiAvailability.server_version() == index["serverVersion"]


def test_eine_dokumentierte_und_vorhandene_route() -> None:
    # GET /api/v1/tickets/own: in der offiziellen Schnittstellenbeschreibung gefuehrt, auf 10.10
    # vorhanden und mit dem Login-Token erreichbar.
    assert ApiAvailability.is_known("GET", "/api/v1/tickets/own")
    assert ApiAvailability.is_documented("GET", "/api/v1/tickets/own")
    assert ApiAvailability.is_available_on_1010("GET", "/api/v1/tickets/own")
    assert ApiAvailability.is_reachable_on_1010("GET", "/api/v1/tickets/own")
    assert ApiAvailability.token_class("GET", "/api/v1/tickets/own") == "general"
    assert "USER" in ApiAvailability.roles("GET", "/api/v1/tickets/own")


def test_eine_dokumentierte_route_die_nicht_erreichbar_ist() -> None:
    # GET /api/v1/bankaccounts steht in der Schnittstellenbeschreibung und ist auf 10.10 auch
    # vorhanden - nur passt keine Regel der Sicherheitskonfiguration, also kommt kein Token hin.
    assert ApiAvailability.is_documented("GET", "/api/v1/bankaccounts")
    assert ApiAvailability.is_available_on_1010("GET", "/api/v1/bankaccounts")
    assert not ApiAvailability.is_reachable_on_1010("GET", "/api/v1/bankaccounts")
    assert ApiAvailability.token_class("GET", "/api/v1/bankaccounts") == ApiAvailability.DENIED_TOKEN_CLASS

    # GET /api/v1/sla ist dokumentiert, auf 10.10 aber gar nicht erst vorhanden.
    assert ApiAvailability.is_documented("GET", "/api/v1/sla")
    assert not ApiAvailability.is_available_on_1010("GET", "/api/v1/sla")
    assert not ApiAvailability.is_reachable_on_1010("GET", "/api/v1/sla")


def test_eine_route_die_der_index_nicht_kennt() -> None:
    assert not ApiAvailability.is_known("GET", "/api/v1/gibtesnicht")
    assert not ApiAvailability.is_documented("GET", "/api/v1/gibtesnicht")
    assert not ApiAvailability.is_available_on_1010("GET", "/api/v1/gibtesnicht")
    assert not ApiAvailability.is_reachable_on_1010("GET", "/api/v1/gibtesnicht")
    assert ApiAvailability.token_class("GET", "/api/v1/gibtesnicht") is None
    assert ApiAvailability.roles("GET", "/api/v1/gibtesnicht") == ()
    assert ApiAvailability.operation_id("GET", "/api/v1/gibtesnicht") is None


def test_platzhalter_zaehlen_ihre_namen_nicht() -> None:
    # Derselbe Eintrag, dreimal geschrieben - und ein woertlicher Pfad hat Vorrang.
    assert ApiAvailability.is_known("GET", "/api/v1/tickets/{ticketId}")
    assert ApiAvailability.is_known("get", "/api/v1/tickets/{id}")
    assert ApiAvailability.is_known("GET", "/api/v1/tickets/4711?loggedInUserId=42")
    assert ApiAvailability.operation_id("GET", "/api/v1/tickets/own") != ApiAvailability.operation_id(
        "GET", "/api/v1/tickets/4711"
    )


def test_eine_nur_auf_dem_server_gefundene_route_ist_nicht_dokumentiert() -> None:
    # GET /api/v1/todos bedient die Instanz, die offizielle Schnittstellenbeschreibung fuehrt sie
    # nicht.
    assert ApiAvailability.is_known("GET", "/api/v1/todos")
    assert not ApiAvailability.is_documented("GET", "/api/v1/todos")
    assert ApiAvailability.is_reachable_on_1010("GET", "/api/v1/todos")
