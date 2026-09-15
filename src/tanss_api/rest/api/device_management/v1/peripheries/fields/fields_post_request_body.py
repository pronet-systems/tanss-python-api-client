from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .fields_post_request_body_type import FieldsPostRequestBody_type

@dataclass
class FieldsPostRequestBody(AdditionalDataHolder, Parsable):
    """
    Request body.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Unique identifier of the additional field
    id: Optional[int] = None
    # Identifier of the periphery device type this field belongs to
    periphery_type_id: Optional[int] = None
    # Label of the additional field
    title: Optional[str] = None
    # Input type of the additional field
    type: Optional[FieldsPostRequestBody_type] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> FieldsPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: FieldsPostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return FieldsPostRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .fields_post_request_body_type import FieldsPostRequestBody_type

        from .fields_post_request_body_type import FieldsPostRequestBody_type

        fields: dict[str, Callable[[Any], None]] = {
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "peripheryTypeId": lambda n : setattr(self, 'periphery_type_id', n.get_int_value()),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(FieldsPostRequestBody_type)),
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
        writer.write_int_value("peripheryTypeId", self.periphery_type_id)
        writer.write_str_value("title", self.title)
        writer.write_enum_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    

