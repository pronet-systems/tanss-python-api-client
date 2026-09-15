from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tns_tag import TnsTag
    from .tns_tanss_event_mail_object import TnsTanssEventMailObject
    from .tns_tanss_event_posting_object import TnsTanssEventPostingObject
    from .tns_tanss_event_support_object import TnsTanssEventSupportObject
    from .tns_tanss_event_ticket_object import TnsTanssEventTicketObject

@dataclass
class TnsTanssEventTicketContent(AdditionalDataHolder, Parsable):
    """
    ticket content of a tanss event
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # if tags were added, here the list of added tags is given
    added_tags: Optional[list[TnsTag]] = None
    # if the tanss ticket object contains infos about a comment, then the infos are given here
    comment: Optional[TnsTanssEventPostingObject] = None
    # if the tanss ticket object contains infos about a mail, then the infos are given here
    mail: Optional[TnsTanssEventMailObject] = None
    # infos regarding a ticket which is stored as content in an tanss event
    old_values: Optional[TnsTanssEventTicketObject] = None
    # if tags were removed, here the list of removed tags is given
    removed_tags: Optional[list[TnsTag]] = None
    # if the tanss ticket object contains infos about a support, then the infos are given here
    support: Optional[TnsTanssEventSupportObject] = None
    # infos regarding a ticket which is stored as content in an tanss event
    ticket: Optional[TnsTanssEventTicketObject] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsTanssEventTicketContent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsTanssEventTicketContent
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsTanssEventTicketContent()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .tns_tag import TnsTag
        from .tns_tanss_event_mail_object import TnsTanssEventMailObject
        from .tns_tanss_event_posting_object import TnsTanssEventPostingObject
        from .tns_tanss_event_support_object import TnsTanssEventSupportObject
        from .tns_tanss_event_ticket_object import TnsTanssEventTicketObject

        from .tns_tag import TnsTag
        from .tns_tanss_event_mail_object import TnsTanssEventMailObject
        from .tns_tanss_event_posting_object import TnsTanssEventPostingObject
        from .tns_tanss_event_support_object import TnsTanssEventSupportObject
        from .tns_tanss_event_ticket_object import TnsTanssEventTicketObject

        fields: dict[str, Callable[[Any], None]] = {
            "addedTags": lambda n : setattr(self, 'added_tags', n.get_collection_of_object_values(TnsTag)),
            "comment": lambda n : setattr(self, 'comment', n.get_object_value(TnsTanssEventPostingObject)),
            "mail": lambda n : setattr(self, 'mail', n.get_object_value(TnsTanssEventMailObject)),
            "oldValues": lambda n : setattr(self, 'old_values', n.get_object_value(TnsTanssEventTicketObject)),
            "removedTags": lambda n : setattr(self, 'removed_tags', n.get_collection_of_object_values(TnsTag)),
            "support": lambda n : setattr(self, 'support', n.get_object_value(TnsTanssEventSupportObject)),
            "ticket": lambda n : setattr(self, 'ticket', n.get_object_value(TnsTanssEventTicketObject)),
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
        writer.write_collection_of_object_values("addedTags", self.added_tags)
        writer.write_object_value("comment", self.comment)
        writer.write_object_value("mail", self.mail)
        writer.write_object_value("oldValues", self.old_values)
        writer.write_collection_of_object_values("removedTags", self.removed_tags)
        writer.write_object_value("support", self.support)
        writer.write_object_value("ticket", self.ticket)
        writer.write_additional_data_value(self.additional_data)
    

