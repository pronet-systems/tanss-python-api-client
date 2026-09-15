from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .with_type_post_request_body_custom_type_ids import WithTypePostRequestBody_customTypeIds
    from .with_type_post_request_body_department_ids import WithTypePostRequestBody_departmentIds
    from .with_type_post_request_body_employee_ids import WithTypePostRequestBody_employeeIds
    from .with_type_post_request_body_exclude_vacation_request_ids import WithTypePostRequestBody_excludeVacationRequestIds
    from .with_type_post_request_body_planning_additional_ids import WithTypePostRequestBody_planningAdditionalIds
    from .with_type_post_request_body_planning_types import WithTypePostRequestBody_planningTypes
    from .with_type_post_request_body_states_only import WithTypePostRequestBody_statesOnly

@dataclass
class WithTypePostRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Whether to include display flags such as editable, deletable and acceptable
    add_frontend_values: Optional[bool] = None
    # Whether permission checks are applied when listing
    check_permissions: Optional[bool] = None
    # Custom absence type identifiers to filter by
    custom_type_ids: Optional[list[WithTypePostRequestBody_customTypeIds]] = None
    # Identifiers of departments to include
    department_ids: Optional[list[WithTypePostRequestBody_departmentIds]] = None
    # Identifiers of employees to include
    employee_ids: Optional[list[WithTypePostRequestBody_employeeIds]] = None
    # Identifiers of vacation requests to exclude from the result
    exclude_vacation_request_ids: Optional[list[WithTypePostRequestBody_excludeVacationRequestIds]] = None
    # Month to restrict the listing to; 0 means the whole year
    month: Optional[int] = None
    # Additional absence sub-type identifiers to filter by
    planning_additional_ids: Optional[list[WithTypePostRequestBody_planningAdditionalIds]] = None
    # Planning types to filter the requests by
    planning_types: Optional[list[WithTypePostRequestBody_planningTypes]] = None
    # Restrict the result to requests in these approval states
    states_only: Optional[list[WithTypePostRequestBody_statesOnly]] = None
    # Year to list vacation requests for
    year: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WithTypePostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WithTypePostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WithTypePostRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .with_type_post_request_body_custom_type_ids import WithTypePostRequestBody_customTypeIds
        from .with_type_post_request_body_department_ids import WithTypePostRequestBody_departmentIds
        from .with_type_post_request_body_employee_ids import WithTypePostRequestBody_employeeIds
        from .with_type_post_request_body_exclude_vacation_request_ids import WithTypePostRequestBody_excludeVacationRequestIds
        from .with_type_post_request_body_planning_additional_ids import WithTypePostRequestBody_planningAdditionalIds
        from .with_type_post_request_body_planning_types import WithTypePostRequestBody_planningTypes
        from .with_type_post_request_body_states_only import WithTypePostRequestBody_statesOnly

        from .with_type_post_request_body_custom_type_ids import WithTypePostRequestBody_customTypeIds
        from .with_type_post_request_body_department_ids import WithTypePostRequestBody_departmentIds
        from .with_type_post_request_body_employee_ids import WithTypePostRequestBody_employeeIds
        from .with_type_post_request_body_exclude_vacation_request_ids import WithTypePostRequestBody_excludeVacationRequestIds
        from .with_type_post_request_body_planning_additional_ids import WithTypePostRequestBody_planningAdditionalIds
        from .with_type_post_request_body_planning_types import WithTypePostRequestBody_planningTypes
        from .with_type_post_request_body_states_only import WithTypePostRequestBody_statesOnly

        fields: dict[str, Callable[[Any], None]] = {
            "addFrontendValues": lambda n : setattr(self, 'add_frontend_values', n.get_bool_value()),
            "checkPermissions": lambda n : setattr(self, 'check_permissions', n.get_bool_value()),
            "customTypeIds": lambda n : setattr(self, 'custom_type_ids', n.get_collection_of_object_values(WithTypePostRequestBody_customTypeIds)),
            "departmentIds": lambda n : setattr(self, 'department_ids', n.get_collection_of_object_values(WithTypePostRequestBody_departmentIds)),
            "employeeIds": lambda n : setattr(self, 'employee_ids', n.get_collection_of_object_values(WithTypePostRequestBody_employeeIds)),
            "excludeVacationRequestIds": lambda n : setattr(self, 'exclude_vacation_request_ids', n.get_collection_of_object_values(WithTypePostRequestBody_excludeVacationRequestIds)),
            "month": lambda n : setattr(self, 'month', n.get_int_value()),
            "planningAdditionalIds": lambda n : setattr(self, 'planning_additional_ids', n.get_collection_of_object_values(WithTypePostRequestBody_planningAdditionalIds)),
            "planningTypes": lambda n : setattr(self, 'planning_types', n.get_collection_of_object_values(WithTypePostRequestBody_planningTypes)),
            "statesOnly": lambda n : setattr(self, 'states_only', n.get_collection_of_object_values(WithTypePostRequestBody_statesOnly)),
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
        writer.write_bool_value("addFrontendValues", self.add_frontend_values)
        writer.write_bool_value("checkPermissions", self.check_permissions)
        writer.write_collection_of_object_values("customTypeIds", self.custom_type_ids)
        writer.write_collection_of_object_values("departmentIds", self.department_ids)
        writer.write_collection_of_object_values("employeeIds", self.employee_ids)
        writer.write_collection_of_object_values("excludeVacationRequestIds", self.exclude_vacation_request_ids)
        writer.write_int_value("month", self.month)
        writer.write_collection_of_object_values("planningAdditionalIds", self.planning_additional_ids)
        writer.write_collection_of_object_values("planningTypes", self.planning_types)
        writer.write_collection_of_object_values("statesOnly", self.states_only)
        writer.write_int_value("year", self.year)
        writer.write_additional_data_value(self.additional_data)
    

