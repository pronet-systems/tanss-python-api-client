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
    from ....models.services403_error import Services403Error
    from ....models.tns_service import TnsService
    from .item.services_item_request_builder import ServicesItemRequestBuilder
    from .services_get_response import ServicesGetResponse
    from .services_post_response import ServicesPostResponse

class ServicesRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/services
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new ServicesRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/services", path_parameters)
    
    def by_id(self,id: int) -> ServicesItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.v1.services.item collection
        param id: ID of the service to fetch.
        Returns: ServicesItemRequestBuilder
        """
        if id is None:
            raise TypeError("id cannot be null.")
        from .item.services_item_request_builder import ServicesItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["id"] = id
        return ServicesItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[ServicesGetResponse]:
        """
        Gets a list of all defined services
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ServicesGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ....models.services403_error import Services403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Services403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .services_get_response import ServicesGetResponse

        return await self.request_adapter.send_async(request_info, ServicesGetResponse, error_mapping)
    
    async def post(self,body: TnsService, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[ServicesPostResponse]:
        """
        Creates a serviceServices are used in pcs or periphery (on ip addresses) to launch an external software
        param body: represents a service (which can be assigned to an ip address on a pc/periphery)
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ServicesPostResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ....models.services403_error import Services403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Services403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .services_post_response import ServicesPostResponse

        return await self.request_adapter.send_async(request_info, ServicesPostResponse, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Gets a list of all defined services
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: TnsService, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Creates a serviceServices are used in pcs or periphery (on ip addresses) to launch an external software
        param body: represents a service (which can be assigned to an ip address on a pc/periphery)
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
    
    def with_url(self,raw_url: str) -> ServicesRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: ServicesRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return ServicesRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class ServicesRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class ServicesRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

