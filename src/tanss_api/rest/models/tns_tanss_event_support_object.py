from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tns_planning_type import TnsPlanningType
    from .tns_support_location import TnsSupportLocation

@dataclass
class TnsTanssEventSupportObject(AdditionalDataHolder, Parsable):
    """
    if the tanss ticket object contains infos about a support, then the infos are given here
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # id of the company
    company_id: Optional[int] = None
    # name of the company
    company_name: Optional[str] = None
    # date of the support as timestamp
    date: Optional[int] = None
    # formatted date of the support
    date_formatted: Optional[str] = None
    # duration in minutes
    duration: Optional[int] = None
    # id of the technician
    employee_id: Optional[int] = None
    # name of the technician
    employee_name: Optional[str] = None
    # id of the support
    id: Optional[int] = None
    # true if it's an internal support
    internal: Optional[bool] = None
    # Defines, where a support takes place
    location: Optional[TnsSupportLocation] = None
    # true if it's an outlook appointment
    outlook: Optional[bool] = None
    # The planning type defines if a support is actually a support, appointment (or some other type)
    planning_type: Optional[TnsPlanningType] = None
    # name of the planning typ (i.e. "Getätigte Leistung", "Termin")
    planning_type_name: Optional[str] = None
    # text(description of the support
    text: Optional[str] = None
    # id of the support type
    type_id: Optional[int] = None
    # name of the support type
    type_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsTanssEventSupportObject:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsTanssEventSupportObject
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsTanssEventSupportObject()
    
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
            "companyId": lambda n : setattr(self, 'company_id', n.get_int_value()),
            "companyName": lambda n : setattr(self, 'company_name', n.get_str_value()),
            "date": lambda n : setattr(self, 'date', n.get_int_value()),
            "dateFormatted": lambda n : setattr(self, 'date_formatted', n.get_str_value()),
            "duration": lambda n : setattr(self, 'duration', n.get_int_value()),
            "employeeId": lambda n : setattr(self, 'employee_id', n.get_int_value()),
            "employeeName": lambda n : setattr(self, 'employee_name', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "internal": lambda n : setattr(self, 'internal', n.get_bool_value()),
            "location": lambda n : setattr(self, 'location', n.get_enum_value(TnsSupportLocation)),
            "outlook": lambda n : setattr(self, 'outlook', n.get_bool_value()),
            "planningType": lambda n : setattr(self, 'planning_type', n.get_enum_value(TnsPlanningType)),
            "planningTypeName": lambda n : setattr(self, 'planning_type_name', n.get_str_value()),
            "text": lambda n : setattr(self, 'text', n.get_str_value()),
            "typeId": lambda n : setattr(self, 'type_id', n.get_int_value()),
            "typeName": lambda n : setattr(self, 'type_name', n.get_str_value()),
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
        writer.write_int_value("companyId", self.company_id)
        writer.write_str_value("companyName", self.company_name)
        writer.write_int_value("date", self.date)
        writer.write_str_value("dateFormatted", self.date_formatted)
        writer.write_int_value("duration", self.duration)
        writer.write_int_value("employeeId", self.employee_id)
        writer.write_str_value("employeeName", self.employee_name)
        writer.write_int_value("id", self.id)
        writer.write_bool_value("internal", self.internal)
        writer.write_enum_value("location", self.location)
        writer.write_bool_value("outlook", self.outlook)
        writer.write_enum_value("planningType", self.planning_type)
        writer.write_str_value("planningTypeName", self.planning_type_name)
        writer.write_str_value("text", self.text)
        writer.write_int_value("typeId", self.type_id)
        writer.write_str_value("typeName", self.type_name)
        writer.write_additional_data_value(self.additional_data)
    

