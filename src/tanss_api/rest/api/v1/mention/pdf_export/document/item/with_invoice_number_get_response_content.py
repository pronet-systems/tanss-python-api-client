from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class WithInvoiceNumberGetResponse_content(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The bytes property
    bytes: Optional[bytes] = None
    # The fileName property
    file_name: Optional[str] = None
    # The invoiceNumber property
    invoice_number: Optional[str] = None
    # The status property
    status: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WithInvoiceNumberGetResponse_content:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WithInvoiceNumberGetResponse_content
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WithInvoiceNumberGetResponse_content()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "bytes": lambda n : setattr(self, 'bytes', n.get_bytes_value()),
            "fileName": lambda n : setattr(self, 'file_name', n.get_str_value()),
            "invoiceNumber": lambda n : setattr(self, 'invoice_number', n.get_str_value()),
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
        writer.write_bytes_value("bytes", self.bytes)
        writer.write_str_value("fileName", self.file_name)
        writer.write_str_value("invoiceNumber", self.invoice_number)
        writer.write_str_value("status", self.status)
        writer.write_additional_data_value(self.additional_data)
    

