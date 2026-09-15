from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tns_callback_state import TnsCallbackState

@dataclass
class TnsCallbackStateLog(AdditionalDataHolder, Parsable):
    """
    Describes a state change of a callback
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Timestamp of this log entry
    date: Optional[int] = None
    # This employee has done the state change
    employee_id: Optional[int] = None
    # If a info was given, it will be shown here
    info_text: Optional[str] = None
    # Describes a current "state" of a callback
    state: Optional[TnsCallbackState] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsCallbackStateLog:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsCallbackStateLog
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsCallbackStateLog()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .tns_callback_state import TnsCallbackState

        from .tns_callback_state import TnsCallbackState

        fields: dict[str, Callable[[Any], None]] = {
            "date": lambda n : setattr(self, 'date', n.get_int_value()),
            "employeeId": lambda n : setattr(self, 'employee_id', n.get_int_value()),
            "infoText": lambda n : setattr(self, 'info_text', n.get_str_value()),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(TnsCallbackState)),
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
        writer.write_str_value("infoText", self.info_text)
        writer.write_enum_value("state", self.state)
        writer.write_additional_data_value(self.additional_data)
    

