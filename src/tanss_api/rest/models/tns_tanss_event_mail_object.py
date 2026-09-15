from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class TnsTanssEventMailObject(AdditionalDataHolder, Parsable):
    """
    if the tanss ticket object contains infos about a mail, then the infos are given here
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # plaintext body of the mail
    body_plain: Optional[str] = None
    # id of the mail
    id: Optional[int] = None
    # true if it's an inbound E-Mail
    inbound: Optional[bool] = None
    # true if it's an internal E-Mail
    internal: Optional[bool] = None
    # list of E-Mail receivers
    receiver_e_mails: Optional[list[str]] = None
    # email of the sender
    sender_e_mail: Optional[str] = None
    # name of the sender
    sender_name: Optional[str] = None
    # mail subject
    subject: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsTanssEventMailObject:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsTanssEventMailObject
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsTanssEventMailObject()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "bodyPlain": lambda n : setattr(self, 'body_plain', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "inbound": lambda n : setattr(self, 'inbound', n.get_bool_value()),
            "internal": lambda n : setattr(self, 'internal', n.get_bool_value()),
            "receiverEMails": lambda n : setattr(self, 'receiver_e_mails', n.get_collection_of_primitive_values(str)),
            "senderEMail": lambda n : setattr(self, 'sender_e_mail', n.get_str_value()),
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
        writer.write_str_value("bodyPlain", self.body_plain)
        writer.write_int_value("id", self.id)
        writer.write_bool_value("inbound", self.inbound)
        writer.write_bool_value("internal", self.internal)
        writer.write_collection_of_primitive_values("receiverEMails", self.receiver_e_mails)
        writer.write_str_value("senderEMail", self.sender_e_mail)
        writer.write_str_value("senderName", self.sender_name)
        writer.write_str_value("subject", self.subject)
        writer.write_additional_data_value(self.additional_data)
    

