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
    from ....models.files_and_links_media403_error import FilesAndLinksMedia403Error
    from .files_and_links_media_post_response import FilesAndLinksMediaPostResponse
    from .files_and_links_media_put_request_body import FilesAndLinksMediaPutRequestBody
    from .files_and_links_media_put_response import FilesAndLinksMediaPutResponse
    from .item.files_and_links_media_item_request_builder import FilesAndLinksMediaItemRequestBuilder

class FilesAndLinksMediaRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/filesAndLinksMedia
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new FilesAndLinksMediaRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/filesAndLinksMedia", path_parameters)
    
    def by_id(self,id: int) -> FilesAndLinksMediaItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.v1.filesAndLinksMedia.item collection
        param id: Id of the files-and-links entry.
        Returns: FilesAndLinksMediaItemRequestBuilder
        """
        if id is None:
            raise TypeError("id cannot be null.")
        from .item.files_and_links_media_item_request_builder import FilesAndLinksMediaItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["id"] = id
        return FilesAndLinksMediaItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def post(self,request_configuration: Optional[RequestConfiguration[FilesAndLinksMediaRequestBuilderPostQueryParameters]] = None) -> Optional[FilesAndLinksMediaPostResponse]:
        """
        Uploads a binary file as a multipart attachment under an existing files-and-links node (`assignedId`). Requires the knowledge base v2 feature, FILES_LINKS_ACTIVATED config, and the MANAGE_FILE_IMPORTANT_LINKS permission. The server stores the original filename, mime type and a generated UUID/filename for retrieval.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[FilesAndLinksMediaPostResponse]
        """
        request_info = self.to_post_request_information(
            request_configuration
        )
        from ....models.files_and_links_media403_error import FilesAndLinksMedia403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": FilesAndLinksMedia403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .files_and_links_media_post_response import FilesAndLinksMediaPostResponse

        return await self.request_adapter.send_async(request_info, FilesAndLinksMediaPostResponse, error_mapping)
    
    async def put(self,body: FilesAndLinksMediaPutRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[FilesAndLinksMediaPutResponse]:
        """
        Returns all media attachments for the supplied list configuration (typically filtered by `assignedId`). Each entry carries its stored filename, mime type and upload metadata.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[FilesAndLinksMediaPutResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        from ....models.files_and_links_media403_error import FilesAndLinksMedia403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": FilesAndLinksMedia403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .files_and_links_media_put_response import FilesAndLinksMediaPutResponse

        return await self.request_adapter.send_async(request_info, FilesAndLinksMediaPutResponse, error_mapping)
    
    def to_post_request_information(self,request_configuration: Optional[RequestConfiguration[FilesAndLinksMediaRequestBuilderPostQueryParameters]] = None) -> RequestInformation:
        """
        Uploads a binary file as a multipart attachment under an existing files-and-links node (`assignedId`). Requires the knowledge base v2 feature, FILES_LINKS_ACTIVATED config, and the MANAGE_FILE_IMPORTANT_LINKS permission. The server stores the original filename, mime type and a generated UUID/filename for retrieval.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.POST, '{+baseurl}/api/v1/filesAndLinksMedia?assignedId={assignedId}&file={file}&title={title}', self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_put_request_information(self,body: FilesAndLinksMediaPutRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Returns all media attachments for the supplied list configuration (typically filtered by `assignedId`). Each entry carries its stored filename, mime type and upload metadata.
        param body: The request body
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
    
    def with_url(self,raw_url: str) -> FilesAndLinksMediaRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: FilesAndLinksMediaRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return FilesAndLinksMediaRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class FilesAndLinksMediaRequestBuilderPostQueryParameters():
        """
        Uploads a binary file as a multipart attachment under an existing files-and-links node (`assignedId`). Requires the knowledge base v2 feature, FILES_LINKS_ACTIVATED config, and the MANAGE_FILE_IMPORTANT_LINKS permission. The server stores the original filename, mime type and a generated UUID/filename for retrieval.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "assigned_id":
                return "assignedId"
            if original_name == "file":
                return "file"
            if original_name == "title":
                return "title"
            return original_name
        
        # ID of the files-and-links node the attachment belongs to.
        assigned_id: Optional[int] = None

        # Binary file payload reference for the upload.
        file: Optional[str] = None

        # Display title for the uploaded attachment.
        title: Optional[str] = None

    
    @dataclass
    class FilesAndLinksMediaRequestBuilderPostRequestConfiguration(RequestConfiguration[FilesAndLinksMediaRequestBuilderPostQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class FilesAndLinksMediaRequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

