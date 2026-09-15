from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class TimestampDayClosingTillDateError(AdditionalDataHolder, Parsable):
    """
    details on an error that occured while creating multiple day closings
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # day when the error occured
    date: Optional[datetime.date] = None
    # id of the employee
    employee_id: Optional[int] = None
    # localized text of the error message
    localized_text: Optional[str] = None
    # key/identifier of the error message
    text: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TimestampDayClosingTillDateError:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TimestampDayClosingTillDateError
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TimestampDayClosingTillDateError()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "date": lambda n : setattr(self, 'date', n.get_date_value()),
            "employeeId": lambda n : setattr(self, 'employee_id', n.get_int_value()),
            "localizedText": lambda n : setattr(self, 'localized_text', n.get_str_value()),
            "text": lambda n : setattr(self, 'text', n.get_str_value()),
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
        writer.write_str_value("localizedText", self.localized_text)
        writer.write_str_value("text", self.text)
        writer.write_additional_data_value(self.additional_data)
    

