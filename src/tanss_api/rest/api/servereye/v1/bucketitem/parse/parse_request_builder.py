from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.parse_item_request_builder import ParseItemRequestBuilder

class ParseRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/servereye/v1/bucketitem/parse
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new ParseRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/servereye/v1/bucketitem/parse", path_parameters)
    
    def by_id(self,id: int) -> ParseItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.servereye.v1.bucketitem.parse.item collection
        param id: ID of the stored Server-Eye bucket item to parse.
        Returns: ParseItemRequestBuilder
        """
        if id is None:
            raise TypeError("id cannot be null.")
        from .item.parse_item_request_builder import ParseItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["id"] = id
        return ParseItemRequestBuilder(self.request_adapter, url_tpl_params)
    

