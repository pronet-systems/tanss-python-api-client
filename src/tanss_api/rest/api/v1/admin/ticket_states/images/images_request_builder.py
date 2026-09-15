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
    from ......models.images403_error import Images403Error
    from .images_get_response import ImagesGetResponse
    from .images_post_response import ImagesPostResponse

class ImagesRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/admin/ticketStates/images
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new ImagesRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/admin/ticketStates/images", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[ImagesRequestBuilderDeleteQueryParameters]] = None) -> None:
        """
        Deletes an uploaded ticket-state icon by file name. Requires admin permissionon the ticket-state-image aspect.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ......models.images403_error import Images403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Images403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[ImagesGetResponse]:
        """
        Returns the list of uploaded ticket-state icon file names available for use onticket states. Requires admin permission on the ticket-state-image aspect.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ImagesGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ......models.images403_error import Images403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Images403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .images_get_response import ImagesGetResponse

        return await self.request_adapter.send_async(request_info, ImagesGetResponse, error_mapping)
    
    async def post(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[ImagesPostResponse]:
        """
        Uploads one or more icon images (multipart `files` field) for use on ticketstates. Returns the stored file names. Requires admin permission on theticket-state-image aspect.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ImagesPostResponse]
        """
        request_info = self.to_post_request_information(
            request_configuration
        )
        from ......models.images403_error import Images403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Images403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .images_post_response import ImagesPostResponse

        return await self.request_adapter.send_async(request_info, ImagesPostResponse, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[ImagesRequestBuilderDeleteQueryParameters]] = None) -> RequestInformation:
        """
        Deletes an uploaded ticket-state icon by file name. Requires admin permissionon the ticket-state-image aspect.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, '{+baseurl}/api/v1/admin/ticketStates/images?imageName={imageName}', self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Returns the list of uploaded ticket-state icon file names available for use onticket states. Requires admin permission on the ticket-state-image aspect.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Uploads one or more icon images (multipart `files` field) for use on ticketstates. Returns the stored file names. Requires admin permission on theticket-state-image aspect.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.POST, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> ImagesRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: ImagesRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return ImagesRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class ImagesRequestBuilderDeleteQueryParameters():
        """
        Deletes an uploaded ticket-state icon by file name. Requires admin permissionon the ticket-state-image aspect.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "image_name":
                return "imageName"
            return original_name
        
        # File name of the ticket-state icon to delete.
        image_name: Optional[str] = None

    
    @dataclass
    class ImagesRequestBuilderDeleteRequestConfiguration(RequestConfiguration[ImagesRequestBuilderDeleteQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class ImagesRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class ImagesRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

