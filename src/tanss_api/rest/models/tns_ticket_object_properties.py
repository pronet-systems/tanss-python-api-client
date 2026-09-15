from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .ticket_complete import TicketComplete
    from .tns_meta_properties import TnsMetaProperties

@dataclass
class TnsTicketObjectProperties(AdditionalDataHolder, Parsable):
    """
    Ticket mit berechneten Meta-Properties (TnsObjectProperties<TnsTicket>)
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # ticket model with all fields
    data: Optional[TicketComplete] = None
    # The properties property
    properties: Optional[TnsMetaProperties] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsTicketObjectProperties:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsTicketObjectProperties
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsTicketObjectProperties()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .ticket_complete import TicketComplete
        from .tns_meta_properties import TnsMetaProperties

        from .ticket_complete import TicketComplete
        from .tns_meta_properties import TnsMetaProperties

        fields: dict[str, Callable[[Any], None]] = {
            "data": lambda n : setattr(self, 'data', n.get_object_value(TicketComplete)),
            "properties": lambda n : setattr(self, 'properties', n.get_object_value(TnsMetaProperties)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_object_value("data", self.data)
        writer.write_object_value("properties", self.properties)
        writer.write_additional_data_value(self.additional_data)
    

