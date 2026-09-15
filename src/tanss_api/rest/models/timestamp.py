from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .timestamp_state import TimestampState
    from .timestamp_type import TimestampType

@dataclass
class Timestamp(AdditionalDataHolder, Parsable):
    """
    ....
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # date
    date: Optional[int] = None
    # id of the employee
    employee_id: Optional[int] = None
    # Id of the timestamp. On `PUT /api/v1/timestamps/{employeeId}/day/{day}` this fieldselects which entry of the day is meant: an existing id updates that entry, `0`creates a new one, and entries of the day that are missing from the list aredeleted. Elsewhere the value is generated server-side.
    id: Optional[int] = None
    # Determines the state for the timestamp (i.e. on, off)
    state: Optional[TimestampState] = None
    # Determines the type for the timestamp (i.e. work)
    type: Optional[TimestampType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Timestamp:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Timestamp
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Timestamp()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .timestamp_state import TimestampState
        from .timestamp_type import TimestampType

        from .timestamp_state import TimestampState
        from .timestamp_type import TimestampType

        fields: dict[str, Callable[[Any], None]] = {
            "date": lambda n : setattr(self, 'date', n.get_int_value()),
            "employeeId": lambda n : setattr(self, 'employee_id', n.get_int_value()),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(TimestampState)),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(TimestampType)),
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
        writer.write_int_value("date", self.date)
        writer.write_int_value("employeeId", self.employee_id)
        writer.write_int_value("id", self.id)
        writer.write_enum_value("state", self.state)
        writer.write_enum_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    

