from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tns_mail_transport_security_type import TnsMailTransportSecurityType

@dataclass
class TnsEmailSettingsSmtp(AdditionalDataHolder, Parsable):
    """
    configuration of smtp server settings (for sending mails)
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # e-mail address for sending e-mails
    smtp_address: Optional[str] = None
    # true if the smtp server requires authentication
    smtp_auth: Optional[bool] = None
    # enum representing the security setting of the mail server
    smtp_encryption_type: Optional[TnsMailTransportSecurityType] = None
    # host (address) of the smtp server
    smtp_host: Optional[str] = None
    # password of the smtp server
    smtp_password: Optional[str] = None
    # send mails with this displayed name (optional)
    smtp_sender_name: Optional[str] = None
    # username of the smtp server
    smtp_user: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsEmailSettingsSmtp:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsEmailSettingsSmtp
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsEmailSettingsSmtp()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .tns_mail_transport_security_type import TnsMailTransportSecurityType

        from .tns_mail_transport_security_type import TnsMailTransportSecurityType

        fields: dict[str, Callable[[Any], None]] = {
            "smtpAddress": lambda n : setattr(self, 'smtp_address', n.get_str_value()),
            "smtpAuth": lambda n : setattr(self, 'smtp_auth', n.get_bool_value()),
            "smtpEncryptionType": lambda n : setattr(self, 'smtp_encryption_type', n.get_enum_value(TnsMailTransportSecurityType)),
            "smtpHost": lambda n : setattr(self, 'smtp_host', n.get_str_value()),
            "smtpPassword": lambda n : setattr(self, 'smtp_password', n.get_str_value()),
            "smtpSenderName": lambda n : setattr(self, 'smtp_sender_name', n.get_str_value()),
            "smtpUser": lambda n : setattr(self, 'smtp_user', n.get_str_value()),
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
        writer.write_str_value("smtpAddress", self.smtp_address)
        writer.write_bool_value("smtpAuth", self.smtp_auth)
        writer.write_enum_value("smtpEncryptionType", self.smtp_encryption_type)
        writer.write_str_value("smtpHost", self.smtp_host)
        writer.write_str_value("smtpPassword", self.smtp_password)
        writer.write_str_value("smtpSenderName", self.smtp_sender_name)
        writer.write_str_value("smtpUser", self.smtp_user)
        writer.write_additional_data_value(self.additional_data)
    

