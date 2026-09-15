from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .pdf_export_post_response_content_documents import PdfExportPostResponse_content_documents

@dataclass
class PdfExportPostResponse_content(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The documents property
    documents: Optional[list[PdfExportPostResponse_content_documents]] = None
    # The status property
    status: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PdfExportPostResponse_content:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PdfExportPostResponse_content
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PdfExportPostResponse_content()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .pdf_export_post_response_content_documents import PdfExportPostResponse_content_documents

        from .pdf_export_post_response_content_documents import PdfExportPostResponse_content_documents

        fields: dict[str, Callable[[Any], None]] = {
            "documents": lambda n : setattr(self, 'documents', n.get_collection_of_object_values(PdfExportPostResponse_content_documents)),
            "status": lambda n : setattr(self, 'status', n.get_str_value()),
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
        writer.write_collection_of_object_values("documents", self.documents)
        writer.write_str_value("status", self.status)
        writer.write_additional_data_value(self.additional_data)
    

