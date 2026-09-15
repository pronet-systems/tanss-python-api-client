"""Alles, was der Zugang zu einer TANSS-Instanz an Einstellungen braucht."""

from __future__ import annotations

from dataclasses import dataclass
from urllib.parse import urlsplit

from . import _paths


@dataclass(frozen=True, slots=True)
class TanssApiOptions:
    """Adresse, Mitarbeiter, Zeitgrenze, Proxy, TLS-Pruefung.

    Die Klasse traegt nur Werte; angewandt werden sie beim Bau des Clients
    (:meth:`tanss_api.api.TanssApi.create`). Geprueft wird allein die Basisadresse, und zwar sofort:
    Ein Tippfehler darin faellt sonst erst bei der ersten Anfrage auf.
    """

    base_url: str
    """Die Basisadresse, der jeder Pfad der Schnittstellenbeschreibung angehaengt wird.

    Die Schnittstellenbeschreibung traegt als einzigen Server-Eintrag ``https://{host}`` mit der
    Variablen ``host``. Sie sagt damit **nicht**, unter welchem Pfad die Schnittstelle einer
    Installation liegt.

    Auf einer TANSS-Installation wird die Schnittstelle unter ``/backend`` ausgeliefert; die
    Weboberflaeche liegt daneben unter dem Stammpfad. Die Bibliothek stellt deshalb nichts von sich aus
    voran, sondern erwartet die **vollstaendige** Basis einschliesslich ``/backend``, etwa
    ``https://tanss.example.de/backend``. Wer statt dessen die Oberflaeche angibt, bekommt deren
    Antworten und nicht die der Schnittstelle.

    Verlangt wird eine absolute ``http``- oder ``https``-Adresse; ein Schraegstrich am Ende ist
    gleichgueltig.
    """

    employee_id: int | None = None
    """Die Mitarbeiter-Id, die als Abfrageparameter ``loggedInUserId`` mitgeschickt wird.

    Der Parameter ist kein Zierrat: Der Server gibt einem Token vom Typ ``TANSS_APP`` die Rolle
    ``ROLE_USER`` nur dann, wenn ``loggedInUserId`` in der Anfrage steht — ohne ihn fehlt der
    Mitarbeiterkontext und die Route antwortet 403. Ein Login-Token (``ACCESS``) traegt den Mitarbeiter
    bereits im Anspruch ``sub``; der Parameter stoert dort nicht.

    Ist der Wert ``None``, haengt die Bibliothek nichts an. Das ist richtig fuer Modul-Token (ERP,
    PHONE, REMOTE_SUPPORT, ...), die ohnehin keinen Mitarbeiter kennen. Die Id liefert
    ``POST /api/v1/login`` im Feld ``content.employeeId``.
    """

    timeout: float = 30.0
    """Zeitgrenze einer einzelnen Anfrage in Sekunden; Vorgabe 30."""

    proxy: str | None = None
    """Vorgeschalteter Proxy, etwa ``http://proxy.example.de:3128``; ``None`` fuer den Direktweg.

    Verlangt der Proxy eine Anmeldung, stehen Name und Kennwort in der Adresse
    (``http://benutzer:kennwort@proxy.example.de:3128``); httpx liest sie von dort.
    """

    verify_tls: bool = True
    """Prueft die Bibliothek das TLS-Zertifikat der Instanz? Vorgabe ``True``.

    **Warnung:** ``False`` schaltet die Zertifikatspruefung vollstaendig ab. Die Verbindung ist dann
    gegen einen Angreifer in der Mitte wertlos: Wer den Netzweg kontrolliert, liest Token und Daten mit
    und kann Antworten faelschen. Vertretbar allenfalls fuer eine Instanz im eigenen Netz mit
    selbstsigniertem Zertifikat, und auch dort nur, bis das Zertifikat im Rechnerspeicher hinterlegt
    ist.
    """

    def __post_init__(self) -> None:
        """Prueft die Basisadresse.

        :raises ValueError: Die Adresse ist keine absolute http(s)-Adresse.
        """
        parts = urlsplit(self.base_url.strip() if self.base_url else "")
        if parts.scheme not in ("http", "https") or not parts.netloc:
            raise ValueError(
                f'Die Basisadresse "{self.base_url}" ist keine absolute http(s)-Adresse. Erwartet '
                "wird die vollstaendige Basis der Schnittstelle einschliesslich des Pfads, unter dem "
                "die Installation sie ausliefert (auf einer TANSS-Installation /backend), etwa "
                "https://tanss.example.de/backend."
            )

    @property
    def normalised_base_url(self) -> str:
        """Die Basisadresse ohne Schraegstrich am Ende — so, wie der erzeugte Client sie erwartet."""
        return self.base_url.strip().rstrip("/")

    @property
    def base_path(self) -> str:
        """Der Pfadanteil der Basisadresse, etwa ``/backend``; leer, wenn die Adresse keinen hat."""
        return _paths.base_path_of(self.normalised_base_url)
