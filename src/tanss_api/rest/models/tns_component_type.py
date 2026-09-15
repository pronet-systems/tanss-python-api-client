from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class TnsComponentType(AdditionalDataHolder, Parsable):
    """
    Component type
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # id of the component type
    id: Optional[int] = None
    # short name of the component type
    short_name: Optional[str] = None
    # if false, this type won't be shown in the select field (meaning its an inactive type)
    shown: Optional[bool] = None
    # name of the component type
    type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsComponentType:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsComponentType
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsComponentType()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "shortName": lambda n : setattr(self, 'short_name', n.get_str_value()),
            "shown": lambda n : setattr(self, 'shown', n.get_bool_value()),
            "type": lambda n : setattr(self, 'type', n.get_str_value()),
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
        writer.write_str_value("shortName", self.short_name)
        writer.write_bool_value("shown", self.shown)
        writer.write_str_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    

