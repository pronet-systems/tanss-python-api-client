from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from kiota_abstractions.default_query_parameters import QueryParameters
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Optional, TYPE_CHECKING, Union
from warnings import warn

if TYPE_CHECKING:
    from .....models.ws403_error import Ws403Error
    from .ws_get_response import WsGetResponse
    from .ws_post_response import WsPostResponse

class WsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/util/ws
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new WsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/util/ws{?all*}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[WsRequestBuilderGetQueryParameters]] = None) -> Optional[WsGetResponse]:
        """
        Returns the WebSocket session ids of the currently authenticated user. When `all=true` and the caller holds `ONLINE_SYSTEM_CONFIGURATION`, the response contains every connected session in the system — useful for admins debugging push delivery.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[WsGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .....models.ws403_error import Ws403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Ws403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .ws_get_response import WsGetResponse

        return await self.request_adapter.send_async(request_info, WsGetResponse, error_mapping)
    
    async def post(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[WsPostResponse]:
        """
        Broadcasts a `TEST` message over the WebSocket handler. Used by admins to verify that push delivery to the caller is working; the response contains how many sessions received the test.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[WsPostResponse]
        """
        request_info = self.to_post_request_information(
            request_configuration
        )
        from .....models.ws403_error import Ws403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Ws403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .ws_post_response import WsPostResponse

        return await self.request_adapter.send_async(request_info, WsPostResponse, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[WsRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Returns the WebSocket session ids of the currently authenticated user. When `all=true` and the caller holds `ONLINE_SYSTEM_CONFIGURATION`, the response contains every connected session in the system — useful for admins debugging push delivery.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Broadcasts a `TEST` message over the WebSocket handler. Used by admins to verify that push delivery to the caller is working; the response contains how many sessions received the test.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.POST, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> WsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: WsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return WsRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class WsRequestBuilderGetQueryParameters():
        """
        Returns the WebSocket session ids of the currently authenticated user. When `all=true` and the caller holds `ONLINE_SYSTEM_CONFIGURATION`, the response contains every connected session in the system — useful for admins debugging push delivery.
        """
        # When true, return every connected session (requires ONLINE_SYSTEM_CONFIGURATION) instead of only the caller's.
        all: Optional[bool] = None

    
    @dataclass
    class WsRequestBuilderGetRequestConfiguration(RequestConfiguration[WsRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class WsRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

