from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.with_type_item_request_builder import WithTypeItemRequestBuilder

class PromptsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/ai/prompts
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new PromptsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/ai/prompts", path_parameters)
    
    def by_type(self,type: str) -> WithTypeItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.v1.ai.prompts.item collection
        param type: Textbaustein-Typ (Enum-Name).
        Returns: WithTypeItemRequestBuilder
        """
        if type is None:
            raise TypeError("type cannot be null.")
        from .item.with_type_item_request_builder import WithTypeItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["type"] = type
        return WithTypeItemRequestBuilder(self.request_adapter, url_tpl_params)
    

