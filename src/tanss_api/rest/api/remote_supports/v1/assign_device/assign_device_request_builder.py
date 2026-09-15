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
    from .....models.assign_device403_error import AssignDevice403Error
    from .....models.tns_remote_maintenance_device_assignment import TnsRemoteMaintenanceDeviceAssignment
    from .....models.tns_remote_maintenance_device_assignment_id import TnsRemoteMaintenanceDeviceAssignmentId
    from .assign_device_get_response import AssignDeviceGetResponse
    from .assign_device_post_response import AssignDevicePostResponse

class AssignDeviceRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/remoteSupports/v1/assignDevice
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new AssignDeviceRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/remoteSupports/v1/assignDevice", path_parameters)
    
    async def delete(self,body: TnsRemoteMaintenanceDeviceAssignmentId, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        This call deletes an entry in a "translation table" that allows identification of a remote support to a company / assignmentbased of the `deviceId`
        param body: Identifies a "translation" of a deviceId based on a remote support "type" to a TANSS company.
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
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[AssignDeviceGetResponse]:
        """
        This call gets all device assignments of the given remote support "type". A list is returned containing all informationhow to match a `deviceId` for the given remote support type to a TANSS company / assignment.The "type" is fix and is stored in the used Api token.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[AssignDeviceGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .....models.assign_device403_error import AssignDevice403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": AssignDevice403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .assign_device_get_response import AssignDeviceGetResponse

        return await self.request_adapter.send_async(request_info, AssignDeviceGetResponse, error_mapping)
    
    async def post(self,body: TnsRemoteMaintenanceDeviceAssignment, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[AssignDevicePostResponse]:
        """
        This call creates an entry in a "translation table" that allows identification of a remote support to a company / assignmentbased of the `deviceId`
        param body: Object containing the "translation" of a deviceId based on a remote support "type" to a TANSS company. Optionally,a linkTypeId / linkId (assignment) can be given as well, so the system knows exactly to which device the deviceId refers.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[AssignDevicePostResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from .....models.assign_device403_error import AssignDevice403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": AssignDevice403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .assign_device_post_response import AssignDevicePostResponse

        return await self.request_adapter.send_async(request_info, AssignDevicePostResponse, error_mapping)
    
    def to_delete_request_information(self,body: TnsRemoteMaintenanceDeviceAssignmentId, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        This call deletes an entry in a "translation table" that allows identification of a remote support to a company / assignmentbased of the `deviceId`
        param body: Identifies a "translation" of a deviceId based on a remote support "type" to a TANSS company.
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
        This call gets all device assignments of the given remote support "type". A list is returned containing all informationhow to match a `deviceId` for the given remote support type to a TANSS company / assignment.The "type" is fix and is stored in the used Api token.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: TnsRemoteMaintenanceDeviceAssignment, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        This call creates an entry in a "translation table" that allows identification of a remote support to a company / assignmentbased of the `deviceId`
        param body: Object containing the "translation" of a deviceId based on a remote support "type" to a TANSS company. Optionally,a linkTypeId / linkId (assignment) can be given as well, so the system knows exactly to which device the deviceId refers.
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
    
    def with_url(self,raw_url: str) -> AssignDeviceRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: AssignDeviceRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return AssignDeviceRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class AssignDeviceRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class AssignDeviceRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class AssignDeviceRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

