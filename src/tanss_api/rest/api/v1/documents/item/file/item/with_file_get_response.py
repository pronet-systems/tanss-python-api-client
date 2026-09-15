from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .......models.tns_meta_message import TnsMetaMessage
    from .with_file_get_response_content import WithFileGetResponse_content

@dataclass
class WithFileGetResponse(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # object carrying the temporary download URL/token.
    content: Optional[WithFileGetResponse_content] = None
    # The meta property
    meta: Optional[TnsMetaMessage] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WithFileGetResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WithFileGetResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WithFileGetResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .......models.tns_meta_message import TnsMetaMessage
        from .with_file_get_response_content import WithFileGetResponse_content

        from .......models.tns_meta_message import TnsMetaMessage
        from .with_file_get_response_content import WithFileGetResponse_content

        fields: dict[str, Callable[[Any], None]] = {
            "content": lambda n : setattr(self, 'content', n.get_object_value(WithFileGetResponse_content)),
            "meta": lambda n : setattr(self, 'meta', n.get_object_value(TnsMetaMessage)),
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
        writer.write_object_value("content", self.content)
        writer.write_object_value("meta", self.meta)
        writer.write_additional_data_value(self.additional_data)
    

