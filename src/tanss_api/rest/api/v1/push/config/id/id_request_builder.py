from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.id_item_request_builder import IdItemRequestBuilder

class IdRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/push/config/id
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new IdRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/push/config/id", path_parameters)
    
    def by_id(self,id: str) -> IdItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.v1.push.config.id.item collection
        param id: numerische Datensatz-ID (als String übergeben)
        Returns: IdItemRequestBuilder
        """
        if id is None:
            raise TypeError("id cannot be null.")
        from .item.id_item_request_builder import IdItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["id"] = id
        return IdItemRequestBuilder(self.request_adapter, url_tpl_params)
    

