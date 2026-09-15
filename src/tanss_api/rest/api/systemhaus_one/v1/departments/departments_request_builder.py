from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.with_department_item_request_builder import WithDepartmentItemRequestBuilder

class DepartmentsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/systemhaus_one/v1/departments
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new DepartmentsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/systemhaus_one/v1/departments", path_parameters)
    
    def by_department_id(self,department_id: int) -> WithDepartmentItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.systemhaus_one.v1.departments.item collection
        param department_id: ID der Abteilung.
        Returns: WithDepartmentItemRequestBuilder
        """
        if department_id is None:
            raise TypeError("department_id cannot be null.")
        from .item.with_department_item_request_builder import WithDepartmentItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["departmentId"] = department_id
        return WithDepartmentItemRequestBuilder(self.request_adapter, url_tpl_params)
    

