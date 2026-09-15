from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.with_link_type_item_request_builder import WithLinkTypeItemRequestBuilder
    from .properties.properties_request_builder import PropertiesRequestBuilder

class ListRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/log/list
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new ListRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/log/list", path_parameters)
    
    def by_link_type(self,link_type: str) -> WithLinkTypeItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.v1.log.list.item collection
        param link_type: Link type whose audit log entries should be queried (e.g. TICKET).
        Returns: WithLinkTypeItemRequestBuilder
        """
        if link_type is None:
            raise TypeError("link_type cannot be null.")
        from .item.with_link_type_item_request_builder import WithLinkTypeItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["linkType"] = link_type
        return WithLinkTypeItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    @property
    def properties(self) -> PropertiesRequestBuilder:
        """
        The properties property
        """
        from .properties.properties_request_builder import PropertiesRequestBuilder

        return PropertiesRequestBuilder(self.request_adapter, self.path_parameters)
    

