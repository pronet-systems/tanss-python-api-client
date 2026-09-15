from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .assign_group.assign_group_request_builder import AssignGroupRequestBuilder
    from .ticket.ticket_request_builder import TicketRequestBuilder
    from .tickets_from_group.tickets_from_group_request_builder import TicketsFromGroupRequestBuilder

class V1RequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/monitoring/v1
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new V1RequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/monitoring/v1", path_parameters)
    
    @property
    def assign_group(self) -> AssignGroupRequestBuilder:
        """
        The assignGroup property
        """
        from .assign_group.assign_group_request_builder import AssignGroupRequestBuilder

        return AssignGroupRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def ticket(self) -> TicketRequestBuilder:
        """
        The ticket property
        """
        from .ticket.ticket_request_builder import TicketRequestBuilder

        return TicketRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def tickets_from_group(self) -> TicketsFromGroupRequestBuilder:
        """
        The ticketsFromGroup property
        """
        from .tickets_from_group.tickets_from_group_request_builder import TicketsFromGroupRequestBuilder

        return TicketsFromGroupRequestBuilder(self.request_adapter, self.path_parameters)
    

