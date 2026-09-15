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
    from ......models.with_mins403_error import WithMins403Error
    from .with_mins_get_response import WithMinsGetResponse

class WithMinsItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/round/support/{mins}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new WithMinsItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/round/support/{mins}{?companyId*,contractId*,employeeId*,location*,typeId*}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[WithMinsItemRequestBuilderGetQueryParameters]] = None) -> Optional[WithMinsGetResponse]:
        """
        Looks up the rounding rule (object) that matches the given context (location, company, support type, employee, contract) and applies it to `mins`. Used by the UI to display the duration that would actually be billed when the tech stops the stopwatch. Returns `NOT_FOUND` (no body content) when no rounding rule applies.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[WithMinsGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ......models.with_mins403_error import WithMins403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": WithMins403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .with_mins_get_response import WithMinsGetResponse

        return await self.request_adapter.send_async(request_info, WithMinsGetResponse, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[WithMinsItemRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Looks up the rounding rule (object) that matches the given context (location, company, support type, employee, contract) and applies it to `mins`. Used by the UI to display the duration that would actually be billed when the tech stops the stopwatch. Returns `NOT_FOUND` (no body content) when no rounding rule applies.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> WithMinsItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: WithMinsItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return WithMinsItemRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class WithMinsItemRequestBuilderGetQueryParameters():
        """
        Looks up the rounding rule (object) that matches the given context (location, company, support type, employee, contract) and applies it to `mins`. Used by the UI to display the duration that would actually be billed when the tech stops the stopwatch. Returns `NOT_FOUND` (no body content) when no rounding rule applies.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "company_id":
                return "companyId"
            if original_name == "contract_id":
                return "contractId"
            if original_name == "employee_id":
                return "employeeId"
            if original_name == "type_id":
                return "typeId"
            if original_name == "location":
                return "location"
            return original_name
        
        # Company context used to select the matching rounding rule; 0 means none.
        company_id: Optional[int] = None

        # Contract context used to select the matching rounding rule; 0 means none.
        contract_id: Optional[int] = None

        # Employee context used to select the matching rounding rule; 0 means none.
        employee_id: Optional[int] = None

        # Support location used to select the matching rounding rule.
        location: Optional[str] = None

        # Support-type context used to select the matching rounding rule; 0 means none.
        type_id: Optional[int] = None

    
    @dataclass
    class WithMinsItemRequestBuilderGetRequestConfiguration(RequestConfiguration[WithMinsItemRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

