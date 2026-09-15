from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.with_destination_ticket_item_request_builder import WithDestinationTicketItemRequestBuilder

class MergeRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/tickets/{-id}/merge
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new MergeRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/tickets/{%2Did}/merge", path_parameters)
    
    def by_destination_ticket_id(self,destination_ticket_id: int) -> WithDestinationTicketItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.v1.tickets.item.merge.item collection
        param destination_ticket_id: Id of the ticket to merge into (receives the source's entities).
        Returns: WithDestinationTicketItemRequestBuilder
        """
        if destination_ticket_id is None:
            raise TypeError("destination_ticket_id cannot be null.")
        from .item.with_destination_ticket_item_request_builder import WithDestinationTicketItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["destinationTicketId"] = destination_ticket_id
        return WithDestinationTicketItemRequestBuilder(self.request_adapter, url_tpl_params)
    

