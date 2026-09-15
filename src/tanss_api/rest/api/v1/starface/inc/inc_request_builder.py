from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.with_user_item_request_builder import WithUserItemRequestBuilder

class IncRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/starface/inc
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new IncRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/starface/inc", path_parameters)
    
    def by_user_id(self,user_id: int) -> WithUserItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.v1.starface.inc.item collection
        param user_id: Id of the employee the incoming call is forwarded to.
        Returns: WithUserItemRequestBuilder
        """
        if user_id is None:
            raise TypeError("user_id cannot be null.")
        from .item.with_user_item_request_builder import WithUserItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["userId"] = user_id
        return WithUserItemRequestBuilder(self.request_adapter, url_tpl_params)
    

