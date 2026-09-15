from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tns_chat_load_message_type import TnsChatLoadMessageType
    from .tns_chat_status import TnsChatStatus

@dataclass
class TnsChatConfiguration(AdditionalDataHolder, Parsable):
    """
    Here, the filter settings for the chat list are stored
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # if a list of specific chat ids shall be used, you can place the here
    chat_ids: Optional[list[int]] = None
    # filters chats from this given chat creator
    creator_id: Optional[int] = None
    # filters chats for a given employee id. All chats will be returned to which this employee has access to
    employee_id: Optional[int] = None
    # if true, the "linked entities" will be filled as well (with information regarding employees, tickets etc.)
    fill_linked_entities: Optional[bool] = None
    # if pagination is used, you can enter the number of items per page
    items_per_page: Optional[int] = None
    # id of assignment
    link_id: Optional[int] = None
    # if multiple assignment ids schall be fetched, you can use an array of integers here
    link_ids: Optional[list[int]] = None
    # linkType of assignment
    link_type_id: Optional[int] = None
    # describes if/which messages shall be loaded in a chat list
    load_messages: Optional[TnsChatLoadMessageType] = None
    # only returns chats with at least the given creation date
    minimum_creation_date: Optional[int] = None
    # if true, only open chats with an expired expected time will be shown (overrides "status")
    only_expected_time_expired: Optional[bool] = None
    # if pagination is used, you can enter the page number here
    page: Optional[int] = None
    # If chats shall be filtered for a given search text, this text goes here
    search_string: Optional[str] = None
    # if true, only returns chats which the employee is assigned as creator or participant.Otherwise returns all chats whith access.
    show_only_participated_chat: Optional[bool] = None
    # Enum representing a the state of the chat
    status: Optional[TnsChatStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsChatConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsChatConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsChatConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .tns_chat_load_message_type import TnsChatLoadMessageType
        from .tns_chat_status import TnsChatStatus

        from .tns_chat_load_message_type import TnsChatLoadMessageType
        from .tns_chat_status import TnsChatStatus

        fields: dict[str, Callable[[Any], None]] = {
            "chatIds": lambda n : setattr(self, 'chat_ids', n.get_collection_of_primitive_values(int)),
            "creatorId": lambda n : setattr(self, 'creator_id', n.get_int_value()),
            "employeeId": lambda n : setattr(self, 'employee_id', n.get_int_value()),
            "fillLinkedEntities": lambda n : setattr(self, 'fill_linked_entities', n.get_bool_value()),
            "itemsPerPage": lambda n : setattr(self, 'items_per_page', n.get_int_value()),
            "linkId": lambda n : setattr(self, 'link_id', n.get_int_value()),
            "linkIds": lambda n : setattr(self, 'link_ids', n.get_collection_of_primitive_values(int)),
            "linkTypeId": lambda n : setattr(self, 'link_type_id', n.get_int_value()),
            "loadMessages": lambda n : setattr(self, 'load_messages', n.get_enum_value(TnsChatLoadMessageType)),
            "minimumCreationDate": lambda n : setattr(self, 'minimum_creation_date', n.get_int_value()),
            "onlyExpectedTimeExpired": lambda n : setattr(self, 'only_expected_time_expired', n.get_bool_value()),
            "page": lambda n : setattr(self, 'page', n.get_int_value()),
            "searchString": lambda n : setattr(self, 'search_string', n.get_str_value()),
            "showOnlyParticipatedChat": lambda n : setattr(self, 'show_only_participated_chat', n.get_bool_value()),
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
        writer.write_collection_of_primitive_values("chatIds", self.chat_ids)
        writer.write_int_value("creatorId", self.creator_id)
        writer.write_int_value("employeeId", self.employee_id)
        writer.write_bool_value("fillLinkedEntities", self.fill_linked_entities)
        writer.write_int_value("itemsPerPage", self.items_per_page)
        writer.write_int_value("linkId", self.link_id)
        writer.write_collection_of_primitive_values("linkIds", self.link_ids)
        writer.write_int_value("linkTypeId", self.link_type_id)
        writer.write_enum_value("loadMessages", self.load_messages)
        writer.write_int_value("minimumCreationDate", self.minimum_creation_date)
        writer.write_bool_value("onlyExpectedTimeExpired", self.only_expected_time_expired)
        writer.write_int_value("page", self.page)
        writer.write_str_value("searchString", self.search_string)
        writer.write_bool_value("showOnlyParticipatedChat", self.show_only_participated_chat)
        writer.write_enum_value("status", self.status)
        writer.write_additional_data_value(self.additional_data)
    

