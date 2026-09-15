from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.with_browser_type_item_request_builder import WithBrowserTypeItemRequestBuilder

class BrowserRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/browser
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new BrowserRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/browser", path_parameters)
    
    def by_browser_type(self,browser_type: str) -> WithBrowserTypeItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.v1.browser.item collection
        param browser_type: Browser-Typ (nur SOFTWARELICENSE implementiert; weitere Werte KNOWLEDGE_BASE, FILE_LINKS, DOCUMENT)
        Returns: WithBrowserTypeItemRequestBuilder
        """
        if browser_type is None:
            raise TypeError("browser_type cannot be null.")
        from .item.with_browser_type_item_request_builder import WithBrowserTypeItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["browserType"] = browser_type
        return WithBrowserTypeItemRequestBuilder(self.request_adapter, url_tpl_params)
    

