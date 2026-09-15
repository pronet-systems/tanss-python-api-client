from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class PutRequestBody(AdditionalDataHolder, Parsable):
    """
    Request body.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Whether the task is currently active
    active: Optional[bool] = None
    # Identifier of the company the task is assigned to
    company_id: Optional[int] = None
    # Identifier of the maintenance contract the task belongs to
    contract_id: Optional[int] = None
    # Scheduled date of the task as a unix timestamp
    date: Optional[int] = None
    # Date after which the task expires as a unix timestamp
    expiration_date: Optional[int] = None
    # Unique identifier of the task
    id: Optional[int] = None
    # Name of the task
    name: Optional[str] = None
    # Identifier of the preferred employee for the task
    preferred_employee_id: Optional[int] = None
    # Price associated with the task
    price: Optional[float] = None
    # Planned support duration in minutes
    support_duration: Optional[int] = None
    # Identifier of the support type associated with the task
    support_type_id: Optional[int] = None
    # Descriptive text of the task
    text: Optional[str] = None
    # Identifier of the ticket linked to the task
    ticket_id: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PutRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PutRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PutRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "active": lambda n : setattr(self, 'active', n.get_bool_value()),
            "companyId": lambda n : setattr(self, 'company_id', n.get_int_value()),
            "contractId": lambda n : setattr(self, 'contract_id', n.get_int_value()),
            "date": lambda n : setattr(self, 'date', n.get_int_value()),
            "expirationDate": lambda n : setattr(self, 'expiration_date', n.get_int_value()),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "preferredEmployeeId": lambda n : setattr(self, 'preferred_employee_id', n.get_int_value()),
            "price": lambda n : setattr(self, 'price', n.get_float_value()),
            "supportDuration": lambda n : setattr(self, 'support_duration', n.get_int_value()),
            "supportTypeId": lambda n : setattr(self, 'support_type_id', n.get_int_value()),
            "text": lambda n : setattr(self, 'text', n.get_str_value()),
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
        writer.write_bool_value("active", self.active)
        writer.write_int_value("companyId", self.company_id)
        writer.write_int_value("contractId", self.contract_id)
        writer.write_int_value("date", self.date)
        writer.write_int_value("expirationDate", self.expiration_date)
        writer.write_str_value("name", self.name)
        writer.write_int_value("preferredEmployeeId", self.preferred_employee_id)
        writer.write_float_value("price", self.price)
        writer.write_int_value("supportDuration", self.support_duration)
        writer.write_int_value("supportTypeId", self.support_type_id)
        writer.write_str_value("text", self.text)
        writer.write_int_value("ticketId", self.ticket_id)
        writer.write_additional_data_value(self.additional_data)
    

