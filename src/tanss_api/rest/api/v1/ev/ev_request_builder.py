from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .appointments.appointments_request_builder import AppointmentsRequestBuilder
    from .attendees.attendees_request_builder import AttendeesRequestBuilder
    from .contacts.contacts_request_builder import ContactsRequestBuilder
    from .rooms.rooms_request_builder import RoomsRequestBuilder
    from .supports.supports_request_builder import SupportsRequestBuilder
    from .timeline.timeline_request_builder import TimelineRequestBuilder

class EvRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/ev
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new EvRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/ev", path_parameters)
    
    @property
    def appointments(self) -> AppointmentsRequestBuilder:
        """
        The appointments property
        """
        from .appointments.appointments_request_builder import AppointmentsRequestBuilder

        return AppointmentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def attendees(self) -> AttendeesRequestBuilder:
        """
        The attendees property
        """
        from .attendees.attendees_request_builder import AttendeesRequestBuilder

        return AttendeesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def contacts(self) -> ContactsRequestBuilder:
        """
        The contacts property
        """
        from .contacts.contacts_request_builder import ContactsRequestBuilder

        return ContactsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def rooms(self) -> RoomsRequestBuilder:
        """
        The rooms property
        """
        from .rooms.rooms_request_builder import RoomsRequestBuilder

        return RoomsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def supports(self) -> SupportsRequestBuilder:
        """
        The supports property
        """
        from .supports.supports_request_builder import SupportsRequestBuilder

        return SupportsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def timeline(self) -> TimelineRequestBuilder:
        """
        The timeline property
        """
        from .timeline.timeline_request_builder import TimelineRequestBuilder

        return TimelineRequestBuilder(self.request_adapter, self.path_parameters)
    

