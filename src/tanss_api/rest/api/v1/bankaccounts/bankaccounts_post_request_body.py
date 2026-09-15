from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class BankaccountsPostRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The accountNumber property
    account_number: Optional[str] = None
    # The accountOwner property
    account_owner: Optional[str] = None
    # The bank property
    bank: Optional[str] = None
    # The bic property
    bic: Optional[str] = None
    # The blz property
    blz: Optional[str] = None
    # The cheques property
    cheques: Optional[bool] = None
    # The companyId property
    company_id: Optional[int] = None
    # The countingNumber property
    counting_number: Optional[int] = None
    # The currencyId property
    currency_id: Optional[int] = None
    # The debits property
    debits: Optional[bool] = None
    # The iban property
    iban: Optional[str] = None
    # The mandateReference property
    mandate_reference: Optional[str] = None
    # The mandateReferenceDate property
    mandate_reference_date: Optional[int] = None
    # The sequenceTypeDebitId property
    sequence_type_debit_id: Optional[int] = None
    # The transfers property
    transfers: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> BankaccountsPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: BankaccountsPostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return BankaccountsPostRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "accountNumber": lambda n : setattr(self, 'account_number', n.get_str_value()),
            "accountOwner": lambda n : setattr(self, 'account_owner', n.get_str_value()),
            "bank": lambda n : setattr(self, 'bank', n.get_str_value()),
            "bic": lambda n : setattr(self, 'bic', n.get_str_value()),
            "blz": lambda n : setattr(self, 'blz', n.get_str_value()),
            "cheques": lambda n : setattr(self, 'cheques', n.get_bool_value()),
            "companyId": lambda n : setattr(self, 'company_id', n.get_int_value()),
            "countingNumber": lambda n : setattr(self, 'counting_number', n.get_int_value()),
            "currencyId": lambda n : setattr(self, 'currency_id', n.get_int_value()),
            "debits": lambda n : setattr(self, 'debits', n.get_bool_value()),
            "iban": lambda n : setattr(self, 'iban', n.get_str_value()),
            "mandateReference": lambda n : setattr(self, 'mandate_reference', n.get_str_value()),
            "mandateReferenceDate": lambda n : setattr(self, 'mandate_reference_date', n.get_int_value()),
            "sequenceTypeDebitId": lambda n : setattr(self, 'sequence_type_debit_id', n.get_int_value()),
            "transfers": lambda n : setattr(self, 'transfers', n.get_bool_value()),
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
        writer.write_str_value("accountNumber", self.account_number)
        writer.write_str_value("accountOwner", self.account_owner)
        writer.write_str_value("bank", self.bank)
        writer.write_str_value("bic", self.bic)
        writer.write_str_value("blz", self.blz)
        writer.write_bool_value("cheques", self.cheques)
        writer.write_int_value("companyId", self.company_id)
        writer.write_int_value("countingNumber", self.counting_number)
        writer.write_int_value("currencyId", self.currency_id)
        writer.write_bool_value("debits", self.debits)
        writer.write_str_value("iban", self.iban)
        writer.write_str_value("mandateReference", self.mandate_reference)
        writer.write_int_value("mandateReferenceDate", self.mandate_reference_date)
        writer.write_int_value("sequenceTypeDebitId", self.sequence_type_debit_id)
        writer.write_bool_value("transfers", self.transfers)
        writer.write_additional_data_value(self.additional_data)
    

