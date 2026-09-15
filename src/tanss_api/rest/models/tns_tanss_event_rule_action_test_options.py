from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tns_link_type import TnsLinkType
    from .tns_tanss_event_rule_action import TnsTanssEventRuleAction
    from .tns_ticket_notification_options import TnsTicketNotificationOptions

@dataclass
class TnsTanssEventRuleActionTestOptions(AdditionalDataHolder, Parsable):
    """
    defines the infos needed to trigger a rule test action
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Defines an assignment from a TANSS event rule to an assignment (i.e. Ticket Board Panel)
    action: Optional[TnsTanssEventRuleAction] = None
    # id of the assignment, for which an action shall be triggered (mostly a ticket id)
    link_id: Optional[int] = None
    # Enum representing the "link type" of an assignment. The id is given in the field "linkId"
    link_type: Optional[TnsLinkType] = None
    # object containing infos needed for a ticket notification
    ticket_notification_options: Optional[TnsTicketNotificationOptions] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsTanssEventRuleActionTestOptions:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsTanssEventRuleActionTestOptions
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsTanssEventRuleActionTestOptions()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .tns_link_type import TnsLinkType
        from .tns_tanss_event_rule_action import TnsTanssEventRuleAction
        from .tns_ticket_notification_options import TnsTicketNotificationOptions

        from .tns_link_type import TnsLinkType
        from .tns_tanss_event_rule_action import TnsTanssEventRuleAction
        from .tns_ticket_notification_options import TnsTicketNotificationOptions

        fields: dict[str, Callable[[Any], None]] = {
            "action": lambda n : setattr(self, 'action', n.get_object_value(TnsTanssEventRuleAction)),
            "linkId": lambda n : setattr(self, 'link_id', n.get_int_value()),
            "linkType": lambda n : setattr(self, 'link_type', n.get_enum_value(TnsLinkType)),
            "ticketNotificationOptions": lambda n : setattr(self, 'ticket_notification_options', n.get_object_value(TnsTicketNotificationOptions)),
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
        writer.write_object_value("action", self.action)
        writer.write_int_value("linkId", self.link_id)
        writer.write_enum_value("linkType", self.link_type)
        writer.write_object_value("ticketNotificationOptions", self.ticket_notification_options)
        writer.write_additional_data_value(self.additional_data)
    

