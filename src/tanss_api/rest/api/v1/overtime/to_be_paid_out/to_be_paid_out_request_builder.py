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
    from .....models.to_be_paid_out403_error import ToBePaidOut403Error
    from .mark.mark_request_builder import MarkRequestBuilder
    from .to_be_paid_out_get_response import ToBePaidOutGetResponse

class ToBePaidOutRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/overtime/toBePaidOut
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new ToBePaidOutRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/overtime/toBePaidOut{?employeeId*}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[ToBePaidOutRequestBuilderGetQueryParameters]] = None) -> Optional[ToBePaidOutGetResponse]:
        """
        Returns the overtime pay-out requests that are pending pay-out.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ToBePaidOutGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .....models.to_be_paid_out403_error import ToBePaidOut403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": ToBePaidOut403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .to_be_paid_out_get_response import ToBePaidOutGetResponse

        return await self.request_adapter.send_async(request_info, ToBePaidOutGetResponse, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[ToBePaidOutRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Returns the overtime pay-out requests that are pending pay-out.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> ToBePaidOutRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: ToBePaidOutRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return ToBePaidOutRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def mark(self) -> MarkRequestBuilder:
        """
        The mark property
        """
        from .mark.mark_request_builder import MarkRequestBuilder

        return MarkRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class ToBePaidOutRequestBuilderGetQueryParameters():
        """
        Returns the overtime pay-out requests that are pending pay-out.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "employee_id":
                return "employeeId"
            return original_name
        
        # Restrict the result to a single employee; omit for all accessible employees
        employee_id: Optional[int] = None

    
    @dataclass
    class ToBePaidOutRequestBuilderGetRequestConfiguration(RequestConfiguration[ToBePaidOutRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

