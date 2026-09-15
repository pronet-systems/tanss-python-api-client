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
    from .....models.permission_packages403_error import PermissionPackages403Error
    from .item.with_package_item_request_builder import WithPackageItemRequestBuilder
    from .permission_packages_get_response import PermissionPackagesGetResponse
    from .permission_packages_post_request_body import PermissionPackagesPostRequestBody
    from .permission_packages_post_response import PermissionPackagesPostResponse
    from .permission_packages_put_response import PermissionPackagesPutResponse

class PermissionPackagesRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/admin/permissionPackages
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new PermissionPackagesRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/admin/permissionPackages{?withPermissions*}", path_parameters)
    
    def by_package_id(self,package_id: int) -> WithPackageItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.v1.admin.permissionPackages.item collection
        param package_id: Id of the permission package to delete.
        Returns: WithPackageItemRequestBuilder
        """
        if package_id is None:
            raise TypeError("package_id cannot be null.")
        from .item.with_package_item_request_builder import WithPackageItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["packageId"] = package_id
        return WithPackageItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[PermissionPackagesRequestBuilderGetQueryParameters]] = None) -> Optional[PermissionPackagesGetResponse]:
        """
        Returns all permission packages, sorted by name. When `withPermissions=true`each package also carries its categories and contained permissions. Callermust be from the own company and hold `MANAGE_PERMISSION_PACKAGES`.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[PermissionPackagesGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .....models.permission_packages403_error import PermissionPackages403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": PermissionPackages403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .permission_packages_get_response import PermissionPackagesGetResponse

        return await self.request_adapter.send_async(request_info, PermissionPackagesGetResponse, error_mapping)
    
    async def post(self,body: PermissionPackagesPostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[PermissionPackagesPostResponse]:
        """
        Creates a new permission package. Caller must be from the own company andhold `MANAGE_PERMISSION_PACKAGES`.
        param body: Request body.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[PermissionPackagesPostResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from .....models.permission_packages403_error import PermissionPackages403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": PermissionPackages403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .permission_packages_post_response import PermissionPackagesPostResponse

        return await self.request_adapter.send_async(request_info, PermissionPackagesPostResponse, error_mapping)
    
    async def put(self,request_configuration: Optional[RequestConfiguration[PermissionPackagesRequestBuilderPutQueryParameters]] = None) -> Optional[PermissionPackagesPutResponse]:
        """
        Toggles each `permissionId` in the comma-separated list inside the given`packageId`: permissions currently in the package are removed, those notin it are added. Caller must be from the own company and hold`MANAGE_PERMISSION_PACKAGES`.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[PermissionPackagesPutResponse]
        """
        request_info = self.to_put_request_information(
            request_configuration
        )
        from .....models.permission_packages403_error import PermissionPackages403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": PermissionPackages403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .permission_packages_put_response import PermissionPackagesPutResponse

        return await self.request_adapter.send_async(request_info, PermissionPackagesPutResponse, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[PermissionPackagesRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Returns all permission packages, sorted by name. When `withPermissions=true`each package also carries its categories and contained permissions. Callermust be from the own company and hold `MANAGE_PERMISSION_PACKAGES`.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: PermissionPackagesPostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Creates a new permission package. Caller must be from the own company andhold `MANAGE_PERMISSION_PACKAGES`.
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
    
    def to_put_request_information(self,request_configuration: Optional[RequestConfiguration[PermissionPackagesRequestBuilderPutQueryParameters]] = None) -> RequestInformation:
        """
        Toggles each `permissionId` in the comma-separated list inside the given`packageId`: permissions currently in the package are removed, those notin it are added. Caller must be from the own company and hold`MANAGE_PERMISSION_PACKAGES`.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.PUT, '{+baseurl}/api/v1/admin/permissionPackages?packageId={packageId}&permissionIds={permissionIds}', self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> PermissionPackagesRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: PermissionPackagesRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return PermissionPackagesRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class PermissionPackagesRequestBuilderGetQueryParameters():
        """
        Returns all permission packages, sorted by name. When `withPermissions=true`each package also carries its categories and contained permissions. Callermust be from the own company and hold `MANAGE_PERMISSION_PACKAGES`.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "with_permissions":
                return "withPermissions"
            return original_name
        
        # When true, each package also includes its categories and contained permissions.
        with_permissions: Optional[bool] = None

    
    @dataclass
    class PermissionPackagesRequestBuilderGetRequestConfiguration(RequestConfiguration[PermissionPackagesRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class PermissionPackagesRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class PermissionPackagesRequestBuilderPutQueryParameters():
        """
        Toggles each `permissionId` in the comma-separated list inside the given`packageId`: permissions currently in the package are removed, those notin it are added. Caller must be from the own company and hold`MANAGE_PERMISSION_PACKAGES`.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "package_id":
                return "packageId"
            if original_name == "permission_ids":
                return "permissionIds"
            return original_name
        
        # Id of the permission package whose permissions should be toggled.
        package_id: Optional[int] = None

        # Comma-separated list of permission ids to toggle within the package.
        permission_ids: Optional[str] = None

    
    @dataclass
    class PermissionPackagesRequestBuilderPutRequestConfiguration(RequestConfiguration[PermissionPackagesRequestBuilderPutQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

