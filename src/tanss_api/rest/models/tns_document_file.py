from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class TnsDocumentFile(AdditionalDataHolder, Parsable):
    """
    an uploaded file for a document
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # timestamp of the creation (upload)
    created_date: Optional[int] = None
    # id of the document this file belongs to
    document_id: Optional[int] = None
    # id of the employee who uploaded the file
    employee_id: Optional[int] = None
    # stored filename of this file
    filename: Optional[str] = None
    # id of the uploaded file
    id: Optional[int] = None
    # mime type for this file
    mime: Optional[str] = None
    # timestamp of the modification
    modified_date: Optional[int] = None
    # original filename
    original_filename: Optional[str] = None
    # size of file (in bytes)
    size: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsDocumentFile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsDocumentFile
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsDocumentFile()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "createdDate": lambda n : setattr(self, 'created_date', n.get_int_value()),
            "documentId": lambda n : setattr(self, 'document_id', n.get_int_value()),
            "employeeId": lambda n : setattr(self, 'employee_id', n.get_int_value()),
            "filename": lambda n : setattr(self, 'filename', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "mime": lambda n : setattr(self, 'mime', n.get_str_value()),
            "modifiedDate": lambda n : setattr(self, 'modified_date', n.get_int_value()),
            "originalFilename": lambda n : setattr(self, 'original_filename', n.get_str_value()),
            "size": lambda n : setattr(self, 'size', n.get_int_value()),
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
        writer.write_int_value("createdDate", self.created_date)
        writer.write_int_value("documentId", self.document_id)
        writer.write_int_value("employeeId", self.employee_id)
        writer.write_str_value("filename", self.filename)
        writer.write_int_value("id", self.id)
        writer.write_str_value("mime", self.mime)
        writer.write_int_value("modifiedDate", self.modified_date)
        writer.write_str_value("originalFilename", self.original_filename)
        writer.write_int_value("size", self.size)
        writer.write_additional_data_value(self.additional_data)
    

