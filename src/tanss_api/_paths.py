"""Schneidet aus einer vollstaendigen Adresse den Teil heraus, auf den die Routenregeln rechnen.

`token_roles` und der Endpunkt-Index kennen Pfade, wie die Schnittstellenbeschreibung sie fuehrt:
``/api/v1/tickets/own``. Auf der Leitung steht davor aber der Pfadanteil der Basisadresse — auf einer
TANSS-Installation im Regelfall ``/backend``. Wer die Regel auf den vollen Pfad anwendet, findet
``/api/v1`` nie am Anfang und haengt ``loggedInUserId`` nirgends an; die Folge waere eine 403 auf jeder
Route.

Dieses Modul ist nicht Teil der oeffentlichen Schnittstelle der Bibliothek.
"""

from __future__ import annotations

from urllib.parse import urlsplit

API_MARKER = "/api/"


def below_base(absolute_path: str, base_path: str) -> str:
    """Der Pfad unterhalb der Basisadresse.

    :param absolute_path: Der Pfad der Anfrage, etwa ``/backend/api/v1/timers``.
    :param base_path: Der Pfadanteil der Basisadresse, etwa ``/backend``; leer, wenn keiner.
    :returns: Der Rest hinter der Basis. Passt die Basis nicht, gilt der erste Abschnitt ``/api/`` als
        Anfang — TANSS stellt alle Routen darunter, und eine abweichend gebaute Adresse soll die Regel
        nicht stumm aushebeln.
    """
    if base_path and absolute_path.startswith(base_path) and (
        len(absolute_path) == len(base_path) or absolute_path[len(base_path)] == "/"
    ):
        return absolute_path[len(base_path):]

    index = absolute_path.find(API_MARKER)
    return absolute_path[index:] if index >= 0 else absolute_path


def base_path_of(base_url: str) -> str:
    """Der Pfadanteil der Basisadresse ohne Schraegstrich am Ende; leer, wenn die Adresse keinen hat.

    :param base_url: Die Basisadresse, etwa ``https://tanss.example.de/backend``.
    """
    parts = urlsplit(base_url)
    return parts.path.rstrip("/") if parts.scheme and parts.netloc else ""


def strip_query(path: str) -> str:
    """Entfernt Abfragezeichenkette und Fragment.

    :param path: Der Pfad, gegebenenfalls mit ``?`` oder ``#``.
    """
    cut = len(path)
    for mark in ("?", "#"):
        found = path.find(mark)
        if 0 <= found < cut:
            cut = found
    return path[:cut]


def path_of(path_or_url: str) -> str:
    """Der Pfad einer Angabe, die ein Pfad oder eine vollstaendige http(s)-Adresse sein darf.

    Eine vollstaendige Adresse wird ab ihrem ersten ``/api/`` gelesen; ein Pfad bleibt unveraendert.
    Abfrage und Fragment fallen weg, ein Schraegstrich am Ende ebenfalls.

    :param path_or_url: Der Pfad oder die Adresse.
    """
    bare = path_or_url.strip()
    parts = urlsplit(bare)
    if parts.scheme in ("http", "https") and parts.netloc:
        bare = below_base(parts.path, "")

    bare = strip_query(bare)
    return bare.rstrip("/") if len(bare) > 1 else bare
