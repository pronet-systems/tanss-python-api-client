from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .supports_post_request_body_status import SupportsPostRequestBody_status

@dataclass
class SupportsPostRequestBody(AdditionalDataHolder, Parsable):
    """
    Request body.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Identifier of the employee who approved the request
    approved_by_employee_id: Optional[int] = None
    # Comment provided upon approval
    comment_approved: Optional[str] = None
    # Comment provided with the request
    comment_request: Optional[str] = None
    # Timestamp when the request was created
    date: Optional[int] = None
    # Calendar day the overtime applies to (yyyy-MM-dd)
    day: Optional[datetime.date] = None
    # Identifier of the employee submitting the overtime request
    employee_id: Optional[int] = None
    # Hourly rate used to calculate the payout amount
    hourly_rate: Optional[float] = None
    # Unique identifier of the overtime request
    id: Optional[int] = None
    # Number of overtime minutes approved
    minutes_approved: Optional[int] = None
    # Number of overtime minutes requested
    minutes_requested: Optional[int] = None
    # Timestamp when the overtime was paid out
    payment_date: Optional[int] = None
    # Current status of the overtime request
    status: Optional[SupportsPostRequestBody_status] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SupportsPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SupportsPostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SupportsPostRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .supports_post_request_body_status import SupportsPostRequestBody_status

        from .supports_post_request_body_status import SupportsPostRequestBody_status

        fields: dict[str, Callable[[Any], None]] = {
            "approvedByEmployeeId": lambda n : setattr(self, 'approved_by_employee_id', n.get_int_value()),
            "commentApproved": lambda n : setattr(self, 'comment_approved', n.get_str_value()),
            "commentRequest": lambda n : setattr(self, 'comment_request', n.get_str_value()),
            "date": lambda n : setattr(self, 'date', n.get_int_value()),
            "day": lambda n : setattr(self, 'day', n.get_date_value()),
            "employeeId": lambda n : setattr(self, 'employee_id', n.get_int_value()),
            "hourlyRate": lambda n : setattr(self, 'hourly_rate', n.get_float_value()),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "minutesApproved": lambda n : setattr(self, 'minutes_approved', n.get_int_value()),
            "minutesRequested": lambda n : setattr(self, 'minutes_requested', n.get_int_value()),
            "paymentDate": lambda n : setattr(self, 'payment_date', n.get_int_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(SupportsPostRequestBody_status)),
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
        writer.write_int_value("approvedByEmployeeId", self.approved_by_employee_id)
        writer.write_str_value("commentApproved", self.comment_approved)
        writer.write_str_value("commentRequest", self.comment_request)
        writer.write_int_value("date", self.date)
        writer.write_date_value("day", self.day)
        writer.write_int_value("employeeId", self.employee_id)
        writer.write_float_value("hourlyRate", self.hourly_rate)
        writer.write_int_value("minutesApproved", self.minutes_approved)
        writer.write_int_value("minutesRequested", self.minutes_requested)
        writer.write_int_value("paymentDate", self.payment_date)
        writer.write_enum_value("status", self.status)
        writer.write_additional_data_value(self.additional_data)
    

