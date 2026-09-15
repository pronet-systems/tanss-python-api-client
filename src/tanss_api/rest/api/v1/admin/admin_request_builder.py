from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .ai.ai_request_builder import AiRequestBuilder
    from .permission_packages.permission_packages_request_builder import PermissionPackagesRequestBuilder
    from .ticket_states.ticket_states_request_builder import TicketStatesRequestBuilder
    from .ticket_types.ticket_types_request_builder import TicketTypesRequestBuilder

class AdminRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/admin
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new AdminRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/admin", path_parameters)
    
    @property
    def ai(self) -> AiRequestBuilder:
        """
        The ai property
        """
        from .ai.ai_request_builder import AiRequestBuilder

        return AiRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def permission_packages(self) -> PermissionPackagesRequestBuilder:
        """
        The permissionPackages property
        """
        from .permission_packages.permission_packages_request_builder import PermissionPackagesRequestBuilder

        return PermissionPackagesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def ticket_states(self) -> TicketStatesRequestBuilder:
        """
        The ticketStates property
        """
        from .ticket_states.ticket_states_request_builder import TicketStatesRequestBuilder

        return TicketStatesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def ticket_types(self) -> TicketTypesRequestBuilder:
        """
        The ticketTypes property
        """
        from .ticket_types.ticket_types_request_builder import TicketTypesRequestBuilder

        return TicketTypesRequestBuilder(self.request_adapter, self.path_parameters)
    

