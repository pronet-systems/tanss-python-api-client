from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .holidays_post_request_body_type import HolidaysPostRequestBody_type

@dataclass
class HolidaysPostRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Day of month of the holiday.
    day: Optional[int] = None
    # Timestamp representing the holiday date (epoch seconds).
    day_timestamp: Optional[int] = None
    # Name or description of the holiday.
    description: Optional[str] = None
    # Weighting factor applied for the holiday.
    factor: Optional[float] = None
    # Month of the holiday.
    month: Optional[int] = None
    # Portion of the day the holiday covers.
    type: Optional[HolidaysPostRequestBody_type] = None
    # Year of the holiday, or 0 for a recurring fixed holiday.
    year: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> HolidaysPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: HolidaysPostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return HolidaysPostRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .holidays_post_request_body_type import HolidaysPostRequestBody_type

        from .holidays_post_request_body_type import HolidaysPostRequestBody_type

        fields: dict[str, Callable[[Any], None]] = {
            "day": lambda n : setattr(self, 'day', n.get_int_value()),
            "dayTimestamp": lambda n : setattr(self, 'day_timestamp', n.get_int_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "factor": lambda n : setattr(self, 'factor', n.get_float_value()),
            "month": lambda n : setattr(self, 'month', n.get_int_value()),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(HolidaysPostRequestBody_type)),
            "year": lambda n : setattr(self, 'year', n.get_int_value()),
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
        writer.write_int_value("day", self.day)
        writer.write_int_value("dayTimestamp", self.day_timestamp)
        writer.write_str_value("description", self.description)
        writer.write_float_value("factor", self.factor)
        writer.write_int_value("month", self.month)
        writer.write_enum_value("type", self.type)
        writer.write_int_value("year", self.year)
        writer.write_additional_data_value(self.additional_data)
    

