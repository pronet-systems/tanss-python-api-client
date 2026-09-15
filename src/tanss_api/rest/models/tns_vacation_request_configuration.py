from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tns_planning_type import TnsPlanningType
    from .tns_vacation_request_status import TnsVacationRequestStatus

@dataclass
class TnsVacationRequestConfiguration(AdditionalDataHolder, Parsable):
    """
    object to specify query parameters for fetching a list of vacation requests
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # filter for certain custom types
    custom_type_ids: Optional[list[int]] = None
    # filter for certain departments
    department_ids: Optional[list[int]] = None
    # filter for certain employees
    employee_ids: Optional[list[int]] = None
    # only show vacation requests from certain month
    month: Optional[int] = None
    # filter for certain "additional" planning types (used on absences)
    planning_additional_ids: Optional[list[int]] = None
    # filter for certain planning types
    planning_types: Optional[list[TnsPlanningType]] = None
    # filter for certain planning type states
    states_only: Optional[list[TnsVacationRequestStatus]] = None
    # only show vacation requests from certain year
    year: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsVacationRequestConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsVacationRequestConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsVacationRequestConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .tns_planning_type import TnsPlanningType
        from .tns_vacation_request_status import TnsVacationRequestStatus

        from .tns_planning_type import TnsPlanningType
        from .tns_vacation_request_status import TnsVacationRequestStatus

        fields: dict[str, Callable[[Any], None]] = {
            "customTypeIds": lambda n : setattr(self, 'custom_type_ids', n.get_collection_of_primitive_values(int)),
            "departmentIds": lambda n : setattr(self, 'department_ids', n.get_collection_of_primitive_values(int)),
            "employeeIds": lambda n : setattr(self, 'employee_ids', n.get_collection_of_primitive_values(int)),
            "month": lambda n : setattr(self, 'month', n.get_int_value()),
            "planningAdditionalIds": lambda n : setattr(self, 'planning_additional_ids', n.get_collection_of_primitive_values(int)),
            "planningTypes": lambda n : setattr(self, 'planning_types', n.get_collection_of_enum_values(TnsPlanningType)),
            "statesOnly": lambda n : setattr(self, 'states_only', n.get_collection_of_enum_values(TnsVacationRequestStatus)),
            "year": lambda n : setattr(self, 'year', n.get_int_value()),
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
        writer.write_collection_of_primitive_values("customTypeIds", self.custom_type_ids)
        writer.write_collection_of_primitive_values("departmentIds", self.department_ids)
        writer.write_collection_of_primitive_values("employeeIds", self.employee_ids)
        writer.write_int_value("month", self.month)
        writer.write_collection_of_primitive_values("planningAdditionalIds", self.planning_additional_ids)
        writer.write_collection_of_enum_values("planningTypes", self.planning_types)
        writer.write_collection_of_enum_values("statesOnly", self.states_only)
        writer.write_int_value("year", self.year)
        writer.write_additional_data_value(self.additional_data)
    

