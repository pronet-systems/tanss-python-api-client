from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class SlaPostRequestBody(AdditionalDataHolder, Parsable):
    """
    Request body.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Whether the service level agreement is currently active.
    active: Optional[bool] = None
    # Purchase price associated with the service level agreement.
    buying_price: Optional[float] = None
    # Cost associated with the service level agreement.
    cost: Optional[float] = None
    # Resolution deadline expressed in days.
    deadline_days: Optional[int] = None
    # Resolution deadline expressed in hours.
    deadline_hours: Optional[int] = None
    # Descriptive text of the service level agreement.
    description: Optional[str] = None
    # Unique identifier of the service level agreement.
    id: Optional[int] = None
    # Reference to the graphic representing the service level agreement.
    image: Optional[str] = None
    # Name of the service level agreement.
    name: Optional[str] = None
    # Priority ranking of the service level agreement.
    priority: Optional[int] = None
    # Guaranteed reaction time in hours.
    reaction_time: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SlaPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SlaPostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SlaPostRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "active": lambda n : setattr(self, 'active', n.get_bool_value()),
            "buyingPrice": lambda n : setattr(self, 'buying_price', n.get_float_value()),
            "cost": lambda n : setattr(self, 'cost', n.get_float_value()),
            "deadlineDays": lambda n : setattr(self, 'deadline_days', n.get_int_value()),
            "deadlineHours": lambda n : setattr(self, 'deadline_hours', n.get_int_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "image": lambda n : setattr(self, 'image', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "priority": lambda n : setattr(self, 'priority', n.get_int_value()),
            "reactionTime": lambda n : setattr(self, 'reaction_time', n.get_int_value()),
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
        writer.write_float_value("buyingPrice", self.buying_price)
        writer.write_float_value("cost", self.cost)
        writer.write_int_value("deadlineDays", self.deadline_days)
        writer.write_int_value("deadlineHours", self.deadline_hours)
        writer.write_str_value("description", self.description)
        writer.write_str_value("image", self.image)
        writer.write_str_value("name", self.name)
        writer.write_int_value("priority", self.priority)
        writer.write_int_value("reactionTime", self.reaction_time)
        writer.write_additional_data_value(self.additional_data)
    

