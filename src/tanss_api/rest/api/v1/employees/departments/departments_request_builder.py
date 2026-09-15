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
    from .....models.department import Department
    from .....models.departments403_error import Departments403Error
    from .departments_get_response import DepartmentsGetResponse
    from .departments_post_response import DepartmentsPostResponse
    from .item.departments_item_request_builder import DepartmentsItemRequestBuilder

class DepartmentsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/employees/departments
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new DepartmentsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/employees/departments", path_parameters)
    
    def by_id(self,id: str) -> DepartmentsItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.v1.employees.departments.item collection
        param id: Id of the department to delete.
        Returns: DepartmentsItemRequestBuilder
        """
        if id is None:
            raise TypeError("id cannot be null.")
        from .item.departments_item_request_builder import DepartmentsItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["id"] = id
        return DepartmentsItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[DepartmentsGetResponse]:
        """
        Returns all departments of the own company. Caller must be a technician orfreelancer.
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
    
    async def post(self,body: Department, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[DepartmentsPostResponse]:
        """
        Creates a department. Caller must be a technician or freelancer and hold the`BASE_DATA_MANAGEMENT_SYSTEM_TABLES` permission.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[DepartmentsPostResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from .....models.departments403_error import Departments403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Departments403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .departments_post_response import DepartmentsPostResponse

        return await self.request_adapter.send_async(request_info, DepartmentsPostResponse, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Returns all departments of the own company. Caller must be a technician orfreelancer.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: Department, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Creates a department. Caller must be a technician or freelancer and hold the`BASE_DATA_MANAGEMENT_SYSTEM_TABLES` permission.
        param body: The request body
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
    class DepartmentsRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class DepartmentsRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

