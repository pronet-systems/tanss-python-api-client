from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .ticket_complete import TicketComplete
    from .ticket_save_attention import TicketSave_attention
    from .ticket_save_installation_fee import TicketSave_installationFee
    from .ticket_save_installation_fee_drive_mode import TicketSave_installationFeeDriveMode
    from .ticket_save_local_ticket_admin_flag import TicketSave_localTicketAdminFlag
    from .tns_tag_assign import TnsTagAssign
    from .tns_ticket_clearance_mode import TnsTicketClearanceMode
    from .tns_ticket_resubmission_mail_options import TnsTicketResubmissionMailOptions
    from .tns_ticket_resubmission_mode import TnsTicketResubmissionMode

@dataclass
class TicketSave(AdditionalDataHolder, Parsable):
    """
    ticket model to be saved
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    from .tns_ticket_resubmission_mode import TnsTicketResubmissionMode

    # Determines what happens when a ticket's resubmission ("Wiedervorlage") dateis reached:- HIGHLIGHT_TICKET: the ticket is highlighted (default)- CLOSE_TICKET: the ticket is closed- SEND_MAIL: an e-mail is sent (recipients / subject from `resubmissionMailOptions`)- SET_STATUS: the ticket status is set to a target state (`resubmissionMailOptions.setStateTo`)
    resubmission_mode: Optional[TnsTicketResubmissionMode] = TnsTicketResubmissionMode("HIGHLIGHT_TICKET")
    # id of department which ticket is assigned to.Name is stored in "linked entities" - "departments"
    assigned_to_department_id: Optional[int] = None
    # id of employee which ticket is assigned to.Name is stored in "linked entities" - "employees"
    assigned_to_employee_id: Optional[int] = None
    # If ticket is assigned to a device (or employee), here the name is stored
    assignment_name: Optional[str] = None
    # Determines the "attention" flag state of a ticket
    attention: Optional[TicketSave_attention] = None
    # Alternate invoice address ("abweichende Rechnungsanschrift"): id of thecompany whose address is used for billing instead of the ticket's owncompany. `0` means no alternate address (the ticket's own company isbilled).Name is stored in the "linked entities" - "companies".Note: when creating (POST) a ticket that belongs to a separately-billedproject (`projectId` set), this value is overwritten with the project'sbilling company and cannot be set independently. On update (PUT) of anexisting ticket it is not overwritten.
    billing_to_company_id: Optional[int] = None
    # describes "how" the supports of a ticket may be cleared. Here, the default value of the OSK may be "overwritten"
    clearance_mode: Optional[TnsTicketClearanceMode] = None
    # Company id of the ticket.Name is stored in the "linked entities" - "companies".Can only be set if the user has access to the company
    company_id: Optional[int] = None
    # The content / description of the ticket
    content: Optional[str] = None
    # id of the employee who has created this ticket
    created_employee_id: Optional[int] = None
    # creation date of tickets as unix timestamp
    creation_date: Optional[int] = None
    # If ticket has a deadline, the date is given here
    deadline_date: Optional[int] = None
    # If true, the delivery address is printed on the ticket's PDF documents.Defaults to `true`. Belongs to the same permission gate as`billingToCompanyId`.
    delivery_address_on_pdf: Optional[bool] = None
    # if ticket has a due date, the timestamp is given here
    due_date: Optional[int] = None
    # Number of estimated minutes which is planned for the ticket
    estimated_minutes: Optional[int] = None
    # This is used to display the correct image for the "estimated minutes" icon in the ticket lists
    estimated_minutes_image: Optional[str] = None
    # External ticket id (optional)
    ext_ticket_id: Optional[str] = None
    # The id property
    id: Optional[int] = None
    # If the ticket has an installation fee, this value is true
    installation_fee: Optional[TicketSave_installationFee] = None
    # Amount for the installation fee
    installation_fee_amount: Optional[float] = None
    # Sets the installation fee drive mode.If it is set to NONE then the system config parameter "leistung.ip.fahrzeit_berechnen" will be used.If the company from the ticket has an installation fee drive mode set then that will be used instead of the system config parameter.
    installation_fee_drive_mode: Optional[TicketSave_installationFeeDriveMode] = None
    # if ticket is assigned to device / employee, the id of the entity is given here
    link_id: Optional[int] = None
    # if ticket is assigned to device / employee, linktype is given here
    link_type_id: Optional[int] = None
    # if the ticket is assigned to a local ticket admin, this represents the employee (local ticket admin) who is assigned for this ticket
    local_ticket_admin_employee_id: Optional[int] = None
    # Determines wether the ticket is assigned to a local ticket admin or not- NONE: "normal" ticket- LOCAL_ADMIN: ticket is assigned to a local ticket admin- TECHNICIAN: local ticket admin has forwarded the ticket to a technician
    local_ticket_admin_flag: Optional[TicketSave_localTicketAdminFlag] = None
    # gives infos about how the remitter gave the order.Infos are stored in the "linked entities" - "orderBys"
    order_by_id: Optional[int] = None
    # Sets the order number
    order_number: Optional[str] = None
    # if the ticket is assignet to a project phase.The name of the phase is stored in the "linked entities" - "phases"
    phase_id: Optional[int] = None
    # if ticket is actually a project, this value is true
    project: Optional[bool] = None
    # if ticket is a sub-ticket of a project, the id of the project goes here.Name of the project is in the "linked entities" - "tickets"
    project_id: Optional[int] = None
    # linkId of the relationship (if ticket has a relation)
    relationship_link_id: Optional[int] = None
    # linkTypeId of the relationship (if ticket has a relation)
    relationship_link_type_id: Optional[int] = None
    # If the ticket has a reminder set, the timestamp is returned here
    reminder: Optional[int] = None
    # Repeat interval of the reminder in **days**. Combined with`reminderIntervalHours` to define how often the reminder recurs.`0` = no day component. Unlike `reminder` itself, this field is notindividually permission-gated; on ticket re-open it is reset to theconfigured default interval.
    reminder_interval: Optional[int] = None
    # Repeat interval of the reminder in **hours**. Combined with`reminderInterval` to define how often the reminder recurs.`0` = no hour component.
    reminder_interval_hours: Optional[int] = None
    # If the ticket has a remitter, the id goes here.Name is stored in the "linked entities" - "employees"
    remitter_id: Optional[int] = None
    # if true, this ticket is a "repair ticket"
    repair: Optional[bool] = None
    # If the ticket has a resubmission date ("Wiedervorlage") set, it is givenhere as a unix timestamp.
    resubmission_date: Optional[int] = None
    # Options applied when a resubmission fires. Used for the SEND_MAIL mode(recipients + subject) and to optionally move the ticket to a target status.
    resubmission_mail_options: Optional[TnsTicketResubmissionMailOptions] = None
    # Free-text note ("Wiedervorlage"-Text) that is shown / used when the resubmission is due.
    resubmission_text: Optional[str] = None
    # If true, the ticket shall be billed separately
    separate_billing: Optional[bool] = None
    # If the ticket has a service cap ("Obergrenze"), here the amount is given.Note: the value is only applied if the request is authenticated as anemployee who may authorize a service cap for the ticket's company. Requestsauthenticated with an integration token (`ErpToken`, `MonitoringToken`, ...)have no employee behind them, so a `serviceCapAmount` sent on those routes isignored and the ticket is created with `0`. Use `POST /api/v1/tickets` /`PUT /api/v1/tickets/{ticketId}` with a user token to set it, or`GET /api/v1/tickets/{ticketId}/serviceCap/request/{employeeId}/{newAmount}`to mail an approval request to an employee who may authorize it.
    service_cap_amount: Optional[float] = None
    # id of the ticket state.Name is give in "linked entities" - "ticketStates"
    status_id: Optional[int] = None
    # when persisting a project, you can also send a list of sub-tickets here (optional).The tickets will immediately be assigned as sub-tickets to the created project.
    sub_tickets: Optional[list[TicketComplete]] = None
    # Tags which shall be assigned to the ticket. Every entry references an existing tagby its `id`:```json"tags": [{"id": 123}]```Only `id` is evaluated - all other tag fields are ignored.When a ticket is created, every listed tag is assigned. When a ticket is updated,the list is the **complete** set of tags for this ticket: tags which are missingfrom the list are removed again (except tags which the current user may notremove). Omit the field completely to leave the existing assignments untouched.
    tags: Optional[list[TnsTagAssign]] = None
    # The title / subject of the ticket
    title: Optional[str] = None
    # id of the ticket type.Name is give in "linked entities" - "ticketTypes"
    type_id: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TicketSave:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TicketSave
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TicketSave()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .ticket_complete import TicketComplete
        from .ticket_save_attention import TicketSave_attention
        from .ticket_save_installation_fee import TicketSave_installationFee
        from .ticket_save_installation_fee_drive_mode import TicketSave_installationFeeDriveMode
        from .ticket_save_local_ticket_admin_flag import TicketSave_localTicketAdminFlag
        from .tns_tag_assign import TnsTagAssign
        from .tns_ticket_clearance_mode import TnsTicketClearanceMode
        from .tns_ticket_resubmission_mail_options import TnsTicketResubmissionMailOptions
        from .tns_ticket_resubmission_mode import TnsTicketResubmissionMode

        from .ticket_complete import TicketComplete
        from .ticket_save_attention import TicketSave_attention
        from .ticket_save_installation_fee import TicketSave_installationFee
        from .ticket_save_installation_fee_drive_mode import TicketSave_installationFeeDriveMode
        from .ticket_save_local_ticket_admin_flag import TicketSave_localTicketAdminFlag
        from .tns_tag_assign import TnsTagAssign
        from .tns_ticket_clearance_mode import TnsTicketClearanceMode
        from .tns_ticket_resubmission_mail_options import TnsTicketResubmissionMailOptions
        from .tns_ticket_resubmission_mode import TnsTicketResubmissionMode

        fields: dict[str, Callable[[Any], None]] = {
            "assignedToDepartmentId": lambda n : setattr(self, 'assigned_to_department_id', n.get_int_value()),
            "assignedToEmployeeId": lambda n : setattr(self, 'assigned_to_employee_id', n.get_int_value()),
            "assignmentName": lambda n : setattr(self, 'assignment_name', n.get_str_value()),
            "attention": lambda n : setattr(self, 'attention', n.get_enum_value(TicketSave_attention)),
            "billingToCompanyId": lambda n : setattr(self, 'billing_to_company_id', n.get_int_value()),
            "clearanceMode": lambda n : setattr(self, 'clearance_mode', n.get_enum_value(TnsTicketClearanceMode)),
            "companyId": lambda n : setattr(self, 'company_id', n.get_int_value()),
            "content": lambda n : setattr(self, 'content', n.get_str_value()),
            "createdEmployeeId": lambda n : setattr(self, 'created_employee_id', n.get_int_value()),
            "creationDate": lambda n : setattr(self, 'creation_date', n.get_int_value()),
            "deadlineDate": lambda n : setattr(self, 'deadline_date', n.get_int_value()),
            "deliveryAddressOnPdf": lambda n : setattr(self, 'delivery_address_on_pdf', n.get_bool_value()),
            "dueDate": lambda n : setattr(self, 'due_date', n.get_int_value()),
            "estimatedMinutes": lambda n : setattr(self, 'estimated_minutes', n.get_int_value()),
            "estimatedMinutesImage": lambda n : setattr(self, 'estimated_minutes_image', n.get_str_value()),
            "extTicketId": lambda n : setattr(self, 'ext_ticket_id', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "installationFee": lambda n : setattr(self, 'installation_fee', n.get_enum_value(TicketSave_installationFee)),
            "installationFeeAmount": lambda n : setattr(self, 'installation_fee_amount', n.get_float_value()),
            "installationFeeDriveMode": lambda n : setattr(self, 'installation_fee_drive_mode', n.get_enum_value(TicketSave_installationFeeDriveMode)),
            "linkId": lambda n : setattr(self, 'link_id', n.get_int_value()),
            "linkTypeId": lambda n : setattr(self, 'link_type_id', n.get_int_value()),
            "localTicketAdminEmployeeId": lambda n : setattr(self, 'local_ticket_admin_employee_id', n.get_int_value()),
            "localTicketAdminFlag": lambda n : setattr(self, 'local_ticket_admin_flag', n.get_enum_value(TicketSave_localTicketAdminFlag)),
            "orderById": lambda n : setattr(self, 'order_by_id', n.get_int_value()),
            "orderNumber": lambda n : setattr(self, 'order_number', n.get_str_value()),
            "phaseId": lambda n : setattr(self, 'phase_id', n.get_int_value()),
            "project": lambda n : setattr(self, 'project', n.get_bool_value()),
            "projectId": lambda n : setattr(self, 'project_id', n.get_int_value()),
            "relationshipLinkId": lambda n : setattr(self, 'relationship_link_id', n.get_int_value()),
            "relationshipLinkTypeId": lambda n : setattr(self, 'relationship_link_type_id', n.get_int_value()),
            "reminder": lambda n : setattr(self, 'reminder', n.get_int_value()),
            "reminderInterval": lambda n : setattr(self, 'reminder_interval', n.get_int_value()),
            "reminderIntervalHours": lambda n : setattr(self, 'reminder_interval_hours', n.get_int_value()),
            "remitterId": lambda n : setattr(self, 'remitter_id', n.get_int_value()),
            "repair": lambda n : setattr(self, 'repair', n.get_bool_value()),
            "resubmissionDate": lambda n : setattr(self, 'resubmission_date', n.get_int_value()),
            "resubmissionMailOptions": lambda n : setattr(self, 'resubmission_mail_options', n.get_object_value(TnsTicketResubmissionMailOptions)),
            "resubmissionMode": lambda n : setattr(self, 'resubmission_mode', n.get_enum_value(TnsTicketResubmissionMode)),
            "resubmissionText": lambda n : setattr(self, 'resubmission_text', n.get_str_value()),
            "separateBilling": lambda n : setattr(self, 'separate_billing', n.get_bool_value()),
            "serviceCapAmount": lambda n : setattr(self, 'service_cap_amount', n.get_float_value()),
            "statusId": lambda n : setattr(self, 'status_id', n.get_int_value()),
            "subTickets": lambda n : setattr(self, 'sub_tickets', n.get_collection_of_object_values(TicketComplete)),
            "tags": lambda n : setattr(self, 'tags', n.get_collection_of_object_values(TnsTagAssign)),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
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
        writer.write_int_value("assignedToDepartmentId", self.assigned_to_department_id)
        writer.write_int_value("assignedToEmployeeId", self.assigned_to_employee_id)
        writer.write_enum_value("attention", self.attention)
        writer.write_int_value("billingToCompanyId", self.billing_to_company_id)
        writer.write_enum_value("clearanceMode", self.clearance_mode)
        writer.write_int_value("companyId", self.company_id)
        writer.write_str_value("content", self.content)
        writer.write_int_value("deadlineDate", self.deadline_date)
        writer.write_bool_value("deliveryAddressOnPdf", self.delivery_address_on_pdf)
        writer.write_int_value("dueDate", self.due_date)
        writer.write_int_value("estimatedMinutes", self.estimated_minutes)
        writer.write_str_value("extTicketId", self.ext_ticket_id)
        writer.write_enum_value("installationFee", self.installation_fee)
        writer.write_float_value("installationFeeAmount", self.installation_fee_amount)
        writer.write_enum_value("installationFeeDriveMode", self.installation_fee_drive_mode)
        writer.write_int_value("linkId", self.link_id)
        writer.write_int_value("linkTypeId", self.link_type_id)
        writer.write_int_value("localTicketAdminEmployeeId", self.local_ticket_admin_employee_id)
        writer.write_enum_value("localTicketAdminFlag", self.local_ticket_admin_flag)
        writer.write_int_value("orderById", self.order_by_id)
        writer.write_str_value("orderNumber", self.order_number)
        writer.write_int_value("phaseId", self.phase_id)
        writer.write_bool_value("project", self.project)
        writer.write_int_value("projectId", self.project_id)
        writer.write_int_value("relationshipLinkId", self.relationship_link_id)
        writer.write_int_value("relationshipLinkTypeId", self.relationship_link_type_id)
        writer.write_int_value("reminder", self.reminder)
        writer.write_int_value("reminderInterval", self.reminder_interval)
        writer.write_int_value("reminderIntervalHours", self.reminder_interval_hours)
        writer.write_int_value("remitterId", self.remitter_id)
        writer.write_bool_value("repair", self.repair)
        writer.write_int_value("resubmissionDate", self.resubmission_date)
        writer.write_object_value("resubmissionMailOptions", self.resubmission_mail_options)
        writer.write_enum_value("resubmissionMode", self.resubmission_mode)
        writer.write_str_value("resubmissionText", self.resubmission_text)
        writer.write_bool_value("separateBilling", self.separate_billing)
        writer.write_float_value("serviceCapAmount", self.service_cap_amount)
        writer.write_int_value("statusId", self.status_id)
        writer.write_collection_of_object_values("subTickets", self.sub_tickets)
        writer.write_collection_of_object_values("tags", self.tags)
        writer.write_str_value("title", self.title)
        writer.write_int_value("typeId", self.type_id)
        writer.write_additional_data_value(self.additional_data)
    

