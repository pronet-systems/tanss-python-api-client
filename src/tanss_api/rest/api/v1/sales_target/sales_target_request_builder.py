from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .departments.departments_request_builder import DepartmentsRequestBuilder
    from .employees.employees_request_builder import EmployeesRequestBuilder
    from .get.get_request_builder import GetRequestBuilder
    from .set.set_request_builder import SetRequestBuilder

class SalesTargetRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/salesTarget
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new SalesTargetRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/salesTarget", path_parameters)
    
    @property
    def departments(self) -> DepartmentsRequestBuilder:
        """
        The departments property
        """
        from .departments.departments_request_builder import DepartmentsRequestBuilder

        return DepartmentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def employees(self) -> EmployeesRequestBuilder:
        """
        The employees property
        """
        from .employees.employees_request_builder import EmployeesRequestBuilder

        return EmployeesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_path(self) -> GetRequestBuilder:
        """
        The getPath property
        """
        from .get.get_request_builder import GetRequestBuilder

        return GetRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def set(self) -> SetRequestBuilder:
        """
        The set property
        """
        from .set.set_request_builder import SetRequestBuilder

        return SetRequestBuilder(self.request_adapter, self.path_parameters)
    

