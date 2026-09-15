from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class WithOfferPutRequestBody(AdditionalDataHolder, Parsable):
    """
    Request body.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Identifier of the company the offer belongs to
    company_id: Optional[int] = None
    # Identifier of the employee who created the offer
    created_by_employee_id: Optional[int] = None
    # Creation timestamp of the offer
    date: Optional[int] = None
    # Identifier of the associated ERP project
    erp_project_id: Optional[str] = None
    # Unique identifier of the offer
    id: Optional[int] = None
    # Invoice number associated with the offer
    invoice_number: Optional[str] = None
    # Identifier of the linked object
    link_id: Optional[int] = None
    # Type of object the offer is linked to
    link_type_id: Optional[int] = None
    # Display name of the offer
    name: Optional[str] = None
    # Offer number
    number: Optional[str] = None
    # Identifier of the template the offer is based on
    template_id: Optional[int] = None
    # Timestamp until which the offer is valid
    valid_till: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WithOfferPutRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WithOfferPutRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WithOfferPutRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "companyId": lambda n : setattr(self, 'company_id', n.get_int_value()),
            "createdByEmployeeId": lambda n : setattr(self, 'created_by_employee_id', n.get_int_value()),
            "date": lambda n : setattr(self, 'date', n.get_int_value()),
            "erpProjectId": lambda n : setattr(self, 'erp_project_id', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "invoiceNumber": lambda n : setattr(self, 'invoice_number', n.get_str_value()),
            "linkId": lambda n : setattr(self, 'link_id', n.get_int_value()),
            "linkTypeId": lambda n : setattr(self, 'link_type_id', n.get_int_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "number": lambda n : setattr(self, 'number', n.get_str_value()),
            "templateId": lambda n : setattr(self, 'template_id', n.get_int_value()),
            "validTill": lambda n : setattr(self, 'valid_till', n.get_int_value()),
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
        writer.write_int_value("companyId", self.company_id)
        writer.write_int_value("createdByEmployeeId", self.created_by_employee_id)
        writer.write_int_value("date", self.date)
        writer.write_str_value("erpProjectId", self.erp_project_id)
        writer.write_str_value("invoiceNumber", self.invoice_number)
        writer.write_int_value("linkId", self.link_id)
        writer.write_int_value("linkTypeId", self.link_type_id)
        writer.write_str_value("name", self.name)
        writer.write_str_value("number", self.number)
        writer.write_int_value("templateId", self.template_id)
        writer.write_int_value("validTill", self.valid_till)
        writer.write_additional_data_value(self.additional_data)
    

