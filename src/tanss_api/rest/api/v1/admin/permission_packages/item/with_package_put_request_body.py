from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .with_package_put_request_body_categories import WithPackagePutRequestBody_categories
    from .with_package_put_request_body_type import WithPackagePutRequestBody_type

@dataclass
class WithPackagePutRequestBody(AdditionalDataHolder, Parsable):
    """
    Request body.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Permission category definitions contained in the package
    categories: Optional[list[WithPackagePutRequestBody_categories]] = None
    # Unique identifier of the permission package
    id: Optional[int] = None
    # Descriptive information about the permission package
    info: Optional[str] = None
    # Display name of the permission package
    name: Optional[str] = None
    # User category this permission package applies to
    type: Optional[WithPackagePutRequestBody_type] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WithPackagePutRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WithPackagePutRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WithPackagePutRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .with_package_put_request_body_categories import WithPackagePutRequestBody_categories
        from .with_package_put_request_body_type import WithPackagePutRequestBody_type

        from .with_package_put_request_body_categories import WithPackagePutRequestBody_categories
        from .with_package_put_request_body_type import WithPackagePutRequestBody_type

        fields: dict[str, Callable[[Any], None]] = {
            "categories": lambda n : setattr(self, 'categories', n.get_collection_of_object_values(WithPackagePutRequestBody_categories)),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "info": lambda n : setattr(self, 'info', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(WithPackagePutRequestBody_type)),
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
        writer.write_collection_of_object_values("categories", self.categories)
        writer.write_str_value("info", self.info)
        writer.write_str_value("name", self.name)
        writer.write_enum_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    

