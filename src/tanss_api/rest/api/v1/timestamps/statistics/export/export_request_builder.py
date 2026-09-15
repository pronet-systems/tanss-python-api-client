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
    from ......models.export403_error import Export403Error
    from .export_get_response import ExportGetResponse

class ExportRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/timestamps/statistics/export
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new ExportRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/timestamps/statistics/export{?employeeIds*,from*,till*}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[ExportRequestBuilderGetQueryParameters]] = None) -> Optional[ExportGetResponse]:
        """
        Returns the same per-day timestamp/statistics aggregation as `GET /statistics`, but rendered as a CSV file readyto be downloaded — typically used to hand work-time reports to payroll. The `Accept: text/csv` header controlswhether the file is streamed directly (`text/csv`) or wrapped in the standard meta/content envelope. Period andemployee list use the same query parameters as the regular statistics endpoint.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ExportGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ......models.export403_error import Export403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Export403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .export_get_response import ExportGetResponse

        return await self.request_adapter.send_async(request_info, ExportGetResponse, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[ExportRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Returns the same per-day timestamp/statistics aggregation as `GET /statistics`, but rendered as a CSV file readyto be downloaded — typically used to hand work-time reports to payroll. The `Accept: text/csv` header controlswhether the file is streamed directly (`text/csv`) or wrapped in the standard meta/content envelope. Period andemployee list use the same query parameters as the regular statistics endpoint.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> ExportRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: ExportRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return ExportRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class ExportRequestBuilderGetQueryParameters():
        """
        Returns the same per-day timestamp/statistics aggregation as `GET /statistics`, but rendered as a CSV file readyto be downloaded — typically used to hand work-time reports to payroll. The `Accept: text/csv` header controlswhether the file is streamed directly (`text/csv`) or wrapped in the standard meta/content envelope. Period andemployee list use the same query parameters as the regular statistics endpoint.
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
            if original_name == "from_":
                return "from"
            if original_name == "till":
                return "till"
            return original_name
        
        # comma-separated ids of the employees whose statistics are exported
        employee_ids: Optional[str] = None

        # timestamp of start of period; if omitted the beginning of the current day is used
        from_: Optional[int] = None

        # timestamp of end of period; if omitted the end of the current day is used
        till: Optional[int] = None

    
    @dataclass
    class ExportRequestBuilderGetRequestConfiguration(RequestConfiguration[ExportRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

