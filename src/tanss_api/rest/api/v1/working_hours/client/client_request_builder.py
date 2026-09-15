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
    from .....models.client403_error import Client403Error
    from .client_get_response import ClientGetResponse
    from .client_post_request_body import ClientPostRequestBody
    from .client_post_response import ClientPostResponse
    from .client_put_request_body import ClientPutRequestBody
    from .client_put_response import ClientPutResponse
    from .item.client_item_request_builder import ClientItemRequestBuilder

class ClientRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/workingHours/client
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new ClientRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/workingHours/client", path_parameters)
    
    def by_id(self,id: int) -> ClientItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.v1.workingHours.client.item collection
        param id: Id of the client working-time model to delete.
        Returns: ClientItemRequestBuilder
        """
        if id is None:
            raise TypeError("id cannot be null.")
        from .item.client_item_request_builder import ClientItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["id"] = id
        return ClientItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[ClientGetResponse]:
        """
        Returns every customer-side working-time model with its weekday entries plus counters of related companies and contracts. Open to technicians/freelancers; the counters are computed by joining contract and company-pref tables.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ClientGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .....models.client403_error import Client403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Client403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .client_get_response import ClientGetResponse

        return await self.request_adapter.send_async(request_info, ClientGetResponse, error_mapping)
    
    async def post(self,body: ClientPostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[ClientPostResponse]:
        """
        Creates a new customer-side working-time model from the supplied container (id plus a map of weekday entries). Requires `MANAGE_WORKING_HOURS_OF_CUSTOMERS`; the new model can then be assigned to companies, contracts, or SLAs.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ClientPostResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from .....models.client403_error import Client403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Client403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .client_post_response import ClientPostResponse

        return await self.request_adapter.send_async(request_info, ClientPostResponse, error_mapping)
    
    async def put(self,body: ClientPutRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[ClientPutResponse]:
        """
        Replaces the weekday entries of an existing customer working-time model identified by `id` inside the body. Requires `MANAGE_WORKING_HOURS_OF_CUSTOMERS`; no payload is returned, just a 202 status.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ClientPutResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        from .....models.client403_error import Client403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Client403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .client_put_response import ClientPutResponse

        return await self.request_adapter.send_async(request_info, ClientPutResponse, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Returns every customer-side working-time model with its weekday entries plus counters of related companies and contracts. Open to technicians/freelancers; the counters are computed by joining contract and company-pref tables.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: ClientPostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Creates a new customer-side working-time model from the supplied container (id plus a map of weekday entries). Requires `MANAGE_WORKING_HOURS_OF_CUSTOMERS`; the new model can then be assigned to companies, contracts, or SLAs.
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
    
    def to_put_request_information(self,body: ClientPutRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Replaces the weekday entries of an existing customer working-time model identified by `id` inside the body. Requires `MANAGE_WORKING_HOURS_OF_CUSTOMERS`; no payload is returned, just a 202 status.
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
    
    def with_url(self,raw_url: str) -> ClientRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: ClientRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return ClientRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class ClientRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class ClientRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class ClientRequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

