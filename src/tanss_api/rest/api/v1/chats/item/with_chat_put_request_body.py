from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .....models.tns_chat_message import TnsChatMessage
    from .....models.tns_chat_participant import TnsChatParticipant

@dataclass
class WithChatPutRequestBody(AdditionalDataHolder, Parsable):
    """
    Teilupdate mit TnsChat-Feldern
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The description property
    description: Optional[str] = None
    # The expectedResponseAlert property
    expected_response_alert: Optional[bool] = None
    # The expectedResponseTime property
    expected_response_time: Optional[int] = None
    # The messages property
    messages: Optional[list[TnsChatMessage]] = None
    # The participants property
    participants: Optional[list[TnsChatParticipant]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WithChatPutRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WithChatPutRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WithChatPutRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .....models.tns_chat_message import TnsChatMessage
        from .....models.tns_chat_participant import TnsChatParticipant

        from .....models.tns_chat_message import TnsChatMessage
        from .....models.tns_chat_participant import TnsChatParticipant

        fields: dict[str, Callable[[Any], None]] = {
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "expectedResponseAlert": lambda n : setattr(self, 'expected_response_alert', n.get_bool_value()),
            "expectedResponseTime": lambda n : setattr(self, 'expected_response_time', n.get_int_value()),
            "messages": lambda n : setattr(self, 'messages', n.get_collection_of_object_values(TnsChatMessage)),
            "participants": lambda n : setattr(self, 'participants', n.get_collection_of_object_values(TnsChatParticipant)),
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
        writer.write_str_value("description", self.description)
        writer.write_bool_value("expectedResponseAlert", self.expected_response_alert)
        writer.write_int_value("expectedResponseTime", self.expected_response_time)
        writer.write_collection_of_object_values("messages", self.messages)
        writer.write_collection_of_object_values("participants", self.participants)
        writer.write_additional_data_value(self.additional_data)
    

