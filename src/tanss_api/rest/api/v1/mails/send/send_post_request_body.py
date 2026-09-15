from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .send_post_request_body_create_ticket import SendPostRequestBody_createTicket
    from .send_post_request_body_mail_attachments import SendPostRequestBody_mailAttachments

@dataclass
class SendPostRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Blind carbon copy recipient addresses. Several addresses can be given in one string, separated by comma or semicolon.
    bcc: Optional[str] = None
    # Carbon copy recipient addresses. Several addresses can be given in one string, separated by comma or semicolon.
    cc: Optional[str] = None
    # Identifier of the company the mail relates to
    company_id: Optional[int] = None
    # Whether a copy of the mail is sent back to the sender
    copy_to_self: Optional[bool] = None
    # Optional ticket to be created together with the mail
    create_ticket: Optional[SendPostRequestBody_createTicket] = None
    # Identifier of the contact person the mail relates to
    employee_id: Optional[int] = None
    # List of file attachments included with the mail
    mail_attachments: Optional[list[SendPostRequestBody_mailAttachments]] = None
    # Plain text body of the mail
    plain_text: Optional[str] = None
    # Identifier of the reason or category assigned to the mail
    reason_id: Optional[int] = None
    # Subject line of the mail
    subject: Optional[str] = None
    # Primary recipient address. Several addresses can be given in one string, separated by comma or semicolon.
    to: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SendPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SendPostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SendPostRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .send_post_request_body_create_ticket import SendPostRequestBody_createTicket
        from .send_post_request_body_mail_attachments import SendPostRequestBody_mailAttachments

        from .send_post_request_body_create_ticket import SendPostRequestBody_createTicket
        from .send_post_request_body_mail_attachments import SendPostRequestBody_mailAttachments

        fields: dict[str, Callable[[Any], None]] = {
            "bcc": lambda n : setattr(self, 'bcc', n.get_str_value()),
            "cc": lambda n : setattr(self, 'cc', n.get_str_value()),
            "companyId": lambda n : setattr(self, 'company_id', n.get_int_value()),
            "copyToSelf": lambda n : setattr(self, 'copy_to_self', n.get_bool_value()),
            "createTicket": lambda n : setattr(self, 'create_ticket', n.get_object_value(SendPostRequestBody_createTicket)),
            "employeeId": lambda n : setattr(self, 'employee_id', n.get_int_value()),
            "mailAttachments": lambda n : setattr(self, 'mail_attachments', n.get_collection_of_object_values(SendPostRequestBody_mailAttachments)),
            "plainText": lambda n : setattr(self, 'plain_text', n.get_str_value()),
            "reasonId": lambda n : setattr(self, 'reason_id', n.get_int_value()),
            "subject": lambda n : setattr(self, 'subject', n.get_str_value()),
            "to": lambda n : setattr(self, 'to', n.get_str_value()),
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
        writer.write_int_value("companyId", self.company_id)
        writer.write_bool_value("copyToSelf", self.copy_to_self)
        writer.write_object_value("createTicket", self.create_ticket)
        writer.write_int_value("employeeId", self.employee_id)
        writer.write_collection_of_object_values("mailAttachments", self.mail_attachments)
        writer.write_str_value("plainText", self.plain_text)
        writer.write_int_value("reasonId", self.reason_id)
        writer.write_str_value("subject", self.subject)
        writer.write_str_value("to", self.to)
        writer.write_additional_data_value(self.additional_data)
    

