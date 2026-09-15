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
    from ....models.ticket_board403_error import TicketBoard403Error
    from .global_panels.global_panels_request_builder import GlobalPanelsRequestBuilder
    from .panel.panel_request_builder import PanelRequestBuilder
    from .panels.panels_request_builder import PanelsRequestBuilder
    from .project.project_request_builder import ProjectRequestBuilder
    from .ticket_board_get_response import TicketBoardGetResponse

class TicketBoardRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/ticketBoard
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new TicketBoardRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/ticketBoard", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[TicketBoardGetResponse]:
        """
        Returns the calling employee's ticket board: every panel they own (`ONLY_FOR_MYSELF`) plus every global panel (`EVERYBODY`) for which their department, employee assignment, or company-type membership matches the panel's visibility scope. Each panel comes with its linked-entity decorations (employees, departments, tags, ...) already resolved.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[TicketBoardGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ....models.ticket_board403_error import TicketBoard403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": TicketBoard403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .ticket_board_get_response import TicketBoardGetResponse

        return await self.request_adapter.send_async(request_info, TicketBoardGetResponse, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Returns the calling employee's ticket board: every panel they own (`ONLY_FOR_MYSELF`) plus every global panel (`EVERYBODY`) for which their department, employee assignment, or company-type membership matches the panel's visibility scope. Each panel comes with its linked-entity decorations (employees, departments, tags, ...) already resolved.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> TicketBoardRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: TicketBoardRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return TicketBoardRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def global_panels(self) -> GlobalPanelsRequestBuilder:
        """
        The globalPanels property
        """
        from .global_panels.global_panels_request_builder import GlobalPanelsRequestBuilder

        return GlobalPanelsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def panel(self) -> PanelRequestBuilder:
        """
        The panel property
        """
        from .panel.panel_request_builder import PanelRequestBuilder

        return PanelRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def panels(self) -> PanelsRequestBuilder:
        """
        The panels property
        """
        from .panels.panels_request_builder import PanelsRequestBuilder

        return PanelsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def project(self) -> ProjectRequestBuilder:
        """
        The project property
        """
        from .project.project_request_builder import ProjectRequestBuilder

        return ProjectRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class TicketBoardRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

