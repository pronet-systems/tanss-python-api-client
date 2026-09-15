"""Was der Endpunkt-Index ueber eine Operation weiss."""

from __future__ import annotations

import json
import re
import threading
from dataclasses import dataclass, field
from importlib import resources

_PLACEHOLDER = re.compile(r"\{[^}]*\}")


@dataclass(frozen=True, slots=True)
class _Operation:
    """Ein Eintrag des Index."""

    method: str
    path: str
    operation_id: str
    tags: tuple[str, ...]
    token_class: str
    roles: tuple[str, ...]
    documented: bool
    in_1010: bool
    reachable_1010: bool
    segments: tuple[str, ...] = field(default=())


@dataclass(frozen=True, slots=True)
class _Catalogue:
    """Der gelesene Index: Serverfassung, Zahl der Eintraege und die Operationen."""

    server_version: str
    count: int
    operations: dict[str, _Operation]


class ApiAvailability:
    """Dokumentiert, auf 10.10 vorhanden, mit dem Token erreichbar, Token-Klasse und Rollen.

    Der erzeugte Client kennt 1137 Operationen: 842 aus der offiziellen Schnittstellenbeschreibung und
    295, die dort fehlen, die der Server aber bedient. Die gepruefte Instanz laeuft auf 10.10 und
    bedient 958 davon; fuer 11 davon passt aber keine Regel der Sicherheitskonfiguration (Token-Klasse
    ``denied``), sodass 947 wirklich erreichbar sind. Alles andere antwortet mit 403, 404 oder 405, ohne
    dass dem Aufrufer der Grund gesagt wuerde. Diese Klasse liest den mitgelieferten Endpunkt-Index und
    beantwortet die Frage vor dem Aufruf statt danach.

    **Platzhalter zaehlen, ihre Namen nicht.** Der Index schreibt ``/api/v1/tickets/{ticketId}``, ein
    Aufrufer vielleicht ``/api/v1/tickets/{id}`` oder gleich ``/api/v1/tickets/4711``. Verglichen wird
    nach Ersetzen jedes ``{...}`` durch ``{}``; findet sich so nichts, gilt ein konkreter Wert an einer
    Platzhalterstelle als Treffer. Ein woertlicher Pfad hat Vorrang: ``/api/v1/tickets/own`` trifft die
    eigene Route und nicht ``{ticketId}``.

    **Die vier Fragen bauen aufeinander auf:** :meth:`is_known` - steht die Operation ueberhaupt im
    Index; :meth:`is_documented` - steht sie in der offiziellen Schnittstellenbeschreibung (falsch fuer
    die 295 nur auf dem Server gefundenen Routen, obwohl sie laufen); :meth:`is_available_on_1010` - hat
    10.10 sie; :meth:`is_reachable_on_1010` - hat sie sie *und* laesst die Sicherheitskonfiguration ein
    Token dorthin.

    Der Index wird beim ersten Zugriff gelesen (ueber ``importlib.resources`` aus dem Paket) und danach
    gehalten.
    """

    RESOURCE_NAME = "endpoint_index.json"
    """Der Name der Datei im Paket ``tanss_api``."""

    DENIED_TOKEN_CLASS = "denied"
    """Die Token-Klasse, fuer die in der Sicherheitskonfiguration von 10.10 keine Regel passt: nicht
    erreichbar."""

    _lock = threading.Lock()
    _catalogue: _Catalogue | None = None

    @classmethod
    def server_version(cls) -> str:
        """Die Serverfassung, gegen die Verfuegbarkeit und Rollen im Index geprueft sind."""
        return cls._loaded().server_version

    @classmethod
    def count(cls) -> int:
        """Die Zahl der Eintraege im Index - jede Operation des erzeugten Clients."""
        return cls._loaded().count

    @classmethod
    def operations(cls) -> tuple[str, ...]:
        """Alle Operationen als ``METHODE /pfad``, Platzhalter als ``{}``.

        Ein Alias, der sich nur durch den Schraegstrich am Ende unterscheidet, faellt mit seinem
        Geschwister zusammen.
        """
        return tuple(cls._loaded().operations.keys())

    @classmethod
    def is_known(cls, method: str, path: str) -> bool:
        """Steht die Operation im Index, dokumentiert oder nur auf dem Server gefunden?

        :param method: Das Verb, etwa ``GET``; Gross- und Kleinschreibung ist gleich.
        :param path: Der Pfad, mit oder ohne Abfragezeichenkette, Platzhalter beliebig benannt.
        """
        return cls._find(method, path) is not None

    @classmethod
    def is_documented(cls, method: str, path: str) -> bool:
        """Steht die Operation in der offiziellen Schnittstellenbeschreibung?

        Falsch fuer die nur auf dem Server gefundenen.

        :param method: Das Verb.
        :param path: Der Pfad.
        """
        found = cls._find(method, path)
        return found.documented if found else False

    @classmethod
    def is_available_on_1010(cls, method: str, path: str) -> bool:
        """Hat TANSS 10.10 die Operation? Sagt nichts darueber, ob ein Token dorthin darf.

        :param method: Das Verb.
        :param path: Der Pfad.
        """
        found = cls._find(method, path)
        return found.in_1010 if found else False

    @classmethod
    def is_reachable_on_1010(cls, method: str, path: str) -> bool:
        """Bedient TANSS 10.10 die Operation wirklich?

        Vorhanden *und* mit einer Token-Klasse ungleich :attr:`DENIED_TOKEN_CLASS`.

        :param method: Das Verb.
        :param path: Der Pfad.
        """
        found = cls._find(method, path)
        return found.reachable_1010 if found else False

    @classmethod
    def token_class(cls, method: str, path: str) -> str | None:
        """Die Token-Klasse aus der Sicherheitskonfiguration von 10.10.

        ``general`` (Login-Token), ``module`` (Modul-Token), ``mixed``, ``public``, ``internal`` oder
        ``denied``; ``None``, wenn die Operation nicht im Index steht.

        :param method: Das Verb.
        :param path: Der Pfad.
        """
        found = cls._find(method, path)
        return found.token_class if found else None

    @classmethod
    def roles(cls, method: str, path: str) -> tuple[str, ...]:
        """Die Rollen, die die Operation verlangt (``USER``, ``ERP``, ``TANSS_APP``, ...).

        Leer, wenn die Operation nicht im Index steht.

        :param method: Das Verb.
        :param path: Der Pfad.
        """
        found = cls._find(method, path)
        return found.roles if found else ()

    @classmethod
    def tags(cls, method: str, path: str) -> tuple[str, ...]:
        """Die Schlagworte der Schnittstellenbeschreibung zur Operation; leer, wenn nicht im Index.

        :param method: Das Verb.
        :param path: Der Pfad.
        """
        found = cls._find(method, path)
        return found.tags if found else ()

    @classmethod
    def operation_id(cls, method: str, path: str) -> str | None:
        """Die ``operationId`` aus dem Index; ``None``, wenn die Operation nicht darin steht.

        :param method: Das Verb.
        :param path: Der Pfad.
        """
        found = cls._find(method, path)
        return found.operation_id if found else None

    @staticmethod
    def normalise_path(path: str) -> str:
        """Bringt einen Pfad in die Schreibweise des Index.

        Ohne Abfrage, ohne Schraegstrich am Ende, jeder Platzhalter als ``{}``.

        :param path: Der Pfad.
        """
        if path is None:
            raise TypeError("Der Pfad darf nicht None sein.")

        bare = path.strip()
        cut = len(bare)
        for mark in ("?", "#"):
            found = bare.find(mark)
            if 0 <= found < cut:
                cut = found
        bare = bare[:cut]
        if len(bare) > 1:
            bare = bare.rstrip("/")

        return _PLACEHOLDER.sub("{}", bare)

    @classmethod
    def _find(cls, method: str, path: str) -> _Operation | None:
        if not method or not method.strip():
            raise ValueError("Die Methode darf nicht leer sein.")
        if not path or not path.strip():
            raise ValueError("Der Pfad darf nicht leer sein.")

        catalogue = cls._loaded()
        verb = method.strip().upper()
        normalised = cls.normalise_path(path)

        exact = catalogue.operations.get(cls._key(verb, normalised))
        if exact is not None:
            return exact

        # Konkrete Werte an Platzhalterstellen: /api/v1/tickets/4711 trifft {ticketId}.
        segments = tuple(normalised.split("/"))
        for candidate in catalogue.operations.values():
            if candidate.method == verb and cls._segments_match(candidate.segments, segments):
                return candidate

        return None

    @staticmethod
    def _segments_match(pattern: tuple[str, ...], actual: tuple[str, ...]) -> bool:
        if len(pattern) != len(actual):
            return False

        for expected, given in zip(pattern, actual):
            placeholder = expected == "{}" and len(given) > 0
            if not placeholder and expected != given:
                return False

        return True

    @staticmethod
    def _key(verb: str, path: str) -> str:
        return verb + " " + path

    @classmethod
    def _loaded(cls) -> _Catalogue:
        if cls._catalogue is None:
            with cls._lock:
                if cls._catalogue is None:
                    cls._catalogue = cls._load()
        return cls._catalogue

    @classmethod
    def _load(cls) -> _Catalogue:
        try:
            raw = resources.files(__package__).joinpath(cls.RESOURCE_NAME).read_text(encoding="utf-8")
        except (FileNotFoundError, ModuleNotFoundError) as cause:
            raise RuntimeError(
                f'Die Paketdatei "{cls.RESOURCE_NAME}" fehlt. Das Paket tanss-api liefert den '
                "Endpunkt-Index mit; ohne ihn ist die Bibliothek unvollstaendig installiert."
            ) from cause

        document = json.loads(raw)
        server = document.get("serverVersion") if isinstance(document.get("serverVersion"), str) else "?"

        count = 0
        operations: dict[str, _Operation] = {}
        for entry in document.get("operations", []):
            if not isinstance(entry, dict):
                continue

            verb = entry.get("method")
            raw_path = entry.get("path")
            if not isinstance(verb, str) or not isinstance(raw_path, str) or not verb or not raw_path:
                continue

            count += 1
            verb = verb.strip().upper()
            path = cls.normalise_path(raw_path)
            token_class = entry.get("tokenClass") if isinstance(entry.get("tokenClass"), str) else ""
            in_1010 = entry.get("in1010") is True
            operation = _Operation(
                method=verb,
                path=path,
                operation_id=entry.get("operationId") if isinstance(entry.get("operationId"), str) else "",
                tags=cls._strings(entry.get("tags")),
                token_class=token_class,
                roles=cls._strings(entry.get("roles")),
                documented=entry.get("documented") is True,
                in_1010=in_1010,
                reachable_1010=in_1010 and token_class != cls.DENIED_TOKEN_CLASS,
                segments=tuple(path.split("/")),
            )

            # Erster Eintrag gewinnt: zwei Schluessel, die nur im Platzhalternamen oder im
            # Schraegstrich am Ende abweichen, meinen dieselbe Route.
            operations.setdefault(cls._key(verb, path), operation)

        return _Catalogue(server_version=server, count=count, operations=operations)

    @staticmethod
    def _strings(value: object) -> tuple[str, ...]:
        if not isinstance(value, list):
            return ()
        return tuple(item for item in value if isinstance(item, str))
