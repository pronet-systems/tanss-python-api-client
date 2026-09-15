from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class AttachmentPutRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Content identifier used to reference the attachment inline in the mail body. Part of the attachment object, ignored on this request.
    cid: Optional[str] = None
    # File extension of the attachment. Part of the attachment object, ignored on this request.
    extension: Optional[str] = None
    # Original file name of the attachment. The only body field that is evaluated - the attachment is resolved by mail id (from the path) plus this name.
    file_name: Optional[str] = None
    # Storage folder where the attachment file resides. Part of the attachment object, ignored on this request.
    folder: Optional[str] = None
    # Identifier of the mail this attachment belongs to. Taken from the path parameter - a value sent here is ignored.
    mail_id: Optional[int] = None
    # Name under which the attachment is stored internally. Part of the attachment object, ignored on this request.
    stored_filename: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AttachmentPutRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AttachmentPutRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AttachmentPutRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "cid": lambda n : setattr(self, 'cid', n.get_str_value()),
            "extension": lambda n : setattr(self, 'extension', n.get_str_value()),
            "fileName": lambda n : setattr(self, 'file_name', n.get_str_value()),
            "folder": lambda n : setattr(self, 'folder', n.get_str_value()),
            "mailId": lambda n : setattr(self, 'mail_id', n.get_int_value()),
            "storedFilename": lambda n : setattr(self, 'stored_filename', n.get_str_value()),
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
        writer.write_str_value("fileName", self.file_name)
        writer.write_additional_data_value(self.additional_data)
    

