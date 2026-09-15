from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class GetPutRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The departmentId property
    department_id: Optional[int] = None
    # The employeeId property
    employee_id: Optional[int] = None
    # The getAchievedWhenNoTargetIsSet property
    get_achieved_when_no_target_is_set: Optional[bool] = None
    # The includeDepartmentValues property
    include_department_values: Optional[bool] = None
    # 1-12, or 0 for whole year
    month: Optional[int] = None
    # The year property
    year: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> GetPutRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: GetPutRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return GetPutRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "departmentId": lambda n : setattr(self, 'department_id', n.get_int_value()),
            "employeeId": lambda n : setattr(self, 'employee_id', n.get_int_value()),
            "getAchievedWhenNoTargetIsSet": lambda n : setattr(self, 'get_achieved_when_no_target_is_set', n.get_bool_value()),
            "includeDepartmentValues": lambda n : setattr(self, 'include_department_values', n.get_bool_value()),
            "month": lambda n : setattr(self, 'month', n.get_int_value()),
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
        writer.write_int_value("departmentId", self.department_id)
        writer.write_int_value("employeeId", self.employee_id)
        writer.write_bool_value("getAchievedWhenNoTargetIsSet", self.get_achieved_when_no_target_is_set)
        writer.write_bool_value("includeDepartmentValues", self.include_department_values)
        writer.write_int_value("month", self.month)
        writer.write_int_value("year", self.year)
        writer.write_additional_data_value(self.additional_data)
    

