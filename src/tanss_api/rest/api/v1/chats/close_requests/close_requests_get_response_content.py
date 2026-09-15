from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .....models.tns_chat import TnsChat

@dataclass
class CloseRequestsGetResponse_content(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The chatsWithUnreadMessages property
    chats_with_unread_messages: Optional[list[TnsChat]] = None
    # The closeRequests property
    close_requests: Optional[list[TnsChat]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CloseRequestsGetResponse_content:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CloseRequestsGetResponse_content
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CloseRequestsGetResponse_content()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .....models.tns_chat import TnsChat

        from .....models.tns_chat import TnsChat

        fields: dict[str, Callable[[Any], None]] = {
            "chatsWithUnreadMessages": lambda n : setattr(self, 'chats_with_unread_messages', n.get_collection_of_object_values(TnsChat)),
            "closeRequests": lambda n : setattr(self, 'close_requests', n.get_collection_of_object_values(TnsChat)),
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
        writer.write_collection_of_object_values("chatsWithUnreadMessages", self.chats_with_unread_messages)
        writer.write_collection_of_object_values("closeRequests", self.close_requests)
        writer.write_additional_data_value(self.additional_data)
    

