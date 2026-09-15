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
    from .......models.completion_infos403_error import CompletionInfos403Error
    from .completion_infos_get_response import CompletionInfosGetResponse

class CompletionInfosRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/ownDailyServices/{day}/statisticAllServicesByDay/completionInfos
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new CompletionInfosRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/ownDailyServices/{day}/statisticAllServicesByDay/completionInfos{?employeeIds*}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[CompletionInfosRequestBuilderGetQueryParameters]] = None) -> Optional[CompletionInfosGetResponse]:
        """
        Returns one completion-status entry per requested employee for the given day — telling the team-overview screen whether eachemployee `HAS_TO_COMPLETE`, has `COMPLETED` the day, completed on `COMPLETED_OTHER_DAY`, or `NONE` (no daily-servicesconfiguration / not active yet). Requires `STATISTICS_ALL_SERVICES_OF_A_DAY` from the own company.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[CompletionInfosGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .......models.completion_infos403_error import CompletionInfos403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": CompletionInfos403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .completion_infos_get_response import CompletionInfosGetResponse

        return await self.request_adapter.send_async(request_info, CompletionInfosGetResponse, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[CompletionInfosRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Returns one completion-status entry per requested employee for the given day — telling the team-overview screen whether eachemployee `HAS_TO_COMPLETE`, has `COMPLETED` the day, completed on `COMPLETED_OTHER_DAY`, or `NONE` (no daily-servicesconfiguration / not active yet). Requires `STATISTICS_ALL_SERVICES_OF_A_DAY` from the own company.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> CompletionInfosRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: CompletionInfosRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return CompletionInfosRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class CompletionInfosRequestBuilderGetQueryParameters():
        """
        Returns one completion-status entry per requested employee for the given day — telling the team-overview screen whether eachemployee `HAS_TO_COMPLETE`, has `COMPLETED` the day, completed on `COMPLETED_OTHER_DAY`, or `NONE` (no daily-servicesconfiguration / not active yet). Requires `STATISTICS_ALL_SERVICES_OF_A_DAY` from the own company.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "employee_ids":
                return "employeeIds"
            return original_name
        
        # Comma-separated list of employee ids to include; empty means all employees.
        employee_ids: Optional[str] = None

    
    @dataclass
    class CompletionInfosRequestBuilderGetRequestConfiguration(RequestConfiguration[CompletionInfosRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

