from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tns_chat import TnsChat
    from .tns_chat_log import TnsChatLog
    from .tns_chat_message import TnsChatMessage
    from .tns_chat_participant import TnsChatParticipant

from .tns_chat import TnsChat

@dataclass
class TnsChatDetail(TnsChat, Parsable):
    """
    TANSS chat (including info regarding messages, participants, logs)
    """
    # The logs property
    logs: Optional[list[TnsChatLog]] = None
    # The messages property
    messages: Optional[list[TnsChatMessage]] = None
    # The participants property
    participants: Optional[list[TnsChatParticipant]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsChatDetail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsChatDetail
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsChatDetail()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .tns_chat import TnsChat
        from .tns_chat_log import TnsChatLog
        from .tns_chat_message import TnsChatMessage
        from .tns_chat_participant import TnsChatParticipant

        from .tns_chat import TnsChat
        from .tns_chat_log import TnsChatLog
        from .tns_chat_message import TnsChatMessage
        from .tns_chat_participant import TnsChatParticipant

        fields: dict[str, Callable[[Any], None]] = {
            "logs": lambda n : setattr(self, 'logs', n.get_collection_of_object_values(TnsChatLog)),
            "messages": lambda n : setattr(self, 'messages', n.get_collection_of_object_values(TnsChatMessage)),
            "participants": lambda n : setattr(self, 'participants', n.get_collection_of_object_values(TnsChatParticipant)),
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
        writer.write_collection_of_object_values("logs", self.logs)
        writer.write_collection_of_object_values("messages", self.messages)
        writer.write_collection_of_object_values("participants", self.participants)
    

