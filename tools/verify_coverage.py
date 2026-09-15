#!/usr/bin/env python3
"""Prueft, ob der erzeugte Client jede Operation des mitgelieferten Endpunkt-Index bedient.

Der Index ``src/tanss_api/endpoint_index.json`` fuehrt jede Operation als Paar aus Verb und Pfad. Der
erzeugte Client fuehrt dieselbe Operation als Anfragenbauer: eine Klasse mit der Vorlage
``url_template`` und je Verb eine Methode ``async def get``, ``post``, ``put`` oder ``delete``. Dieses
Werkzeug liest beide Seiten und sagt, wie viele Eintraege des Index auf der anderen Seite ankommen.

Gelesen wird ohne Import: Die Bauer werden als Quelltext geparst (:mod:`ast`). So braucht das Werkzeug
weder eine Instanz noch die Abhaengigkeiten des Clients.

Verglichen wird nach Platzhaltern, nicht nach deren Namen: ``/api/v1/tickets/{ticketId}`` und
``/api/v1/tickets/{%2Did}`` sind dieselbe Route. Ein Schraegstrich am Ende faellt weg, die
Abfrageparameter der Vorlage (``{?...}``) ebenfalls.

Aufruf::

    python tools/verify_coverage.py [--index PFAD] [--rest PFAD] [--limit N]

Ausgabe: eine Zeile ``Abdeckung: X/Y = Z %``. Fehlt auch nur eine Operation, nennt das Werkzeug sie und
endet mit dem Rueckgabewert 1.
"""

from __future__ import annotations

import argparse
import ast
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path

PLACEHOLDER = re.compile(r"\{[^}]*\}")
"""Jeder Platzhalter, gleich wie er heisst."""

BASE_URL_PREFIX = "{+baseurl}"
"""Der Anfang jeder Vorlage des erzeugten Clients; dahinter beginnt der Pfad der Schnittstelle."""

HTTP_METHODS = ("get", "post", "put", "delete", "patch", "head", "options")
"""Die Methodennamen, die im erzeugten Client ein Verb der Schnittstelle bedeuten."""

BUILDER_SUFFIX = "_request_builder.py"
"""Die Endung, an der ein Anfragenbauer zu erkennen ist."""


@dataclass(frozen=True)
class Builder:
    """Ein gelesener Anfragenbauer: seine Vorlage und die Verben, die er bedient."""

    source: Path
    template: str
    methods: tuple[str, ...]


def normalise(path: str) -> str:
    """Bringt einen Pfad in die Schreibweise des Vergleichs.

    Ohne Abfrage, ohne Schraegstrich am Ende, jeder Platzhalter als ``{}``.

    :param path: Der Pfad aus dem Index oder aus einer Vorlage.
    """
    bare = path.strip()
    for mark in ("?", "#"):
        cut = bare.find(mark)
        if cut >= 0:
            bare = bare[:cut]
    if len(bare) > 1:
        bare = bare.rstrip("/")
    return PLACEHOLDER.sub("{}", bare)


def path_of_template(template: str) -> str | None:
    """Der Pfad einer Vorlage des erzeugten Clients; ``None``, wenn sie keinen traegt.

    Aus ``{+baseurl}/api/v1/tickets{?remitterCheck*}`` wird ``/api/v1/tickets``. Die Vorlage des
    Wurzelbauers ist ``{+baseurl}`` allein und bedient keine Operation.

    :param template: Die Vorlage, so wie sie im Quelltext steht.
    """
    if not template.startswith(BASE_URL_PREFIX):
        return None

    rest = template[len(BASE_URL_PREFIX):]
    cut = rest.find("{?")
    if cut >= 0:
        rest = rest[:cut]

    return normalise(rest) if rest.startswith("/") else None


def _template_of(klass: ast.ClassDef) -> str | None:
    """Die Vorlage der Klasse: aus dem Aufruf von ``super().__init__`` oder aus ``url_template``."""
    for node in ast.walk(klass):
        if (
            isinstance(node, ast.Call)
            and isinstance(node.func, ast.Attribute)
            and node.func.attr == "__init__"
        ):
            for argument in node.args:
                if (
                    isinstance(argument, ast.Constant)
                    and isinstance(argument.value, str)
                    and argument.value.startswith(BASE_URL_PREFIX)
                ):
                    return argument.value

        # Manche Bauer setzen die Vorlage als eigene Zuweisung an url_template.
        if isinstance(node, ast.Assign):
            for target in node.targets:
                name = target.attr if isinstance(target, ast.Attribute) else getattr(target, "id", None)
                if (
                    name == "url_template"
                    and isinstance(node.value, ast.Constant)
                    and isinstance(node.value.value, str)
                    and node.value.value.startswith(BASE_URL_PREFIX)
                ):
                    return node.value.value

    return None


