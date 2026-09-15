from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class Timer(AdditionalDataHolder, Parsable):
    """
    a TANSS timer
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # (optional) if the timer was created for a callback, the id is given here
    callback_id: Optional[int] = None
    # id of the company (otional)
    company_id: Optional[int] = None
    # total duration (in seconds) for this timer
    duration: Optional[int] = None
    # id of the employee of this timer
    employee_id: Optional[int] = None
    # The id property
    id: Optional[int] = None
    # (optional) if the timer was created for a misc. assignment, the linkId goes here
    link_id: Optional[int] = None
    # (optional) if the timer was created for a misc. assignment, the linkTypeId goes here
    link_type_id: Optional[int] = None
    # (optional) if the timer was created for a ticket, the id is given here
    ticket_id: Optional[int] = None
    # a title for this timer
    title: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Timer:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Timer
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Timer()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "callbackId": lambda n : setattr(self, 'callback_id', n.get_int_value()),
            "companyId": lambda n : setattr(self, 'company_id', n.get_int_value()),
            "duration": lambda n : setattr(self, 'duration', n.get_int_value()),
            "employeeId": lambda n : setattr(self, 'employee_id', n.get_int_value()),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "linkId": lambda n : setattr(self, 'link_id', n.get_int_value()),
            "linkTypeId": lambda n : setattr(self, 'link_type_id', n.get_int_value()),
            "ticketId": lambda n : setattr(self, 'ticket_id', n.get_int_value()),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
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
        writer.write_int_value("callbackId", self.callback_id)
        writer.write_int_value("companyId", self.company_id)
        writer.write_int_value("duration", self.duration)
        writer.write_int_value("employeeId", self.employee_id)
        writer.write_int_value("id", self.id)
        writer.write_int_value("linkId", self.link_id)
        writer.write_int_value("linkTypeId", self.link_type_id)
        writer.write_int_value("ticketId", self.ticket_id)
        writer.write_str_value("title", self.title)
        writer.write_additional_data_value(self.additional_data)
    

