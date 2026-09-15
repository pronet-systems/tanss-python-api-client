from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .planning_additional_types_put_request_body_type import PlanningAdditionalTypesPutRequestBody_type

@dataclass
class PlanningAdditionalTypesPutRequestBody(AdditionalDataHolder, Parsable):
    """
    Request body.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Whether the additional type is currently active
    active: Optional[bool] = None
    # Background color used to display this type in the planning view
    background_color: Optional[str] = None
    # Whether time booked to this type is billable
    charged: Optional[bool] = None
    # Font color used to display this type in the planning view
    font_color: Optional[str] = None
    # Unique identifier of the planning additional type. Taken from the path parameter - a value sent here is ignored.
    id: Optional[int] = None
    # Display name of the additional type
    name: Optional[str] = None
    # Sub-category of the additional type
    type: Optional[PlanningAdditionalTypesPutRequestBody_type] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PlanningAdditionalTypesPutRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PlanningAdditionalTypesPutRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PlanningAdditionalTypesPutRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .planning_additional_types_put_request_body_type import PlanningAdditionalTypesPutRequestBody_type

        from .planning_additional_types_put_request_body_type import PlanningAdditionalTypesPutRequestBody_type

        fields: dict[str, Callable[[Any], None]] = {
            "active": lambda n : setattr(self, 'active', n.get_bool_value()),
            "backgroundColor": lambda n : setattr(self, 'background_color', n.get_str_value()),
            "charged": lambda n : setattr(self, 'charged', n.get_bool_value()),
            "fontColor": lambda n : setattr(self, 'font_color', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(PlanningAdditionalTypesPutRequestBody_type)),
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
        writer.write_str_value("backgroundColor", self.background_color)
        writer.write_bool_value("charged", self.charged)
        writer.write_str_value("fontColor", self.font_color)
        writer.write_str_value("name", self.name)
        writer.write_enum_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    

