from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .company_detail import CompanyDetail
    from .employee import Employee

from .company_detail import CompanyDetail

@dataclass
class CompanyPost(CompanyDetail, Parsable):
    """
    Company object to be saved.
    """
    # defines if this company is a "personal customer" - meaning that company and employee are the same person
    personal_customer: Optional[bool] = None
    # object representing an employee
    personal_customer_employee: Optional[Employee] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CompanyPost:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CompanyPost
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CompanyPost()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .company_detail import CompanyDetail
        from .employee import Employee

        from .company_detail import CompanyDetail
        from .employee import Employee

        fields: dict[str, Callable[[Any], None]] = {
            "personalCustomer": lambda n : setattr(self, 'personal_customer', n.get_bool_value()),
            "personalCustomerEmployee": lambda n : setattr(self, 'personal_customer_employee', n.get_object_value(Employee)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_bool_value("personalCustomer", self.personal_customer)
        writer.write_object_value("personalCustomerEmployee", self.personal_customer_employee)
    

