"""Welche Rolle ein Token tragen muss, damit TANSS eine Route ueberhaupt durchreicht."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum, auto

from . import _paths


class TokenRole(Enum):
    """Die Rolle, die ein Token tragen muss, damit TANSS eine Route an den Handler durchreicht.

    Aus der Sicherheitskonfiguration des Servers, gegen TANSS 10.10 geprueft. Die Rolle entscheidet nur
    die erste Huerde; ob der Mitarbeiter das Ticket dann auch sehen darf, prueft TANSS je Route ueber
    seine Rechte.
    """

    DENIED = auto()
    """``denyAll``: Kein Token der Welt oeffnet diese Route."""

    NONE = auto()
    """Frei: Die Route braucht kein Token - die Anmeldung selbst und ein paar oeffentliche Pfade."""

    USER = auto()
    """Das Login-Token des Technikers aus der Anmeldung."""

    SYSTEMHAUS_ONE = auto()
    """ERP-Anbindung Systemhaus.ONE, eigenes Token."""

    ERP_OR_CENTRON = auto()
    """ERP-Token, Rolle ``ERP`` oder ``CENTRON``."""

    COERO = auto()
    """TANSS-X-Plattform (COERO GmbH)."""

    PHONE = auto()
    """Telefonanlagen-Anbindung."""

    REMOTE_SUPPORT = auto()
    """Fernwartungs-Import, Praefix ``/api/remoteSupports/v1``."""

    MONITORING = auto()
    """Monitoring-Anbindung."""

    TANSS_APP = auto()
    """App- und TANSS-X-Token, gepraegt ueber ``GET /api/v1/jwts/tanss_app``."""

    TIMESTAMP = auto()
    """Stempeluhr-Anbindung."""

    DEVICE_MANAGEMENT = auto()
    """Geraetemanagement-Anbindung."""

    SERVEREYE = auto()
    """Server-Eye."""

    USER_OR_OFFER = auto()
    """Angebote: Login-Token oder Angebots-Token."""

    USER_OR_PHP = auto()
    """Intern (PHP-Oberflaeche): Login-Token oder PHP-Token."""

    USER_OR_LANDING_PAGE = auto()
    """Sprachen: Login-Token oder eines der beiden Landingpage-Token."""

    LANDING_PAGE_TICKET_WORKFLOW = auto()
    """Kundenportal-Landingpage fuer Ticket-Ablaeufe."""

    LANDING_PAGE_CONTRACT_WORKFLOW = auto()
    """Kundenportal-Landingpage fuer Vertrags-Ablaeufe."""

    ACTUATOR = auto()
    """Betriebsdaten unter ``/actuator``."""


@dataclass(frozen=True, slots=True)
class _Rule:
    """Eine Zeile der Tabelle: Praefix, Rolle und die beiden Feinheiten des Vergleichs."""

    prefix: str
    role: TokenRole
    exact: bool = False
    min_segments_below: int = 0

    def matches(self, path: str) -> bool:
        """Trifft diese Zeile den Pfad?

        :param path: Der bereinigte Pfad unterhalb der Basisadresse.
        """
        if path == self.prefix:
            return self.min_segments_below == 0

        if self.exact or not path.startswith(self.prefix + "/"):
            return False

        if self.min_segments_below == 0:
            return True

        segments = sum(1 for segment in path[len(self.prefix) + 1:].split("/") if segment)
        return segments >= self.min_segments_below


# Die Regeln in der Auswertungsreihenfolge des Servers (vom Server so umgesetzt, gegen 10.10
# geprueft). Die Reihenfolge ist Teil der Regel: Es gilt der erste Treffer.
_TABLE: tuple[_Rule, ...] = (
    _Rule("/api/v1/login", TokenRole.NONE, exact=True),
    _Rule("/api/systemhaus_one/v1", TokenRole.SYSTEMHAUS_ONE),
    _Rule("/api/erp/v1", TokenRole.ERP_OR_CENTRON),
    _Rule("/api/coero/v1", TokenRole.COERO),
    _Rule("/api/calls/v1", TokenRole.PHONE),
    _Rule("/api/remoteSupports/v1", TokenRole.REMOTE_SUPPORT),
    _Rule("/api/monitoring/v1", TokenRole.MONITORING),
    _Rule("/api/tanss.app/v1", TokenRole.TANSS_APP),
    _Rule("/api/tanss.x/v1", TokenRole.TANSS_APP),
    _Rule("/api/timestamps/v1", TokenRole.TIMESTAMP),
    _Rule("/api/deviceManagement/v1", TokenRole.DEVICE_MANAGEMENT),
    _Rule("/api/servereye/v1", TokenRole.SERVEREYE),
    _Rule("/api/v1/tickets", TokenRole.USER),
    _Rule("/api/v1/checklists", TokenRole.USER),
    _Rule("/api/v1/checklistItems", TokenRole.USER),
    _Rule("/api/v1/checklistEvents", TokenRole.USER),
    _Rule("/api/v1/timers", TokenRole.USER),
    _Rule("/api/v1/supports", TokenRole.USER),
    _Rule("/api/v1/todos", TokenRole.USER),
    _Rule("/api/v1/tasks", TokenRole.USER),
    _Rule("/api/v1/employees", TokenRole.USER),
    _Rule("/api/v1/telephoneSystems", TokenRole.USER),
    _Rule("/api/v1/util/files", TokenRole.NONE),
    _Rule("/api/v1/util/languages", TokenRole.USER_OR_LANDING_PAGE),
    _Rule("/api/v1/util", TokenRole.USER),
    _Rule("/api/v1/cloud/isTokenValid", TokenRole.NONE),
    _Rule("/api/v1/cloud/upload", TokenRole.NONE),
    _Rule("/api/v1/cloud", TokenRole.USER),
    _Rule("/.well-known/jwks.json", TokenRole.NONE, exact=True),
    _Rule("/api/v1/companies", TokenRole.USER),
    _Rule("/api/v1/projects", TokenRole.USER),
    _Rule("/api/v1/supports", TokenRole.USER),
    _Rule("/api/v1/timeline", TokenRole.USER),
    _Rule("/api/v1/cache", TokenRole.USER_OR_PHP),
    _Rule("/api/v1/roles", TokenRole.USER),
    _Rule("/api/v1/ev", TokenRole.USER),
    _Rule("/api/v1/test", TokenRole.USER),
    _Rule("/api/v1/mails", TokenRole.USER),
    _Rule("/api/v1/chats", TokenRole.USER),
    _Rule("/api/v1/jwts", TokenRole.USER),
    _Rule("/api/v1/templates", TokenRole.USER),
    _Rule("/api/v1/availability", TokenRole.USER),
    _Rule("/api/v1/ws", TokenRole.NONE),
    _Rule("/api/v1/offers", TokenRole.USER_OR_OFFER),
    _Rule("/api/v1/tags", TokenRole.USER),
    _Rule("/api/v1/sysTasks", TokenRole.USER),
    _Rule("/api/v1/callbacks", TokenRole.USER),
    _Rule("/api/v1/search", TokenRole.USER),
    _Rule("/api/v1/ticketBoard", TokenRole.USER),
    _Rule("/actuator", TokenRole.ACTUATOR),
    _Rule("/api/v1/timestamps", TokenRole.USER),
    _Rule("/api/v1/externals", TokenRole.USER),
    _Rule("/api/v1/planning", TokenRole.USER),
    _Rule("/api/v1/tmpFileUploads", TokenRole.USER),
    _Rule("/api/v1/remoteSupports", TokenRole.USER),
    _Rule("/api/v1/pcs", TokenRole.USER),
    _Rule("/api/v1/peripheries", TokenRole.USER),
    _Rule("/api/v1/components", TokenRole.USER),
    _Rule("/api/v1/tanssEvents", TokenRole.USER),
    _Rule("/api/v1/log", TokenRole.USER),
    _Rule("/api/v1/paymentMethods", TokenRole.USER),
    _Rule("/api/v1/push", TokenRole.USER),
    _Rule("/api/v1/admin", TokenRole.USER),
    _Rule("/api/v1/escalations", TokenRole.USER),
    _Rule("/api/v1/textModules", TokenRole.USER),
    _Rule("/api/v1/tanssLicenses", TokenRole.USER),
    _Rule("/api/v1/qr", TokenRole.USER),
    _Rule("/api/v1/cars", TokenRole.USER),
    _Rule("/api/v1/recurrence", TokenRole.USER),
    _Rule("/api/v1/os", TokenRole.USER),
    _Rule("/api/v1/manufacturers", TokenRole.USER),
    _Rule("/api/v1/cpus", TokenRole.USER),
    _Rule("/api/v1/hddTypes", TokenRole.USER),
    _Rule("/api/v1/services", TokenRole.USER),
    _Rule("/api/v1/systemhaus_one", TokenRole.USER),
    _Rule("/api/v1/erp", TokenRole.USER),
    _Rule("/api/v1/identify", TokenRole.USER),
    _Rule("/api/v1/domains", TokenRole.USER),
    _Rule("/api/v1/managementDashboard", TokenRole.USER),
    _Rule("/api/v1/genericAssignments", TokenRole.USER),
    _Rule("/api/v1/holidays", TokenRole.USER),
    _Rule("/api/v1/mass", TokenRole.USER),
    _Rule("/api/v1/emailSettings", TokenRole.USER),
    _Rule("/api/v1/mailRobot", TokenRole.USER),
    _Rule("/api/v1/companyCategories", TokenRole.USER),
    _Rule("/api/v1/vacationRequests", TokenRole.USER),
    _Rule("/api/v1/overtime", TokenRole.USER),
    _Rule("/api/v1/ownDailyServices", TokenRole.USER),
    _Rule("/api/v1/geocodes", TokenRole.USER),
    _Rule("/api/v1/ips", TokenRole.USER),
    _Rule("/api/v1/passwords", TokenRole.USER),
    _Rule("/api/v1/emailAccounts", TokenRole.USER),
    _Rule("/api/v1/softwarelicenses", TokenRole.USER),
    _Rule("/api/v1/softwarelicenses/types", TokenRole.USER),
    _Rule("/api/v1/phoneCalls", TokenRole.USER),
    _Rule("/api/v1/documents", TokenRole.USER),
    _Rule("/api/v1/guarantee", TokenRole.USER),
    _Rule("/api/v1/favorites", TokenRole.USER),
    _Rule("/api/v1/sentry", TokenRole.USER),
    _Rule("/api/v1/git/commits", TokenRole.USER),
    _Rule("/api/v1/knowledgeBase", TokenRole.USER),
    _Rule("/api/v1/ical/fetch", TokenRole.NONE),
    _Rule("/api/v1/ical", TokenRole.USER),
    _Rule("/api/v1/popUpNotifications", TokenRole.USER),
    _Rule("/api/v1/supportTypes", TokenRole.USER),
    _Rule("/api/v1/assignments", TokenRole.USER),
    _Rule("/api/v1/contracts", TokenRole.USER),
    _Rule("/api/v1/starface/inc", TokenRole.NONE, min_segments_below=2),
    _Rule("/api/v1/starface", TokenRole.USER),
    _Rule("/api/v1/portal", TokenRole.USER),
    _Rule("/api/v1/mention", TokenRole.USER),
    _Rule("/api/v1/customerNotifications", TokenRole.USER),
    _Rule("/api/v1/salesTarget", TokenRole.USER),
    _Rule("/api/v1/logo", TokenRole.NONE),
    _Rule("/api/v1/supportRules", TokenRole.USER),
    _Rule("/api/v1/browser", TokenRole.USER),
    _Rule("/api/v1/customerPortalWizards", TokenRole.USER),
    _Rule("/api/v1/accountingTypes", TokenRole.USER),
    _Rule("/api/v1/supportProfileCategories", TokenRole.USER),
    _Rule("/api/v1/landingPage/ticketWorkflow", TokenRole.LANDING_PAGE_TICKET_WORKFLOW),
    _Rule("/api/v1/landingPage/contractWorkflow", TokenRole.LANDING_PAGE_CONTRACT_WORKFLOW),
    _Rule("/api/v1/workflowContracts", TokenRole.USER),
    _Rule("/api/v1/ticketWorkflows", TokenRole.USER),
    _Rule("/api/v1/entityFiles", TokenRole.USER),
    _Rule("/api/v1/tempCache", TokenRole.USER),
    _Rule("/api/v1/permissions", TokenRole.USER),
    _Rule("/api/v1/ai", TokenRole.USER),
    _Rule("/api/v1/admin/ai", TokenRole.USER),
    _Rule("/api/v1/admin/permissionPackages", TokenRole.USER),
)


def required_for(path: str) -> TokenRole:
    """Die Rolle, die der Pfad verlangt; :attr:`TokenRole.DENIED` fuer alles, was in keiner Zeile steht.

    **Die erste Uebereinstimmung gewinnt**, in der Reihenfolge der Tabelle, so wie der Server sie
    auswertet. ``/api/v1/offers`` steht deshalb vor den uebrigen Zeilen unter ``/api/v1``, und
    ``/api/v1/login`` ganz oben.

    **Ein Login-Token erreicht nur die USER-Praefixe.** Das Sitzungstoken aus der Anmeldung traegt die
    Rolle ``USER`` und oeffnet damit die USER-Module unter ``/api/v1``, sonst nichts. ``/api/erp/v1``,
    ``/api/tanss.x/v1``, ``/api/remoteSupports/v1`` und alle anderen Praefixe verlangen ein je Modul
    gepraegtes Token mit der jeweiligen Rolle; mit dem Login-Token antworten sie 403, und die Meldung
    sieht genauso aus wie bei einem abgelaufenen Token. Wer eine solche Route aufrufen will, prueft
    vorher mit :func:`is_reachable_with_login_token` oder beschafft das passende Token, fuer ``tanss.x``
    etwa ueber ``GET /api/v1/jwts/tanss_app``.

    **Es gibt keine Sammelregel fuer ``/api/v1``**: TANSS zaehlt die USER-Module einzeln auf und sperrt
    alles Uebrige mit ``denyAll``. Ein ``/api/v1``-Pfad, dessen Modul in keiner Zeile steht (in 10.10
    z. B. ``sla``, ``priorities``, ``vouchers``, ``filesAndLinks``), ist :attr:`TokenRole.DENIED`, auch
    wenn die offizielle Schnittstellenbeschreibung ihn kennt. Ob die Instanz eine erlaubte Route dann
    kennt, sagt :class:`tanss_api.availability.ApiAvailability`.

    :param path: Der Pfad unterhalb der Basisadresse, etwa ``/api/v1/tickets/own``, mit oder ohne
        Abfragezeichenkette. Eine vollstaendige Adresse wird ab ihrem ersten ``/api/`` gelesen.
    """
    if path is None:
        raise TypeError("Der Pfad darf nicht None sein.")

    bare = _paths.path_of(path)
    for rule in _TABLE:
        if rule.matches(bare):
            return rule.role

    return TokenRole.DENIED


def includes_user(role: TokenRole) -> bool:
    """Schliesst diese Rolle ``USER`` ein, verlangt die Route also einen Mitarbeiterkontext?

    Wahr fuer :attr:`TokenRole.USER` und die gemischten Zeilen, in denen neben einem zweiten Token auch
    das Login-Token zugelassen ist (:attr:`TokenRole.USER_OR_OFFER`, :attr:`TokenRole.USER_OR_PHP`,
    :attr:`TokenRole.USER_OR_LANDING_PAGE`). Falsch fuer :attr:`TokenRole.NONE`: Wo gar kein Token
    noetig ist, gibt es auch keinen Mitarbeiter.

    Das ist die Bedingung, unter der die Bibliothek den Abfrageparameter ``loggedInUserId`` anhaengt:
    Der Server spricht einem ``TANSS_APP``-Token die Rolle ``ROLE_USER`` nur dann zu, wenn der
    Parameter in der Anfrage steht.

    :param role: Die Rolle, die der Pfad verlangt.
    """
    return role in (
        TokenRole.USER,
        TokenRole.USER_OR_OFFER,
        TokenRole.USER_OR_PHP,
        TokenRole.USER_OR_LANDING_PAGE,
    )


def is_reachable_with_login_token(path: str) -> bool:
    """Oeffnet das Login-Token des Technikers diese Route?

    Wahr fuer die USER-Praefixe und fuer alles, was gar kein Token braucht.

    :param path: Der Pfad unterhalb der Basisadresse.
    """
    role = required_for(path)
    return role is TokenRole.NONE or includes_user(role)
