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
    from ......models.four_zero_three_error import FourZeroThreeError
    from ......models.tns_ticket_board_panel import TnsTicketBoardPanel
    from .filters.filters_request_builder import FiltersRequestBuilder
    from .get_response import GetResponse
    from .put_response import PutResponse
    from .registers.registers_request_builder import RegistersRequestBuilder

class ItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/ticketBoard/panel/{-id}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new ItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/ticketBoard/panel/{%2Did}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Deletes a ticket board panel along with its scoped relations and per-user filter rows. Non-administrators may only delete panels they own; the change is logged and the ticket board cache is cleared.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ......models.four_zero_three_error import FourZeroThreeError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": FourZeroThreeError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[GetResponse]:
        """
        Returns a single ticket board panel by id, with its transient relations and linked entities populated. Access is granted to administrators, the panel's owner, and (for global panels) any user that passes the ticket board access check. When `mode=edit` is supplied the response also includes the catalogues of assignable companies/departments/employees/tags/ticket types/status.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[GetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ......models.four_zero_three_error import FourZeroThreeError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": FourZeroThreeError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .get_response import GetResponse

        return await self.request_adapter.send_async(request_info, GetResponse, error_mapping)
    
    async def put(self,body: TnsTicketBoardPanel, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[PutResponse]:
        """
        Updates an existing ticket board panel and re-syncs its scoped relations (companies, departments, employees, tags, ticket types/status, visibilities). Non-administrators may only update panels they own; `modified` is stamped server-side and the ticket board cache is invalidated.
        param body: Ticket board panel
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[PutResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        from ......models.four_zero_three_error import FourZeroThreeError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": FourZeroThreeError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .put_response import PutResponse

        return await self.request_adapter.send_async(request_info, PutResponse, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Deletes a ticket board panel along with its scoped relations and per-user filter rows. Non-administrators may only delete panels they own; the change is logged and the ticket board cache is cleared.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Returns a single ticket board panel by id, with its transient relations and linked entities populated. Access is granted to administrators, the panel's owner, and (for global panels) any user that passes the ticket board access check. When `mode=edit` is supplied the response also includes the catalogues of assignable companies/departments/employees/tags/ticket types/status.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_put_request_information(self,body: TnsTicketBoardPanel, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Updates an existing ticket board panel and re-syncs its scoped relations (companies, departments, employees, tags, ticket types/status, visibilities). Non-administrators may only update panels they own; `modified` is stamped server-side and the ticket board cache is invalidated.
        param body: Ticket board panel
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
    
    @property
    def filters(self) -> FiltersRequestBuilder:
        """
        The filters property
        """
        from .filters.filters_request_builder import FiltersRequestBuilder

        return FiltersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def registers(self) -> RegistersRequestBuilder:
        """
        The registers property
        """
        from .registers.registers_request_builder import RegistersRequestBuilder

        return RegistersRequestBuilder(self.request_adapter, self.path_parameters)
    
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
    

