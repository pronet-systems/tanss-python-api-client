from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .put_request_body_document_type import PutRequestBody_documentType

@dataclass
class PutRequestBody(AdditionalDataHolder, Parsable):
    """
    Request body.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Category of the document
    document_type: Optional[PutRequestBody_documentType] = None
    # Original display name of the file
    filename: Optional[str] = None
    # Unique identifier of the stored file
    id: Optional[int] = None
    # Whether the file is marked as internal only
    internal: Optional[bool] = None
    # Email address of the sender who provided the file
    sender_email: Optional[str] = None
    # Identifier of the sender who uploaded the file
    sender_id: Optional[int] = None
    # Internal name under which the file is stored
    stored_filename: Optional[str] = None
    # Descriptive label of the file
    title: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PutRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PutRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PutRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .put_request_body_document_type import PutRequestBody_documentType

        from .put_request_body_document_type import PutRequestBody_documentType

        fields: dict[str, Callable[[Any], None]] = {
            "documentType": lambda n : setattr(self, 'document_type', n.get_enum_value(PutRequestBody_documentType)),
            "filename": lambda n : setattr(self, 'filename', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "internal": lambda n : setattr(self, 'internal', n.get_bool_value()),
            "senderEmail": lambda n : setattr(self, 'sender_email', n.get_str_value()),
            "senderId": lambda n : setattr(self, 'sender_id', n.get_int_value()),
            "storedFilename": lambda n : setattr(self, 'stored_filename', n.get_str_value()),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
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
        writer.write_enum_value("documentType", self.document_type)
        writer.write_str_value("filename", self.filename)
        writer.write_bool_value("internal", self.internal)
        writer.write_str_value("senderEmail", self.sender_email)
        writer.write_int_value("senderId", self.sender_id)
        writer.write_str_value("storedFilename", self.stored_filename)
        writer.write_str_value("title", self.title)
        writer.write_additional_data_value(self.additional_data)
    

