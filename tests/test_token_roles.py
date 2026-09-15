"""Die Praefix-Tabelle des Servers (gegen TANSS 10.10 geprueft), Zeile fuer Zeile."""

from __future__ import annotations

import pytest

from tanss_api import TokenRole, includes_user, is_reachable_with_login_token, required_for


@pytest.mark.parametrize(
    ("path", "expected"),
    [
        ("/api/v1/tickets/own", TokenRole.USER),
        ("/api/v1/tickets/own?loggedInUserId=42", TokenRole.USER),
        ("/api/v1/timers/", TokenRole.USER),
        ("/api/erp/v1/customers", TokenRole.ERP_OR_CENTRON),
        ("/api/tanss.x/v1/supports", TokenRole.TANSS_APP),
        ("/api/tanss.app/v1/supports", TokenRole.TANSS_APP),
        ("/api/v1/login", TokenRole.NONE),
        ("/api/v1/login/", TokenRole.NONE),
        ("/foo", TokenRole.DENIED),
        ("/api/v1", TokenRole.DENIED),
        ("/api/v2/tickets", TokenRole.DENIED),
        ("/api/systemhaus_one/v1/x", TokenRole.SYSTEMHAUS_ONE),
        ("/api/coero/v1", TokenRole.COERO),
        ("/api/calls/v1/calls", TokenRole.PHONE),
        ("/api/remoteSupports/v1/remoteSupports", TokenRole.REMOTE_SUPPORT),
        ("/api/monitoring/v1/x", TokenRole.MONITORING),
        ("/api/timestamps/v1/x", TokenRole.TIMESTAMP),
        ("/api/deviceManagement/v1/x", TokenRole.DEVICE_MANAGEMENT),
        ("/api/servereye/v1/x", TokenRole.SERVEREYE),
        # Sonderzeilen unter /api/v1 stehen vor den uebrigen Zeilen.
        ("/api/v1/offers/17", TokenRole.USER_OR_OFFER),
        ("/api/v1/cache", TokenRole.USER_OR_PHP),
        ("/api/v1/util/languages", TokenRole.USER_OR_LANDING_PAGE),
        ("/api/v1/util/files/x", TokenRole.NONE),
        ("/api/v1/util/other", TokenRole.USER),
        ("/api/v1/landingPage/ticketWorkflow/x", TokenRole.LANDING_PAGE_TICKET_WORKFLOW),
        ("/api/v1/landingPage/contractWorkflow", TokenRole.LANDING_PAGE_CONTRACT_WORKFLOW),
        ("/actuator/health", TokenRole.ACTUATOR),
        ("/api/v1/cloud/isTokenValid/x", TokenRole.NONE),
        ("/api/v1/cloud/other", TokenRole.USER),
        # Zwei Abschnitte unter /api/v1/starface/inc sind frei, einer allein nicht.
        ("/api/v1/starface/inc/5/abc", TokenRole.NONE),
        ("/api/v1/starface/inc/5", TokenRole.USER),
        ("/.well-known/jwks.json", TokenRole.NONE),
        # Der Praefixvergleich ist abschnittsweise: /api/v1/loginX ist nicht /api/v1/login.
        ("/api/v1/loginX", TokenRole.DENIED),
        ("/api/erp/v1x/customers", TokenRole.DENIED),
        # Eine vollstaendige Adresse wird ab dem ersten /api/ gelesen.
        ("https://tanss.example.de/backend/api/erp/v1/customers", TokenRole.ERP_OR_CENTRON),
        ("https://tanss.example.de/backend/api/v1/tickets/own", TokenRole.USER),
    ],
)
def test_die_rolle_folgt_der_ersten_passenden_zeile(path: str, expected: TokenRole) -> None:
    assert required_for(path) == expected


@pytest.mark.parametrize(
    ("path", "expected"),
    [
        ("/api/v1/tickets/own", True),
        ("/api/v1/login", True),
        ("/api/v1/offers/1", True),
        ("/api/erp/v1/customers", False),
        ("/api/tanss.x/v1/supports", False),
        ("/api/remoteSupports/v1/remoteSupports", False),
        ("/foo", False),
    ],
)
def test_das_login_token_oeffnet_nur_die_user_praefixe(path: str, expected: bool) -> None:
    assert is_reachable_with_login_token(path) == expected


@pytest.mark.parametrize(
    ("role", "expected"),
    [
        # Die Bedingung, unter der loggedInUserId angehaengt wird (vom Server so umgesetzt, gegen
        # 10.10 geprueft).
        (TokenRole.USER, True),
        (TokenRole.USER_OR_OFFER, True),
        (TokenRole.USER_OR_PHP, True),
        (TokenRole.USER_OR_LANDING_PAGE, True),
        (TokenRole.NONE, False),
        (TokenRole.DENIED, False),
        (TokenRole.TANSS_APP, False),
        (TokenRole.ERP_OR_CENTRON, False),
        (TokenRole.REMOTE_SUPPORT, False),
        (TokenRole.ACTUATOR, False),
    ],
)
def test_user_steckt_nur_in_den_user_rollen(role: TokenRole, expected: bool) -> None:
    assert includes_user(role) == expected
