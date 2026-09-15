from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .timestamp import Timestamp
    from .timestamp_info_types import TimestampInfo_types
    from .week_day import WeekDay

@dataclass
class TimestampInfo(AdditionalDataHolder, Parsable):
    """
    Object containing informations about timestamps grouped by employee and days:* a list of timestamp objects* infos about the single "periods" of timestamps* the working time model of the employee for the given day
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # day in the format YYYY-mm-dd
    date: Optional[datetime.date] = None
    # id of the employee
    employee_id: Optional[int] = None
    # A list of all timestamps of the given day
    timestamps: Optional[list[Timestamp]] = None
    # a list of timestamp periods, grouped by the timestamp type. The key is the TimestampType, the value is a list of TimestampPeriods
    types: Optional[TimestampInfo_types] = None
    # Enum representing a weekday
    week_day: Optional[WeekDay] = None
    # id of the working time model. Infos are stored in the "list properties" - "workingTimeModels" - (ID) - "extras" - "model"
    working_time_model_id: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TimestampInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TimestampInfo
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TimestampInfo()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .timestamp import Timestamp
        from .timestamp_info_types import TimestampInfo_types
        from .week_day import WeekDay

        from .timestamp import Timestamp
        from .timestamp_info_types import TimestampInfo_types
        from .week_day import WeekDay

        fields: dict[str, Callable[[Any], None]] = {
            "date": lambda n : setattr(self, 'date', n.get_date_value()),
            "employeeId": lambda n : setattr(self, 'employee_id', n.get_int_value()),
            "timestamps": lambda n : setattr(self, 'timestamps', n.get_collection_of_object_values(Timestamp)),
            "types": lambda n : setattr(self, 'types', n.get_object_value(TimestampInfo_types)),
            "weekDay": lambda n : setattr(self, 'week_day', n.get_enum_value(WeekDay)),
            "workingTimeModelId": lambda n : setattr(self, 'working_time_model_id', n.get_int_value()),
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
        writer.write_date_value("date", self.date)
        writer.write_int_value("employeeId", self.employee_id)
        writer.write_collection_of_object_values("timestamps", self.timestamps)
        writer.write_object_value("types", self.types)
        writer.write_enum_value("weekDay", self.week_day)
        writer.write_int_value("workingTimeModelId", self.working_time_model_id)
        writer.write_additional_data_value(self.additional_data)
    

