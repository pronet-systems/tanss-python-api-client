from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .manual_booking_put_request_body_timeframe import ManualBookingPutRequestBody_timeframe

@dataclass
class ManualBookingPutRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Identifier of the employee for whom the manual timestamp booking is created.
    employee_id: Optional[int] = None
    # Whether frontend-oriented values should be used for the booking.
    frontend_values: Optional[bool] = None
    # Time range (from/to) of the manual booking.
    timeframe: Optional[ManualBookingPutRequestBody_timeframe] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ManualBookingPutRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ManualBookingPutRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ManualBookingPutRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .manual_booking_put_request_body_timeframe import ManualBookingPutRequestBody_timeframe

        from .manual_booking_put_request_body_timeframe import ManualBookingPutRequestBody_timeframe

        fields: dict[str, Callable[[Any], None]] = {
            "employeeId": lambda n : setattr(self, 'employee_id', n.get_int_value()),
            "frontendValues": lambda n : setattr(self, 'frontend_values', n.get_bool_value()),
            "timeframe": lambda n : setattr(self, 'timeframe', n.get_object_value(ManualBookingPutRequestBody_timeframe)),
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
        writer.write_int_value("employeeId", self.employee_id)
        writer.write_bool_value("frontendValues", self.frontend_values)
        writer.write_object_value("timeframe", self.timeframe)
        writer.write_additional_data_value(self.additional_data)
    

