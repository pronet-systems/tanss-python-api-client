from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .appointment_wizard_put_request_body_department_ids import AppointmentWizardPutRequestBody_departmentIds
    from .appointment_wizard_put_request_body_employee_ids import AppointmentWizardPutRequestBody_employeeIds
    from .appointment_wizard_put_request_body_timeframe import AppointmentWizardPutRequestBody_timeframe
    from .appointment_wizard_put_request_body_week_days import AppointmentWizardPutRequestBody_weekDays

@dataclass
class AppointmentWizardPutRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Whether every listed technician must be available for a slot to match.
    all_employees_must_participate: Optional[bool] = None
    # Estimated duration of the appointment in minutes.
    appointment_duration: Optional[int] = None
    # Identifier of the company the appointment is for.
    company_id: Optional[int] = None
    # Identifiers of the departments to check availability for, as an alternative to specific employees.
    department_ids: Optional[list[AppointmentWizardPutRequestBody_departmentIds]] = None
    # Identifiers of the technicians to check availability for.
    employee_ids: Optional[list[AppointmentWizardPutRequestBody_employeeIds]] = None
    # Whether drive time parameters are included in the proposed slots.
    include_drive: Optional[bool] = None
    # Latest hour of the day to consider; if left at zero the employee working hours are used.
    max_hour: Optional[int] = None
    # Earliest hour of the day to consider; if left at zero the employee working hours are used.
    min_hour: Optional[int] = None
    # Minimum number of technicians that must be available when not all are required.
    number_of_employees_who_must_participate: Optional[int] = None
    # Time window (from/to timestamps) within which available slots are searched.
    timeframe: Optional[AppointmentWizardPutRequestBody_timeframe] = None
    # Tolerance in minutes allowing a slightly smaller gap to still qualify as a slot.
    tolerance: Optional[int] = None
    # Restricts the search to the given weekdays.
    week_days: Optional[list[AppointmentWizardPutRequestBody_weekDays]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AppointmentWizardPutRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AppointmentWizardPutRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AppointmentWizardPutRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .appointment_wizard_put_request_body_department_ids import AppointmentWizardPutRequestBody_departmentIds
        from .appointment_wizard_put_request_body_employee_ids import AppointmentWizardPutRequestBody_employeeIds
        from .appointment_wizard_put_request_body_timeframe import AppointmentWizardPutRequestBody_timeframe
        from .appointment_wizard_put_request_body_week_days import AppointmentWizardPutRequestBody_weekDays

        from .appointment_wizard_put_request_body_department_ids import AppointmentWizardPutRequestBody_departmentIds
        from .appointment_wizard_put_request_body_employee_ids import AppointmentWizardPutRequestBody_employeeIds
        from .appointment_wizard_put_request_body_timeframe import AppointmentWizardPutRequestBody_timeframe
        from .appointment_wizard_put_request_body_week_days import AppointmentWizardPutRequestBody_weekDays

        fields: dict[str, Callable[[Any], None]] = {
            "allEmployeesMustParticipate": lambda n : setattr(self, 'all_employees_must_participate', n.get_bool_value()),
            "appointmentDuration": lambda n : setattr(self, 'appointment_duration', n.get_int_value()),
            "companyId": lambda n : setattr(self, 'company_id', n.get_int_value()),
            "departmentIds": lambda n : setattr(self, 'department_ids', n.get_collection_of_object_values(AppointmentWizardPutRequestBody_departmentIds)),
            "employeeIds": lambda n : setattr(self, 'employee_ids', n.get_collection_of_object_values(AppointmentWizardPutRequestBody_employeeIds)),
            "includeDrive": lambda n : setattr(self, 'include_drive', n.get_bool_value()),
            "maxHour": lambda n : setattr(self, 'max_hour', n.get_int_value()),
            "minHour": lambda n : setattr(self, 'min_hour', n.get_int_value()),
            "numberOfEmployeesWhoMustParticipate": lambda n : setattr(self, 'number_of_employees_who_must_participate', n.get_int_value()),
            "timeframe": lambda n : setattr(self, 'timeframe', n.get_object_value(AppointmentWizardPutRequestBody_timeframe)),
            "tolerance": lambda n : setattr(self, 'tolerance', n.get_int_value()),
            "weekDays": lambda n : setattr(self, 'week_days', n.get_collection_of_enum_values(AppointmentWizardPutRequestBody_weekDays)),
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
        writer.write_bool_value("allEmployeesMustParticipate", self.all_employees_must_participate)
        writer.write_int_value("appointmentDuration", self.appointment_duration)
        writer.write_int_value("companyId", self.company_id)
        writer.write_collection_of_object_values("departmentIds", self.department_ids)
        writer.write_collection_of_object_values("employeeIds", self.employee_ids)
        writer.write_bool_value("includeDrive", self.include_drive)
        writer.write_int_value("maxHour", self.max_hour)
        writer.write_int_value("minHour", self.min_hour)
        writer.write_int_value("numberOfEmployeesWhoMustParticipate", self.number_of_employees_who_must_participate)
        writer.write_object_value("timeframe", self.timeframe)
        writer.write_int_value("tolerance", self.tolerance)
        writer.write_collection_of_enum_values("weekDays", self.week_days)
        writer.write_additional_data_value(self.additional_data)
    

