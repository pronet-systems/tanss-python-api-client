from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .....models.ticket_save import TicketSave

from .....models.ticket_save import TicketSave

@dataclass
class TicketPostRequestBody(TicketSave, Parsable):
    # A group name can be entered, to identify the "source" or "device" of the ticket.
    group_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TicketPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TicketPostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TicketPostRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .....models.ticket_save import TicketSave

        from .....models.ticket_save import TicketSave

        fields: dict[str, Callable[[Any], None]] = {
            "groupName": lambda n : setattr(self, 'group_name', n.get_str_value()),
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
        writer.write_str_value("groupName", self.group_name)
    

