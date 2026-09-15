from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class SapOneInvoice(AdditionalDataHolder, Parsable):
    """
    One invoice or credit note as delivered by the connected SAP Business One system. Field namesare the SAP ones; `TypeCancellation`, `CancellationDate`, `OpenSum` and `Paid` are derived byTANSS.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # SAP cancellation flag; `C` marks a cancelled document.
    canceled: Optional[str] = None
    # Creation date of the document when it is cancelled, empty otherwise.
    cancellation_date: Optional[str] = None
    # Customer number (CardCode) in SAP.
    card_code: Optional[str] = None
    # The CardName property
    card_name: Optional[str] = None
    # The Comments property
    comments: Optional[str] = None
    # The CreateDate property
    create_date: Optional[str] = None
    # The DocDate property
    doc_date: Optional[str] = None
    # The DocDueDate property
    doc_due_date: Optional[str] = None
    # The DocEntry property
    doc_entry: Optional[int] = None
    # The DocNum property
    doc_num: Optional[int] = None
    # Gross total. Negative for credit notes.
    doc_total: Optional[float] = None
    # For invoices `DocTotal - PaidToDate`, for credit notes `0`.
    open_sum: Optional[float] = None
    # `1` when an invoice is fully paid; credit notes are always `1`.
    paid: Optional[int] = None
    # The PaidToDate property
    paid_to_date: Optional[float] = None
    # `1` when `Canceled` is `C`.
    type_cancellation: Optional[int] = None
    # `1` when the document is a credit note (ORIN).
    type_credit: Optional[int] = None
    # `1` when the document is an invoice (OINV).
    type_invoice: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SapOneInvoice:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SapOneInvoice
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SapOneInvoice()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "Canceled": lambda n : setattr(self, 'canceled', n.get_str_value()),
            "CancellationDate": lambda n : setattr(self, 'cancellation_date', n.get_str_value()),
            "CardCode": lambda n : setattr(self, 'card_code', n.get_str_value()),
            "CardName": lambda n : setattr(self, 'card_name', n.get_str_value()),
            "Comments": lambda n : setattr(self, 'comments', n.get_str_value()),
            "CreateDate": lambda n : setattr(self, 'create_date', n.get_str_value()),
            "DocDate": lambda n : setattr(self, 'doc_date', n.get_str_value()),
            "DocDueDate": lambda n : setattr(self, 'doc_due_date', n.get_str_value()),
            "DocEntry": lambda n : setattr(self, 'doc_entry', n.get_int_value()),
            "DocNum": lambda n : setattr(self, 'doc_num', n.get_int_value()),
            "DocTotal": lambda n : setattr(self, 'doc_total', n.get_float_value()),
            "OpenSum": lambda n : setattr(self, 'open_sum', n.get_float_value()),
            "Paid": lambda n : setattr(self, 'paid', n.get_int_value()),
            "PaidToDate": lambda n : setattr(self, 'paid_to_date', n.get_float_value()),
            "TypeCancellation": lambda n : setattr(self, 'type_cancellation', n.get_int_value()),
            "TypeCredit": lambda n : setattr(self, 'type_credit', n.get_int_value()),
            "TypeInvoice": lambda n : setattr(self, 'type_invoice', n.get_int_value()),
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
        writer.write_str_value("Canceled", self.canceled)
        writer.write_str_value("CancellationDate", self.cancellation_date)
        writer.write_str_value("CardCode", self.card_code)
        writer.write_str_value("CardName", self.card_name)
        writer.write_str_value("Comments", self.comments)
        writer.write_str_value("CreateDate", self.create_date)
        writer.write_str_value("DocDate", self.doc_date)
        writer.write_str_value("DocDueDate", self.doc_due_date)
        writer.write_int_value("DocEntry", self.doc_entry)
        writer.write_int_value("DocNum", self.doc_num)
        writer.write_float_value("DocTotal", self.doc_total)
        writer.write_float_value("OpenSum", self.open_sum)
        writer.write_int_value("Paid", self.paid)
        writer.write_float_value("PaidToDate", self.paid_to_date)
        writer.write_int_value("TypeCancellation", self.type_cancellation)
        writer.write_int_value("TypeCredit", self.type_credit)
        writer.write_int_value("TypeInvoice", self.type_invoice)
        writer.write_additional_data_value(self.additional_data)
    

