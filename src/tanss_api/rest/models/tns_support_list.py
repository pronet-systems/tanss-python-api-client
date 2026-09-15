from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tns_planning_type import TnsPlanningType
    from .tns_support_clearance_status import TnsSupportClearanceStatus
    from .tns_support_icon_type import TnsSupportIconType
    from .tns_support_list_material import TnsSupportList_material
    from .tns_support_location import TnsSupportLocation
    from .tns_support_meta_infos import TnsSupportMetaInfos
    from .tns_tag import TnsTag
    from .tns_voucher_export_state import TnsVoucherExportState

@dataclass
class TnsSupportList(AdditionalDataHolder, Parsable):
    """
    A single support entry as returned by `PUT /api/v1/supports/list`. This is deliberately NOT the full `TnsSupport` model: the list endpoint serialises a reduced, permission-dependent projection (backend: `TnsSupportListService.getListFilters()` + `TnsSupportFilter`). Fields that belong only to the detail view (`GET /api/v1/supports/{id}`) or the create/update model are NOT part of the list response, e.g. `driveType`, the drive `*Charged` flags, `taskId`, `zoneId`, `orderedViaId`, `softwareLicenseId`, `importType`, `installationFeeDriveMode`, `teamsUrl`, `serviceLocationId`, `separateBilling` and `reasonNotChargedText`. In addition, single fields are omitted depending on the caller's rights, licensed modules and configuration, e.g. `hourlyRate` (right VIEW_HOURLY_RATE), `voucherId` (VIEW_VOUCHERS), `internal` / `textIntern` (may-see-internal-entities), `accountingTypeId` / `createdEmployeeId` (customer logins), `duration*` (SHOW_SUPPORT_DURATION_FOR_CUSTOMER), `ticketId` / `externalTicketId` (module TICKET / config TICKET_EXTERNAL_ID_ACTIVATED), `contractId` (module MAINTENANCE).
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # id of the accounting type used for this support (omitted for customers lacking the right)
    accounting_type_id: Optional[int] = None
    # whether the support was already booked
    booked: Optional[bool] = None
    # id of the car (if a car is used)
    car_id: Optional[int] = None
    # determines if a support was already "cleared" for billing
    clearance_status: Optional[TnsSupportClearanceStatus] = None
    # id of the company for this support
    company_id: Optional[int] = None
    # true if this support was booked after consultation ("Rücksprache")
    consultation: Optional[bool] = None
    # id of the maintenance contract (omitted if module MAINTENANCE is not licensed)
    contract_id: Optional[int] = None
    # id of the cost center
    cost_center_id: Optional[int] = None
    # id of the employee who created this support (omitted for customer logins)
    created_employee_id: Optional[int] = None
    # beginning of the support
    date: Optional[int] = None
    # id of the department assigned to this support
    department_id: Optional[int] = None
    # duration of the service in minutes (omitted for customers lacking SHOW_SUPPORT_DURATION_FOR_CUSTOMER)
    duration: Optional[int] = None
    # duration (in minutes) of the approach (drive)
    duration_approach: Optional[int] = None
    # duration of the pause (in minutes)
    duration_break: Optional[int] = None
    # duration (in minutes) of the departure (drive)
    duration_departure: Optional[int] = None
    # duration which is not charged (in minutes)
    duration_not_charged: Optional[int] = None
    # id of the employee who has done this support
    employee_id: Optional[int] = None
    # erp number of the support (if entered)
    erp_number: Optional[str] = None
    # state of the voucher / erp export for a support
    export: Optional[TnsVoucherExportState] = None
    # true if this support was created by a customer login
    extern: Optional[bool] = None
    # external ticket number (only present with module TICKET and config TICKET_EXTERNAL_ID_ACTIVATED)
    external_ticket_id: Optional[str] = None
    # hourly rate for this support (only present with the right VIEW_HOURLY_RATE)
    hourly_rate: Optional[float] = None
    # id of this support
    id: Optional[int] = None
    # whether the support is billed as a fixed-price installation fee
    installation_fee: Optional[bool] = None
    # amount of the installation fee (only present for technicians/freelancers)
    installation_fee_amount: Optional[float] = None
    # id of the installation fee type
    installation_fee_type_id: Optional[int] = None
    # if this support is marked as "internal" (only present if the caller may see internal entities)
    internal: Optional[bool] = None
    # km of the approach (drive)
    km_approach: Optional[int] = None
    # km of the departure (drive)
    km_departure: Optional[int] = None
    # id of the assignment
    link_id: Optional[int] = None
    # link type of the assignment
    link_type_id: Optional[int] = None
    # Defines, where a support takes place
    location: Optional[TnsSupportLocation] = None
    # material booked on the support (present when material is fetched)
    material: Optional[list[TnsSupportList_material]] = None
    # Optional map of meta information for a support, present only when the support carries such data (e.g. appointments synced from Outlook). Individual keys are omitted when not set.
    meta_infos: Optional[TnsSupportMetaInfos] = None
    # true if this support is a synced Outlook/TANSS2Ex appointment
    outlook: Optional[bool] = None
    # location for outlook appointments
    outlook_location: Optional[str] = None
    # title for outlook appointments
    outlook_title: Optional[str] = None
    # percent that shall be applied
    percent: Optional[float] = None
    # The planning type defines if a support is actually a support, appointment (or some other type)
    planning_type: Optional[TnsPlanningType] = None
    # id of the "not charged reason" (if the support was completely not charged)
    reason_not_charged_id: Optional[int] = None
    # id of the "not charged reason" (if the support was partially not charged)
    reason_partial_not_charged_id: Optional[int] = None
    # link id of a related entity (0 if none)
    relationship_link_id: Optional[int] = None
    # link type of a related entity (0 if none)
    relationship_link_type_id: Optional[int] = None
    # timestamp when the pause starts (0 if no pause is given)
    start_break: Optional[int] = None
    # determines the icon used to display this support
    support_icon_type: Optional[TnsSupportIconType] = None
    # Tags assigned to the support (only present for technicians/freelancers).The field can also be **sent** when a support is created or updated. Every entryreferences an existing tag by its `id`:```json"tags": [{"id": 123}]```Only `id` is evaluated - all other tag fields are ignored (see `TnsTag-Assign`).On create every listed tag is assigned. On update the list is the **complete** setof tags for this support: tags which are missing from the list are removed again(except tags which the current user may not remove). Omit the field completely toleave the existing assignments untouched.
    tags: Optional[list[TnsTag]] = None
    # description / text for this support entry (may be truncated, see meta.properties.extras.truncateTextLength)
    text: Optional[str] = None
    # internal remarks (only present if the caller may see internal entities)
    text_intern: Optional[str] = None
    # id of the connected ticket (omitted if module TICKET is not licensed)
    ticket_id: Optional[int] = None
    # id of the support type
    type_id: Optional[int] = None
    # id of the linked vacation request (0 if none)
    vacation_request_id: Optional[int] = None
    # id of the voucher this support was booked to (only present with the right VIEW_VOUCHERS)
    voucher_id: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsSupportList:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsSupportList
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsSupportList()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .tns_planning_type import TnsPlanningType
        from .tns_support_clearance_status import TnsSupportClearanceStatus
        from .tns_support_icon_type import TnsSupportIconType
        from .tns_support_list_material import TnsSupportList_material
        from .tns_support_location import TnsSupportLocation
        from .tns_support_meta_infos import TnsSupportMetaInfos
        from .tns_tag import TnsTag
        from .tns_voucher_export_state import TnsVoucherExportState

        from .tns_planning_type import TnsPlanningType
        from .tns_support_clearance_status import TnsSupportClearanceStatus
        from .tns_support_icon_type import TnsSupportIconType
        from .tns_support_list_material import TnsSupportList_material
        from .tns_support_location import TnsSupportLocation
        from .tns_support_meta_infos import TnsSupportMetaInfos
        from .tns_tag import TnsTag
        from .tns_voucher_export_state import TnsVoucherExportState

        fields: dict[str, Callable[[Any], None]] = {
            "accountingTypeId": lambda n : setattr(self, 'accounting_type_id', n.get_int_value()),
            "booked": lambda n : setattr(self, 'booked', n.get_bool_value()),
            "carId": lambda n : setattr(self, 'car_id', n.get_int_value()),
            "clearanceStatus": lambda n : setattr(self, 'clearance_status', n.get_enum_value(TnsSupportClearanceStatus)),
            "companyId": lambda n : setattr(self, 'company_id', n.get_int_value()),
            "consultation": lambda n : setattr(self, 'consultation', n.get_bool_value()),
            "contractId": lambda n : setattr(self, 'contract_id', n.get_int_value()),
            "costCenterId": lambda n : setattr(self, 'cost_center_id', n.get_int_value()),
            "createdEmployeeId": lambda n : setattr(self, 'created_employee_id', n.get_int_value()),
            "date": lambda n : setattr(self, 'date', n.get_int_value()),
            "departmentId": lambda n : setattr(self, 'department_id', n.get_int_value()),
            "duration": lambda n : setattr(self, 'duration', n.get_int_value()),
            "durationApproach": lambda n : setattr(self, 'duration_approach', n.get_int_value()),
            "durationBreak": lambda n : setattr(self, 'duration_break', n.get_int_value()),
            "durationDeparture": lambda n : setattr(self, 'duration_departure', n.get_int_value()),
            "durationNotCharged": lambda n : setattr(self, 'duration_not_charged', n.get_int_value()),
            "employeeId": lambda n : setattr(self, 'employee_id', n.get_int_value()),
            "erpNumber": lambda n : setattr(self, 'erp_number', n.get_str_value()),
            "export": lambda n : setattr(self, 'export', n.get_enum_value(TnsVoucherExportState)),
            "extern": lambda n : setattr(self, 'extern', n.get_bool_value()),
            "externalTicketId": lambda n : setattr(self, 'external_ticket_id', n.get_str_value()),
            "hourlyRate": lambda n : setattr(self, 'hourly_rate', n.get_float_value()),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "installationFee": lambda n : setattr(self, 'installation_fee', n.get_bool_value()),
            "installationFeeAmount": lambda n : setattr(self, 'installation_fee_amount', n.get_float_value()),
            "installationFeeTypeId": lambda n : setattr(self, 'installation_fee_type_id', n.get_int_value()),
            "internal": lambda n : setattr(self, 'internal', n.get_bool_value()),
            "kmApproach": lambda n : setattr(self, 'km_approach', n.get_int_value()),
            "kmDeparture": lambda n : setattr(self, 'km_departure', n.get_int_value()),
            "linkId": lambda n : setattr(self, 'link_id', n.get_int_value()),
            "linkTypeId": lambda n : setattr(self, 'link_type_id', n.get_int_value()),
            "location": lambda n : setattr(self, 'location', n.get_enum_value(TnsSupportLocation)),
            "material": lambda n : setattr(self, 'material', n.get_collection_of_object_values(TnsSupportList_material)),
            "metaInfos": lambda n : setattr(self, 'meta_infos', n.get_object_value(TnsSupportMetaInfos)),
            "outlook": lambda n : setattr(self, 'outlook', n.get_bool_value()),
            "outlookLocation": lambda n : setattr(self, 'outlook_location', n.get_str_value()),
            "outlookTitle": lambda n : setattr(self, 'outlook_title', n.get_str_value()),
            "percent": lambda n : setattr(self, 'percent', n.get_float_value()),
            "planningType": lambda n : setattr(self, 'planning_type', n.get_enum_value(TnsPlanningType)),
            "reasonNotChargedId": lambda n : setattr(self, 'reason_not_charged_id', n.get_int_value()),
            "reasonPartialNotChargedId": lambda n : setattr(self, 'reason_partial_not_charged_id', n.get_int_value()),
            "relationshipLinkId": lambda n : setattr(self, 'relationship_link_id', n.get_int_value()),
            "relationshipLinkTypeId": lambda n : setattr(self, 'relationship_link_type_id', n.get_int_value()),
            "startBreak": lambda n : setattr(self, 'start_break', n.get_int_value()),
            "supportIconType": lambda n : setattr(self, 'support_icon_type', n.get_enum_value(TnsSupportIconType)),
            "tags": lambda n : setattr(self, 'tags', n.get_collection_of_object_values(TnsTag)),
            "text": lambda n : setattr(self, 'text', n.get_str_value()),
            "textIntern": lambda n : setattr(self, 'text_intern', n.get_str_value()),
            "ticketId": lambda n : setattr(self, 'ticket_id', n.get_int_value()),
            "typeId": lambda n : setattr(self, 'type_id', n.get_int_value()),
            "vacationRequestId": lambda n : setattr(self, 'vacation_request_id', n.get_int_value()),
            "voucherId": lambda n : setattr(self, 'voucher_id', n.get_int_value()),
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
        writer.write_int_value("accountingTypeId", self.accounting_type_id)
        writer.write_bool_value("booked", self.booked)
        writer.write_int_value("carId", self.car_id)
        writer.write_enum_value("clearanceStatus", self.clearance_status)
        writer.write_int_value("companyId", self.company_id)
        writer.write_bool_value("consultation", self.consultation)
        writer.write_int_value("contractId", self.contract_id)
        writer.write_int_value("costCenterId", self.cost_center_id)
        writer.write_int_value("createdEmployeeId", self.created_employee_id)
        writer.write_int_value("date", self.date)
        writer.write_int_value("departmentId", self.department_id)
        writer.write_int_value("duration", self.duration)
        writer.write_int_value("durationApproach", self.duration_approach)
        writer.write_int_value("durationBreak", self.duration_break)
        writer.write_int_value("durationDeparture", self.duration_departure)
        writer.write_int_value("durationNotCharged", self.duration_not_charged)
        writer.write_int_value("employeeId", self.employee_id)
        writer.write_str_value("erpNumber", self.erp_number)
        writer.write_enum_value("export", self.export)
        writer.write_bool_value("extern", self.extern)
        writer.write_str_value("externalTicketId", self.external_ticket_id)
        writer.write_float_value("hourlyRate", self.hourly_rate)
        writer.write_int_value("id", self.id)
        writer.write_bool_value("installationFee", self.installation_fee)
        writer.write_float_value("installationFeeAmount", self.installation_fee_amount)
        writer.write_int_value("installationFeeTypeId", self.installation_fee_type_id)
        writer.write_bool_value("internal", self.internal)
        writer.write_int_value("kmApproach", self.km_approach)
        writer.write_int_value("kmDeparture", self.km_departure)
        writer.write_int_value("linkId", self.link_id)
        writer.write_int_value("linkTypeId", self.link_type_id)
        writer.write_enum_value("location", self.location)
        writer.write_collection_of_object_values("material", self.material)
        writer.write_object_value("metaInfos", self.meta_infos)
        writer.write_bool_value("outlook", self.outlook)
        writer.write_str_value("outlookLocation", self.outlook_location)
        writer.write_str_value("outlookTitle", self.outlook_title)
        writer.write_float_value("percent", self.percent)
        writer.write_enum_value("planningType", self.planning_type)
        writer.write_int_value("reasonNotChargedId", self.reason_not_charged_id)
        writer.write_int_value("reasonPartialNotChargedId", self.reason_partial_not_charged_id)
        writer.write_int_value("relationshipLinkId", self.relationship_link_id)
        writer.write_int_value("relationshipLinkTypeId", self.relationship_link_type_id)
        writer.write_int_value("startBreak", self.start_break)
        writer.write_enum_value("supportIconType", self.support_icon_type)
        writer.write_collection_of_object_values("tags", self.tags)
        writer.write_str_value("text", self.text)
        writer.write_str_value("textIntern", self.text_intern)
        writer.write_int_value("ticketId", self.ticket_id)
        writer.write_int_value("typeId", self.type_id)
        writer.write_int_value("vacationRequestId", self.vacation_request_id)
        writer.write_int_value("voucherId", self.voucher_id)
        writer.write_additional_data_value(self.additional_data)
    

