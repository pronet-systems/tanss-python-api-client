from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tns_planning_additional_sub_type import TnsPlanningAdditionalSubType

@dataclass
class TnsPlanningAdditionalType(AdditionalDataHolder, Parsable):
    """
    describes a "additional" absence type OR a custom type
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # is this type still active (is displayed in forms)?
    active: Optional[bool] = None
    # background color that shall be used (only for custom types)
    background_color: Optional[str] = None
    # shall this absence type be charged?
    charged: Optional[bool] = None
    # font color that shall be used (only for custom types)
    font_color: Optional[str] = None
    # if of this entry
    id: Optional[int] = None
    # displayed name for this absence type / custom type
    name: Optional[str] = None
    # determines the type - either ABSENCE or CUSTOM
    type: Optional[TnsPlanningAdditionalSubType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsPlanningAdditionalType:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsPlanningAdditionalType
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsPlanningAdditionalType()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .tns_planning_additional_sub_type import TnsPlanningAdditionalSubType

        from .tns_planning_additional_sub_type import TnsPlanningAdditionalSubType

        fields: dict[str, Callable[[Any], None]] = {
            "active": lambda n : setattr(self, 'active', n.get_bool_value()),
            "backgroundColor": lambda n : setattr(self, 'background_color', n.get_str_value()),
            "charged": lambda n : setattr(self, 'charged', n.get_bool_value()),
            "fontColor": lambda n : setattr(self, 'font_color', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(TnsPlanningAdditionalSubType)),
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
        writer.write_int_value("id", self.id)
        writer.write_str_value("name", self.name)
        writer.write_enum_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    

