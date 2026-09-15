"""Eine Antwort, die TANSS als Fehler ausgewiesen hat."""

from __future__ import annotations

import json
from http import HTTPStatus
from typing import Any


def _text(owner: Any, name: str) -> str | None:
    """Der Wert eines Feldes, wenn es eine Zeichenkette ist; sonst ``None``."""
    if isinstance(owner, dict):
        value = owner.get(name)
        if isinstance(value, str):
            return value
    return None


def _status_text(status_code: int) -> str:
    """``HTTP 403 (FORBIDDEN)``: Statuszahl und der Name, den Python dafuer kennt."""
    try:
        return f"HTTP {status_code} ({HTTPStatus(status_code).name})"
    except ValueError:
        return f"HTTP {status_code}"


class TanssApiError(Exception):
    """Ein Fehler der Schnittstelle, in einer der Formen, die eine 10.10-Instanz gemessen liefert.

    **Der fachliche Umschlag.** Die Schnittstellenbeschreibung kennt fuer Fehler eine wiederverwendete
    Antwort: ein Objekt mit der einen Eigenschaft ``error``, darin ``text``, ``localizedText``,
    ``thrownExceptionMessage`` und ``type``. Gegen TANSS 10.10 gemessen kommt ein fuenftes Feld hinzu:
    ``traceId``.

    **Der Code steckt in ``error.text``.** Dessen Beschreibung sagt es woertlich: ein stabiler
    Fehlercode, etwa ``CANT_CHECK_ITEM_TWICE``, gedacht fuer die maschinelle Auswertung, nicht
    ``localizedText``. Er steht hier in :attr:`error_code`.

    **Die zweite Form: RFC 7807.** Fehler, die schon die Rahmenanwendung abweist, etwa ein
    Pfadparameter vom falschen Typ, kommen nicht im TANSS-Umschlag, sondern als
    "problem detail"-Dokument ``{type, title, status, detail, instance}`` (gegen TANSS 10.10 gemessen).
    Ein Client muss beide lesen koennen. Diese Klasse haelt es so: :attr:`error_code` bleibt dabei
    ``None``, denn ``title`` ("Bad Request") ist kein stabiler TANSS-Code und darf nicht als einer
    durchgehen; der ``title`` steht in :attr:`problem_title` und macht die Form erkennbar, ``detail``
    steht in :attr:`localized_text`, und ``type``, ``status`` und ``instance`` stehen unveraendert in
    :attr:`raw_body`.

    **Zwei weitere Formen werden mitgelesen:** das Feld ``meta.text``, das etwa die 403-Antwort der
    Tagesabschluesse traegt, sowie ``content.detailMessage`` der abgelehnten Anmeldung
    (``LOGIN_ERROR_INVALID_USERNAME_OR_PASSWORD``), die gegen TANSS 10.10 gemessen mit HTTP 200 kommt.

    **Und die dritte Form ist gar keine.** Jede Ablehnung, also fehlendes Token, fehlendes Praefix
    ``Bearer``, ``Authorization`` statt ``apiToken``, ein Modul-Praefix ohne dessen Rolle oder eine von
    der Sicherheitskonfiguration des Servers gesperrte Route, kommt mit **leerem Rumpf** (gegen TANSS
    10.10 gemessen). Dafuer gibt es nichts zu lesen; :meth:`from_response` schreibt den Grund in die
    Meldung.
    """

    def __init__(
        self,
        message: str,
        status_code: int | None = None,
        error_code: str | None = None,
        localized_text: str | None = None,
        trace_id: str | None = None,
        raw_body: str | None = None,
        problem_title: str | None = None,
    ) -> None:
        """Baut den Fehler aus dem, was die Antwort hergab.

        :param message: Der Text fuer den Aufrufer.
        :param status_code: Der HTTP-Status der Antwort; ``None``, wenn es keinen gab.
        :param error_code: Der maschinenlesbare Code aus ``error.text`` beziehungsweise
            ``content.detailMessage``.
        :param localized_text: Der lesbare Text aus ``error.localizedText``, ``meta.text`` oder, bei
            einem RFC-7807-Dokument, ``detail``.
        :param trace_id: Die Ablaufkennung aus ``error.traceId``.
        :param raw_body: Der Rumpf der Antwort, unveraendert.
        :param problem_title: Der ``title`` eines RFC-7807-Dokuments; sonst ``None``.
        """
        super().__init__(message)

        self.status_code = status_code
        """Der HTTP-Status der Antwort, etwa 403."""

        self.error_code = error_code
        """Der stabile, maschinenlesbare Code, nach dem ein Aufrufer verzweigen soll.

        Bei einem RFC-7807-Dokument bleibt er ``None``: Dessen ``title`` ist die Fassung des
        Statuscodes, kein TANSS-Code.
        """

        self.localized_text = localized_text
        """Der lesbare Text: ``error.localizedText``, ersatzweise ``meta.text`` oder das ``detail``
        eines RFC-7807-Dokuments. Nichts, worauf Code sich stuetzen sollte."""

        self.trace_id = trace_id
        """Die Ablaufkennung aus ``error.traceId``.

        Die Schnittstellenbeschreibung fuehrt dieses Feld nicht; eine 10.10-Instanz schickt es trotzdem
        in jedem fachlichen Fehlerumschlag mit (gegen TANSS 10.10 gemessen). Es ist der Wert, mit dem
        der Vorgang im Protokoll der Instanz wiederzufinden ist. ``None`` bleibt es bei Formen, die
        keine Kennung tragen: RFC-7807-Dokument, leerer Rumpf.
        """

        self.problem_title = problem_title
        """Der ``title`` eines RFC-7807-Dokuments, etwa ``Bad Request``; ``None`` bei jeder anderen
        Form. Ist er gesetzt, kam der Fehler nicht aus der Fachanwendung, und :attr:`error_code` ist
        dann ``None``."""

        self.raw_body = raw_body
        """Der Rumpf der Antwort, unveraendert, fuer Protokoll und Fehlersuche."""

    @classmethod
    def try_parse(cls, status_code: int, body: str | None) -> "TanssApiError | None":
        """Liest den Fehlerrumpf; ``None``, wenn er keine der bekannten Formen traegt.

        Gelesen werden ``error.text``, ``error.localizedText``, ``error.traceId``, ``meta.text``,
        ``content.detailMessage`` und die Felder ``title``/``detail`` des RFC-7807-Dokuments, sonst
        nichts. Ist der Rumpf kein JSON-Objekt oder enthaelt er keines dieser Felder, kommt ``None``
        zurueck; der Aufrufer nimmt dann :meth:`from_response`, das auch aus einem leeren oder fremden
        Rumpf einen Fehler mit Status und :attr:`raw_body` macht.

        :param status_code: Der HTTP-Status der Antwort.
        :param body: Der Rumpf der Antwort.
        """
        if not body or not body.strip():
            return None

        try:
            document = json.loads(body)
        except ValueError:
            # Kein JSON: dann steht auch nichts Bekanntes darin.
            return None

        if not isinstance(document, dict):
            return None

        error_code: str | None = None
        localized_text: str | None = None
        trace_id: str | None = None

        # Der fachliche Umschlag: { "error": { text, localizedText, traceId } }, gemessen samt traceId.
        error = document.get("error")
        if isinstance(error, dict):
            error_code = _text(error, "text")
            localized_text = _text(error, "localizedText")
            trace_id = _text(error, "traceId")

        # { "meta": { "text": "..." } }
        meta = document.get("meta")
        if isinstance(meta, dict) and localized_text is None:
            localized_text = _text(meta, "text")

        # Abgelehnte Anmeldung: { "content": { "detailMessage": "..." } }
        content = document.get("content")
        if isinstance(content, dict) and error_code is None:
            error_code = _text(content, "detailMessage")

        if trace_id is None:
            trace_id = _text(document, "traceId")

        # RFC 7807: { "type", "title", "status", "detail", "instance" }, nur dann, wenn der
        # TANSS-Umschlag nichts hergab; sonst gewinnt der fachliche Code.
        if error_code is None and localized_text is None:
            problem_title = _text(document, "title")
            problem_detail = _text(document, "detail")
            if problem_title is not None or problem_detail is not None:
                return cls(
                    cls._problem_message(status_code, problem_title, problem_detail),
                    status_code=status_code,
                    error_code=None,
                    localized_text=problem_detail or problem_title,
                    trace_id=trace_id,
                    raw_body=body,
                    problem_title=problem_title,
                )
            return None

        return cls(
            cls._message_for(status_code, error_code, localized_text),
            status_code=status_code,
            error_code=error_code,
            localized_text=localized_text,
            trace_id=trace_id,
            raw_body=body,
        )

    @classmethod
    def from_response(cls, status_code: int, body: str | None) -> "TanssApiError":
        """Der Fehler zu einer Antwort: die gelesenen Felder, wenn sie da sind, sonst Status und Rumpf.

        Ist der Rumpf leer, nennt die Meldung den Grund: Eine 10.10-Instanz beantwortet jede Ablehnung
        genau so, ohne einen einzigen Hinweis im Rumpf (gegen TANSS 10.10 gemessen).

        :param status_code: Der HTTP-Status der Antwort.
        :param body: Der Rumpf der Antwort.
        """
        parsed = cls.try_parse(status_code, body)
        if parsed is not None:
            return parsed

        return cls(cls._empty_or_foreign(status_code, body), status_code=status_code, raw_body=body)

    @staticmethod
    def _empty_or_foreign(status_code: int, body: str | None) -> str:
        if body and body.strip():
            return TanssApiError._message_for(status_code, None, None)

        status = f"TANSS antwortete mit {_status_text(status_code)} und leerem Rumpf"
        if status_code in (401, 403):
            return (
                status + ". TANSS beantwortet Ablehnungen mit einem leeren Rumpf: Der Grund steht "
                "nirgends in der Antwort. Gemessen kommt diese Form bei fehlendem Token, bei einem "
                "Token ohne das Praefix Bearer, bei der Kopfzeile Authorization statt apiToken, bei "
                "einem Modul-Praefix ohne dessen Rolle und bei einer Route, die die "
                "Sicherheitskonfiguration des Servers sperrt (gegen TANSS 10.10 gemessen)."
            )
        return status + "."

    @staticmethod
    def _problem_message(status_code: int, title: str | None, detail: str | None) -> str:
        status = f"TANSS antwortete mit {_status_text(status_code)}"
        if title and detail:
            return f"{status}: {title} - {detail}"
        if title:
            return f"{status}: {title}"
        if detail:
            return f"{status}: {detail}"
        return status + "."

    @staticmethod
    def _message_for(status_code: int, error_code: str | None, localized_text: str | None) -> str:
        status = f"TANSS antwortete mit {_status_text(status_code)}"
        if error_code and localized_text:
            return f"{status}: {error_code} - {localized_text}"
        if error_code:
            return f"{status}: {error_code}"
        if localized_text:
            return f"{status}: {localized_text}"
        return status + "."
