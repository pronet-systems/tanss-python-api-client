from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class TnsTanssEventTicketObject(AdditionalDataHolder, Parsable):
    """
    infos regarding a ticket which is stored as content in an tanss event
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # id of the assigned department
    assigned_to_department_id: Optional[int] = None
    # name of the assigned department
    assigned_to_department_name: Optional[str] = None
    # id of the assigned employee
    assigned_to_employee_id: Optional[int] = None
    # name of the assigned employee
    assigned_to_employee_name: Optional[str] = None
    # id of the company of the ticket
    company_id: Optional[int] = None
    # name of the company
    company_name: Optional[str] = None
    # content of the ticket
    content: Optional[str] = None
    # deadline date as timestamp
    deadline_date: Optional[int] = None
    # formatted deadline date
    deadline_date_formatted: Optional[str] = None
    # due date as timestamp
    due_date: Optional[int] = None
    # formatted due date
    due_date_formatted: Optional[str] = None
    # id of the ticket
    id: Optional[int] = None
    # id of the remitter (employee id)
    remitter_id: Optional[int] = None
    # name of the remitter
    remitter_name: Optional[str] = None
    # service cap of the ticket
    service_cap_amount: Optional[float] = None
    # formatted service cap
    service_cap_amount_formatted: Optional[str] = None
    # id of the ticket status
    status_id: Optional[int] = None
    # name of the ticket status
    status_name: Optional[str] = None
    # title of the ticket
    title: Optional[str] = None
    # id of the ticket type
    type_id: Optional[int] = None
    # name of the ticket type
    type_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsTanssEventTicketObject:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsTanssEventTicketObject
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsTanssEventTicketObject()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "assignedToDepartmentId": lambda n : setattr(self, 'assigned_to_department_id', n.get_int_value()),
            "assignedToDepartmentName": lambda n : setattr(self, 'assigned_to_department_name', n.get_str_value()),
            "assignedToEmployeeId": lambda n : setattr(self, 'assigned_to_employee_id', n.get_int_value()),
            "assignedToEmployeeName": lambda n : setattr(self, 'assigned_to_employee_name', n.get_str_value()),
            "companyId": lambda n : setattr(self, 'company_id', n.get_int_value()),
            "companyName": lambda n : setattr(self, 'company_name', n.get_str_value()),
            "content": lambda n : setattr(self, 'content', n.get_str_value()),
            "deadlineDate": lambda n : setattr(self, 'deadline_date', n.get_int_value()),
            "deadlineDateFormatted": lambda n : setattr(self, 'deadline_date_formatted', n.get_str_value()),
            "dueDate": lambda n : setattr(self, 'due_date', n.get_int_value()),
            "dueDateFormatted": lambda n : setattr(self, 'due_date_formatted', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "remitterId": lambda n : setattr(self, 'remitter_id', n.get_int_value()),
            "remitterName": lambda n : setattr(self, 'remitter_name', n.get_str_value()),
            "serviceCapAmount": lambda n : setattr(self, 'service_cap_amount', n.get_float_value()),
            "serviceCapAmountFormatted": lambda n : setattr(self, 'service_cap_amount_formatted', n.get_str_value()),
            "statusId": lambda n : setattr(self, 'status_id', n.get_int_value()),
            "statusName": lambda n : setattr(self, 'status_name', n.get_str_value()),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
            "typeId": lambda n : setattr(self, 'type_id', n.get_int_value()),
            "typeName": lambda n : setattr(self, 'type_name', n.get_str_value()),
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
        writer.write_str_value("assignedToDepartmentName", self.assigned_to_department_name)
        writer.write_int_value("assignedToEmployeeId", self.assigned_to_employee_id)
        writer.write_str_value("assignedToEmployeeName", self.assigned_to_employee_name)
        writer.write_int_value("companyId", self.company_id)
        writer.write_str_value("companyName", self.company_name)
        writer.write_str_value("content", self.content)
        writer.write_int_value("deadlineDate", self.deadline_date)
        writer.write_str_value("deadlineDateFormatted", self.deadline_date_formatted)
        writer.write_int_value("dueDate", self.due_date)
        writer.write_str_value("dueDateFormatted", self.due_date_formatted)
        writer.write_int_value("id", self.id)
        writer.write_int_value("remitterId", self.remitter_id)
        writer.write_str_value("remitterName", self.remitter_name)
        writer.write_float_value("serviceCapAmount", self.service_cap_amount)
        writer.write_str_value("serviceCapAmountFormatted", self.service_cap_amount_formatted)
        writer.write_int_value("statusId", self.status_id)
        writer.write_str_value("statusName", self.status_name)
        writer.write_str_value("title", self.title)
        writer.write_int_value("typeId", self.type_id)
        writer.write_str_value("typeName", self.type_name)
        writer.write_additional_data_value(self.additional_data)
    

