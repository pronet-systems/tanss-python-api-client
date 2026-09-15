from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .employee import Employee

@dataclass
class TnsEmployeeVacationDays(AdditionalDataHolder, Parsable):
    """
    gives details on the vacation days of an employee
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Resolved employee, filled server-side for output. Use `employeeId` on input.
    employee: Optional[Employee] = None
    # employee id
    employee_id: Optional[int] = None
    # how many days does this employee have
    number_of_days: Optional[int] = None
    # number of days transferred from the previous year
    transferred: Optional[int] = None
    # infos for which year
    year: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsEmployeeVacationDays:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsEmployeeVacationDays
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsEmployeeVacationDays()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .employee import Employee

        from .employee import Employee

        fields: dict[str, Callable[[Any], None]] = {
            "employee": lambda n : setattr(self, 'employee', n.get_object_value(Employee)),
            "employeeId": lambda n : setattr(self, 'employee_id', n.get_int_value()),
            "numberOfDays": lambda n : setattr(self, 'number_of_days', n.get_int_value()),
            "transferred": lambda n : setattr(self, 'transferred', n.get_int_value()),
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
        writer.write_int_value("employeeId", self.employee_id)
        writer.write_int_value("numberOfDays", self.number_of_days)
        writer.write_int_value("transferred", self.transferred)
        writer.write_int_value("year", self.year)
        writer.write_additional_data_value(self.additional_data)
    

