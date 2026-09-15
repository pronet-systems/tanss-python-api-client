from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .state_post_request_body_state import StatePostRequestBody_state

@dataclass
class StatePostRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Identifier of the callback this log entry belongs to. Taken from the path parameter - a value sent here is ignored.
    callback_id: Optional[int] = None
    # Timestamp when the state change occurred. Set server-side - a value sent here is ignored.
    date: Optional[int] = None
    # Identifier of the employee who triggered the state change. Taken from the authenticated user - a value sent here is ignored.
    employee_id: Optional[int] = None
    # Free-text note describing the state change
    info_text: Optional[str] = None
    # State recorded for the callback
    state: Optional[StatePostRequestBody_state] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> StatePostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: StatePostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return StatePostRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .state_post_request_body_state import StatePostRequestBody_state

        from .state_post_request_body_state import StatePostRequestBody_state

        fields: dict[str, Callable[[Any], None]] = {
            "callbackId": lambda n : setattr(self, 'callback_id', n.get_int_value()),
            "date": lambda n : setattr(self, 'date', n.get_int_value()),
            "employeeId": lambda n : setattr(self, 'employee_id', n.get_int_value()),
            "infoText": lambda n : setattr(self, 'info_text', n.get_str_value()),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(StatePostRequestBody_state)),
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
        writer.write_str_value("infoText", self.info_text)
        writer.write_enum_value("state", self.state)
        writer.write_additional_data_value(self.additional_data)
    

