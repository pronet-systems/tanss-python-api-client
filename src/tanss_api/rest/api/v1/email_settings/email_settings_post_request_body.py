from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .email_settings_post_request_body_assignment_type import EmailSettingsPostRequestBody_assignmentType
    from .email_settings_post_request_body_pop3_type import EmailSettingsPostRequestBody_pop3Type
    from .email_settings_post_request_body_smtp_type import EmailSettingsPostRequestBody_smtpType

@dataclass
class EmailSettingsPostRequestBody(AdditionalDataHolder, Parsable):
    """
    Request body.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Whether the mailbox configuration is active.
    active: Optional[bool] = None
    # Identifier of the entity this mailbox is assigned to.
    assignment_id: Optional[int] = None
    # Type of entity this mailbox is assigned to.
    assignment_type: Optional[EmailSettingsPostRequestBody_assignmentType] = None
    # Unique identifier of the mailbox configuration.
    id: Optional[int] = None
    # Display name of the mailbox configuration.
    name: Optional[str] = None
    # Incoming mail server host name.
    pop3_host: Optional[str] = None
    # Incoming mail connection type.
    pop3_type: Optional[EmailSettingsPostRequestBody_pop3Type] = None
    # Incoming mail server user name.
    pop3_user: Optional[str] = None
    # Sender email address used for outgoing mail.
    smtp_address: Optional[str] = None
    # Whether the outgoing mail server requires authentication.
    smtp_auth: Optional[bool] = None
    # Outgoing mail server host name.
    smtp_host: Optional[str] = None
    # Outgoing mail connection type.
    smtp_type: Optional[EmailSettingsPostRequestBody_smtpType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EmailSettingsPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EmailSettingsPostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return EmailSettingsPostRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .email_settings_post_request_body_assignment_type import EmailSettingsPostRequestBody_assignmentType
        from .email_settings_post_request_body_pop3_type import EmailSettingsPostRequestBody_pop3Type
        from .email_settings_post_request_body_smtp_type import EmailSettingsPostRequestBody_smtpType

        from .email_settings_post_request_body_assignment_type import EmailSettingsPostRequestBody_assignmentType
        from .email_settings_post_request_body_pop3_type import EmailSettingsPostRequestBody_pop3Type
        from .email_settings_post_request_body_smtp_type import EmailSettingsPostRequestBody_smtpType

        fields: dict[str, Callable[[Any], None]] = {
            "active": lambda n : setattr(self, 'active', n.get_bool_value()),
            "assignmentId": lambda n : setattr(self, 'assignment_id', n.get_int_value()),
            "assignmentType": lambda n : setattr(self, 'assignment_type', n.get_enum_value(EmailSettingsPostRequestBody_assignmentType)),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "pop3Host": lambda n : setattr(self, 'pop3_host', n.get_str_value()),
            "pop3Type": lambda n : setattr(self, 'pop3_type', n.get_enum_value(EmailSettingsPostRequestBody_pop3Type)),
            "pop3User": lambda n : setattr(self, 'pop3_user', n.get_str_value()),
            "smtpAddress": lambda n : setattr(self, 'smtp_address', n.get_str_value()),
            "smtpAuth": lambda n : setattr(self, 'smtp_auth', n.get_bool_value()),
            "smtpHost": lambda n : setattr(self, 'smtp_host', n.get_str_value()),
            "smtpType": lambda n : setattr(self, 'smtp_type', n.get_enum_value(EmailSettingsPostRequestBody_smtpType)),
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
        writer.write_bool_value("active", self.active)
        writer.write_int_value("assignmentId", self.assignment_id)
        writer.write_enum_value("assignmentType", self.assignment_type)
        writer.write_str_value("name", self.name)
        writer.write_str_value("pop3Host", self.pop3_host)
        writer.write_enum_value("pop3Type", self.pop3_type)
        writer.write_str_value("pop3User", self.pop3_user)
        writer.write_str_value("smtpAddress", self.smtp_address)
        writer.write_bool_value("smtpAuth", self.smtp_auth)
        writer.write_str_value("smtpHost", self.smtp_host)
        writer.write_enum_value("smtpType", self.smtp_type)
        writer.write_additional_data_value(self.additional_data)
    

