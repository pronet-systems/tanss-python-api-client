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
    from .....models.employee_assignment403_error import EmployeeAssignment403Error
    from .....models.tns_phone_employee import TnsPhoneEmployee
    from .employee_assignment_get_response import EmployeeAssignmentGetResponse
    from .employee_assignment_post_response import EmployeeAssignmentPostResponse

class EmployeeAssignmentRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/calls/v1/employeeAssignment
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new EmployeeAssignmentRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/calls/v1/employeeAssignment", path_parameters)
    
    async def delete(self,body: TnsPhoneEmployee, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Deletes an assignment between an "idString" and a TANSS employee id from the database
        param body: Refers to an assignment between an identifier string (TnsPhoneParticipant.idString) and a TANSS employee id
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_delete_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, None)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[EmployeeAssignmentGetResponse]:
        """
        Get all assignments between idStrings and TANSS employees
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[EmployeeAssignmentGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .....models.employee_assignment403_error import EmployeeAssignment403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": EmployeeAssignment403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .employee_assignment_get_response import EmployeeAssignmentGetResponse

        return await self.request_adapter.send_async(request_info, EmployeeAssignmentGetResponse, error_mapping)
    
    async def post(self,body: TnsPhoneEmployee, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[EmployeeAssignmentPostResponse]:
        """
        Create a new assignment between an "idString" and a TANSS employee id
        param body: Refers to an assignment between an identifier string (TnsPhoneParticipant.idString) and a TANSS employee id
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[EmployeeAssignmentPostResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from .....models.employee_assignment403_error import EmployeeAssignment403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": EmployeeAssignment403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .employee_assignment_post_response import EmployeeAssignmentPostResponse

        return await self.request_adapter.send_async(request_info, EmployeeAssignmentPostResponse, error_mapping)
    
    def to_delete_request_information(self,body: TnsPhoneEmployee, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Deletes an assignment between an "idString" and a TANSS employee id from the database
        param body: Refers to an assignment between an identifier string (TnsPhoneParticipant.idString) and a TANSS employee id
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Get all assignments between idStrings and TANSS employees
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: TnsPhoneEmployee, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Create a new assignment between an "idString" and a TANSS employee id
        param body: Refers to an assignment between an identifier string (TnsPhoneParticipant.idString) and a TANSS employee id
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
    
    def with_url(self,raw_url: str) -> EmployeeAssignmentRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: EmployeeAssignmentRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return EmployeeAssignmentRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class EmployeeAssignmentRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class EmployeeAssignmentRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class EmployeeAssignmentRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

