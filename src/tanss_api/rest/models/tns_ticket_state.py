from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class TnsTicketState(AdditionalDataHolder, Parsable):
    """
    represents a ticket state
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # is this an active state? (otherwise won't be shown)
    active: Optional[bool] = None
    # The id property
    id: Optional[int] = None
    # Name of the image. Must be in the folder `media/hp/bug_status`
    image: Optional[str] = None
    # Name of the ticket state
    name: Optional[str] = None
    # Rank of this state (position in lists)
    rank: Optional[int] = None
    # determines if this state is a waiting state
    wait_state: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsTicketState:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsTicketState
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsTicketState()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "active": lambda n : setattr(self, 'active', n.get_bool_value()),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "image": lambda n : setattr(self, 'image', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "rank": lambda n : setattr(self, 'rank', n.get_int_value()),
            "waitState": lambda n : setattr(self, 'wait_state', n.get_bool_value()),
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
        writer.write_str_value("image", self.image)
        writer.write_str_value("name", self.name)
        writer.write_int_value("rank", self.rank)
        writer.write_bool_value("waitState", self.wait_state)
        writer.write_additional_data_value(self.additional_data)
    

