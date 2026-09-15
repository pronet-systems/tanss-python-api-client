from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .with_category_post_request_body_types import WithCategoryPostRequestBody_types

@dataclass
class WithCategoryPostRequestBody(AdditionalDataHolder, Parsable):
    """
    Request body.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Unique identifier of the company type category
    id: Optional[int] = None
    # Name of the category
    name: Optional[str] = None
    # Company types belonging to this category
    types: Optional[list[WithCategoryPostRequestBody_types]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WithCategoryPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WithCategoryPostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WithCategoryPostRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .with_category_post_request_body_types import WithCategoryPostRequestBody_types

        from .with_category_post_request_body_types import WithCategoryPostRequestBody_types

        fields: dict[str, Callable[[Any], None]] = {
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "types": lambda n : setattr(self, 'types', n.get_collection_of_object_values(WithCategoryPostRequestBody_types)),
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
        writer.write_str_value("name", self.name)
        writer.write_collection_of_object_values("types", self.types)
        writer.write_additional_data_value(self.additional_data)
    

