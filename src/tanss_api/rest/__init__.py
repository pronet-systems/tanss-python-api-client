"""Der erzeugte Teil: jede Operation der Schnittstellenbeschreibung, typisiert.

Der Inhalt dieses Verzeichnisses wird aus der offiziellen Schnittstellenbeschreibung erzeugt und von
Hand nicht geaendert. Der Einstieg ist :class:`TanssRestClient`; gebaut wird er von
:meth:`tanss_api.api.TanssApi.create`, das ihm die Basisadresse, die Kopfzeile ``apiToken`` und die
Regel fuer ``loggedInUserId`` mitgibt.

Die Unterverzeichnisse tragen keine eigene ``__init__.py``: Sie sind Namensraumpakete, und der Pfad im
Code ist der Pfad in der Schnittstelle - ``client.api.v1.tickets.own`` fuer ``/api/v1/tickets/own``.
"""

from .tanss_rest_client import TanssRestClient

__all__ = ["TanssRestClient"]
