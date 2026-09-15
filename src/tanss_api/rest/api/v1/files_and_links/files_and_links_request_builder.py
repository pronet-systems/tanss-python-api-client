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
    from ....models.files_and_links403_error import FilesAndLinks403Error
    from .favorites.favorites_request_builder import FavoritesRequestBuilder
    from .files_and_links_post_request_body import FilesAndLinksPostRequestBody
    from .files_and_links_post_response import FilesAndLinksPostResponse
    from .files_and_links_put_request_body import FilesAndLinksPutRequestBody
    from .files_and_links_put_response import FilesAndLinksPutResponse
    from .item.files_and_links_item_request_builder import FilesAndLinksItemRequestBuilder
    from .latest_uploads.latest_uploads_request_builder import LatestUploadsRequestBuilder

class FilesAndLinksRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/filesAndLinks
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new FilesAndLinksRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/filesAndLinks", path_parameters)
    
    def by_id(self,id: int) -> FilesAndLinksItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.v1.filesAndLinks.item collection
        param id: Id of the files-and-links entry.
        Returns: FilesAndLinksItemRequestBuilder
        """
        if id is None:
            raise TypeError("id cannot be null.")
        from .item.files_and_links_item_request_builder import FilesAndLinksItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["id"] = id
        return FilesAndLinksItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def post(self,body: FilesAndLinksPostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[FilesAndLinksPostResponse]:
        """
        Creates a new files-and-links node (used as a folder/container in the knowledge base tree). Requires the knowledge base v2 feature plus the FILES_LINKS_ACTIVATED config flag, and the MANAGE_FILE_IMPORTANT_LINKS permission. `createdAt`/`createdBy` and `modifiedAt`/`modifiedBy` are set server-side.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[FilesAndLinksPostResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ....models.files_and_links403_error import FilesAndLinks403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": FilesAndLinks403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .files_and_links_post_response import FilesAndLinksPostResponse

        return await self.request_adapter.send_async(request_info, FilesAndLinksPostResponse, error_mapping)
    
    async def put(self,body: FilesAndLinksPutRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[FilesAndLinksPutResponse]:
        """
        Returns files-and-links nodes for a given `parentId`. With `withChildren=true` the response is recursively expanded into a full tree; for each node the attached media filenames and URL titles are collected into `fileNames`.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[FilesAndLinksPutResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        from ....models.files_and_links403_error import FilesAndLinks403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": FilesAndLinks403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .files_and_links_put_response import FilesAndLinksPutResponse

        return await self.request_adapter.send_async(request_info, FilesAndLinksPutResponse, error_mapping)
    
    def to_post_request_information(self,body: FilesAndLinksPostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Creates a new files-and-links node (used as a folder/container in the knowledge base tree). Requires the knowledge base v2 feature plus the FILES_LINKS_ACTIVATED config flag, and the MANAGE_FILE_IMPORTANT_LINKS permission. `createdAt`/`createdBy` and `modifiedAt`/`modifiedBy` are set server-side.
        param body: The request body
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
    
    def to_put_request_information(self,body: FilesAndLinksPutRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Returns files-and-links nodes for a given `parentId`. With `withChildren=true` the response is recursively expanded into a full tree; for each node the attached media filenames and URL titles are collected into `fileNames`.
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
    
    def with_url(self,raw_url: str) -> FilesAndLinksRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: FilesAndLinksRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return FilesAndLinksRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def favorites(self) -> FavoritesRequestBuilder:
        """
        The favorites property
        """
        from .favorites.favorites_request_builder import FavoritesRequestBuilder

        return FavoritesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def latest_uploads(self) -> LatestUploadsRequestBuilder:
        """
        The latestUploads property
        """
        from .latest_uploads.latest_uploads_request_builder import LatestUploadsRequestBuilder

        return LatestUploadsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class FilesAndLinksRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class FilesAndLinksRequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

