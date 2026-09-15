from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tns_document import TnsDocument

from .tns_document import TnsDocument

@dataclass
class TnsDocumentWithContent(TnsDocument, Parsable):
    # content of this document
    content: Optional[str] = None
    # Is only used if this document is "encrypted". In this case the decoded content is shown here
    decoded_content: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsDocumentWithContent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsDocumentWithContent
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsDocumentWithContent()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .tns_document import TnsDocument

        from .tns_document import TnsDocument

        fields: dict[str, Callable[[Any], None]] = {
            "content": lambda n : setattr(self, 'content', n.get_str_value()),
            "decodedContent": lambda n : setattr(self, 'decoded_content', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_str_value("content", self.content)
        writer.write_str_value("decodedContent", self.decoded_content)
    

