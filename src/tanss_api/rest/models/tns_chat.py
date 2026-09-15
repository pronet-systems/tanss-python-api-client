from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tns_chat_status import TnsChatStatus

@dataclass
class TnsChat(AdditionalDataHolder, Parsable):
    """
    TANSS chat
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # id of employee who has closed this chat
    closed_by_employee_id: Optional[int] = None
    # id of employee who has created this chat
    created_by_employee_id: Optional[int] = None
    # timestamp of an chat creation
    creation_date: Optional[int] = None
    # if a general chat (without assignment) is created, a description is needed
    description: Optional[str] = None
    # timestamp of an expected response (if chat has an expected response)
    expected_response_time: Optional[int] = None
    # The id property
    id: Optional[int] = None
    # id of assignment
    link_id: Optional[int] = None
    # linkType of assignment
    link_type_id: Optional[int] = None
    # Enum representing a the state of the chat
    status: Optional[TnsChatStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsChat:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsChat
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsChat()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .tns_chat_status import TnsChatStatus

        from .tns_chat_status import TnsChatStatus

        fields: dict[str, Callable[[Any], None]] = {
            "closedByEmployeeId": lambda n : setattr(self, 'closed_by_employee_id', n.get_int_value()),
            "createdByEmployeeId": lambda n : setattr(self, 'created_by_employee_id', n.get_int_value()),
            "creationDate": lambda n : setattr(self, 'creation_date', n.get_int_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "expectedResponseTime": lambda n : setattr(self, 'expected_response_time', n.get_int_value()),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "linkId": lambda n : setattr(self, 'link_id', n.get_int_value()),
            "linkTypeId": lambda n : setattr(self, 'link_type_id', n.get_int_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(TnsChatStatus)),
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
        writer.write_int_value("closedByEmployeeId", self.closed_by_employee_id)
        writer.write_int_value("createdByEmployeeId", self.created_by_employee_id)
        writer.write_int_value("creationDate", self.creation_date)
        writer.write_str_value("description", self.description)
        writer.write_int_value("expectedResponseTime", self.expected_response_time)
        writer.write_int_value("linkId", self.link_id)
        writer.write_int_value("linkTypeId", self.link_type_id)
        writer.write_enum_value("status", self.status)
        writer.write_additional_data_value(self.additional_data)
    

