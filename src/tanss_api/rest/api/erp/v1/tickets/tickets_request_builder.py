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
    from .....models.tickets403_error import Tickets403Error
    from .item.with_ticket_item_request_builder import WithTicketItemRequestBuilder
    from .status.status_request_builder import StatusRequestBuilder
    from .tickets_post_request_body import TicketsPostRequestBody
    from .tickets_post_response import TicketsPostResponse
    from .types.types_request_builder import TypesRequestBuilder

class TicketsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/erp/v1/tickets
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new TicketsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/erp/v1/tickets", path_parameters)
    
    def by_ticket_id(self,ticket_id: int) -> WithTicketItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.erp.v1.tickets.item collection
        param ticket_id: id of the ticket the file(s) are uploaded into
        Returns: WithTicketItemRequestBuilder
        """
        if ticket_id is None:
            raise TypeError("ticket_id cannot be null.")
        from .item.with_ticket_item_request_builder import WithTicketItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["ticketId"] = ticket_id
        return WithTicketItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def post(self,body: TicketsPostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[TicketsPostResponse]:
        """
        This call creates a new ticket in the database.`serviceCapAmount` cannot be set through this route: a service cap has to beauthorized by an employee who holds the corresponding right, and an ERP token has noemployee behind it. A `serviceCapAmount` sent here is ignored, the ticket is createdwith a service cap of `0`.To set one, use a normal user token (`ApiTokenAuth`) of an employee who may authorizea service cap: either directly on creation via `POST /api/v1/tickets`, or afterwardson the ticket created here via `PUT /api/v1/tickets/{ticketId}`. Alternatively,`GET /api/v1/tickets/{ticketId}/serviceCap/request/{employeeId}/{newAmount}` mails anapproval request to an employee who may authorize it.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[TicketsPostResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from .....models.tickets403_error import Tickets403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Tickets403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .tickets_post_response import TicketsPostResponse

        return await self.request_adapter.send_async(request_info, TicketsPostResponse, error_mapping)
    
    def to_post_request_information(self,body: TicketsPostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        This call creates a new ticket in the database.`serviceCapAmount` cannot be set through this route: a service cap has to beauthorized by an employee who holds the corresponding right, and an ERP token has noemployee behind it. A `serviceCapAmount` sent here is ignored, the ticket is createdwith a service cap of `0`.To set one, use a normal user token (`ApiTokenAuth`) of an employee who may authorizea service cap: either directly on creation via `POST /api/v1/tickets`, or afterwardson the ticket created here via `PUT /api/v1/tickets/{ticketId}`. Alternatively,`GET /api/v1/tickets/{ticketId}/serviceCap/request/{employeeId}/{newAmount}` mails anapproval request to an employee who may authorize it.
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
    
    def with_url(self,raw_url: str) -> TicketsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: TicketsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return TicketsRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def status(self) -> StatusRequestBuilder:
        """
        The status property
        """
        from .status.status_request_builder import StatusRequestBuilder

        return StatusRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def types(self) -> TypesRequestBuilder:
        """
        The types property
        """
        from .types.types_request_builder import TypesRequestBuilder

        return TypesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class TicketsRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

