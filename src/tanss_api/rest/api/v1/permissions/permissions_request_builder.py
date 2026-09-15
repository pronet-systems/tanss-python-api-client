from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .employee.employee_request_builder import EmployeeRequestBuilder
    from .employees_with_permission.employees_with_permission_request_builder import EmployeesWithPermissionRequestBuilder
    from .item.with_permission_item_request_builder import WithPermissionItemRequestBuilder
    from .packages.packages_request_builder import PackagesRequestBuilder
    from .permission_package.permission_package_request_builder import PermissionPackageRequestBuilder
    from .remove_all_from.remove_all_from_request_builder import RemoveAllFromRequestBuilder
    from .set_all_for.set_all_for_request_builder import SetAllForRequestBuilder
    from .type.type_request_builder import TypeRequestBuilder

class PermissionsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/permissions
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new PermissionsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/permissions", path_parameters)
    
    def by_permission_id(self,permission_id: int) -> WithPermissionItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.v1.permissions.item collection
        param permission_id: Id of the permission to revoke.
        Returns: WithPermissionItemRequestBuilder
        """
        if permission_id is None:
            raise TypeError("permission_id cannot be null.")
        from .item.with_permission_item_request_builder import WithPermissionItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["permissionId"] = permission_id
        return WithPermissionItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    @property
    def employee(self) -> EmployeeRequestBuilder:
        """
        The employee property
        """
        from .employee.employee_request_builder import EmployeeRequestBuilder

        return EmployeeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def employees_with_permission(self) -> EmployeesWithPermissionRequestBuilder:
        """
        The employeesWithPermission property
        """
        from .employees_with_permission.employees_with_permission_request_builder import EmployeesWithPermissionRequestBuilder

        return EmployeesWithPermissionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def packages(self) -> PackagesRequestBuilder:
        """
        The packages property
        """
        from .packages.packages_request_builder import PackagesRequestBuilder

        return PackagesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def permission_package(self) -> PermissionPackageRequestBuilder:
        """
        The permissionPackage property
        """
        from .permission_package.permission_package_request_builder import PermissionPackageRequestBuilder

        return PermissionPackageRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def remove_all_from(self) -> RemoveAllFromRequestBuilder:
        """
        The removeAllFrom property
        """
        from .remove_all_from.remove_all_from_request_builder import RemoveAllFromRequestBuilder

        return RemoveAllFromRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def set_all_for(self) -> SetAllForRequestBuilder:
        """
        The setAllFor property
        """
        from .set_all_for.set_all_for_request_builder import SetAllForRequestBuilder

        return SetAllForRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def type(self) -> TypeRequestBuilder:
        """
        The type property
        """
        from .type.type_request_builder import TypeRequestBuilder

        return TypeRequestBuilder(self.request_adapter, self.path_parameters)
    

