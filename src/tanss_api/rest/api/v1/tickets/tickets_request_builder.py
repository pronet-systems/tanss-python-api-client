from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from kiota_abstractions.default_query_parameters import QueryParameters
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Optional, TYPE_CHECKING, Union
from warnings import warn

if TYPE_CHECKING:
    from ....models.tickets403_error import Tickets403Error
    from ....models.ticket_configuration import TicketConfiguration
    from ....models.ticket_save import TicketSave
    from .absent_technicians.absent_technicians_request_builder import AbsentTechniciansRequestBuilder
    from .assignments.assignments_request_builder import AssignmentsRequestBuilder
    from .company.company_request_builder import CompanyRequestBuilder
    from .company_tickets_for_merge.company_tickets_for_merge_request_builder import CompanyTicketsForMergeRequestBuilder
    from .company_tickets_for_other_ticket.company_tickets_for_other_ticket_request_builder import CompanyTicketsForOtherTicketRequestBuilder
    from .company_tickets_for_project.company_tickets_for_project_request_builder import CompanyTicketsForProjectRequestBuilder
    from .department_order.department_order_request_builder import DepartmentOrderRequestBuilder
    from .flags.flags_request_builder import FlagsRequestBuilder
    from .general.general_request_builder import GeneralRequestBuilder
    from .history.history_request_builder import HistoryRequestBuilder
    from .item.item_request_builder import ItemRequestBuilder
    from .last_entry.last_entry_request_builder import LastEntryRequestBuilder
    from .list_.list_request_builder import ListRequestBuilder
    from .local_admin_overview.local_admin_overview_request_builder import LocalAdminOverviewRequestBuilder
    from .local_admin_tickets.local_admin_tickets_request_builder import LocalAdminTicketsRequestBuilder
    from .not_identified.not_identified_request_builder import NotIdentifiedRequestBuilder
    from .own.own_request_builder import OwnRequestBuilder
    from .pinned.pinned_request_builder import PinnedRequestBuilder
    from .preferred_technicians.preferred_technicians_request_builder import PreferredTechniciansRequestBuilder
    from .projects.projects_request_builder import ProjectsRequestBuilder
    from .repair.repair_request_builder import RepairRequestBuilder
    from .status.status_request_builder import StatusRequestBuilder
    from .technician.technician_request_builder import TechnicianRequestBuilder
    from .tickets_get_response import TicketsGetResponse
    from .tickets_post_response import TicketsPostResponse
    from .tickets_put_response import TicketsPutResponse
    from .types.types_request_builder import TypesRequestBuilder
    from .unwanted_technicians.unwanted_technicians_request_builder import UnwantedTechniciansRequestBuilder
    from .waiting_states.waiting_states_request_builder import WaitingStatesRequestBuilder
    from .with_role.with_role_request_builder import WithRoleRequestBuilder

class TicketsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/tickets
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new TicketsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/tickets{?remitterCheck*}", path_parameters)
    
    def by_id(self,id: int) -> ItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.v1.tickets.item collection
        param id: Id of the ticket to retrieve.
        Returns: ItemRequestBuilder
        """
        if id is None:
            raise TypeError("id cannot be null.")
        from .item.item_request_builder import ItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["%2Did"] = id
        return ItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[TicketsRequestBuilderGetQueryParameters]] = None) -> Optional[TicketsGetResponse]:
        """
        Liefert eine Ticket-Vorlage (leeres Ticket für eine Firma) samt Feld-Eigenschaften zum Anlegen eines neuen Tickets.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId.Hinweise: Tatsächliches Mapping ist '/api/v1/tickets/' MIT Trailing-Slash (Spring Boot 3 unterscheidet das von /api/v1/tickets). Query companyId ist Pflicht. Kein expliziter Rechte-Check; Rechte fließen nur in properties.editable und die Feld-Eigenschaften ein. Vorbelegung: companyId=Query, assignedToEmployeeId=aktueller Benutzer, statusId=0.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[TicketsGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .tickets_get_response import TicketsGetResponse

        return await self.request_adapter.send_async(request_info, TicketsGetResponse, None)
    
    async def post(self,body: TicketSave, request_configuration: Optional[RequestConfiguration[TicketsRequestBuilderPostQueryParameters]] = None) -> Optional[TicketsPostResponse]:
        """
        Creates a new ticket. The request body must contain at minimum a`companyId`, `subject`, and a `remitterId` (the contact who reported theissue) — unless `remitterCheck=false` is passed to bypass the remitterrequirement (useful when importing or when the originating contact isunknown).When creating a project, sub-tickets can be supplied inline via`subTickets[]` and will be attached as children in a single call.Tag assignments can be sent under `tags[]`.Returns the fully-saved `Ticket-Complete` shape, including theserver-assigned `id` and any computed fields.
        param body: ticket model to be saved
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[TicketsPostResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ....models.tickets403_error import Tickets403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Tickets403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .tickets_post_response import TicketsPostResponse

        return await self.request_adapter.send_async(request_info, TicketsPostResponse, error_mapping)
    
    async def put(self,body: TicketConfiguration, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[TicketsPutResponse]:
        """
        Retrieves a ticket list using arbitrary filter, sort, and paginationcriteria supplied in the request body (`TicketConfiguration`). This is thegeneral-purpose list endpoint behind most UI ticket views.When one of the specialised list endpoints (`/own`, `/general`,`/technician`, `/repair`, `/notIdentified`, `/projects`, `/withRole`,`/localAdminOverview`, `/company/{companyId}`) matches your use caseexactly, prefer it — those are faster, take no body, and don't requireyou to compose a filter object.
        param body: query parameters for fetching a custom ticket list
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[TicketsPutResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        from ....models.tickets403_error import Tickets403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Tickets403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .tickets_put_response import TicketsPutResponse

        return await self.request_adapter.send_async(request_info, TicketsPutResponse, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[TicketsRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Liefert eine Ticket-Vorlage (leeres Ticket für eine Firma) samt Feld-Eigenschaften zum Anlegen eines neuen Tickets.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId.Hinweise: Tatsächliches Mapping ist '/api/v1/tickets/' MIT Trailing-Slash (Spring Boot 3 unterscheidet das von /api/v1/tickets). Query companyId ist Pflicht. Kein expliziter Rechte-Check; Rechte fließen nur in properties.editable und die Feld-Eigenschaften ein. Vorbelegung: companyId=Query, assignedToEmployeeId=aktueller Benutzer, statusId=0.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, '{+baseurl}/api/v1/tickets?companyId={companyId}', self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: TicketSave, request_configuration: Optional[RequestConfiguration[TicketsRequestBuilderPostQueryParameters]] = None) -> RequestInformation:
        """
        Creates a new ticket. The request body must contain at minimum a`companyId`, `subject`, and a `remitterId` (the contact who reported theissue) — unless `remitterCheck=false` is passed to bypass the remitterrequirement (useful when importing or when the originating contact isunknown).When creating a project, sub-tickets can be supplied inline via`subTickets[]` and will be attached as children in a single call.Tag assignments can be sent under `tags[]`.Returns the fully-saved `Ticket-Complete` shape, including theserver-assigned `id` and any computed fields.
        param body: ticket model to be saved
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.POST, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def to_put_request_information(self,body: TicketConfiguration, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Retrieves a ticket list using arbitrary filter, sort, and paginationcriteria supplied in the request body (`TicketConfiguration`). This is thegeneral-purpose list endpoint behind most UI ticket views.When one of the specialised list endpoints (`/own`, `/general`,`/technician`, `/repair`, `/notIdentified`, `/projects`, `/withRole`,`/localAdminOverview`, `/company/{companyId}`) matches your use caseexactly, prefer it — those are faster, take no body, and don't requireyou to compose a filter object.
        param body: query parameters for fetching a custom ticket list
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.PUT, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> TicketsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: TicketsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return TicketsRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def absent_technicians(self) -> AbsentTechniciansRequestBuilder:
        """
        The absentTechnicians property
        """
        from .absent_technicians.absent_technicians_request_builder import AbsentTechniciansRequestBuilder

        return AbsentTechniciansRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def assignments(self) -> AssignmentsRequestBuilder:
        """
        The assignments property
        """
        from .assignments.assignments_request_builder import AssignmentsRequestBuilder

        return AssignmentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def company(self) -> CompanyRequestBuilder:
        """
        The company property
        """
        from .company.company_request_builder import CompanyRequestBuilder

        return CompanyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def company_tickets_for_merge(self) -> CompanyTicketsForMergeRequestBuilder:
        """
        The companyTicketsForMerge property
        """
        from .company_tickets_for_merge.company_tickets_for_merge_request_builder import CompanyTicketsForMergeRequestBuilder

        return CompanyTicketsForMergeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def company_tickets_for_other_ticket(self) -> CompanyTicketsForOtherTicketRequestBuilder:
        """
        The companyTicketsForOtherTicket property
        """
        from .company_tickets_for_other_ticket.company_tickets_for_other_ticket_request_builder import CompanyTicketsForOtherTicketRequestBuilder

        return CompanyTicketsForOtherTicketRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def company_tickets_for_project(self) -> CompanyTicketsForProjectRequestBuilder:
        """
        The companyTicketsForProject property
        """
        from .company_tickets_for_project.company_tickets_for_project_request_builder import CompanyTicketsForProjectRequestBuilder

        return CompanyTicketsForProjectRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def department_order(self) -> DepartmentOrderRequestBuilder:
        """
        The departmentOrder property
        """
        from .department_order.department_order_request_builder import DepartmentOrderRequestBuilder

        return DepartmentOrderRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def flags(self) -> FlagsRequestBuilder:
        """
        The flags property
        """
        from .flags.flags_request_builder import FlagsRequestBuilder

        return FlagsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def general(self) -> GeneralRequestBuilder:
        """
        The general property
        """
        from .general.general_request_builder import GeneralRequestBuilder

        return GeneralRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def history(self) -> HistoryRequestBuilder:
        """
        The history property
        """
        from .history.history_request_builder import HistoryRequestBuilder

        return HistoryRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def last_entry(self) -> LastEntryRequestBuilder:
        """
        The lastEntry property
        """
        from .last_entry.last_entry_request_builder import LastEntryRequestBuilder

        return LastEntryRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def list_(self) -> ListRequestBuilder:
        """
        The list property
        """
        from .list_.list_request_builder import ListRequestBuilder

        return ListRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def local_admin_overview(self) -> LocalAdminOverviewRequestBuilder:
        """
        The localAdminOverview property
        """
        from .local_admin_overview.local_admin_overview_request_builder import LocalAdminOverviewRequestBuilder

        return LocalAdminOverviewRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def local_admin_tickets(self) -> LocalAdminTicketsRequestBuilder:
        """
        The localAdminTickets property
        """
        from .local_admin_tickets.local_admin_tickets_request_builder import LocalAdminTicketsRequestBuilder

        return LocalAdminTicketsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def not_identified(self) -> NotIdentifiedRequestBuilder:
        """
        The notIdentified property
        """
        from .not_identified.not_identified_request_builder import NotIdentifiedRequestBuilder

        return NotIdentifiedRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def own(self) -> OwnRequestBuilder:
        """
        The own property
        """
        from .own.own_request_builder import OwnRequestBuilder

        return OwnRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def pinned(self) -> PinnedRequestBuilder:
        """
        The pinned property
        """
        from .pinned.pinned_request_builder import PinnedRequestBuilder

        return PinnedRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def preferred_technicians(self) -> PreferredTechniciansRequestBuilder:
        """
        The preferredTechnicians property
        """
        from .preferred_technicians.preferred_technicians_request_builder import PreferredTechniciansRequestBuilder

        return PreferredTechniciansRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def projects(self) -> ProjectsRequestBuilder:
        """
        The projects property
        """
        from .projects.projects_request_builder import ProjectsRequestBuilder

        return ProjectsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def repair(self) -> RepairRequestBuilder:
        """
        The repair property
        """
        from .repair.repair_request_builder import RepairRequestBuilder

        return RepairRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def status(self) -> StatusRequestBuilder:
        """
        The status property
        """
        from .status.status_request_builder import StatusRequestBuilder

        return StatusRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def technician(self) -> TechnicianRequestBuilder:
        """
        The technician property
        """
        from .technician.technician_request_builder import TechnicianRequestBuilder

        return TechnicianRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def types(self) -> TypesRequestBuilder:
        """
        The types property
        """
        from .types.types_request_builder import TypesRequestBuilder

        return TypesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def unwanted_technicians(self) -> UnwantedTechniciansRequestBuilder:
        """
        The unwantedTechnicians property
        """
        from .unwanted_technicians.unwanted_technicians_request_builder import UnwantedTechniciansRequestBuilder

        return UnwantedTechniciansRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def waiting_states(self) -> WaitingStatesRequestBuilder:
        """
        The waitingStates property
        """
        from .waiting_states.waiting_states_request_builder import WaitingStatesRequestBuilder

        return WaitingStatesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def with_role(self) -> WithRoleRequestBuilder:
        """
        The withRole property
        """
        from .with_role.with_role_request_builder import WithRoleRequestBuilder

        return WithRoleRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class TicketsRequestBuilderGetQueryParameters():
        """
        Liefert eine Ticket-Vorlage (leeres Ticket für eine Firma) samt Feld-Eigenschaften zum Anlegen eines neuen Tickets.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId.Hinweise: Tatsächliches Mapping ist '/api/v1/tickets/' MIT Trailing-Slash (Spring Boot 3 unterscheidet das von /api/v1/tickets). Query companyId ist Pflicht. Kein expliziter Rechte-Check; Rechte fließen nur in properties.editable und die Feld-Eigenschaften ein. Vorbelegung: companyId=Query, assignedToEmployeeId=aktueller Benutzer, statusId=0.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "company_id":
                return "companyId"
            return original_name
        
        # ID der Firma, für die die Vorlage erstellt wird
        company_id: Optional[int] = None

    
    @dataclass
    class TicketsRequestBuilderGetRequestConfiguration(RequestConfiguration[TicketsRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class TicketsRequestBuilderPostQueryParameters():
        """
        Creates a new ticket. The request body must contain at minimum a`companyId`, `subject`, and a `remitterId` (the contact who reported theissue) — unless `remitterCheck=false` is passed to bypass the remitterrequirement (useful when importing or when the originating contact isunknown).When creating a project, sub-tickets can be supplied inline via`subTickets[]` and will be attached as children in a single call.Tag assignments can be sent under `tags[]`.Returns the fully-saved `Ticket-Complete` shape, including theserver-assigned `id` and any computed fields.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "remitter_check":
                return "remitterCheck"
            return original_name
        
        # When `false`, skips the validation that a remitter must be present.Defaults to `true`.
        remitter_check: Optional[bool] = None

    
    @dataclass
    class TicketsRequestBuilderPostRequestConfiguration(RequestConfiguration[TicketsRequestBuilderPostQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class TicketsRequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

