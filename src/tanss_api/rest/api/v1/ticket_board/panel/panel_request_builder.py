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
    from .....models.panel403_error import Panel403Error
    from .....models.tns_ticket_board_panel import TnsTicketBoardPanel
    from .filters.filters_request_builder import FiltersRequestBuilder
    from .item.item_request_builder import ItemRequestBuilder
    from .panel_get_response import PanelGetResponse
    from .panel_post_response import PanelPostResponse
    from .panel_put_response import PanelPutResponse

class PanelRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/ticketBoard/panel
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new PanelRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/ticketBoard/panel{?mode*}", path_parameters)
    
    def by_id(self,id: int) -> ItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.v1.ticketBoard.panel.item collection
        param id: Panel id
        Returns: ItemRequestBuilder
        """
        if id is None:
            raise TypeError("id cannot be null.")
        from .item.item_request_builder import ItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["%2Did"] = id
        return ItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[PanelRequestBuilderGetQueryParameters]] = None) -> Optional[PanelGetResponse]:
        """
        Returns a blank object skeleton used by the UI as the starting point for creating a new panel. When `mode=edit` is passed, the response is additionally enriched with all assignable companies, departments, employees, tags, ticket types and statuses so the editor can populate its selectors in one round-trip.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[PanelGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .....models.panel403_error import Panel403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Panel403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .panel_get_response import PanelGetResponse

        return await self.request_adapter.send_async(request_info, PanelGetResponse, error_mapping)
    
    async def post(self,body: TnsTicketBoardPanel, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[PanelPostResponse]:
        """
        Creates a new ticket board panel owned by the calling employee (`employeeId` is forced to the session user, `created`/`modified` are stamped server-side). `name` and `registerType` are required; the supplied filter row is persisted alongside the panel and the ticket board cache is cleared. Requires the `CREATE_OWN_TICKET_BOARD_PANELS` permission.
        param body: Ticket board panel
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[PanelPostResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from .....models.panel403_error import Panel403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Panel403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .panel_post_response import PanelPostResponse

        return await self.request_adapter.send_async(request_info, PanelPostResponse, error_mapping)
    
    async def put(self,body: TnsTicketBoardPanel, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[PanelPutResponse]:
        """
        Aktualisiert vermutlich ein Ticketboard-Panel (Gegenstück zu POST /api/v1/ticketBoard/panel). Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft. Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId. Keine Analyse vorhanden.
        param body: Ticket board panel
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[PanelPutResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .panel_put_response import PanelPutResponse

        return await self.request_adapter.send_async(request_info, PanelPutResponse, None)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[PanelRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Returns a blank object skeleton used by the UI as the starting point for creating a new panel. When `mode=edit` is passed, the response is additionally enriched with all assignable companies, departments, employees, tags, ticket types and statuses so the editor can populate its selectors in one round-trip.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: TnsTicketBoardPanel, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Creates a new ticket board panel owned by the calling employee (`employeeId` is forced to the session user, `created`/`modified` are stamped server-side). `name` and `registerType` are required; the supplied filter row is persisted alongside the panel and the ticket board cache is cleared. Requires the `CREATE_OWN_TICKET_BOARD_PANELS` permission.
        param body: Ticket board panel
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
    
    def to_put_request_information(self,body: TnsTicketBoardPanel, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Aktualisiert vermutlich ein Ticketboard-Panel (Gegenstück zu POST /api/v1/ticketBoard/panel). Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft. Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId. Keine Analyse vorhanden.
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
    
    def with_url(self,raw_url: str) -> PanelRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: PanelRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return PanelRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def filters(self) -> FiltersRequestBuilder:
        """
        The filters property
        """
        from .filters.filters_request_builder import FiltersRequestBuilder

        return FiltersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class PanelRequestBuilderGetQueryParameters():
        """
        Returns a blank object skeleton used by the UI as the starting point for creating a new panel. When `mode=edit` is passed, the response is additionally enriched with all assignable companies, departments, employees, tags, ticket types and statuses so the editor can populate its selectors in one round-trip.
        """
        # If mode = "edit" you get all possible employees, departments, tags, ticket types and tickets status which can be assigned
        mode: Optional[str] = None

    
    @dataclass
    class PanelRequestBuilderGetRequestConfiguration(RequestConfiguration[PanelRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class PanelRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class PanelRequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

