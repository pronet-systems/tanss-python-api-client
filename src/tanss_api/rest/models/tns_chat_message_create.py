from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class TnsChatMessageCreate(AdditionalDataHolder, Parsable):
    """
    chat message object (for persisting)
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # id of the corresponding chat id
    chat_id: Optional[int] = None
    # actual content / message
    content: Optional[str] = None
    # (optional) number of minutes in which a response is expected
    expected_response: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsChatMessageCreate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsChatMessageCreate
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsChatMessageCreate()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "chatId": lambda n : setattr(self, 'chat_id', n.get_int_value()),
            "content": lambda n : setattr(self, 'content', n.get_str_value()),
            "expectedResponse": lambda n : setattr(self, 'expected_response', n.get_int_value()),
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
        writer.write_int_value("chatId", self.chat_id)
        writer.write_str_value("content", self.content)
        writer.write_int_value("expectedResponse", self.expected_response)
        writer.write_additional_data_value(self.additional_data)
    

