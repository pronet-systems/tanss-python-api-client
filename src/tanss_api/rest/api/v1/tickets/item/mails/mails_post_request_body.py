from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .mails_post_request_body_type import MailsPostRequestBody_type

@dataclass
class MailsPostRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Blind carbon copy recipient email addresses. Several addresses can be given in one string, separated by comma or semicolon.
    bcc: Optional[str] = None
    # Carbon copy recipient email addresses. Several addresses can be given in one string, separated by comma or semicolon.
    cc: Optional[str] = None
    # Identifier of the cost center for the mail
    cost_center_id: Optional[int] = None
    # Whether the mail body is HTML formatted
    html: Optional[bool] = None
    # Whether the mail is treated as an internal message
    internal: Optional[bool] = None
    # Whether the mail is being sent again
    send_again: Optional[bool] = None
    # Start time as a Unix timestamp in seconds
    start_time: Optional[int] = None
    # Ticket status to set when sending the mail
    status_id: Optional[int] = None
    # Body text of the email
    text: Optional[str] = None
    # Subject of the email
    title: Optional[str] = None
    # Primary recipient email address. Several addresses can be given in one string, separated by comma or semicolon.
    to: Optional[str] = None
    # Type of the mail action
    type: Optional[MailsPostRequestBody_type] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MailsPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MailsPostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MailsPostRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .mails_post_request_body_type import MailsPostRequestBody_type

        from .mails_post_request_body_type import MailsPostRequestBody_type

        fields: dict[str, Callable[[Any], None]] = {
            "bcc": lambda n : setattr(self, 'bcc', n.get_str_value()),
            "cc": lambda n : setattr(self, 'cc', n.get_str_value()),
            "costCenterId": lambda n : setattr(self, 'cost_center_id', n.get_int_value()),
            "html": lambda n : setattr(self, 'html', n.get_bool_value()),
            "internal": lambda n : setattr(self, 'internal', n.get_bool_value()),
            "sendAgain": lambda n : setattr(self, 'send_again', n.get_bool_value()),
            "startTime": lambda n : setattr(self, 'start_time', n.get_int_value()),
            "statusId": lambda n : setattr(self, 'status_id', n.get_int_value()),
            "text": lambda n : setattr(self, 'text', n.get_str_value()),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
            "to": lambda n : setattr(self, 'to', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(MailsPostRequestBody_type)),
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
        writer.write_str_value("bcc", self.bcc)
        writer.write_str_value("cc", self.cc)
        writer.write_int_value("costCenterId", self.cost_center_id)
        writer.write_bool_value("html", self.html)
        writer.write_bool_value("internal", self.internal)
        writer.write_bool_value("sendAgain", self.send_again)
        writer.write_int_value("startTime", self.start_time)
        writer.write_int_value("statusId", self.status_id)
        writer.write_str_value("text", self.text)
        writer.write_str_value("title", self.title)
        writer.write_str_value("to", self.to)
        writer.write_enum_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    

