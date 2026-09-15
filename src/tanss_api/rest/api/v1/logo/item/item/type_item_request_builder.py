from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from kiota_abstractions.default_query_parameters import QueryParameters
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.multipart_body import MultipartBody
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Optional, TYPE_CHECKING, Union
from warnings import warn

if TYPE_CHECKING:
    from ......models.type403_error import Type403Error
    from .type_get_response import TypeGetResponse
    from .type_post_response import TypePostResponse

class TypeItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/logo/{type}/{id}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new TypeItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/logo/{type}/{id}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[TypeGetResponse]:
        """
        Returns the avatar (logo image) stored for the entity (`type`, `id`) pair — e.g. an employee avatar, acompany logo, etc. The required permissions depend on the logo type.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[TypeGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ......models.type403_error import Type403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Type403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .type_get_response import TypeGetResponse

        return await self.request_adapter.send_async(request_info, TypeGetResponse, error_mapping)
    
    async def post(self,body: MultipartBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[TypePostResponse]:
        """
        Uploads an avatar (logo image) for the (`type`, `id`) pair. The image is sent as a multipart `logo` formfield. Files larger than 2&nbsp;MB are rejected, and only JPG/PNG/GIF MIME types are accepted (othertypes yield `FILE_WRONG_MIME_TYPE`).Permission to upload is enforced per type(e.g. an employee can upload their own avatar; a company logo requires company-admin permission).
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[TypePostResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ......models.type403_error import Type403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Type403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .type_post_response import TypePostResponse

        return await self.request_adapter.send_async(request_info, TypePostResponse, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Returns the avatar (logo image) stored for the entity (`type`, `id`) pair — e.g. an employee avatar, acompany logo, etc. The required permissions depend on the logo type.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: MultipartBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Uploads an avatar (logo image) for the (`type`, `id`) pair. The image is sent as a multipart `logo` formfield. Files larger than 2&nbsp;MB are rejected, and only JPG/PNG/GIF MIME types are accepted (othertypes yield `FILE_WRONG_MIME_TYPE`).Permission to upload is enforced per type(e.g. an employee can upload their own avatar; a company logo requires company-admin permission).
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.POST, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "multipart/form-data", body)
        return request_info
    
    def with_url(self,raw_url: str) -> TypeItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: TypeItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return TypeItemRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class TypeItemRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class TypeItemRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

