from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.with_permission_package_item_request_builder import WithPermissionPackageItemRequestBuilder

class PermissionPackageRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/permissions/permissionPackage
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new PermissionPackageRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/permissions/permissionPackage", path_parameters)
    
    def by_permission_package_id(self,permission_package_id: int) -> WithPermissionPackageItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.v1.permissions.permissionPackage.item collection
        param permission_package_id: Id of the permission package to remove from the employee.
        Returns: WithPermissionPackageItemRequestBuilder
        """
        if permission_package_id is None:
            raise TypeError("permission_package_id cannot be null.")
        from .item.with_permission_package_item_request_builder import WithPermissionPackageItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["permissionPackageId"] = permission_package_id
        return WithPermissionPackageItemRequestBuilder(self.request_adapter, url_tpl_params)
    

