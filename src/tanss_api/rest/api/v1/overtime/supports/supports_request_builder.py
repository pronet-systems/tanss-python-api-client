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
    from .....models.supports403_error import Supports403Error
    from .supports_get_response import SupportsGetResponse
    from .supports_post_request_body import SupportsPostRequestBody
    from .supports_post_response import SupportsPostResponse

class SupportsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/overtime/supports
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new SupportsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/overtime/supports", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[SupportsRequestBuilderGetQueryParameters]] = None) -> Optional[SupportsGetResponse]:
        """
        Returns the supports that can be booked as overtime within the given time range.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[SupportsGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .....models.supports403_error import Supports403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Supports403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .supports_get_response import SupportsGetResponse

        return await self.request_adapter.send_async(request_info, SupportsGetResponse, error_mapping)
    
    async def post(self,body: SupportsPostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[SupportsPostResponse]:
        """
        Creates a new overtime request.
        param body: Request body.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[SupportsPostResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from .....models.supports403_error import Supports403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Supports403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .supports_post_response import SupportsPostResponse

        return await self.request_adapter.send_async(request_info, SupportsPostResponse, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[SupportsRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Returns the supports that can be booked as overtime within the given time range.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, '{+baseurl}/api/v1/overtime/supports?from={from}&till={till}', self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: SupportsPostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Creates a new overtime request.
        param body: Request body.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.POST, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> SupportsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: SupportsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return SupportsRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class SupportsRequestBuilderGetQueryParameters():
        """
        Returns the supports that can be booked as overtime within the given time range.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "from_":
                return "from"
            if original_name == "till":
                return "till"
            return original_name
        
        # Unix timestamp of the start of the period
        from_: Optional[int] = None

        # Unix timestamp of the end of the period
        till: Optional[int] = None

    
    @dataclass
    class SupportsRequestBuilderGetRequestConfiguration(RequestConfiguration[SupportsRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class SupportsRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

