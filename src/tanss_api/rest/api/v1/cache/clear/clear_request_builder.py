from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.with_cache_type_item_request_builder import WithCacheTypeItemRequestBuilder

class ClearRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/cache/clear
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new ClearRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/cache/clear", path_parameters)
    
    def by_cache_type(self,cache_type: str) -> WithCacheTypeItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.v1.cache.clear.item collection
        param cache_type: Name of the in-memory cache to clear (e.g. `deviceType`, `employeeRights`, `companyHqs`).
        Returns: WithCacheTypeItemRequestBuilder
        """
        if cache_type is None:
            raise TypeError("cache_type cannot be null.")
        from .item.with_cache_type_item_request_builder import WithCacheTypeItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["cacheType"] = cache_type
        return WithCacheTypeItemRequestBuilder(self.request_adapter, url_tpl_params)
    

