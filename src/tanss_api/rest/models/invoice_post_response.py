from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class InvoicePostResponse(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Echoed back when it was part of the request.
    docentry: Optional[int] = None
    # The invoice_number property
    invoice_number: Optional[str] = None
    # Voucher PDF filed in the voucher history, Base64-encoded. Empty for maintenance-contract payments and for skipped entries.
    pdf: Optional[str] = None
    # `OK`, or the reason why the entry was skipped (e.g. unknown `voucher_id`).
    status: Optional[str] = None
    # The voucher_id property
    voucher_id: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> InvoicePostResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: InvoicePostResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return InvoicePostResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "docentry": lambda n : setattr(self, 'docentry', n.get_int_value()),
            "invoice_number": lambda n : setattr(self, 'invoice_number', n.get_str_value()),
            "pdf": lambda n : setattr(self, 'pdf', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_str_value()),
            "voucher_id": lambda n : setattr(self, 'voucher_id', n.get_int_value()),
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
        writer.write_int_value("docentry", self.docentry)
        writer.write_str_value("invoice_number", self.invoice_number)
        writer.write_str_value("pdf", self.pdf)
        writer.write_str_value("status", self.status)
        writer.write_int_value("voucher_id", self.voucher_id)
        writer.write_additional_data_value(self.additional_data)
    

