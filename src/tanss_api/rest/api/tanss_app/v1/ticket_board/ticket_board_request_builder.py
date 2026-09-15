from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .global_panels.global_panels_request_builder import GlobalPanelsRequestBuilder

class TicketBoardRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/tanss.app/v1/ticketBoard
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new TicketBoardRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/tanss.app/v1/ticketBoard", path_parameters)
    
    @property
    def global_panels(self) -> GlobalPanelsRequestBuilder:
        """
        The globalPanels property
        """
        from .global_panels.global_panels_request_builder import GlobalPanelsRequestBuilder

        return GlobalPanelsRequestBuilder(self.request_adapter, self.path_parameters)
    

