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
    from .....models.with_permission403_error import WithPermission403Error
    from .with_permission_put_response import WithPermissionPutResponse

class WithPermissionItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/permissions/{permissionId}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new WithPermissionItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/permissions/{permissionId}?employeeIds={employeeIds}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[WithPermissionItemRequestBuilderDeleteQueryParameters]] = None) -> None:
        """
        Revokes the given `permissionId` from each employee in the comma-separated`employeeIds` query parameter. Caller must be from the own company and hold`MANAGE_PERMISSIONS` + `EMPLOYEE_ADMINISTRATION`.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from .....models.with_permission403_error import WithPermission403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": WithPermission403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def put(self,request_configuration: Optional[RequestConfiguration[WithPermissionItemRequestBuilderPutQueryParameters]] = None) -> Optional[WithPermissionPutResponse]:
        """
        Grants the given `permissionId` to each employee in the comma-separated`employeeIds` query parameter. Caller must be from the own company and hold`MANAGE_PERMISSIONS` + `EMPLOYEE_ADMINISTRATION`.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[WithPermissionPutResponse]
        """
        request_info = self.to_put_request_information(
            request_configuration
        )
        from .....models.with_permission403_error import WithPermission403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": WithPermission403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .with_permission_put_response import WithPermissionPutResponse

        return await self.request_adapter.send_async(request_info, WithPermissionPutResponse, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[WithPermissionItemRequestBuilderDeleteQueryParameters]] = None) -> RequestInformation:
        """
        Revokes the given `permissionId` from each employee in the comma-separated`employeeIds` query parameter. Caller must be from the own company and hold`MANAGE_PERMISSIONS` + `EMPLOYEE_ADMINISTRATION`.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_put_request_information(self,request_configuration: Optional[RequestConfiguration[WithPermissionItemRequestBuilderPutQueryParameters]] = None) -> RequestInformation:
        """
        Grants the given `permissionId` to each employee in the comma-separated`employeeIds` query parameter. Caller must be from the own company and hold`MANAGE_PERMISSIONS` + `EMPLOYEE_ADMINISTRATION`.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.PUT, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> WithPermissionItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: WithPermissionItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return WithPermissionItemRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class WithPermissionItemRequestBuilderDeleteQueryParameters():
        """
        Revokes the given `permissionId` from each employee in the comma-separated`employeeIds` query parameter. Caller must be from the own company and hold`MANAGE_PERMISSIONS` + `EMPLOYEE_ADMINISTRATION`.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "employee_ids":
                return "employeeIds"
            return original_name
        
        # Comma-separated list of employee ids to revoke the permission from.
        employee_ids: Optional[str] = None

    
    @dataclass
    class WithPermissionItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[WithPermissionItemRequestBuilderDeleteQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class WithPermissionItemRequestBuilderPutQueryParameters():
        """
        Grants the given `permissionId` to each employee in the comma-separated`employeeIds` query parameter. Caller must be from the own company and hold`MANAGE_PERMISSIONS` + `EMPLOYEE_ADMINISTRATION`.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "employee_ids":
                return "employeeIds"
            return original_name
        
        # Comma-separated list of employee ids to grant the permission to.
        employee_ids: Optional[str] = None

    
    @dataclass
    class WithPermissionItemRequestBuilderPutRequestConfiguration(RequestConfiguration[WithPermissionItemRequestBuilderPutQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

