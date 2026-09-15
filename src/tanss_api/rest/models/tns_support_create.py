from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .ticket_save import TicketSave
    from .tns_support import TnsSupport

from .tns_support import TnsSupport

@dataclass
class TnsSupportCreate(TnsSupport, Parsable):
    """
    model for creating a new support
    """
    # id of the remitter (employee who ordered the support)
    remitter_id: Optional[int] = None
    # ticket model to be saved
    ticket: Optional[TicketSave] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsSupportCreate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsSupportCreate
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsSupportCreate()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .ticket_save import TicketSave
        from .tns_support import TnsSupport

        from .ticket_save import TicketSave
        from .tns_support import TnsSupport

        fields: dict[str, Callable[[Any], None]] = {
            "remitterId": lambda n : setattr(self, 'remitter_id', n.get_int_value()),
            "ticket": lambda n : setattr(self, 'ticket', n.get_object_value(TicketSave)),
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
        writer.write_int_value("remitterId", self.remitter_id)
        writer.write_object_value("ticket", self.ticket)
    

