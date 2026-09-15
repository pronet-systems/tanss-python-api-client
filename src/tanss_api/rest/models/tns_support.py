from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tns_installation_fee_drive_mode import TnsInstallationFeeDriveMode
    from .tns_planning_type import TnsPlanningType
    from .tns_support_clearance_status import TnsSupportClearanceStatus
    from .tns_support_drive_type import TnsSupportDriveType
    from .tns_support_icon_type import TnsSupportIconType
    from .tns_support_small import TnsSupportSmall

from .tns_support_small import TnsSupportSmall

@dataclass
class TnsSupport(TnsSupportSmall, Parsable):
    """
    describes a support entry (same for appointment)
    """
    # id of the accountingtype used for this support (i.e. "Techniker")
    accounting_type_id: Optional[int] = None
    # wether the support was already booked
    booked: Optional[bool] = None
    # id of the car (if car is used)
    car_id: Optional[int] = None
    # determines if a support was already "cleared" for billing
    clearance_status: Optional[TnsSupportClearanceStatus] = None
    # id of the company for this support
    company_id: Optional[int] = None
    # id of the contract, used for this support
    contract_id: Optional[int] = None
    # id of the employee who has created this support
    created_employee_id: Optional[int] = None
    # if used, id of the department which is assigned to this support
    department_id: Optional[int] = None
    # determines if the drive shall be charged or not
    drive_charged: Optional[bool] = None
    # defines which drive type is used
    drive_type: Optional[TnsSupportDriveType] = None
    # duration (in minutes) of the approach (drive)
    duration_approach: Optional[int] = None
    # false if the duration approach is not charged (should be true by default)
    duration_approach_charged: Optional[bool] = None
    # duration of the pause (in minutes)
    duration_break: Optional[int] = None
    # duration (in minutes) of the departure (drive)
    duration_departure: Optional[int] = None
    # false if the duration departure is not charged (should be true by default)
    duration_departure_charged: Optional[bool] = None
    # if the support has an erp number entered
    erp_number: Optional[str] = None
    # if this support was created by a customer login, this value is "true"
    extern: Optional[bool] = None
    # if the support has an external ticket number entered, this number is given here
    external_ticket_id: Optional[str] = None
    # the hourly rate for this support (or the rate per working unit)
    hourly_rate: Optional[float] = None
    # The planning type defines if a support is actually a support, appointment (or some other type)
    import_type: Optional[TnsPlanningType] = None
    # wether the support will be billed as an "installation fee" with a fixed price
    installation_fee: Optional[bool] = None
    # if the support will be billed as an "installation fee", the amount is given here
    installation_fee_amount: Optional[float] = None
    # defines if the drive shall be included in the instalaltion fee
    installation_fee_drive_mode: Optional[TnsInstallationFeeDriveMode] = None
    # if the support will be billed as an "installation fee", the id of the installation fee type is given here
    installation_fee_type_id: Optional[int] = None
    # if this support is marked as "internal" (customers won't see those)
    internal: Optional[bool] = None
    # km of the approach (drive)
    km_approach: Optional[int] = None
    # false if the km approach is not charged (should be true by default)
    km_approach_charged: Optional[bool] = None
    # km of the departure (drive)
    km_departure: Optional[int] = None
    # false if the km departure is not charged (should be true by default)
    km_departure_charged: Optional[bool] = None
    # id of the method, the remitter hat given the order (optional)
    ordered_via_id: Optional[int] = None
    # true, if this support is a TANSS2Ex appointment
    outlook: Optional[bool] = None
    # location for outlook appointments
    outlook_location: Optional[str] = None
    # title for outlook appointments
    outlook_title: Optional[str] = None
    # percent that shall be applied
    percent: Optional[float] = None
    # if a relationship shall be used, give here the link id of the relationship
    relationship_link_id: Optional[int] = None
    # if a relationship shall be used, give here the link type of the relationship
    relationship_link_type_id: Optional[int] = None
    # true, if this support shall be billed separately
    separate_billing: Optional[bool] = None
    # if a service location is used, give here the company of the service location
    service_location_id: Optional[int] = None
    # if a pc is used as an assignment, a license can be given as well (optional)
    software_license_id: Optional[int] = None
    # timestamp when the pause starts (0 if no pause is given)
    start_break: Optional[int] = None
    # determines the icon used to display this support
    support_icon_type: Optional[TnsSupportIconType] = None
    # if support is assigned to a task, use it here
    task_id: Optional[int] = None
    # if the synced appointment has a teams url, you can specify it here
    teams_url: Optional[str] = None
    # internal remarks for this support (customers won't see this)
    text_intern: Optional[str] = None
    # if the support was already booked and assigned to a voucher, the voucher id is given here
    voucher_id: Optional[int] = None
    # id of the zone (if zone is used)
    zone_id: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsSupport:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsSupport
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsSupport()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .tns_installation_fee_drive_mode import TnsInstallationFeeDriveMode
        from .tns_planning_type import TnsPlanningType
        from .tns_support_clearance_status import TnsSupportClearanceStatus
        from .tns_support_drive_type import TnsSupportDriveType
        from .tns_support_icon_type import TnsSupportIconType
        from .tns_support_small import TnsSupportSmall

        from .tns_installation_fee_drive_mode import TnsInstallationFeeDriveMode
        from .tns_planning_type import TnsPlanningType
        from .tns_support_clearance_status import TnsSupportClearanceStatus
        from .tns_support_drive_type import TnsSupportDriveType
        from .tns_support_icon_type import TnsSupportIconType
        from .tns_support_small import TnsSupportSmall

        fields: dict[str, Callable[[Any], None]] = {
            "accountingTypeId": lambda n : setattr(self, 'accounting_type_id', n.get_int_value()),
            "booked": lambda n : setattr(self, 'booked', n.get_bool_value()),
            "carId": lambda n : setattr(self, 'car_id', n.get_int_value()),
            "clearanceStatus": lambda n : setattr(self, 'clearance_status', n.get_enum_value(TnsSupportClearanceStatus)),
            "companyId": lambda n : setattr(self, 'company_id', n.get_int_value()),
            "contractId": lambda n : setattr(self, 'contract_id', n.get_int_value()),
            "createdEmployeeId": lambda n : setattr(self, 'created_employee_id', n.get_int_value()),
            "departmentId": lambda n : setattr(self, 'department_id', n.get_int_value()),
            "driveCharged": lambda n : setattr(self, 'drive_charged', n.get_bool_value()),
            "driveType": lambda n : setattr(self, 'drive_type', n.get_enum_value(TnsSupportDriveType)),
            "durationApproach": lambda n : setattr(self, 'duration_approach', n.get_int_value()),
            "durationApproachCharged": lambda n : setattr(self, 'duration_approach_charged', n.get_bool_value()),
            "durationBreak": lambda n : setattr(self, 'duration_break', n.get_int_value()),
            "durationDeparture": lambda n : setattr(self, 'duration_departure', n.get_int_value()),
            "durationDepartureCharged": lambda n : setattr(self, 'duration_departure_charged', n.get_bool_value()),
            "erpNumber": lambda n : setattr(self, 'erp_number', n.get_str_value()),
            "extern": lambda n : setattr(self, 'extern', n.get_bool_value()),
            "externalTicketId": lambda n : setattr(self, 'external_ticket_id', n.get_str_value()),
            "hourlyRate": lambda n : setattr(self, 'hourly_rate', n.get_float_value()),
            "importType": lambda n : setattr(self, 'import_type', n.get_enum_value(TnsPlanningType)),
            "installationFee": lambda n : setattr(self, 'installation_fee', n.get_bool_value()),
            "installationFeeAmount": lambda n : setattr(self, 'installation_fee_amount', n.get_float_value()),
            "installationFeeDriveMode": lambda n : setattr(self, 'installation_fee_drive_mode', n.get_enum_value(TnsInstallationFeeDriveMode)),
            "installationFeeTypeId": lambda n : setattr(self, 'installation_fee_type_id', n.get_int_value()),
            "internal": lambda n : setattr(self, 'internal', n.get_bool_value()),
            "kmApproach": lambda n : setattr(self, 'km_approach', n.get_int_value()),
            "kmApproachCharged": lambda n : setattr(self, 'km_approach_charged', n.get_bool_value()),
            "kmDeparture": lambda n : setattr(self, 'km_departure', n.get_int_value()),
            "kmDepartureCharged": lambda n : setattr(self, 'km_departure_charged', n.get_bool_value()),
            "orderedViaId": lambda n : setattr(self, 'ordered_via_id', n.get_int_value()),
            "outlook": lambda n : setattr(self, 'outlook', n.get_bool_value()),
            "outlookLocation": lambda n : setattr(self, 'outlook_location', n.get_str_value()),
            "outlookTitle": lambda n : setattr(self, 'outlook_title', n.get_str_value()),
            "percent": lambda n : setattr(self, 'percent', n.get_float_value()),
            "relationshipLinkId": lambda n : setattr(self, 'relationship_link_id', n.get_int_value()),
            "relationshipLinkTypeId": lambda n : setattr(self, 'relationship_link_type_id', n.get_int_value()),
            "separateBilling": lambda n : setattr(self, 'separate_billing', n.get_bool_value()),
            "serviceLocationId": lambda n : setattr(self, 'service_location_id', n.get_int_value()),
            "softwareLicenseId": lambda n : setattr(self, 'software_license_id', n.get_int_value()),
            "startBreak": lambda n : setattr(self, 'start_break', n.get_int_value()),
            "supportIconType": lambda n : setattr(self, 'support_icon_type', n.get_enum_value(TnsSupportIconType)),
            "taskId": lambda n : setattr(self, 'task_id', n.get_int_value()),
            "teamsUrl": lambda n : setattr(self, 'teams_url', n.get_str_value()),
            "textIntern": lambda n : setattr(self, 'text_intern', n.get_str_value()),
            "voucherId": lambda n : setattr(self, 'voucher_id', n.get_int_value()),
            "zoneId": lambda n : setattr(self, 'zone_id', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_int_value("accountingTypeId", self.accounting_type_id)
        writer.write_bool_value("booked", self.booked)
        writer.write_int_value("carId", self.car_id)
        writer.write_enum_value("clearanceStatus", self.clearance_status)
        writer.write_int_value("companyId", self.company_id)
        writer.write_int_value("contractId", self.contract_id)
        writer.write_int_value("createdEmployeeId", self.created_employee_id)
        writer.write_int_value("departmentId", self.department_id)
        writer.write_bool_value("driveCharged", self.drive_charged)
        writer.write_enum_value("driveType", self.drive_type)
        writer.write_int_value("durationApproach", self.duration_approach)
        writer.write_bool_value("durationApproachCharged", self.duration_approach_charged)
        writer.write_int_value("durationBreak", self.duration_break)
        writer.write_int_value("durationDeparture", self.duration_departure)
        writer.write_bool_value("durationDepartureCharged", self.duration_departure_charged)
        writer.write_str_value("erpNumber", self.erp_number)
        writer.write_bool_value("extern", self.extern)
        writer.write_str_value("externalTicketId", self.external_ticket_id)
        writer.write_float_value("hourlyRate", self.hourly_rate)
        writer.write_enum_value("importType", self.import_type)
        writer.write_bool_value("installationFee", self.installation_fee)
        writer.write_float_value("installationFeeAmount", self.installation_fee_amount)
        writer.write_enum_value("installationFeeDriveMode", self.installation_fee_drive_mode)
        writer.write_int_value("installationFeeTypeId", self.installation_fee_type_id)
        writer.write_bool_value("internal", self.internal)
        writer.write_int_value("kmApproach", self.km_approach)
        writer.write_bool_value("kmApproachCharged", self.km_approach_charged)
        writer.write_int_value("kmDeparture", self.km_departure)
        writer.write_bool_value("kmDepartureCharged", self.km_departure_charged)
        writer.write_int_value("orderedViaId", self.ordered_via_id)
        writer.write_bool_value("outlook", self.outlook)
        writer.write_str_value("outlookLocation", self.outlook_location)
        writer.write_str_value("outlookTitle", self.outlook_title)
        writer.write_float_value("percent", self.percent)
        writer.write_int_value("relationshipLinkId", self.relationship_link_id)
        writer.write_int_value("relationshipLinkTypeId", self.relationship_link_type_id)
        writer.write_bool_value("separateBilling", self.separate_billing)
        writer.write_int_value("serviceLocationId", self.service_location_id)
        writer.write_int_value("softwareLicenseId", self.software_license_id)
        writer.write_int_value("startBreak", self.start_break)
        writer.write_enum_value("supportIconType", self.support_icon_type)
        writer.write_int_value("taskId", self.task_id)
        writer.write_str_value("teamsUrl", self.teams_url)
        writer.write_str_value("textIntern", self.text_intern)
        writer.write_int_value("voucherId", self.voucher_id)
        writer.write_int_value("zoneId", self.zone_id)
    

