from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class TnsTicketFile(AdditionalDataHolder, Parsable):
    """
    a document attached to a ticket
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # date when the document was uploaded
    date: Optional[int] = None
    # (optional) description of the document
    description: Optional[str] = None
    # id of the employee who uploaded this document
    employee_id: Optional[int] = None
    # original filename of the document
    file_name: Optional[str] = None
    # id of the document
    id: Optional[int] = None
    # true if the document is internal (customers won't see it)
    internal: Optional[bool] = None
    # mime type (if given)
    mime_type: Optional[str] = None
    # id of the assigned ticket
    ticket_id: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsTicketFile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsTicketFile
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsTicketFile()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "date": lambda n : setattr(self, 'date', n.get_int_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "employeeId": lambda n : setattr(self, 'employee_id', n.get_int_value()),
            "fileName": lambda n : setattr(self, 'file_name', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "internal": lambda n : setattr(self, 'internal', n.get_bool_value()),
            "mimeType": lambda n : setattr(self, 'mime_type', n.get_str_value()),
            "ticketId": lambda n : setattr(self, 'ticket_id', n.get_int_value()),
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
        writer.write_int_value("date", self.date)
        writer.write_str_value("description", self.description)
        writer.write_int_value("employeeId", self.employee_id)
        writer.write_str_value("fileName", self.file_name)
        writer.write_int_value("id", self.id)
        writer.write_bool_value("internal", self.internal)
        writer.write_str_value("mimeType", self.mime_type)
        writer.write_int_value("ticketId", self.ticket_id)
        writer.write_additional_data_value(self.additional_data)
    

