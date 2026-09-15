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
    from ....models.support_types403_error import SupportTypes403Error
    from ....models.tns_support_type import TnsSupportType
    from .active.active_request_builder import ActiveRequestBuilder
    from .item.support_types_item_request_builder import SupportTypesItemRequestBuilder
    from .support_types_get_response import SupportTypesGetResponse
    from .support_types_post_response import SupportTypesPostResponse

class SupportTypesRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/supportTypes
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new SupportTypesRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/supportTypes", path_parameters)
    
    def by_id(self,id: int) -> SupportTypesItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.v1.supportTypes.item collection
        param id: id of the support type that shall be fetched
        Returns: SupportTypesItemRequestBuilder
        """
        if id is None:
            raise TypeError("id cannot be null.")
        from .item.support_types_item_request_builder import SupportTypesItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["id"] = id
        return SupportTypesItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[SupportTypesGetResponse]:
        """
        Gets all support types
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[SupportTypesGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ....models.support_types403_error import SupportTypes403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": SupportTypes403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .support_types_get_response import SupportTypesGetResponse

        return await self.request_adapter.send_async(request_info, SupportTypesGetResponse, error_mapping)
    
    async def post(self,body: TnsSupportType, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[SupportTypesPostResponse]:
        """
        Creates a support type
        param body: describes a support type
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[SupportTypesPostResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ....models.support_types403_error import SupportTypes403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": SupportTypes403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .support_types_post_response import SupportTypesPostResponse

        return await self.request_adapter.send_async(request_info, SupportTypesPostResponse, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Gets all support types
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: TnsSupportType, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Creates a support type
        param body: describes a support type
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
    
    def with_url(self,raw_url: str) -> SupportTypesRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: SupportTypesRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return SupportTypesRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def active(self) -> ActiveRequestBuilder:
        """
        The active property
        """
        from .active.active_request_builder import ActiveRequestBuilder

        return ActiveRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class SupportTypesRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class SupportTypesRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

