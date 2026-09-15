from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .timer import Timer
    from .tns_timer_fragment import TnsTimerFragment

from .timer import Timer

@dataclass
class TnsTimer(Timer, Parsable):
    """
    Timer der TANSS.App/TANSS.X-Routen (Timer plus startTime, note, fragments, unfolded)
    """
    # Zeitfragmente (bei Listen null)
    fragments: Optional[list[TnsTimerFragment]] = None
    # Notiz (beim Anlegen Notiz des ersten Fragments, Fallback title).
    note: Optional[str] = None
    # Startzeit des laufenden Fragments; 0 wenn der Timer gestoppt ist.
    start_time: Optional[int] = None
    # Aufgeklappt-Flag aus den Benutzerpräferenzen
    unfolded: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsTimer:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsTimer
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsTimer()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .timer import Timer
        from .tns_timer_fragment import TnsTimerFragment

        from .timer import Timer
        from .tns_timer_fragment import TnsTimerFragment

        fields: dict[str, Callable[[Any], None]] = {
            "fragments": lambda n : setattr(self, 'fragments', n.get_collection_of_object_values(TnsTimerFragment)),
            "note": lambda n : setattr(self, 'note', n.get_str_value()),
            "startTime": lambda n : setattr(self, 'start_time', n.get_int_value()),
            "unfolded": lambda n : setattr(self, 'unfolded', n.get_bool_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_collection_of_object_values("fragments", self.fragments)
        writer.write_str_value("note", self.note)
        writer.write_int_value("startTime", self.start_time)
        writer.write_bool_value("unfolded", self.unfolded)
    

