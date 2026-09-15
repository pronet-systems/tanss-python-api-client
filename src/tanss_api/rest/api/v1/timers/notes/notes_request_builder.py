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
    from .....models.notes403_error import Notes403Error
    from .....models.timer_fragment import TimerFragment
    from .item.with_timer_item_request_builder import WithTimerItemRequestBuilder
    from .notes_put_response import NotesPutResponse

class NotesRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/timers/notes
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new NotesRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/timers/notes", path_parameters)
    
    def by_timer_id(self,timer_id: int) -> WithTimerItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.v1.timers.notes.item collection
        param timer_id: id of the timer
        Returns: WithTimerItemRequestBuilder
        """
        if timer_id is None:
            raise TypeError("timer_id cannot be null.")
        from .item.with_timer_item_request_builder import WithTimerItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["timerId"] = timer_id
        return WithTimerItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def delete(self,body: TimerFragment, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        This route will delete a timer fragment
        param body: Timers can have multiple fragments, meaning a start/stop timeframe.Each fragment can have a note.A timer is running if the last fragment has no stop time.If the last fragment has a stop time, the timer is stopped.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_delete_request_information(
            body, request_configuration
        )
        from .....models.notes403_error import Notes403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Notes403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def put(self,body: TimerFragment, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[NotesPutResponse]:
        """
        This route will update a timer fragment and is used to store / update a "note" in the fragment
        param body: Timers can have multiple fragments, meaning a start/stop timeframe.Each fragment can have a note.A timer is running if the last fragment has no stop time.If the last fragment has a stop time, the timer is stopped.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[NotesPutResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        from .....models.notes403_error import Notes403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Notes403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .notes_put_response import NotesPutResponse

        return await self.request_adapter.send_async(request_info, NotesPutResponse, error_mapping)
    
    def to_delete_request_information(self,body: TimerFragment, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        This route will delete a timer fragment
        param body: Timers can have multiple fragments, meaning a start/stop timeframe.Each fragment can have a note.A timer is running if the last fragment has no stop time.If the last fragment has a stop time, the timer is stopped.
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
    
    def to_put_request_information(self,body: TimerFragment, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        This route will update a timer fragment and is used to store / update a "note" in the fragment
        param body: Timers can have multiple fragments, meaning a start/stop timeframe.Each fragment can have a note.A timer is running if the last fragment has no stop time.If the last fragment has a stop time, the timer is stopped.
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
    
    def with_url(self,raw_url: str) -> NotesRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: NotesRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return NotesRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class NotesRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class NotesRequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

