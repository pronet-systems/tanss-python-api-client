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
    from ....models.checklist_event import ChecklistEvent
    from ....models.checklist_events403_error import ChecklistEvents403Error
    from .checklist_events_post_response import ChecklistEventsPostResponse
    from .frontend.frontend_request_builder import FrontendRequestBuilder
    from .item.checklist_events_item_request_builder import ChecklistEventsItemRequestBuilder

class ChecklistEventsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/checklistEvents
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new ChecklistEventsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/checklistEvents", path_parameters)
    
    def by_id(self,id: int) -> ChecklistEventsItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.v1.checklistEvents.item collection
        param id: Id of the checklist event.
        Returns: ChecklistEventsItemRequestBuilder
        """
        if id is None:
            raise TypeError("id cannot be null.")
        from .item.checklist_events_item_request_builder import ChecklistEventsItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["id"] = id
        return ChecklistEventsItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def post(self,body: ChecklistEvent, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[ChecklistEventsPostResponse]:
        """
        Creates a new checklist event — a trigger that fires when a particular item is checked, a multi-select option is picked, or some other condition is met during checklist processing. Standard CRUD permission check applies.
        param body: An automated action attached to a checklist item, a multi-select option or — inside the ITportal wizard — to a card, widget or option.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ChecklistEventsPostResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ....models.checklist_events403_error import ChecklistEvents403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": ChecklistEvents403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .checklist_events_post_response import ChecklistEventsPostResponse

        return await self.request_adapter.send_async(request_info, ChecklistEventsPostResponse, error_mapping)
    
    def to_post_request_information(self,body: ChecklistEvent, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Creates a new checklist event — a trigger that fires when a particular item is checked, a multi-select option is picked, or some other condition is met during checklist processing. Standard CRUD permission check applies.
        param body: An automated action attached to a checklist item, a multi-select option or — inside the ITportal wizard — to a card, widget or option.
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
    
    def with_url(self,raw_url: str) -> ChecklistEventsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: ChecklistEventsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return ChecklistEventsRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def frontend(self) -> FrontendRequestBuilder:
        """
        The frontend property
        """
        from .frontend.frontend_request_builder import FrontendRequestBuilder

        return FrontendRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class ChecklistEventsRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

