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
    from ......models.log403_error import Log403Error
    from .log_get_response import LogGetResponse

class LogRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/tags/assignment/log
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new LogRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/tags/assignment/log?linkId={linkId}&linkTypeId={linkTypeId}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[LogRequestBuilderGetQueryParameters]] = None) -> Optional[LogGetResponse]:
        """
        Gets alist of all tag logs to an entity (for example ticket). Here you can see when tags habe been assigned or removed.Must be technician/freelancer and have access to the assignment!
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[LogGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ......models.log403_error import Log403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Log403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .log_get_response import LogGetResponse

        return await self.request_adapter.send_async(request_info, LogGetResponse, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[LogRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Gets alist of all tag logs to an entity (for example ticket). Here you can see when tags habe been assigned or removed.Must be technician/freelancer and have access to the assignment!
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> LogRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: LogRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return LogRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class LogRequestBuilderGetQueryParameters():
        """
        Gets alist of all tag logs to an entity (for example ticket). Here you can see when tags habe been assigned or removed.Must be technician/freelancer and have access to the assignment!
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "link_id":
                return "linkId"
            if original_name == "link_type_id":
                return "linkTypeId"
            return original_name
        
        # id of the assignment
        link_id: Optional[int] = None

        # linkType of the assignment
        link_type_id: Optional[int] = None

    
    @dataclass
    class LogRequestBuilderGetRequestConfiguration(RequestConfiguration[LogRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

