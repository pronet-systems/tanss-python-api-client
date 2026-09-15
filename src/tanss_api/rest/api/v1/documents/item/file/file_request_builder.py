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
    from ......models.file403_error import File403Error
    from .file_post_response import FilePostResponse
    from .item.with_file_item_request_builder import WithFileItemRequestBuilder

class FileRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/documents/{id}/file
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new FileRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/documents/{id}/file", path_parameters)
    
    def by_file_id(self,file_id: int) -> WithFileItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.v1.documents.item.file.item collection
        param file_id: Id of the file attachment to download.
        Returns: WithFileItemRequestBuilder
        """
        if file_id is None:
            raise TypeError("file_id cannot be null.")
        from .item.with_file_item_request_builder import WithFileItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["fileId"] = file_id
        return WithFileItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def post(self,body: MultipartBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[FilePostResponse]:
        """
        If the document is of type "FILE", then you can set a file for this documentThis is set via this route
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[FilePostResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ......models.file403_error import File403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": File403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .file_post_response import FilePostResponse

        return await self.request_adapter.send_async(request_info, FilePostResponse, error_mapping)
    
    def to_post_request_information(self,body: MultipartBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        If the document is of type "FILE", then you can set a file for this documentThis is set via this route
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
    
    def with_url(self,raw_url: str) -> FileRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: FileRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return FileRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class FileRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

