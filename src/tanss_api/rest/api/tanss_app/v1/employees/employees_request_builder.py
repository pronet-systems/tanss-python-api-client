from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.with_employee_item_request_builder import WithEmployeeItemRequestBuilder

class EmployeesRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/tanss.app/v1/employees
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new EmployeesRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/tanss.app/v1/employees", path_parameters)
    
    def by_employee_id(self,employee_id: int) -> WithEmployeeItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.tanssApp.v1.employees.item collection
        param employee_id: Id des Mitarbeiters
        Returns: WithEmployeeItemRequestBuilder
        """
        if employee_id is None:
            raise TypeError("employee_id cannot be null.")
        from .item.with_employee_item_request_builder import WithEmployeeItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["employeeId"] = employee_id
        return WithEmployeeItemRequestBuilder(self.request_adapter, url_tpl_params)
    

