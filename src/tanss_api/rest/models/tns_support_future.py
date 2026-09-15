from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tns_planning_type import TnsPlanningType
    from .tns_support_location import TnsSupportLocation

@dataclass
class TnsSupportFuture(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # date of the support
    date: Optional[int] = None
    # The duration property
    duration: Optional[int] = None
    # The durationApproach property
    duration_approach: Optional[int] = None
    # The durationDeparture property
    duration_departure: Optional[int] = None
    # The employeeId property
    employee_id: Optional[int] = None
    # The id property
    id: Optional[int] = None
    # Defines, where a support takes place
    location: Optional[TnsSupportLocation] = None
    # The planning type defines if a support is actually a support, appointment (or some other type)
    planning_type: Optional[TnsPlanningType] = None
    # The text property
    text: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsSupportFuture:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsSupportFuture
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsSupportFuture()
    
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
            "date": lambda n : setattr(self, 'date', n.get_int_value()),
            "duration": lambda n : setattr(self, 'duration', n.get_int_value()),
            "durationApproach": lambda n : setattr(self, 'duration_approach', n.get_int_value()),
            "durationDeparture": lambda n : setattr(self, 'duration_departure', n.get_int_value()),
            "employeeId": lambda n : setattr(self, 'employee_id', n.get_int_value()),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "location": lambda n : setattr(self, 'location', n.get_enum_value(TnsSupportLocation)),
            "planningType": lambda n : setattr(self, 'planning_type', n.get_enum_value(TnsPlanningType)),
            "text": lambda n : setattr(self, 'text', n.get_str_value()),
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
        writer.write_int_value("date", self.date)
        writer.write_int_value("duration", self.duration)
        writer.write_int_value("durationApproach", self.duration_approach)
        writer.write_int_value("durationDeparture", self.duration_departure)
        writer.write_int_value("employeeId", self.employee_id)
        writer.write_int_value("id", self.id)
        writer.write_enum_value("location", self.location)
        writer.write_enum_value("planningType", self.planning_type)
        writer.write_str_value("text", self.text)
        writer.write_additional_data_value(self.additional_data)
    

