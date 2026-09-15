from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class TnsTicketResubmissionMailOptions(AdditionalDataHolder, Parsable):
    """
    Options applied when a resubmission fires. Used for the SEND_MAIL mode(recipients + subject) and to optionally move the ticket to a target status.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # "bcc" recipients (e-mail addresses)
    bcc: Optional[list[str]] = None
    # "cc" recipients (e-mail addresses)
    cc: Optional[list[str]] = None
    # if set, the ticket status is changed to this ticket-state id when theresubmission fires.
    set_state_to: Optional[int] = None
    # subject of the resubmission e-mail
    subject: Optional[str] = None
    # "to" recipients (e-mail addresses)
    to: Optional[list[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsTicketResubmissionMailOptions:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsTicketResubmissionMailOptions
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsTicketResubmissionMailOptions()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "bcc": lambda n : setattr(self, 'bcc', n.get_collection_of_primitive_values(str)),
            "cc": lambda n : setattr(self, 'cc', n.get_collection_of_primitive_values(str)),
            "setStateTo": lambda n : setattr(self, 'set_state_to', n.get_int_value()),
            "subject": lambda n : setattr(self, 'subject', n.get_str_value()),
            "to": lambda n : setattr(self, 'to', n.get_collection_of_primitive_values(str)),
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
        writer.write_collection_of_primitive_values("bcc", self.bcc)
        writer.write_collection_of_primitive_values("cc", self.cc)
        writer.write_int_value("setStateTo", self.set_state_to)
        writer.write_str_value("subject", self.subject)
        writer.write_collection_of_primitive_values("to", self.to)
        writer.write_additional_data_value(self.additional_data)
    

