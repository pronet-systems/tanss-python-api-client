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
    from .....models.tns_remote_maintenance import TnsRemoteMaintenance
    from .....models.with_remote_support403_error import WithRemoteSupport403Error
    from .with_remote_support_get_response import WithRemoteSupportGetResponse
    from .with_remote_support_put_response import WithRemoteSupportPutResponse

class WithRemoteSupportItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/remoteSupports/v1/{remoteSupportId}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new WithRemoteSupportItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/remoteSupports/v1/{remoteSupportId}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Deletes a remote support by id. This can only be done for "external" remote support (type >= 1000)
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, None)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[WithRemoteSupportGetResponse]:
        """
        Gets a remote support from the database (based on the id)
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[WithRemoteSupportGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .....models.with_remote_support403_error import WithRemoteSupport403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": WithRemoteSupport403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .with_remote_support_get_response import WithRemoteSupportGetResponse

        return await self.request_adapter.send_async(request_info, WithRemoteSupportGetResponse, error_mapping)
    
    async def put(self,body: TnsRemoteMaintenance, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[WithRemoteSupportPutResponse]:
        """
        Updates a remote support by id and sets the new values
        param body: This object represents a remote support
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[WithRemoteSupportPutResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        from .....models.with_remote_support403_error import WithRemoteSupport403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": WithRemoteSupport403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .with_remote_support_put_response import WithRemoteSupportPutResponse

        return await self.request_adapter.send_async(request_info, WithRemoteSupportPutResponse, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Deletes a remote support by id. This can only be done for "external" remote support (type >= 1000)
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Gets a remote support from the database (based on the id)
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_put_request_information(self,body: TnsRemoteMaintenance, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Updates a remote support by id and sets the new values
        param body: This object represents a remote support
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
    
    def with_url(self,raw_url: str) -> WithRemoteSupportItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: WithRemoteSupportItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return WithRemoteSupportItemRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class WithRemoteSupportItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class WithRemoteSupportItemRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class WithRemoteSupportItemRequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

