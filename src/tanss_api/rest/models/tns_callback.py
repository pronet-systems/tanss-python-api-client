from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tns_callback_state import TnsCallbackState

@dataclass
class TnsCallback(AdditionalDataHolder, Parsable):
    """
    Defines a callback
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # If the callback has to be "later" than a specific time, give here the minimum date for the callback
    callback_after_time: Optional[int] = None
    # If the callback has to be processed before a given date, specify this "latest" date here
    callback_until_time: Optional[int] = None
    # Here, the id of the company is given which has to be called back
    company_id: Optional[int] = None
    # same as "companyId", but here a string can be given (i.e. if the company wasn't created yet in TANSS)
    company_name: Optional[str] = None
    # The callback was created on this date. Set server-side - a value sent here is ignored.
    date: Optional[int] = None
    # Here, the id of the employee is given (who has to be called back)
    employee_id: Optional[int] = None
    # same as "employeeId", but here a string can be given (i.e. if the employee wasn't created yet in TANSS)
    employee_name: Optional[str] = None
    # Defines the employee who entered the callback. Set server-side from the authenticated user - a value sent here is ignored.
    from_employee_id: Optional[int] = None
    # (Optional) Further information regarding the callback
    info: Optional[str] = None
    # If the callback is assigned to a ticket (or other assignment), the id is given here
    link_id: Optional[int] = None
    # If the callback is assigned to a ticket (or other assignment), linkType is given here
    link_type_id: Optional[int] = None
    # You must define the phone number here
    phone_number: Optional[str] = None
    # priority of the callback from 1 (lowest) to 9 (highest)
    priority: Optional[int] = None
    # Describes a current "state" of a callback
    state: Optional[TnsCallbackState] = None
    # Callbacks can be assigned to a special department. Every employee of this department sees the callback.
    to_department_id: Optional[int] = None
    # The callback is assigned to this employee (This person has to do the call)
    to_employee_id: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsCallback:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsCallback
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsCallback()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .tns_callback_state import TnsCallbackState

        from .tns_callback_state import TnsCallbackState

        fields: dict[str, Callable[[Any], None]] = {
            "callbackAfterTime": lambda n : setattr(self, 'callback_after_time', n.get_int_value()),
            "callbackUntilTime": lambda n : setattr(self, 'callback_until_time', n.get_int_value()),
            "companyId": lambda n : setattr(self, 'company_id', n.get_int_value()),
            "companyName": lambda n : setattr(self, 'company_name', n.get_str_value()),
            "date": lambda n : setattr(self, 'date', n.get_int_value()),
            "employeeId": lambda n : setattr(self, 'employee_id', n.get_int_value()),
            "employeeName": lambda n : setattr(self, 'employee_name', n.get_str_value()),
            "fromEmployeeId": lambda n : setattr(self, 'from_employee_id', n.get_int_value()),
            "info": lambda n : setattr(self, 'info', n.get_str_value()),
            "linkId": lambda n : setattr(self, 'link_id', n.get_int_value()),
            "linkTypeId": lambda n : setattr(self, 'link_type_id', n.get_int_value()),
            "phoneNumber": lambda n : setattr(self, 'phone_number', n.get_str_value()),
            "priority": lambda n : setattr(self, 'priority', n.get_int_value()),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(TnsCallbackState)),
            "toDepartmentId": lambda n : setattr(self, 'to_department_id', n.get_int_value()),
            "toEmployeeId": lambda n : setattr(self, 'to_employee_id', n.get_int_value()),
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
        writer.write_int_value("callbackAfterTime", self.callback_after_time)
        writer.write_int_value("callbackUntilTime", self.callback_until_time)
        writer.write_int_value("companyId", self.company_id)
        writer.write_str_value("companyName", self.company_name)
        writer.write_int_value("employeeId", self.employee_id)
        writer.write_str_value("employeeName", self.employee_name)
        writer.write_str_value("info", self.info)
        writer.write_int_value("linkId", self.link_id)
        writer.write_int_value("linkTypeId", self.link_type_id)
        writer.write_str_value("phoneNumber", self.phone_number)
        writer.write_int_value("priority", self.priority)
        writer.write_enum_value("state", self.state)
        writer.write_int_value("toDepartmentId", self.to_department_id)
        writer.write_int_value("toEmployeeId", self.to_employee_id)
        writer.write_additional_data_value(self.additional_data)
    

