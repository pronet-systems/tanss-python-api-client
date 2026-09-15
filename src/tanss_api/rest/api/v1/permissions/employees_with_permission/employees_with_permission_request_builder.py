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
    from .....models.employees_with_permission403_error import EmployeesWithPermission403Error
    from .employees_with_permission_get_response import EmployeesWithPermissionGetResponse

class EmployeesWithPermissionRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/permissions/employeesWithPermission
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new EmployeesWithPermissionRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/permissions/employeesWithPermission?companyId={companyId}&permissionId={permissionId}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[EmployeesWithPermissionRequestBuilderGetQueryParameters]] = None) -> Optional[EmployeesWithPermissionGetResponse]:
        """
        Returns, for the given `companyId`, every employee whose status (`HAS_PERMISSION`,`INHERITED`, `NONE`, ...) is computed from whether they actually have thegiven `permissionId` assigned. The caller must be from the own company andhold both `MANAGE_PERMISSIONS` and `EMPLOYEE_ADMINISTRATION`.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[EmployeesWithPermissionGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .....models.employees_with_permission403_error import EmployeesWithPermission403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": EmployeesWithPermission403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .employees_with_permission_get_response import EmployeesWithPermissionGetResponse

        return await self.request_adapter.send_async(request_info, EmployeesWithPermissionGetResponse, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[EmployeesWithPermissionRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Returns, for the given `companyId`, every employee whose status (`HAS_PERMISSION`,`INHERITED`, `NONE`, ...) is computed from whether they actually have thegiven `permissionId` assigned. The caller must be from the own company andhold both `MANAGE_PERMISSIONS` and `EMPLOYEE_ADMINISTRATION`.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> EmployeesWithPermissionRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: EmployeesWithPermissionRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return EmployeesWithPermissionRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class EmployeesWithPermissionRequestBuilderGetQueryParameters():
        """
        Returns, for the given `companyId`, every employee whose status (`HAS_PERMISSION`,`INHERITED`, `NONE`, ...) is computed from whether they actually have thegiven `permissionId` assigned. The caller must be from the own company andhold both `MANAGE_PERMISSIONS` and `EMPLOYEE_ADMINISTRATION`.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "company_id":
                return "companyId"
            if original_name == "permission_id":
                return "permissionId"
            return original_name
        
        # Id of the company whose employees should be evaluated.
        company_id: Optional[int] = None

        # Id of the permission to check against.
        permission_id: Optional[int] = None

    
    @dataclass
    class EmployeesWithPermissionRequestBuilderGetRequestConfiguration(RequestConfiguration[EmployeesWithPermissionRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

