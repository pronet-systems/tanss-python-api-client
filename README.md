# TANSS Python API Client

**Ein Python-Client für die TANSS-REST-API - Getestet gegen TANSS 10.10.**

---

1137 Endpunkte, typisiert, mit Anmeldung, Token-Verwaltung und den Eigenheiten der Schnittstelle.
Kein Zwischendienst: Die Bibliothek spricht unmittelbar mit eurer Instanz.

## Installation

```
pip install tanss-api
```

Ab Python 3.11, plattformunabhängig.

## Beispiel

```python
import asyncio

from tanss_api import MutableTokenProvider, TanssApi, TanssApiOptions
from tanss_api.rest.models.ticket_configuration import TicketConfiguration


async def main() -> None:
    optionen = TanssApiOptions(
        # Vollständige Basis der Schnittstelle; eine TANSS-Installation liefert sie unter /backend aus.
        base_url="https://tanss.example.de/backend",
        employee_id=42,
    )

    token = MutableTokenProvider()
    async with TanssApi.create(optionen, token) as api:
        # Anmelden — das Zugangstoken landet automatisch im Token-Halter.
        await api.session.login("benutzer", "kennwort")

        # Ab hier steht die gesamte Schnittstelle bereit: Der Pfad im Code ist der Pfad in der API.
        meine_tickets = await api.rest.api.v1.tickets.own.get()   # GET /api/v1/tickets/own

        # Listen sind in TANSS oft ein PUT mit Filter — und trotzdem lesend.
        filter_ = TicketConfiguration()
        filter_.staff = [42]
        filter_.items_per_page = 20
        gefiltert = await api.rest.api.v1.tickets.put(filter_)


asyncio.run(main())
```

Weitere Einstiege: `api.session.login_with_dashboard_key(…)` und
`api.session.login(benutzer, login_token=…)` für die beiden anderen Anmeldewege,
`api.session.refresh(…)` zum Erneuern, `api.session.mint("tanss_app")` für ein Token für ein externes
Programm.

## Was die Bibliothek für euch erledigt

- **Anmeldung.** Alle drei Wege. Eine fehlgeschlagene Anmeldung antwortet mit HTTP 200 — wer den
  Statuscode prüft, hält einen Tippfehler für einen Erfolg. Hier gibt es einen `TanssApiError` mit
  dem Grund. Zugangsdaten mit Umlauten kommen richtig an.
- **Token.** Kopfzeile `apiToken` mit `Bearer`-Präfix, der Parameter `loggedInUserId` genau dort,
  wo er wirkt. `required_for(pfad)` sagt vorher, ob euer Token die Route überhaupt erreicht —
  TANSS beantwortet jede Ablehnung mit leerem Körper.
- **Verfügbarkeit.** `ApiAvailability` sagt, welche Route eure Version kennt und welche der
  Server gesperrt hat.
- **Fehler.** `TanssApiError` mit `error_code`, `localized_text` und `trace_id`.
- **Sicherheit beim Schreiben.** Wiederholt wird nur bei lesenden Aufrufen. Schreibende gehen
  genau einmal auf die Leitung: TANSS dedupliziert nicht.

## Bauen und testen

```
pip install -e ".[dev]"
pytest tests

# Lesende Proben gegen eine echte Instanz; ohne diese Variablen werden sie übersprungen.
TANSS_BASE_URL=https://tanss.example.de/backend TANSS_USER=… TANSS_PASSWORD=… \
  pytest tests/live

# Prüft, ob der erzeugte Client jede Operation des Endpunkt-Index bedient.
python tools/verify_coverage.py
```

Der erzeugte Teil unter `src/tanss_api/rest` entsteht aus der offiziellen
Schnittstellenbeschreibung; sie ist nicht Teil dieses Repositorys.

## Lizenz und Marken

Der Quelltext steht unter der MIT-Lizenz (siehe `LICENSE`).

TANSS ist ein Produkt der HUCK IT GmbH. Dieses Projekt ist ein unabhängiger Client, steht in
keiner Verbindung zur HUCK IT GmbH und wird von ihr weder unterstützt noch geprüft. Marken
gehören ihren jeweiligen Inhabern; die Nennung dient allein dazu, zu sagen, wofür dieser Client
gemacht ist.

---

[ProNet Systems GmbH](https://www.pronet-systems.de) · IT-Systemhaus in Arnsberg
