from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class TnsVacationRequestDay(AdditionalDataHolder, Parsable):
    """
    describes a day used in a vacation request
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # vacation request for the whole afternoon?
    afternoon: Optional[bool] = None
    # timestamp for this day. always us the beginning of the day (0:00 o'clock)
    date: Optional[int] = None
    # if only a certain timeframe is used - end hour
    end_hour: Optional[int] = None
    # if only a certain timeframe is used - end minute
    end_minute: Optional[int] = None
    # vacation request for the whole forenoon?
    forenoon: Optional[bool] = None
    # if only a certain timeframe is used - pause (in minutes)
    pause: Optional[int] = None
    # if only a certain timeframe is used - starting hour
    start_hour: Optional[int] = None
    # if only a certain timeframe is used - starting minute
    start_minute: Optional[int] = None
    # id of the vacation request the day is assigned to
    vacation_request_id: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsVacationRequestDay:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsVacationRequestDay
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsVacationRequestDay()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "afternoon": lambda n : setattr(self, 'afternoon', n.get_bool_value()),
            "date": lambda n : setattr(self, 'date', n.get_int_value()),
            "endHour": lambda n : setattr(self, 'end_hour', n.get_int_value()),
            "endMinute": lambda n : setattr(self, 'end_minute', n.get_int_value()),
            "forenoon": lambda n : setattr(self, 'forenoon', n.get_bool_value()),
            "pause": lambda n : setattr(self, 'pause', n.get_int_value()),
            "startHour": lambda n : setattr(self, 'start_hour', n.get_int_value()),
            "startMinute": lambda n : setattr(self, 'start_minute', n.get_int_value()),
            "vacationRequestId": lambda n : setattr(self, 'vacation_request_id', n.get_int_value()),
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
        writer.write_bool_value("afternoon", self.afternoon)
        writer.write_int_value("date", self.date)
        writer.write_int_value("endHour", self.end_hour)
        writer.write_int_value("endMinute", self.end_minute)
        writer.write_bool_value("forenoon", self.forenoon)
        writer.write_int_value("pause", self.pause)
        writer.write_int_value("startHour", self.start_hour)
        writer.write_int_value("startMinute", self.start_minute)
        writer.write_int_value("vacationRequestId", self.vacation_request_id)
        writer.write_additional_data_value(self.additional_data)
    

