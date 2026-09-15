from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.with_source_type_item_request_builder import WithSourceTypeItemRequestBuilder

class ForRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/genericAssignments/for
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new ForRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/genericAssignments/for", path_parameters)
    
    def by_source_type(self,source_type: str) -> WithSourceTypeItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.v1.genericAssignments.for.item collection
        param source_type: Type of the source entity (e.g. TICKET).
        Returns: WithSourceTypeItemRequestBuilder
        """
        if source_type is None:
            raise TypeError("source_type cannot be null.")
        from .item.with_source_type_item_request_builder import WithSourceTypeItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["sourceType"] = source_type
        return WithSourceTypeItemRequestBuilder(self.request_adapter, url_tpl_params)
    

