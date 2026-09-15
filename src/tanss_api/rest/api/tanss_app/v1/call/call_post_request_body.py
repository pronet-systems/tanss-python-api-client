from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .....models.tns_phone_call_direction import TnsPhoneCallDirection
    from .....models.tns_phone_participant import TnsPhoneParticipant

@dataclass
class CallPostRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The callId property
    call_id: Optional[str] = None
    # The connectionEstablished property
    connection_established: Optional[bool] = None
    # The date property
    date: Optional[int] = None
    # Defines the "direction" of a phone call
    direction: Optional[TnsPhoneCallDirection] = None
    # The durationCall property
    duration_call: Optional[int] = None
    # The durationTotal property
    duration_total: Optional[int] = None
    # The fromCompanyId property
    from_company_id: Optional[int] = None
    # The fromEmployeeId property
    from_employee_id: Optional[int] = None
    # The fromPhoneNumber property
    from_phone_number: Optional[str] = None
    # Enum (z.B. UNIDENTIFIED, IDENTIFIED)
    number_identify_state: Optional[str] = None
    # The phoneParticipants property
    phone_participants: Optional[list[TnsPhoneParticipant]] = None
    # The redirectFrom property
    redirect_from: Optional[int] = None
    # The toCompanyId property
    to_company_id: Optional[int] = None
    # The toEmployeeId property
    to_employee_id: Optional[int] = None
    # The toPhoneNumber property
    to_phone_number: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CallPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CallPostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CallPostRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .....models.tns_phone_call_direction import TnsPhoneCallDirection
        from .....models.tns_phone_participant import TnsPhoneParticipant

        from .....models.tns_phone_call_direction import TnsPhoneCallDirection
        from .....models.tns_phone_participant import TnsPhoneParticipant

        fields: dict[str, Callable[[Any], None]] = {
            "callId": lambda n : setattr(self, 'call_id', n.get_str_value()),
            "connectionEstablished": lambda n : setattr(self, 'connection_established', n.get_bool_value()),
            "date": lambda n : setattr(self, 'date', n.get_int_value()),
            "direction": lambda n : setattr(self, 'direction', n.get_enum_value(TnsPhoneCallDirection)),
            "durationCall": lambda n : setattr(self, 'duration_call', n.get_int_value()),
            "durationTotal": lambda n : setattr(self, 'duration_total', n.get_int_value()),
            "fromCompanyId": lambda n : setattr(self, 'from_company_id', n.get_int_value()),
            "fromEmployeeId": lambda n : setattr(self, 'from_employee_id', n.get_int_value()),
            "fromPhoneNumber": lambda n : setattr(self, 'from_phone_number', n.get_str_value()),
            "numberIdentifyState": lambda n : setattr(self, 'number_identify_state', n.get_str_value()),
            "phoneParticipants": lambda n : setattr(self, 'phone_participants', n.get_collection_of_object_values(TnsPhoneParticipant)),
            "redirectFrom": lambda n : setattr(self, 'redirect_from', n.get_int_value()),
            "toCompanyId": lambda n : setattr(self, 'to_company_id', n.get_int_value()),
            "toEmployeeId": lambda n : setattr(self, 'to_employee_id', n.get_int_value()),
            "toPhoneNumber": lambda n : setattr(self, 'to_phone_number', n.get_str_value()),
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
        writer.write_str_value("callId", self.call_id)
        writer.write_bool_value("connectionEstablished", self.connection_established)
        writer.write_int_value("date", self.date)
        writer.write_enum_value("direction", self.direction)
        writer.write_int_value("durationCall", self.duration_call)
        writer.write_int_value("durationTotal", self.duration_total)
        writer.write_int_value("fromCompanyId", self.from_company_id)
        writer.write_int_value("fromEmployeeId", self.from_employee_id)
        writer.write_str_value("fromPhoneNumber", self.from_phone_number)
        writer.write_str_value("numberIdentifyState", self.number_identify_state)
        writer.write_collection_of_object_values("phoneParticipants", self.phone_participants)
        writer.write_int_value("redirectFrom", self.redirect_from)
        writer.write_int_value("toCompanyId", self.to_company_id)
        writer.write_int_value("toEmployeeId", self.to_employee_id)
        writer.write_str_value("toPhoneNumber", self.to_phone_number)
        writer.write_additional_data_value(self.additional_data)
    

