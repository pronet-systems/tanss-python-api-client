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
    from ......models.employee403_error import Employee403Error
    from .departments.departments_request_builder import DepartmentsRequestBuilder
    from .employee_get_response import EmployeeGetResponse
    from .employee_put_request_body import EmployeePutRequestBody
    from .employee_put_response import EmployeePutResponse

class EmployeeItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/erp/v1/employees/{employee-id}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new EmployeeItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/erp/v1/employees/{employee%2Did}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[EmployeeGetResponse]:
        """
        Returns the single employee record identified by `id`, used by ERP integrations to read TANSS-side employee master data (contact info, department, ERP number, etc.). Intended for ERP integrations — must be called with the dedicated API token bound to the role `ERP`, not a normal user login.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[EmployeeGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ......models.employee403_error import Employee403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Employee403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .employee_get_response import EmployeeGetResponse

        return await self.request_adapter.send_async(request_info, EmployeeGetResponse, error_mapping)
    
    async def put(self,body: EmployeePutRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[EmployeePutResponse]:
        """
        Updates the employee record identified by `id` with the supplied fields (e.g. department, ERP number, contact data). Used by ERP integrations to push employee master-data changes back into TANSS. Intended for ERP integrations — must be called with the dedicated API token bound to the role `ERP`, not a normal user login.
        param body: Request body.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[EmployeePutResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        from ......models.employee403_error import Employee403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Employee403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .employee_put_response import EmployeePutResponse

        return await self.request_adapter.send_async(request_info, EmployeePutResponse, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Returns the single employee record identified by `id`, used by ERP integrations to read TANSS-side employee master data (contact info, department, ERP number, etc.). Intended for ERP integrations — must be called with the dedicated API token bound to the role `ERP`, not a normal user login.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_put_request_information(self,body: EmployeePutRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Updates the employee record identified by `id` with the supplied fields (e.g. department, ERP number, contact data). Used by ERP integrations to push employee master-data changes back into TANSS. Intended for ERP integrations — must be called with the dedicated API token bound to the role `ERP`, not a normal user login.
        param body: Request body.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.PUT, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> EmployeeItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: EmployeeItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return EmployeeItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def departments(self) -> DepartmentsRequestBuilder:
        """
        The departments property
        """
        from .departments.departments_request_builder import DepartmentsRequestBuilder

        return DepartmentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class EmployeeItemRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class EmployeeItemRequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

