from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tns_ev_company_user_information import TnsEvCompanyUserInformation
    from .tns_ev_room import TnsEvRoom

@dataclass
class TnsEvAppointment(AdditionalDataHolder, Parsable):
    """
    EV-Termin (Raumbuchung in Coero) zu einem Support
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Coero-Termin-ID (0 beim Anlegen)
    appointment: Optional[int] = None
    # The attendees property
    attendees: Optional[list[TnsEvCompanyUserInformation]] = None
    # Teilnehmer/Kontakt eines EV-Termins
    contact: Optional[TnsEvCompanyUserInformation] = None
    # The contactId property
    contact_id: Optional[int] = None
    # Ersteller (wird serverseitig auf den aktuellen User gesetzt)
    creator_tns_user_id: Optional[int] = None
    # The description property
    description: Optional[str] = None
    # Dauer
    duration: Optional[int] = None
    # Raum in Coero (EV)
    room: Optional[TnsEvRoom] = None
    # Startzeitpunkt (Unix-Timestamp)
    start: Optional[int] = None
    # The title property
    title: Optional[str] = None
    # The tnsCompanyId property
    tns_company_id: Optional[int] = None
    # Support-ID
    tns_support: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsEvAppointment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsEvAppointment
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsEvAppointment()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .tns_ev_company_user_information import TnsEvCompanyUserInformation
        from .tns_ev_room import TnsEvRoom

        from .tns_ev_company_user_information import TnsEvCompanyUserInformation
        from .tns_ev_room import TnsEvRoom

        fields: dict[str, Callable[[Any], None]] = {
            "appointment": lambda n : setattr(self, 'appointment', n.get_int_value()),
            "attendees": lambda n : setattr(self, 'attendees', n.get_collection_of_object_values(TnsEvCompanyUserInformation)),
            "contact": lambda n : setattr(self, 'contact', n.get_object_value(TnsEvCompanyUserInformation)),
            "contactId": lambda n : setattr(self, 'contact_id', n.get_int_value()),
            "creatorTnsUserId": lambda n : setattr(self, 'creator_tns_user_id', n.get_int_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "duration": lambda n : setattr(self, 'duration', n.get_int_value()),
            "room": lambda n : setattr(self, 'room', n.get_object_value(TnsEvRoom)),
            "start": lambda n : setattr(self, 'start', n.get_int_value()),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
            "tnsCompanyId": lambda n : setattr(self, 'tns_company_id', n.get_int_value()),
            "tnsSupport": lambda n : setattr(self, 'tns_support', n.get_int_value()),
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
        writer.write_int_value("appointment", self.appointment)
        writer.write_collection_of_object_values("attendees", self.attendees)
        writer.write_object_value("contact", self.contact)
        writer.write_int_value("contactId", self.contact_id)
        writer.write_int_value("creatorTnsUserId", self.creator_tns_user_id)
        writer.write_str_value("description", self.description)
        writer.write_int_value("duration", self.duration)
        writer.write_object_value("room", self.room)
        writer.write_int_value("start", self.start)
        writer.write_str_value("title", self.title)
        writer.write_int_value("tnsCompanyId", self.tns_company_id)
        writer.write_int_value("tnsSupport", self.tns_support)
        writer.write_additional_data_value(self.additional_data)
    

