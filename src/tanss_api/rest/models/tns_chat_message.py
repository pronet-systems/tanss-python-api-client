from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tns_chat_message_create import TnsChatMessageCreate

from .tns_chat_message_create import TnsChatMessageCreate

@dataclass
class TnsChatMessage(TnsChatMessageCreate, Parsable):
    """
    chat message object
    """
    # date when the message was sent
    creation_date: Optional[int] = None
    # id of the employee who has sent this message
    employee_id: Optional[int] = None
    # if the message has an expected response time, this is given here (in minutes)
    expected_response: Optional[int] = None
    # id of the chat message
    id: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsChatMessage:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsChatMessage
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsChatMessage()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .tns_chat_message_create import TnsChatMessageCreate

        from .tns_chat_message_create import TnsChatMessageCreate

        fields: dict[str, Callable[[Any], None]] = {
            "creationDate": lambda n : setattr(self, 'creation_date', n.get_int_value()),
            "employeeId": lambda n : setattr(self, 'employee_id', n.get_int_value()),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_int_value("creationDate", self.creation_date)
        writer.write_int_value("employeeId", self.employee_id)
        writer.write_int_value("id", self.id)
    

