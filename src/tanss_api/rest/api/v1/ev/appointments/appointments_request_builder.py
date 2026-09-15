from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.with_appointment_item_request_builder import WithAppointmentItemRequestBuilder
    from .link_or_create.link_or_create_request_builder import Link_or_createRequestBuilder

class AppointmentsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/ev/appointments
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new AppointmentsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/ev/appointments", path_parameters)
    
    def by_appointment_id(self,appointment_id: int) -> WithAppointmentItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.v1.ev.appointments.item collection
        param appointment_id: Coero-Termin-ID
        Returns: WithAppointmentItemRequestBuilder
        """
        if appointment_id is None:
            raise TypeError("appointment_id cannot be null.")
        from .item.with_appointment_item_request_builder import WithAppointmentItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["appointmentId"] = appointment_id
        return WithAppointmentItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    @property
    def link_or_create(self) -> Link_or_createRequestBuilder:
        """
        The link_or_create property
        """
        from .link_or_create.link_or_create_request_builder import Link_or_createRequestBuilder

        return Link_or_createRequestBuilder(self.request_adapter, self.path_parameters)
    

