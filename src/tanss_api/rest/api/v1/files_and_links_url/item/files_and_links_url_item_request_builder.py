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
    from .....models.files_and_links_url403_error import FilesAndLinksUrl403Error
    from .files_and_links_url_get_response import FilesAndLinksUrlGetResponse
    from .files_and_links_url_put_request_body import FilesAndLinksUrlPutRequestBody
    from .files_and_links_url_put_response import FilesAndLinksUrlPutResponse

class FilesAndLinksUrlItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/filesAndLinksUrl/{id}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new FilesAndLinksUrlItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/filesAndLinksUrl/{id}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Deletes the files-and-links entry with the given id. For folder nodes (mounted under `/filesAndLinks/{id}`) this cascades into all child nodes, attached media files, attached URLs and removes the id from every user's favorites preference. Media and URL endpoints simply delete the row. Requires the MANAGE_FILE_IMPORTANT_LINKS permission.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from .....models.files_and_links_url403_error import FilesAndLinksUrl403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": FilesAndLinksUrl403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[FilesAndLinksUrlGetResponse]:
        """
        Returns a single files-and-links entry by id. Used identically by the folder-node, media-attachment and URL endpoints; the returned payload shape depends on which path mounts this operation.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[FilesAndLinksUrlGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .....models.files_and_links_url403_error import FilesAndLinksUrl403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": FilesAndLinksUrl403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .files_and_links_url_get_response import FilesAndLinksUrlGetResponse

        return await self.request_adapter.send_async(request_info, FilesAndLinksUrlGetResponse, error_mapping)
    
    async def put(self,body: FilesAndLinksUrlPutRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[FilesAndLinksUrlPutResponse]:
        """
        Updates a files-and-links entry (folder node, media attachment metadata, or URL link depending on the mounting path). `createdAt`/`createdBy` are preserved from the original record; `modifiedAt`/`modifiedBy` are refreshed. Requires the MANAGE_FILE_IMPORTANT_LINKS permission.
        param body: Request body.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[FilesAndLinksUrlPutResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        from .....models.files_and_links_url403_error import FilesAndLinksUrl403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": FilesAndLinksUrl403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .files_and_links_url_put_response import FilesAndLinksUrlPutResponse

        return await self.request_adapter.send_async(request_info, FilesAndLinksUrlPutResponse, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Deletes the files-and-links entry with the given id. For folder nodes (mounted under `/filesAndLinks/{id}`) this cascades into all child nodes, attached media files, attached URLs and removes the id from every user's favorites preference. Media and URL endpoints simply delete the row. Requires the MANAGE_FILE_IMPORTANT_LINKS permission.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Returns a single files-and-links entry by id. Used identically by the folder-node, media-attachment and URL endpoints; the returned payload shape depends on which path mounts this operation.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_put_request_information(self,body: FilesAndLinksUrlPutRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Updates a files-and-links entry (folder node, media attachment metadata, or URL link depending on the mounting path). `createdAt`/`createdBy` are preserved from the original record; `modifiedAt`/`modifiedBy` are refreshed. Requires the MANAGE_FILE_IMPORTANT_LINKS permission.
        param body: Request body.
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
    
    def with_url(self,raw_url: str) -> FilesAndLinksUrlItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: FilesAndLinksUrlItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return FilesAndLinksUrlItemRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class FilesAndLinksUrlItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class FilesAndLinksUrlItemRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class FilesAndLinksUrlItemRequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

