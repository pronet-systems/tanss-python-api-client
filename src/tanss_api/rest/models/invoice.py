from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class Invoice(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Order request XML of the voucher, Base64-encoded. Empty when the file could not be read.
    order_request: Optional[str] = None
    # Rendered voucher PDF, Base64-encoded. Only present when the request was sent with `pdf=true`.
    pdf: Optional[str] = None
    # `OK`, or the reason why the order request file could not be delivered.
    status: Optional[str] = None
    # Id of the voucher the order request belongs to.
    voucher_id: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Invoice:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Invoice
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Invoice()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "order_request": lambda n : setattr(self, 'order_request', n.get_str_value()),
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
        writer.write_str_value("order_request", self.order_request)
        writer.write_str_value("pdf", self.pdf)
        writer.write_str_value("status", self.status)
        writer.write_int_value("voucher_id", self.voucher_id)
        writer.write_additional_data_value(self.additional_data)
    

