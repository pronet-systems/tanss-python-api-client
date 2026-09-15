from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.with_ticket_item_request_builder import WithTicketItemRequestBuilder

class FlagsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/tickets/flags
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new FlagsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/tickets/flags", path_parameters)
    
    def by_ticket_id(self,ticket_id: int) -> WithTicketItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.v1.tickets.flags.item collection
        param ticket_id: Id of the ticket whose header flag icons should be returned (use 0 for a not-yet-persisted ticket).
        Returns: WithTicketItemRequestBuilder
        """
        if ticket_id is None:
            raise TypeError("ticket_id cannot be null.")
        from .item.with_ticket_item_request_builder import WithTicketItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["ticketId"] = ticket_id
        return WithTicketItemRequestBuilder(self.request_adapter, url_tpl_params)
    

