from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.with_support_item_request_builder import WithSupportItemRequestBuilder

class LinkRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/ev/appointments/{appointmentId}/link
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new LinkRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/ev/appointments/{appointmentId}/link", path_parameters)
    
    def by_support_id(self,support_id: int) -> WithSupportItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.v1.ev.appointments.item.link.item collection
        param support_id: Support-ID
        Returns: WithSupportItemRequestBuilder
        """
        if support_id is None:
            raise TypeError("support_id cannot be null.")
        from .item.with_support_item_request_builder import WithSupportItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["supportId"] = support_id
        return WithSupportItemRequestBuilder(self.request_adapter, url_tpl_params)
    

