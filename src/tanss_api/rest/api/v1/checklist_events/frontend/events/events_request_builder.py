from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.with_event_type_item_request_builder import WithEventTypeItemRequestBuilder

class EventsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/checklistEvents/frontend/events
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new EventsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/checklistEvents/frontend/events", path_parameters)
    
    def by_event_type(self,event_type: str) -> WithEventTypeItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.v1.checklistEvents.frontend.events.item collection
        param event_type: Type of checklist event to load the configuration form for.
        Returns: WithEventTypeItemRequestBuilder
        """
        if event_type is None:
            raise TypeError("event_type cannot be null.")
        from .item.with_event_type_item_request_builder import WithEventTypeItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["eventType"] = event_type
        return WithEventTypeItemRequestBuilder(self.request_adapter, url_tpl_params)
    

