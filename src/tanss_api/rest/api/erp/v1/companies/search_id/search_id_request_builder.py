from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.with_display_item_request_builder import WithDisplayItemRequestBuilder

class SearchIdRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/erp/v1/companies/searchId
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new SearchIdRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/erp/v1/companies/searchId", path_parameters)
    
    def by_display_id(self,display_id: str) -> WithDisplayItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.erp.v1.companies.searchId.item collection
        param display_id: external customer number, which is used by the ERP system
        Returns: WithDisplayItemRequestBuilder
        """
        if display_id is None:
            raise TypeError("display_id cannot be null.")
        from .item.with_display_item_request_builder import WithDisplayItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["displayId"] = display_id
        return WithDisplayItemRequestBuilder(self.request_adapter, url_tpl_params)
    

