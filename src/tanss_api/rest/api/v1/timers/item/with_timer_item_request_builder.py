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
    from .....models.with_timer403_error import WithTimer403Error
    from .with_timer_get_response import WithTimerGetResponse
    from .with_timer_put_response import WithTimerPutResponse

class WithTimerItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/timers/{timerId}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new WithTimerItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/timers/{timerId}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[WithTimerGetResponse]:
        """
        This route will get a specific timer, given by an id
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[WithTimerGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .....models.with_timer403_error import WithTimer403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": WithTimer403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .with_timer_get_response import WithTimerGetResponse

        return await self.request_adapter.send_async(request_info, WithTimerGetResponse, error_mapping)
    
    async def put(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[WithTimerPutResponse]:
        """
        This route will either start or stop a timer
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[WithTimerPutResponse]
        """
        request_info = self.to_put_request_information(
            request_configuration
        )
        from .....models.with_timer403_error import WithTimer403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": WithTimer403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .with_timer_put_response import WithTimerPutResponse

        return await self.request_adapter.send_async(request_info, WithTimerPutResponse, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        This route will get a specific timer, given by an id
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_put_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        This route will either start or stop a timer
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.PUT, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> WithTimerItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: WithTimerItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return WithTimerItemRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class WithTimerItemRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class WithTimerItemRequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

