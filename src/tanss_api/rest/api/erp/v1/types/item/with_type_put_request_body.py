from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class WithTypePutRequestBody(AdditionalDataHolder, Parsable):
    """
    Request body.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Identifier of the category this type belongs to
    category_id: Optional[int] = None
    # Name of the category this type belongs to
    category_name: Optional[str] = None
    # Whether the company type is hidden
    hidden: Optional[bool] = None
    # Icon reference associated with the company type
    icon: Optional[str] = None
    # Unique identifier of the company type
    id: Optional[int] = None
    # Name of the company type
    name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WithTypePutRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WithTypePutRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WithTypePutRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "categoryId": lambda n : setattr(self, 'category_id', n.get_int_value()),
            "categoryName": lambda n : setattr(self, 'category_name', n.get_str_value()),
            "hidden": lambda n : setattr(self, 'hidden', n.get_bool_value()),
            "icon": lambda n : setattr(self, 'icon', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
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
        writer.write_int_value("categoryId", self.category_id)
        writer.write_str_value("categoryName", self.category_name)
        writer.write_bool_value("hidden", self.hidden)
        writer.write_str_value("icon", self.icon)
        writer.write_str_value("name", self.name)
        writer.write_additional_data_value(self.additional_data)
    

