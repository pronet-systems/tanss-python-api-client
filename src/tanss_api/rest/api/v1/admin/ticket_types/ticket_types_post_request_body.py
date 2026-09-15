from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class TicketTypesPostRequestBody(AdditionalDataHolder, Parsable):
    """
    Request body.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Whether the ticket type is currently active.
    active: Optional[bool] = None
    # Unique identifier of the ticket type.
    id: Optional[int] = None
    # Display name of the ticket type.
    name: Optional[str] = None
    # Whether reaction-time hours apply to this ticket type.
    use_reaction_hours: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TicketTypesPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TicketTypesPostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TicketTypesPostRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "active": lambda n : setattr(self, 'active', n.get_bool_value()),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "useReactionHours": lambda n : setattr(self, 'use_reaction_hours', n.get_bool_value()),
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
        writer.write_bool_value("active", self.active)
        writer.write_str_value("name", self.name)
        writer.write_bool_value("useReactionHours", self.use_reaction_hours)
        writer.write_additional_data_value(self.additional_data)
    

