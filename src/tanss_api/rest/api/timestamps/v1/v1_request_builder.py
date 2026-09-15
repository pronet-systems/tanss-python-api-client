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
    from ....models.v1403_error import V1403Error
    from .v1_post_request_body import V1PostRequestBody
    from .v1_post_response import V1PostResponse

class V1RequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/timestamps/v1
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new V1RequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/timestamps/v1{?autoPause*}", path_parameters)
    
    async def post(self,body: V1PostRequestBody, request_configuration: Optional[RequestConfiguration[V1RequestBuilderPostQueryParameters]] = None) -> Optional[V1PostResponse]:
        """
        Records a single time stamp (Stempeluhr punch) for the calling employee — e.g. clocking on, off, starting a pauseor switching the work-time type. When `autoPause=true`, the service skips the minimum-pause check that normallyblocks an OFF/WORK punch if the legally required break for the day has not been reached yet.
        param body: Request body.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[V1PostResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ....models.v1403_error import V1403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": V1403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .v1_post_response import V1PostResponse

        return await self.request_adapter.send_async(request_info, V1PostResponse, error_mapping)
    
    def to_post_request_information(self,body: V1PostRequestBody, request_configuration: Optional[RequestConfiguration[V1RequestBuilderPostQueryParameters]] = None) -> RequestInformation:
        """
        Records a single time stamp (Stempeluhr punch) for the calling employee — e.g. clocking on, off, starting a pauseor switching the work-time type. When `autoPause=true`, the service skips the minimum-pause check that normallyblocks an OFF/WORK punch if the legally required break for the day has not been reached yet.
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
    
    def with_url(self,raw_url: str) -> V1RequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: V1RequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return V1RequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class V1RequestBuilderPostQueryParameters():
        """
        Records a single time stamp (Stempeluhr punch) for the calling employee — e.g. clocking on, off, starting a pauseor switching the work-time type. When `autoPause=true`, the service skips the minimum-pause check that normallyblocks an OFF/WORK punch if the legally required break for the day has not been reached yet.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "auto_pause":
                return "autoPause"
            return original_name
        
        # Skip the minimum-pause check when recording the punch
        auto_pause: Optional[bool] = None

    
    @dataclass
    class V1RequestBuilderPostRequestConfiguration(RequestConfiguration[V1RequestBuilderPostQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

