from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .timestamp_history_type import TimestampHistoryType
    from .timestamp_state import TimestampState
    from .timestamp_type import TimestampType

@dataclass
class TimestampHistory(AdditionalDataHolder, Parsable):
    """
    Describes a change in a timestamp object
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # id of the user which did this change
    change_by_user_id: Optional[int] = None
    # timestamp when the change occured
    date: Optional[int] = None
    # The fromDate property
    from_date: Optional[int] = None
    # Determines the state for the timestamp (i.e. on, off)
    from_state: Optional[TimestampState] = None
    # Determines the type for the timestamp (i.e. work)
    from_type: Optional[TimestampType] = None
    # describes the "type" of a history entry
    history_type: Optional[TimestampHistoryType] = None
    # id of the history log entry
    id: Optional[int] = None
    # id of the timestamp which this history entry is for
    timestamp_id: Optional[int] = None
    # new timestamp (is 0 if the entry was deleted)
    to_date: Optional[int] = None
    # Determines the state for the timestamp (i.e. on, off)
    to_state: Optional[TimestampState] = None
    # Determines the type for the timestamp (i.e. work)
    to_type: Optional[TimestampType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TimestampHistory:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TimestampHistory
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TimestampHistory()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .timestamp_history_type import TimestampHistoryType
        from .timestamp_state import TimestampState
        from .timestamp_type import TimestampType

        from .timestamp_history_type import TimestampHistoryType
        from .timestamp_state import TimestampState
        from .timestamp_type import TimestampType

        fields: dict[str, Callable[[Any], None]] = {
            "changeByUserId": lambda n : setattr(self, 'change_by_user_id', n.get_int_value()),
            "date": lambda n : setattr(self, 'date', n.get_int_value()),
            "fromDate": lambda n : setattr(self, 'from_date', n.get_int_value()),
            "fromState": lambda n : setattr(self, 'from_state', n.get_enum_value(TimestampState)),
            "fromType": lambda n : setattr(self, 'from_type', n.get_enum_value(TimestampType)),
            "historyType": lambda n : setattr(self, 'history_type', n.get_enum_value(TimestampHistoryType)),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "timestampId": lambda n : setattr(self, 'timestamp_id', n.get_int_value()),
            "toDate": lambda n : setattr(self, 'to_date', n.get_int_value()),
            "toState": lambda n : setattr(self, 'to_state', n.get_enum_value(TimestampState)),
            "toType": lambda n : setattr(self, 'to_type', n.get_enum_value(TimestampType)),
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
        writer.write_int_value("changeByUserId", self.change_by_user_id)
        writer.write_int_value("date", self.date)
        writer.write_int_value("fromDate", self.from_date)
        writer.write_enum_value("fromState", self.from_state)
        writer.write_enum_value("fromType", self.from_type)
        writer.write_enum_value("historyType", self.history_type)
        writer.write_int_value("id", self.id)
        writer.write_int_value("timestampId", self.timestamp_id)
        writer.write_int_value("toDate", self.to_date)
        writer.write_enum_value("toState", self.to_state)
        writer.write_enum_value("toType", self.to_type)
        writer.write_additional_data_value(self.additional_data)
    

