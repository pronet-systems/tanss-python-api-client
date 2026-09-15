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
    from ........models.with_category403_error import WithCategory403Error
    from .with_category_put_response import WithCategoryPutResponse

class WithCategoryItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/admin/permissionPackages/{packageId}/category/{categoryId}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new WithCategoryItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/admin/permissionPackages/{packageId}/category/{categoryId}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Removes every permission belonging to the given category from the givenpermission package. Caller must be from the own company and hold`MANAGE_PERMISSION_PACKAGES`.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ........models.with_category403_error import WithCategory403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": WithCategory403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def put(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[WithCategoryPutResponse]:
        """
        Adds every permission belonging to the given category to the givenpermission package. Caller must be from the own company and hold`MANAGE_PERMISSION_PACKAGES`.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[WithCategoryPutResponse]
        """
        request_info = self.to_put_request_information(
            request_configuration
        )
        from ........models.with_category403_error import WithCategory403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": WithCategory403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .with_category_put_response import WithCategoryPutResponse

        return await self.request_adapter.send_async(request_info, WithCategoryPutResponse, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Removes every permission belonging to the given category from the givenpermission package. Caller must be from the own company and hold`MANAGE_PERMISSION_PACKAGES`.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_put_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Adds every permission belonging to the given category to the givenpermission package. Caller must be from the own company and hold`MANAGE_PERMISSION_PACKAGES`.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.PUT, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> WithCategoryItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: WithCategoryItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return WithCategoryItemRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class WithCategoryItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class WithCategoryItemRequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

