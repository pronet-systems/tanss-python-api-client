from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tns_planning_type import TnsPlanningType
    from .tns_support_location import TnsSupportLocation

@dataclass
class TnsSupportSmall(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # id of the cost center
    cost_center_id: Optional[int] = None
    # beginning of the support
    date: Optional[int] = None
    # duration of the service (in minutes)
    duration: Optional[int] = None
    # duration which is not charged (in minutes)
    duration_not_charged: Optional[int] = None
    # id of the employee who has done this support
    employee_id: Optional[int] = None
    # id of this support
    id: Optional[int] = None
    # id of the assignment
    link_id: Optional[int] = None
    # link type of the assignment
    link_type_id: Optional[int] = None
    # Defines, where a support takes place
    location: Optional[TnsSupportLocation] = None
    # The planning type defines if a support is actually a support, appointment (or some other type)
    planning_type: Optional[TnsPlanningType] = None
    # id of the "not charged reason" (if support was completely not charged)
    reason_not_charged_id: Optional[int] = None
    # if support was not chatged, the reason / text goes here
    reason_not_charged_text: Optional[str] = None
    # id of the "not charged reason" (if support was partially not charged)
    reason_partial_not_charged_id: Optional[int] = None
    # description / text for this support entry
    text: Optional[str] = None
    # id of the connected ticket
    ticket_id: Optional[int] = None
    # id of the support type
    type_id: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsSupportSmall:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsSupportSmall
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsSupportSmall()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .tns_planning_type import TnsPlanningType
        from .tns_support_location import TnsSupportLocation

        from .tns_planning_type import TnsPlanningType
        from .tns_support_location import TnsSupportLocation

        fields: dict[str, Callable[[Any], None]] = {
            "costCenterId": lambda n : setattr(self, 'cost_center_id', n.get_int_value()),
            "date": lambda n : setattr(self, 'date', n.get_int_value()),
            "duration": lambda n : setattr(self, 'duration', n.get_int_value()),
            "durationNotCharged": lambda n : setattr(self, 'duration_not_charged', n.get_int_value()),
            "employeeId": lambda n : setattr(self, 'employee_id', n.get_int_value()),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "linkId": lambda n : setattr(self, 'link_id', n.get_int_value()),
            "linkTypeId": lambda n : setattr(self, 'link_type_id', n.get_int_value()),
            "location": lambda n : setattr(self, 'location', n.get_enum_value(TnsSupportLocation)),
            "planningType": lambda n : setattr(self, 'planning_type', n.get_enum_value(TnsPlanningType)),
            "reasonNotChargedId": lambda n : setattr(self, 'reason_not_charged_id', n.get_int_value()),
            "reasonNotChargedText": lambda n : setattr(self, 'reason_not_charged_text', n.get_str_value()),
            "reasonPartialNotChargedId": lambda n : setattr(self, 'reason_partial_not_charged_id', n.get_int_value()),
            "text": lambda n : setattr(self, 'text', n.get_str_value()),
            "ticketId": lambda n : setattr(self, 'ticket_id', n.get_int_value()),
            "typeId": lambda n : setattr(self, 'type_id', n.get_int_value()),
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
        writer.write_int_value("costCenterId", self.cost_center_id)
        writer.write_int_value("date", self.date)
        writer.write_int_value("duration", self.duration)
        writer.write_int_value("durationNotCharged", self.duration_not_charged)
        writer.write_int_value("employeeId", self.employee_id)
        writer.write_int_value("linkId", self.link_id)
        writer.write_int_value("linkTypeId", self.link_type_id)
        writer.write_enum_value("location", self.location)
        writer.write_enum_value("planningType", self.planning_type)
        writer.write_int_value("reasonNotChargedId", self.reason_not_charged_id)
        writer.write_str_value("reasonNotChargedText", self.reason_not_charged_text)
        writer.write_int_value("reasonPartialNotChargedId", self.reason_partial_not_charged_id)
        writer.write_str_value("text", self.text)
        writer.write_int_value("ticketId", self.ticket_id)
        writer.write_int_value("typeId", self.type_id)
        writer.write_additional_data_value(self.additional_data)
    

