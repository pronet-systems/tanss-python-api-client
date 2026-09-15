from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tns_ticket_notification_reason import TnsTicketNotificationReason

@dataclass
class TnsTicketNotificationOptions(AdditionalDataHolder, Parsable):
    """
    object containing infos needed for a ticket notification
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # if reason is "NEW_COMMENT", the id of the comment is given here
    comment_id: Optional[int] = None
    # if reason is "EMAIL_RECEIVED", the id of the mail is given here
    mail_id: Optional[int] = None
    # reason of the ticket notification
    reason: Optional[TnsTicketNotificationReason] = None
    # if reason is "NEW_SUPPORT", the id of the support is given here
    support_id: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsTicketNotificationOptions:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsTicketNotificationOptions
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsTicketNotificationOptions()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .tns_ticket_notification_reason import TnsTicketNotificationReason

        from .tns_ticket_notification_reason import TnsTicketNotificationReason

        fields: dict[str, Callable[[Any], None]] = {
            "commentId": lambda n : setattr(self, 'comment_id', n.get_int_value()),
            "mailId": lambda n : setattr(self, 'mail_id', n.get_int_value()),
            "reason": lambda n : setattr(self, 'reason', n.get_enum_value(TnsTicketNotificationReason)),
            "supportId": lambda n : setattr(self, 'support_id', n.get_int_value()),
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
        writer.write_int_value("commentId", self.comment_id)
        writer.write_int_value("mailId", self.mail_id)
        writer.write_enum_value("reason", self.reason)
        writer.write_int_value("supportId", self.support_id)
        writer.write_additional_data_value(self.additional_data)
    

