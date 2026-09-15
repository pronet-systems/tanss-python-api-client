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
    from .....models.departments403_error import Departments403Error
    from .departments_get_response import DepartmentsGetResponse

class DepartmentsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/companies/departments
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new DepartmentsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/companies/departments{?withEmployees*}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[DepartmentsRequestBuilderGetQueryParameters]] = None) -> Optional[DepartmentsGetResponse]:
        """
        Returns the list of employee departments (id + name) defined in the system. When `withEmployees=true` and the caller is a technician or freelancer, each department is enriched with the list of employee IDs assigned to it; customer users never receive the employee IDs even if they request them. Used to populate department selectors in the UI.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[DepartmentsGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .....models.departments403_error import Departments403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Departments403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .departments_get_response import DepartmentsGetResponse

        return await self.request_adapter.send_async(request_info, DepartmentsGetResponse, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[DepartmentsRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Returns the list of employee departments (id + name) defined in the system. When `withEmployees=true` and the caller is a technician or freelancer, each department is enriched with the list of employee IDs assigned to it; customer users never receive the employee IDs even if they request them. Used to populate department selectors in the UI.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> DepartmentsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: DepartmentsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return DepartmentsRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class DepartmentsRequestBuilderGetQueryParameters():
        """
        Returns the list of employee departments (id + name) defined in the system. When `withEmployees=true` and the caller is a technician or freelancer, each department is enriched with the list of employee IDs assigned to it; customer users never receive the employee IDs even if they request them. Used to populate department selectors in the UI.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "with_employees":
                return "withEmployees"
            return original_name
        
        # When true, each department is enriched with the list of assigned employee IDs (technicians/freelancers only).
        with_employees: Optional[bool] = None

    
    @dataclass
    class DepartmentsRequestBuilderGetRequestConfiguration(RequestConfiguration[DepartmentsRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

