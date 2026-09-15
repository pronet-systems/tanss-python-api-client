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
    from ....models.tns_remote_maintenance import TnsRemoteMaintenance
    from ....models.tns_remote_maintenance_configuration import TnsRemoteMaintenanceConfiguration
    from ....models.v1403_error import V1403Error
    from .assign_device.assign_device_request_builder import AssignDeviceRequestBuilder
    from .assign_employee.assign_employee_request_builder import AssignEmployeeRequestBuilder
    from .item.with_remote_support_item_request_builder import WithRemoteSupportItemRequestBuilder
    from .v1_post_response import V1PostResponse
    from .v1_put_response import V1PutResponse

class V1RequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/remoteSupports/v1
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new V1RequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/remoteSupports/v1", path_parameters)
    
    def by_remote_support_id(self,remote_support_id: int) -> WithRemoteSupportItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.remoteSupports.v1.item collection
        param remote_support_id: Id of the remote support to be fetched
        Returns: WithRemoteSupportItemRequestBuilder
        """
        if remote_support_id is None:
            raise TypeError("remote_support_id cannot be null.")
        from .item.with_remote_support_item_request_builder import WithRemoteSupportItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["remoteSupportId"] = remote_support_id
        return WithRemoteSupportItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def post(self,body: TnsRemoteMaintenance, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[V1PostResponse]:
        """
        Stores/imports a remote support of an external system into the TANSS database.* if `userId` is given, the api can try to "translate" it to a TANSS employee (use route `/api/remoteSupports/v1/assignEmployee` to set the matchings)* if `deviceId` is given, the api can try to "translate" it into a TANSS company and assignment (use route `/api/remoteSupports/v1/assignDevice` to set the matchings)
        param body: This object represents a remote support
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[V1PostResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ....models.v1403_error import V1403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": V1403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .v1_post_response import V1PostResponse

        return await self.request_adapter.send_async(request_info, V1PostResponse, error_mapping)
    
    async def put(self,body: TnsRemoteMaintenanceConfiguration, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[V1PutResponse]:
        """
        Gets a list of remote supports calls based on misc. filter settings
        param body: This object is used to get remote supports based on filter settings
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[V1PutResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        from ....models.v1403_error import V1403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": V1403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .v1_put_response import V1PutResponse

        return await self.request_adapter.send_async(request_info, V1PutResponse, error_mapping)
    
    def to_post_request_information(self,body: TnsRemoteMaintenance, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Stores/imports a remote support of an external system into the TANSS database.* if `userId` is given, the api can try to "translate" it to a TANSS employee (use route `/api/remoteSupports/v1/assignEmployee` to set the matchings)* if `deviceId` is given, the api can try to "translate" it into a TANSS company and assignment (use route `/api/remoteSupports/v1/assignDevice` to set the matchings)
        param body: This object represents a remote support
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
    
    def to_put_request_information(self,body: TnsRemoteMaintenanceConfiguration, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Gets a list of remote supports calls based on misc. filter settings
        param body: This object is used to get remote supports based on filter settings
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.PUT, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> V1RequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: V1RequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return V1RequestBuilder(self.request_adapter, raw_url)
    
    @property
    def assign_device(self) -> AssignDeviceRequestBuilder:
        """
        The assignDevice property
        """
        from .assign_device.assign_device_request_builder import AssignDeviceRequestBuilder

        return AssignDeviceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def assign_employee(self) -> AssignEmployeeRequestBuilder:
        """
        The assignEmployee property
        """
        from .assign_employee.assign_employee_request_builder import AssignEmployeeRequestBuilder

        return AssignEmployeeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class V1RequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class V1RequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

