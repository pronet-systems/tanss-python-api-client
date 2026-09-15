from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tns_mail_receiver_method import TnsMailReceiverMethod
    from .tns_mail_status import TnsMailStatus

@dataclass
class TnsMailReceiver(AdditionalDataHolder, Parsable):
    """
    describes a mail receiver
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # e-Mail address of the receiver
    email_address: Optional[str] = None
    # Method of the mail receiver (TO / CC / BCC)
    method: Optional[TnsMailReceiverMethod] = None
    # name of the receiver
    name: Optional[str] = None
    # date, when the mail was sent
    sent_date: Optional[int] = None
    # Status of the mail sending
    status: Optional[TnsMailStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsMailReceiver:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsMailReceiver
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsMailReceiver()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .tns_mail_receiver_method import TnsMailReceiverMethod
        from .tns_mail_status import TnsMailStatus

        from .tns_mail_receiver_method import TnsMailReceiverMethod
        from .tns_mail_status import TnsMailStatus

        fields: dict[str, Callable[[Any], None]] = {
            "emailAddress": lambda n : setattr(self, 'email_address', n.get_str_value()),
            "method": lambda n : setattr(self, 'method', n.get_enum_value(TnsMailReceiverMethod)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "sentDate": lambda n : setattr(self, 'sent_date', n.get_int_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(TnsMailStatus)),
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
        writer.write_str_value("emailAddress", self.email_address)
        writer.write_enum_value("method", self.method)
        writer.write_str_value("name", self.name)
        writer.write_int_value("sentDate", self.sent_date)
        writer.write_enum_value("status", self.status)
        writer.write_additional_data_value(self.additional_data)
    

