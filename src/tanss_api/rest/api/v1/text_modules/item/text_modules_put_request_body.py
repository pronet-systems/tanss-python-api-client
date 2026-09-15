from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .....models.tns_text_module_type import TnsTextModuleType

@dataclass
class TextModulesPutRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The content property
    content: Optional[str] = None
    # The departments property
    departments: Optional[list[int]] = None
    # The employees property
    employees: Optional[list[int]] = None
    # The html property
    html: Optional[bool] = None
    # The name property
    name: Optional[str] = None
    # The title property
    title: Optional[str] = None
    # The types property
    types: Optional[list[TnsTextModuleType]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TextModulesPutRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TextModulesPutRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TextModulesPutRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .....models.tns_text_module_type import TnsTextModuleType

        from .....models.tns_text_module_type import TnsTextModuleType

        fields: dict[str, Callable[[Any], None]] = {
            "content": lambda n : setattr(self, 'content', n.get_str_value()),
            "departments": lambda n : setattr(self, 'departments', n.get_collection_of_primitive_values(int)),
            "employees": lambda n : setattr(self, 'employees', n.get_collection_of_primitive_values(int)),
            "html": lambda n : setattr(self, 'html', n.get_bool_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
            "types": lambda n : setattr(self, 'types', n.get_collection_of_enum_values(TnsTextModuleType)),
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
        writer.write_str_value("content", self.content)
        writer.write_collection_of_primitive_values("departments", self.departments)
        writer.write_collection_of_primitive_values("employees", self.employees)
        writer.write_bool_value("html", self.html)
        writer.write_str_value("name", self.name)
        writer.write_str_value("title", self.title)
        writer.write_collection_of_enum_values("types", self.types)
        writer.write_additional_data_value(self.additional_data)
    

