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
    from .....models.four_zero_three_error import FourZeroThreeError
    from .get_response import GetResponse
    from .item.with_link_item_request_builder import WithLinkItemRequestBuilder
    from .put_request_body import PutRequestBody
    from .put_response import PutResponse

class ItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/entityFiles/{-id}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new ItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/entityFiles/{%2Did}", path_parameters)
    
    def by_link_id(self,link_id: int) -> WithLinkItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.v1.entityFiles.item.item collection
        param link_id: ID of the linked entity.
        Returns: WithLinkItemRequestBuilder
        """
        if link_id is None:
            raise TypeError("link_id cannot be null.")
        from .item.with_link_item_request_builder import WithLinkItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["linkId"] = link_id
        return WithLinkItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Deletes the entity-file row and the underlying file on disk. Deletion requires full company access plus the matching `DELETE_*` permission depending on the file's `documentType` (standard, barcode, uploaded, knowledge-base). A failure to remove the on-disk file is logged but does not roll back the database delete.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from .....models.four_zero_three_error import FourZeroThreeError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": FourZeroThreeError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[GetResponse]:
        """
        Returns a short-lived object for the entity file, which the frontend then uses to actually download the binary through the file-pass endpoint. Access to the file is checked first, so this also acts as the authorisation gate for the subsequent download.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[GetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .....models.four_zero_three_error import FourZeroThreeError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": FourZeroThreeError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .get_response import GetResponse

        return await self.request_adapter.send_async(request_info, GetResponse, error_mapping)
    
    async def put(self,body: PutRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[PutResponse]:
        """
        Updates the metadata of an entity file (e.g. `title`, `internal` flag, `documentType`). Only the metadata fields are touched here — the actual file payload is not part of this route. Standard permission and access checks apply.
        param body: Request body.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[PutResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        from .....models.four_zero_three_error import FourZeroThreeError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": FourZeroThreeError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .put_response import PutResponse

        return await self.request_adapter.send_async(request_info, PutResponse, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Deletes the entity-file row and the underlying file on disk. Deletion requires full company access plus the matching `DELETE_*` permission depending on the file's `documentType` (standard, barcode, uploaded, knowledge-base). A failure to remove the on-disk file is logged but does not roll back the database delete.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Returns a short-lived object for the entity file, which the frontend then uses to actually download the binary through the file-pass endpoint. Access to the file is checked first, so this also acts as the authorisation gate for the subsequent download.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_put_request_information(self,body: PutRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Updates the metadata of an entity file (e.g. `title`, `internal` flag, `documentType`). Only the metadata fields are touched here — the actual file payload is not part of this route. Standard permission and access checks apply.
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
    
    def with_url(self,raw_url: str) -> ItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: ItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return ItemRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class ItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class ItemRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class ItemRequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

