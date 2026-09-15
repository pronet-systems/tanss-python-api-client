from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .call.call_request_builder import CallRequestBuilder
    from .checklists.checklists_request_builder import ChecklistsRequestBuilder
    from .companies.companies_request_builder import CompaniesRequestBuilder
    from .employees.employees_request_builder import EmployeesRequestBuilder
    from .git.git_request_builder import GitRequestBuilder
    from .modules.modules_request_builder import ModulesRequestBuilder
    from .osk.osk_request_builder import OskRequestBuilder
    from .recurrence.recurrence_request_builder import RecurrenceRequestBuilder
    from .remote_supports.remote_supports_request_builder import RemoteSupportsRequestBuilder
    from .search.search_request_builder import SearchRequestBuilder
    from .supports.supports_request_builder import SupportsRequestBuilder
    from .tanss_events.tanss_events_request_builder import TanssEventsRequestBuilder
    from .technicians.technicians_request_builder import TechniciansRequestBuilder
    from .templates.templates_request_builder import TemplatesRequestBuilder
    from .ticket.ticket_request_builder import TicketRequestBuilder
    from .ticket_board.ticket_board_request_builder import TicketBoardRequestBuilder
    from .timers.timers_request_builder import TimersRequestBuilder

class V1RequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/tanss.x/v1
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new V1RequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/tanss.x/v1", path_parameters)
    
    @property
    def call(self) -> CallRequestBuilder:
        """
        The call property
        """
        from .call.call_request_builder import CallRequestBuilder

        return CallRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def checklists(self) -> ChecklistsRequestBuilder:
        """
        The checklists property
        """
        from .checklists.checklists_request_builder import ChecklistsRequestBuilder

        return ChecklistsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def companies(self) -> CompaniesRequestBuilder:
        """
        The companies property
        """
        from .companies.companies_request_builder import CompaniesRequestBuilder

        return CompaniesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def employees(self) -> EmployeesRequestBuilder:
        """
        The employees property
        """
        from .employees.employees_request_builder import EmployeesRequestBuilder

        return EmployeesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def git(self) -> GitRequestBuilder:
        """
        The git property
        """
        from .git.git_request_builder import GitRequestBuilder

        return GitRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def modules(self) -> ModulesRequestBuilder:
        """
        The modules property
        """
        from .modules.modules_request_builder import ModulesRequestBuilder

        return ModulesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def osk(self) -> OskRequestBuilder:
        """
        The osk property
        """
        from .osk.osk_request_builder import OskRequestBuilder

        return OskRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def recurrence(self) -> RecurrenceRequestBuilder:
        """
        The recurrence property
        """
        from .recurrence.recurrence_request_builder import RecurrenceRequestBuilder

        return RecurrenceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def remote_supports(self) -> RemoteSupportsRequestBuilder:
        """
        The remoteSupports property
        """
        from .remote_supports.remote_supports_request_builder import RemoteSupportsRequestBuilder

        return RemoteSupportsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def search(self) -> SearchRequestBuilder:
        """
        The search property
        """
        from .search.search_request_builder import SearchRequestBuilder

        return SearchRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def supports(self) -> SupportsRequestBuilder:
        """
        The supports property
        """
        from .supports.supports_request_builder import SupportsRequestBuilder

        return SupportsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def tanss_events(self) -> TanssEventsRequestBuilder:
        """
        The tanssEvents property
        """
        from .tanss_events.tanss_events_request_builder import TanssEventsRequestBuilder

        return TanssEventsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def technicians(self) -> TechniciansRequestBuilder:
        """
        The technicians property
        """
        from .technicians.technicians_request_builder import TechniciansRequestBuilder

        return TechniciansRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def templates(self) -> TemplatesRequestBuilder:
        """
        The templates property
        """
        from .templates.templates_request_builder import TemplatesRequestBuilder

        return TemplatesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def ticket(self) -> TicketRequestBuilder:
        """
        The ticket property
        """
        from .ticket.ticket_request_builder import TicketRequestBuilder

        return TicketRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def ticket_board(self) -> TicketBoardRequestBuilder:
        """
        The ticketBoard property
        """
        from .ticket_board.ticket_board_request_builder import TicketBoardRequestBuilder

        return TicketBoardRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def timers(self) -> TimersRequestBuilder:
        """
        The timers property
        """
        from .timers.timers_request_builder import TimersRequestBuilder

        return TimersRequestBuilder(self.request_adapter, self.path_parameters)
    