def read_builder(source: Path) -> Builder | None:
    """Liest einen Anfragenbauer: Vorlage und Verben.

    Gesucht werden die Zeichenkette aus ``super().__init__(request_adapter, "...", path_parameters)``
    und die ``async def``-Methoden mit einem Verbnamen. Ist die Datei kein gueltiger Python-Quelltext
    oder traegt sie keine Vorlage, kommt ``None`` zurueck.

    :param source: Die Datei des Bauers.
    """
    try:
        tree = ast.parse(source.read_text(encoding="utf-8"), filename=str(source))
    except (OSError, SyntaxError):
        return None

    for node in ast.walk(tree):
        if not isinstance(node, ast.ClassDef) or not node.name.endswith("RequestBuilder"):
            continue

        template = _template_of(node)
        if template is None:
            continue

        methods = tuple(
            member.name.lower()
            for member in node.body
            if isinstance(member, ast.AsyncFunctionDef) and member.name.lower() in HTTP_METHODS
        )
        return Builder(source=source, template=template, methods=methods)

    return None


def collect(rest_root: Path) -> dict[str, list[Path]]:
    """Alle Operationen des erzeugten Clients als ``VERB /pfad`` samt der Dateien, die sie tragen.

    :param rest_root: Das Verzeichnis ``src/tanss_api/rest``.
    """
    found: dict[str, list[Path]] = {}
    for source in sorted(rest_root.rglob("*" + BUILDER_SUFFIX)):
        builder = read_builder(source)
        if builder is None:
            continue

        path = path_of_template(builder.template)
        if path is None:
            continue

        for method in builder.methods:
            found.setdefault(method.upper() + " " + path, []).append(source)

    return found


def main(argv: list[str] | None = None) -> int:
    """Liest Index und erzeugten Client, vergleicht beide und meldet die Abdeckung.

    :param argv: Die Aufrufparameter; ``None`` nimmt die der Befehlszeile.
    :returns: 0, wenn jede Operation des Index bedient wird, sonst 1.
    """
    root = Path(__file__).resolve().parent.parent
    parser = argparse.ArgumentParser(description="Prueft die Abdeckung des Endpunkt-Index.")
    parser.add_argument(
        "--index",
        type=Path,
        default=root / "src" / "tanss_api" / "endpoint_index.json",
        help="Der mitgelieferte Endpunkt-Index.",
    )
    parser.add_argument(
        "--rest",
        type=Path,
        default=root / "src" / "tanss_api" / "rest",
        help="Das Verzeichnis des erzeugten Clients.",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=25,
        help="Wie viele fehlende Operationen einzeln genannt werden.",
    )
    arguments = parser.parse_args(argv)

    if not arguments.index.is_file():
        print(f"Der Endpunkt-Index fehlt: {arguments.index}", file=sys.stderr)
        return 1
    if not arguments.rest.is_dir():
        print(f"Der erzeugte Client fehlt: {arguments.rest}", file=sys.stderr)
        return 1

    document = json.loads(arguments.index.read_text(encoding="utf-8"))
    operations = document.get("operations", [])
    available = collect(arguments.rest)

    missing: list[str] = []
    covered = 0
    for entry in operations:
        method = str(entry.get("method", "")).strip().upper()
        path = str(entry.get("path", "")).strip()
        if not method or not path:
            continue

        key = method + " " + normalise(path)
        if key in available:
            covered += 1
        else:
            missing.append(key)

    total = len(operations)
    share = (covered / total * 100) if total else 0.0

    print(f"Operationen im Index: {total}")
    print(f"Operationen im erzeugten Client: {len(available)}")
    if missing:
        print(f"Fehlend: {len(missing)}")
        for key in missing[: max(0, arguments.limit)]:
            print("  - " + key)
        if len(missing) > arguments.limit:
            print(f"  ... und {len(missing) - arguments.limit} weitere")

    print(f"Abdeckung: {covered}/{total} = {share:.1f} %")
    return 1 if missing else 0


if __name__ == "__main__":
    raise SystemExit(main())
