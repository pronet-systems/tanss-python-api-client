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
    from .....models.employees403_error import Employees403Error
    from .employees_post_request_body import EmployeesPostRequestBody
    from .employees_post_response import EmployeesPostResponse
    from .item.employee_item_request_builder import EmployeeItemRequestBuilder

class EmployeesRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/erp/v1/employees
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new EmployeesRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/erp/v1/employees", path_parameters)
    
    def by_employee_id(self,employee_id: int) -> EmployeeItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.erp.v1.employees.item collection
        param employee_id: ID of the employee to retrieve.
        Returns: EmployeeItemRequestBuilder
        """
        if employee_id is None:
            raise TypeError("employee_id cannot be null.")
        from .item.employee_item_request_builder import EmployeeItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["employee%2Did"] = employee_id
        return EmployeeItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def post(self,body: EmployeesPostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[EmployeesPostResponse]:
        """
        Creates a new employee record in TANSS from the supplied payload, so an ERP system can push new staff/customer contacts into TANSS. Intended for ERP integrations — must be called with the dedicated API token bound to the role `ERP`, not a normal user login.
        param body: Request body.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[EmployeesPostResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from .....models.employees403_error import Employees403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Employees403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .employees_post_response import EmployeesPostResponse

        return await self.request_adapter.send_async(request_info, EmployeesPostResponse, error_mapping)
    
    def to_post_request_information(self,body: EmployeesPostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Creates a new employee record in TANSS from the supplied payload, so an ERP system can push new staff/customer contacts into TANSS. Intended for ERP integrations — must be called with the dedicated API token bound to the role `ERP`, not a normal user login.
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
    
    def with_url(self,raw_url: str) -> EmployeesRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: EmployeesRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return EmployeesRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class EmployeesRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

