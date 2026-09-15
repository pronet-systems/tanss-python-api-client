"""Die Formen, in denen TANSS einen Fehler ausweist - und die, in der es gar nichts sagt."""

from __future__ import annotations

import json

from tanss_api import TanssApiError


def test_der_fachliche_umschlag_wird_gelesen() -> None:
    rumpf = json.dumps(
        {
            "error": {
                "text": "CANT_CHECK_ITEM_TWICE",
                "localizedText": "Der Punkt ist bereits abgehakt.",
                "thrownExceptionMessage": None,
                "type": "TnsException",
                "traceId": "a1b2c3",
            }
        }
    )

    fehler = TanssApiError.from_response(400, rumpf)

    assert fehler.error_code == "CANT_CHECK_ITEM_TWICE"
    assert fehler.localized_text == "Der Punkt ist bereits abgehakt."
    assert fehler.trace_id == "a1b2c3"
    assert fehler.status_code == 400
    assert fehler.problem_title is None
    assert fehler.raw_body == rumpf
    assert "CANT_CHECK_ITEM_TWICE" in str(fehler)


def test_das_problem_dokument_wird_gelesen_und_liefert_keinen_fachlichen_code() -> None:
    # RFC 7807: die Form, in der schon die Rahmenanwendung abweist (gegen TANSS 10.10 gemessen).
    rumpf = json.dumps(
        {
            "type": "about:blank",
            "title": "Bad Request",
            "status": 400,
            "detail": "Failed to convert 'id' with value: 'abc'",
            "instance": "/api/v1/tickets/abc",
        }
    )

    fehler = TanssApiError.from_response(400, rumpf)

    assert fehler.problem_title == "Bad Request"
    assert fehler.localized_text == "Failed to convert 'id' with value: 'abc'"
    # title ist die Fassung des Statuscodes und darf nicht als TANSS-Code durchgehen.
    assert fehler.error_code is None
    assert fehler.trace_id is None


def test_meta_text_und_detailmessage_werden_mitgelesen() -> None:
    rumpf = json.dumps(
        {
            "meta": {"text": "Unsuccesful login attempt"},
            "content": {"detailMessage": "LOGIN_ERROR_NO_USER_FOR_DASHBOARD"},
        }
    )

    fehler = TanssApiError.from_response(200, rumpf)

    assert fehler.error_code == "LOGIN_ERROR_NO_USER_FOR_DASHBOARD"
    assert fehler.localized_text == "Unsuccesful login attempt"


def test_ein_leerer_403_rumpf_nennt_wenigstens_den_grund() -> None:
    # TANSS beantwortet jede Ablehnung mit leerem Rumpf; zu lesen gibt es dann nichts.
    fehler = TanssApiError.from_response(403, "")

    assert fehler.status_code == 403
    assert fehler.error_code is None
    assert TanssApiError.try_parse(403, "") is None
    meldung = str(fehler)
    assert "HTTP 403 (FORBIDDEN)" in meldung
    assert "leerem Rumpf" in meldung
    assert "Bearer" in meldung and "apiToken" in meldung


def test_ein_fremder_rumpf_bleibt_erhalten() -> None:
    fehler = TanssApiError.from_response(500, "<html>Proxy</html>")

    assert fehler.raw_body == "<html>Proxy</html>"
    assert fehler.error_code is None
    assert "HTTP 500" in str(fehler)
