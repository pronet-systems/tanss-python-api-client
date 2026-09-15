from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .ticket_standard import TicketStandard
    from .tns_chat_vue import TnsChatVue
    from .tns_support_future import TnsSupportFuture

from .ticket_standard import TicketStandard

@dataclass
class TicketList(TicketStandard, Parsable):
    """
    model used to render tickets in lists
    """
    # list of chat ids for this ticket
    chats: Optional[list[TnsChatVue]] = None
    # returns the internal content if the user has right to
    internal_content: Optional[str] = None
    # timestamp, when the ticket was last modified
    last_state_change_date: Optional[int] = None
    # id of the employee who last modified this ticket
    last_state_change_employee_id: Optional[int] = None
    # timestamp of last modification
    modified: Optional[int] = None
    # The nextSupport property
    next_support: Optional[TnsSupportFuture] = None
    # number of documents for this ticket
    number_of_documents: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TicketList:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TicketList
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TicketList()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .ticket_standard import TicketStandard
        from .tns_chat_vue import TnsChatVue
        from .tns_support_future import TnsSupportFuture

        from .ticket_standard import TicketStandard
        from .tns_chat_vue import TnsChatVue
        from .tns_support_future import TnsSupportFuture

        fields: dict[str, Callable[[Any], None]] = {
            "chats": lambda n : setattr(self, 'chats', n.get_collection_of_object_values(TnsChatVue)),
            "internalContent": lambda n : setattr(self, 'internal_content', n.get_str_value()),
            "lastStateChangeDate": lambda n : setattr(self, 'last_state_change_date', n.get_int_value()),
            "lastStateChangeEmployeeId": lambda n : setattr(self, 'last_state_change_employee_id', n.get_int_value()),
            "modified": lambda n : setattr(self, 'modified', n.get_int_value()),
            "nextSupport": lambda n : setattr(self, 'next_support', n.get_object_value(TnsSupportFuture)),
            "numberOfDocuments": lambda n : setattr(self, 'number_of_documents', n.get_int_value()),
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
        writer.write_str_value("internalContent", self.internal_content)
        writer.write_int_value("modified", self.modified)
        writer.write_object_value("nextSupport", self.next_support)
    

