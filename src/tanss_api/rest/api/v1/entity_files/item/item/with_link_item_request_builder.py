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
    from ......models.with_link403_error import WithLink403Error
    from .with_link_get_response import WithLinkGetResponse
    from .with_link_post_response import WithLinkPostResponse

class WithLinkItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/entityFiles/{-id}/{linkId}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new WithLinkItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/entityFiles/{%2Did}/{linkId}{?file*}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[WithLinkGetResponse]:
        """
        Returns object for the entity identified by `linkType` + `linkId` — i.e. all uploaded documents plus UI hints (`showIcon`, `mayUpload`, per-document `mayDelete` and resolved file size). If the caller has no access to the link type, an empty container with `showIcon=false` is returned instead of an error. Used by ticket/company/asset views to render the paperclip icon and the documents pop-out.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[WithLinkGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ......models.with_link403_error import WithLink403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": WithLink403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .with_link_get_response import WithLinkGetResponse

        return await self.request_adapter.send_async(request_info, WithLinkGetResponse, error_mapping)
    
    async def post(self,request_configuration: Optional[RequestConfiguration[WithLinkItemRequestBuilderPostQueryParameters]] = None) -> Optional[WithLinkPostResponse]:
        """
        Uploads a file (multipart `file`) or several files (multipart `files`) and attaches each to the entity identified by `linkType` + `linkId`. Single uploads return one object, multi-uploads return the list. Returns `BAD_REQUEST` when neither field is set. The service generates a unique stored filename on disk and applies upload permission checks per link type.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[WithLinkPostResponse]
        """
        request_info = self.to_post_request_information(
            request_configuration
        )
        from ......models.with_link403_error import WithLink403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": WithLink403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .with_link_post_response import WithLinkPostResponse

        return await self.request_adapter.send_async(request_info, WithLinkPostResponse, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Returns object for the entity identified by `linkType` + `linkId` — i.e. all uploaded documents plus UI hints (`showIcon`, `mayUpload`, per-document `mayDelete` and resolved file size). If the caller has no access to the link type, an empty container with `showIcon=false` is returned instead of an error. Used by ticket/company/asset views to render the paperclip icon and the documents pop-out.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,request_configuration: Optional[RequestConfiguration[WithLinkItemRequestBuilderPostQueryParameters]] = None) -> RequestInformation:
        """
        Uploads a file (multipart `file`) or several files (multipart `files`) and attaches each to the entity identified by `linkType` + `linkId`. Single uploads return one object, multi-uploads return the list. Returns `BAD_REQUEST` when neither field is set. The service generates a unique stored filename on disk and applies upload permission checks per link type.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.POST, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> WithLinkItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: WithLinkItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return WithLinkItemRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class WithLinkItemRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class WithLinkItemRequestBuilderPostQueryParameters():
        """
        Uploads a file (multipart `file`) or several files (multipart `files`) and attaches each to the entity identified by `linkType` + `linkId`. Single uploads return one object, multi-uploads return the list. Returns `BAD_REQUEST` when neither field is set. The service generates a unique stored filename on disk and applies upload permission checks per link type.
        """
        # Optional single file payload reference for the upload.
        file: Optional[str] = None

    
    @dataclass
    class WithLinkItemRequestBuilderPostRequestConfiguration(RequestConfiguration[WithLinkItemRequestBuilderPostQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

