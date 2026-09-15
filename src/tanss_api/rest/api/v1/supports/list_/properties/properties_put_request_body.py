from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .properties_put_request_body_context import PropertiesPutRequestBody_context
    from .properties_put_request_body_fields import PropertiesPutRequestBody_fields

@dataclass
class PropertiesPutRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Context in which the support configuration is applied
    context: Optional[PropertiesPutRequestBody_context] = None
    # Which filter-form field definitions to return
    fields: Optional[list[PropertiesPutRequestBody_fields]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PropertiesPutRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PropertiesPutRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PropertiesPutRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .properties_put_request_body_context import PropertiesPutRequestBody_context
        from .properties_put_request_body_fields import PropertiesPutRequestBody_fields

        from .properties_put_request_body_context import PropertiesPutRequestBody_context
        from .properties_put_request_body_fields import PropertiesPutRequestBody_fields

        fields: dict[str, Callable[[Any], None]] = {
            "context": lambda n : setattr(self, 'context', n.get_enum_value(PropertiesPutRequestBody_context)),
            "fields": lambda n : setattr(self, 'fields', n.get_collection_of_enum_values(PropertiesPutRequestBody_fields)),
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
        writer.write_enum_value("context", self.context)
        writer.write_collection_of_enum_values("fields", self.fields)
        writer.write_additional_data_value(self.additional_data)
    

