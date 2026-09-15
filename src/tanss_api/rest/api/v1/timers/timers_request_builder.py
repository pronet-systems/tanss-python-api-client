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
    from ....models.timer import Timer
    from ....models.timers403_error import Timers403Error
    from .all_technicians.all_technicians_request_builder import AllTechniciansRequestBuilder
    from .item.with_timer_item_request_builder import WithTimerItemRequestBuilder
    from .notes.notes_request_builder import NotesRequestBuilder
    from .timers_get_response import TimersGetResponse
    from .timers_post_response import TimersPostResponse

class TimersRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/timers
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new TimersRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/timers", path_parameters)
    
    def by_timer_id(self,timer_id: int) -> WithTimerItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.v1.timers.item collection
        param timer_id: Id of the timer.
        Returns: WithTimerItemRequestBuilder
        """
        if timer_id is None:
            raise TypeError("timer_id cannot be null.")
        from .item.with_timer_item_request_builder import WithTimerItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["timerId"] = timer_id
        return WithTimerItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def delete(self,body: Timer, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        This route will delete a timer
        param body: a TANSS timer
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_delete_request_information(
            body, request_configuration
        )
        from ....models.timers403_error import Timers403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Timers403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[TimersGetResponse]:
        """
        This route will get all timers of the currently logged in user
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[TimersGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ....models.timers403_error import Timers403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Timers403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .timers_get_response import TimersGetResponse

        return await self.request_adapter.send_async(request_info, TimersGetResponse, error_mapping)
    
    async def post(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[TimersPostResponse]:
        """
        This route will create a timer for the currently logged in user
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[TimersPostResponse]
        """
        request_info = self.to_post_request_information(
            request_configuration
        )
        from ....models.timers403_error import Timers403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Timers403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .timers_post_response import TimersPostResponse

        return await self.request_adapter.send_async(request_info, TimersPostResponse, error_mapping)
    
    def to_delete_request_information(self,body: Timer, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        This route will delete a timer
        param body: a TANSS timer
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
        This route will get all timers of the currently logged in user
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        This route will create a timer for the currently logged in user
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.POST, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> TimersRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: TimersRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return TimersRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def all_technicians(self) -> AllTechniciansRequestBuilder:
        """
        The allTechnicians property
        """
        from .all_technicians.all_technicians_request_builder import AllTechniciansRequestBuilder

        return AllTechniciansRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def notes(self) -> NotesRequestBuilder:
        """
        The notes property
        """
        from .notes.notes_request_builder import NotesRequestBuilder

        return NotesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class TimersRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class TimersRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class TimersRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

