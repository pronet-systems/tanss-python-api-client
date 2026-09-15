from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.with_link_type_item_request_builder import WithLinkTypeItemRequestBuilder

class WithAccountingTypeItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/accountingTypes/prices/{accountingTypeId}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new WithAccountingTypeItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/accountingTypes/prices/{accountingTypeId}", path_parameters)
    
    def by_link_type_id(self,link_type_id: int) -> WithLinkTypeItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.v1.accountingTypes.prices.item.item collection
        param link_type_id: Link type of the assignment (company, contract, or ticket).
        Returns: WithLinkTypeItemRequestBuilder
        """
        if link_type_id is None:
            raise TypeError("link_type_id cannot be null.")
        from .item.with_link_type_item_request_builder import WithLinkTypeItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["linkTypeId"] = link_type_id
        return WithLinkTypeItemRequestBuilder(self.request_adapter, url_tpl_params)
    

