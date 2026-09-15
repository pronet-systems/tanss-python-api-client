from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.cpus_item_request_builder import CpusItemRequestBuilder

class CpusRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/deviceManagement/v1/cpus
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new CpusRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/deviceManagement/v1/cpus", path_parameters)
    
    def by_id(self,id: int) -> CpusItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.deviceManagement.v1.cpus.item collection
        param id: ID des CPU-Typs
        Returns: CpusItemRequestBuilder
        """
        if id is None:
            raise TypeError("id cannot be null.")
        from .item.cpus_item_request_builder import CpusItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["id"] = id
        return CpusItemRequestBuilder(self.request_adapter, url_tpl_params)
    

