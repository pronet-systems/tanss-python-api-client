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
    from .....models.pinned403_error import Pinned403Error
    from .item.pinned_item_request_builder import PinnedItemRequestBuilder
    from .pinned_get_response import PinnedGetResponse
    from .pinned_post_request_body import PinnedPostRequestBody
    from .pinned_post_response import PinnedPostResponse

class PinnedRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/tickets/pinned
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new PinnedRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/tickets/pinned", path_parameters)
    
    def by_id(self,id: int) -> PinnedItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.v1.tickets.pinned.item collection
        param id: Primary id of the ticket pin record.
        Returns: PinnedItemRequestBuilder
        """
        if id is None:
            raise TypeError("id cannot be null.")
        from .item.pinned_item_request_builder import PinnedItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["id"] = id
        return PinnedItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[PinnedRequestBuilderGetQueryParameters]] = None) -> Optional[PinnedGetResponse]:
        """
        Returns all "pin" records attached to a ticket — references to other entities(employees, assignments, devices, etc.) that should be displayed prominently inthe ticket header. The caller must have access to the ticket.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[PinnedGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .....models.pinned403_error import Pinned403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Pinned403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .pinned_get_response import PinnedGetResponse

        return await self.request_adapter.send_async(request_info, PinnedGetResponse, error_mapping)
    
    async def post(self,body: PinnedPostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[PinnedPostResponse]:
        """
        Pins an entity (employee, assignment, device, etc.) onto a ticket so it isshown in the ticket header. Standard permission checks apply.
        param body: Request body.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[PinnedPostResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from .....models.pinned403_error import Pinned403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Pinned403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .pinned_post_response import PinnedPostResponse

        return await self.request_adapter.send_async(request_info, PinnedPostResponse, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[PinnedRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Returns all "pin" records attached to a ticket — references to other entities(employees, assignments, devices, etc.) that should be displayed prominently inthe ticket header. The caller must have access to the ticket.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, '{+baseurl}/api/v1/tickets/pinned?ticketId={ticketId}', self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: PinnedPostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Pins an entity (employee, assignment, device, etc.) onto a ticket so it isshown in the ticket header. Standard permission checks apply.
        param body: Request body.
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
    
    def with_url(self,raw_url: str) -> PinnedRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: PinnedRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return PinnedRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class PinnedRequestBuilderGetQueryParameters():
        """
        Returns all "pin" records attached to a ticket — references to other entities(employees, assignments, devices, etc.) that should be displayed prominently inthe ticket header. The caller must have access to the ticket.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "ticket_id":
                return "ticketId"
            return original_name
        
        # Id of the ticket whose pin records should be returned.
        ticket_id: Optional[int] = None

    
    @dataclass
    class PinnedRequestBuilderGetRequestConfiguration(RequestConfiguration[PinnedRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class PinnedRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

