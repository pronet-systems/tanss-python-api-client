from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tns_mail_receiver import TnsMailReceiver

@dataclass
class TnsMail(AdditionalDataHolder, Parsable):
    """
    describes a mail object
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # html body
    body_html: Optional[str] = None
    # plain body
    body_plain: Optional[str] = None
    # id of the mail
    id: Optional[int] = None
    # true, if the mail was incoming
    inbound: Optional[bool] = None
    # true, if the mail is "internal" only
    internal: Optional[bool] = None
    # true, if mail was sent "only plain"
    plain_text_only: Optional[bool] = None
    # The receivers property
    receivers: Optional[list[TnsMailReceiver]] = None
    # e-Mail of the sender
    sender_e_mail: Optional[str] = None
    # id of the mail sender (if a tanss employee could be matches)
    sender_id: Optional[int] = None
    # name of the sender
    sender_name: Optional[str] = None
    # subject of the mail
    subject: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsMail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsMail
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsMail()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .tns_mail_receiver import TnsMailReceiver

        from .tns_mail_receiver import TnsMailReceiver

        fields: dict[str, Callable[[Any], None]] = {
            "bodyHtml": lambda n : setattr(self, 'body_html', n.get_str_value()),
            "bodyPlain": lambda n : setattr(self, 'body_plain', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "inbound": lambda n : setattr(self, 'inbound', n.get_bool_value()),
            "internal": lambda n : setattr(self, 'internal', n.get_bool_value()),
            "plainTextOnly": lambda n : setattr(self, 'plain_text_only', n.get_bool_value()),
            "receivers": lambda n : setattr(self, 'receivers', n.get_collection_of_object_values(TnsMailReceiver)),
            "senderEMail": lambda n : setattr(self, 'sender_e_mail', n.get_str_value()),
            "senderId": lambda n : setattr(self, 'sender_id', n.get_int_value()),
            "senderName": lambda n : setattr(self, 'sender_name', n.get_str_value()),
            "subject": lambda n : setattr(self, 'subject', n.get_str_value()),
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
        writer.write_str_value("bodyHtml", self.body_html)
        writer.write_str_value("bodyPlain", self.body_plain)
        writer.write_int_value("id", self.id)
        writer.write_bool_value("inbound", self.inbound)
        writer.write_bool_value("internal", self.internal)
        writer.write_bool_value("plainTextOnly", self.plain_text_only)
        writer.write_collection_of_object_values("receivers", self.receivers)
        writer.write_str_value("senderEMail", self.sender_e_mail)
        writer.write_int_value("senderId", self.sender_id)
        writer.write_str_value("senderName", self.sender_name)
        writer.write_str_value("subject", self.subject)
        writer.write_additional_data_value(self.additional_data)
    

