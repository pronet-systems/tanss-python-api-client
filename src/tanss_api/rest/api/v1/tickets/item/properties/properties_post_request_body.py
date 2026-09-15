from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class PropertiesPostRequestBody(AdditionalDataHolder, Parsable):
    """
    Request body.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Identifier of the department the ticket is assigned to
    assigned_to_department_id: Optional[int] = None
    # Identifier of the employee the ticket is assigned to
    assigned_to_employee_id: Optional[int] = None
    # Identifier of the company the ticket belongs to
    company_id: Optional[int] = None
    # Main description text of the ticket
    content: Optional[str] = None
    # Identifier of the linked maintenance contract
    contract_id: Optional[int] = None
    # Deadline as a Unix timestamp in seconds
    deadline_date: Optional[int] = None
    # Due date as a Unix timestamp in seconds
    due_date: Optional[int] = None
    # Unique identifier of the ticket
    id: Optional[int] = None
    # Priority level of the ticket
    priority: Optional[int] = None
    # Identifier of the current ticket status
    status_id: Optional[int] = None
    # Ticket subject line
    title: Optional[str] = None
    # Identifier of the ticket type
    type_id: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PropertiesPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PropertiesPostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PropertiesPostRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "assignedToDepartmentId": lambda n : setattr(self, 'assigned_to_department_id', n.get_int_value()),
            "assignedToEmployeeId": lambda n : setattr(self, 'assigned_to_employee_id', n.get_int_value()),
            "companyId": lambda n : setattr(self, 'company_id', n.get_int_value()),
            "content": lambda n : setattr(self, 'content', n.get_str_value()),
            "contractId": lambda n : setattr(self, 'contract_id', n.get_int_value()),
            "deadlineDate": lambda n : setattr(self, 'deadline_date', n.get_int_value()),
            "dueDate": lambda n : setattr(self, 'due_date', n.get_int_value()),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "priority": lambda n : setattr(self, 'priority', n.get_int_value()),
            "statusId": lambda n : setattr(self, 'status_id', n.get_int_value()),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
            "typeId": lambda n : setattr(self, 'type_id', n.get_int_value()),
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
        writer.write_int_value("assignedToDepartmentId", self.assigned_to_department_id)
        writer.write_int_value("assignedToEmployeeId", self.assigned_to_employee_id)
        writer.write_int_value("companyId", self.company_id)
        writer.write_str_value("content", self.content)
        writer.write_int_value("contractId", self.contract_id)
        writer.write_int_value("deadlineDate", self.deadline_date)
        writer.write_int_value("dueDate", self.due_date)
        writer.write_int_value("id", self.id)
        writer.write_int_value("priority", self.priority)
        writer.write_int_value("statusId", self.status_id)
        writer.write_str_value("title", self.title)
        writer.write_int_value("typeId", self.type_id)
        writer.write_additional_data_value(self.additional_data)
    

