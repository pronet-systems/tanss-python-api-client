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
    from ......models.ticket403_error import Ticket403Error
    from .ticket import Ticket
    from .ticket_delete_request_body import TicketDeleteRequestBody
    from .ticket_get_response import TicketGetResponse
    from .ticket_post_response import TicketPostResponse
    from .ticket_put_request_body import TicketPutRequestBody
    from .ticket_put_response import TicketPutResponse

class TicketItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/roles/ticket/{id}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new TicketItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/roles/ticket/{id}", path_parameters)
    
    async def delete(self,body: TicketDeleteRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Removes a single role assignment from a ticket — i.e. revokes the access a specific role grants a specific employee on that ticket. Verifies that the caller can access the ticket and the role-picker parameters, then deletes the matching object (link type `TICKET`, role type `EMPLOYEE`). After the deletion the route returns the current set of role assignments for the ticket, so the UI can refresh without a follow-up call.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_delete_request_information(
            body, request_configuration
        )
        from ......models.ticket403_error import Ticket403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Ticket403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[TicketGetResponse]:
        """
        Returns all role assignments on the given ticket (which employees have which role on it). The response `meta` also carries role-picker properties used by the UI to render which roles can still be added or changed. The caller must be able to access the ticket; the underlying ticket access check is therefore enforced.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[TicketGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ......models.ticket403_error import Ticket403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Ticket403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .ticket_get_response import TicketGetResponse

        return await self.request_adapter.send_async(request_info, TicketGetResponse, error_mapping)
    
    async def post(self,body: list[Ticket], request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[TicketPostResponse]:
        """
        Adds one or more role assignments to a ticket in a single call (each item maps an employee to a role on this ticket and optionally describes the inheritance kind). Every assignment in the body is access-checked individually before persistence. Returns the resulting list of role assignments for the ticket so the UI can pick up the new state immediately.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[TicketPostResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ......models.ticket403_error import Ticket403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Ticket403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .ticket_post_response import TicketPostResponse

        return await self.request_adapter.send_async(request_info, TicketPostResponse, error_mapping)
    
    async def put(self,body: TicketPutRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[TicketPutResponse]:
        """
        Updates how an existing role assignment on a ticket is inherited (the `kindOfInheritance` flag — e.g. inherited from the company versus pinned directly on the ticket). The employee and role on the assignment are not changed; for those, use the DELETE + POST pair. The response again contains the full list of role assignments for the ticket.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[TicketPutResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        from ......models.ticket403_error import Ticket403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Ticket403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .ticket_put_response import TicketPutResponse

        return await self.request_adapter.send_async(request_info, TicketPutResponse, error_mapping)
    
    def to_delete_request_information(self,body: TicketDeleteRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Removes a single role assignment from a ticket — i.e. revokes the access a specific role grants a specific employee on that ticket. Verifies that the caller can access the ticket and the role-picker parameters, then deletes the matching object (link type `TICKET`, role type `EMPLOYEE`). After the deletion the route returns the current set of role assignments for the ticket, so the UI can refresh without a follow-up call.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Returns all role assignments on the given ticket (which employees have which role on it). The response `meta` also carries role-picker properties used by the UI to render which roles can still be added or changed. The caller must be able to access the ticket; the underlying ticket access check is therefore enforced.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: list[Ticket], request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Adds one or more role assignments to a ticket in a single call (each item maps an employee to a role on this ticket and optionally describes the inheritance kind). Every assignment in the body is access-checked individually before persistence. Returns the resulting list of role assignments for the ticket so the UI can pick up the new state immediately.
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
    
    def to_put_request_information(self,body: TicketPutRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Updates how an existing role assignment on a ticket is inherited (the `kindOfInheritance` flag — e.g. inherited from the company versus pinned directly on the ticket). The employee and role on the assignment are not changed; for those, use the DELETE + POST pair. The response again contains the full list of role assignments for the ticket.
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
    
    def with_url(self,raw_url: str) -> TicketItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: TicketItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return TicketItemRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class TicketItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class TicketItemRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class TicketItemRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class TicketItemRequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

