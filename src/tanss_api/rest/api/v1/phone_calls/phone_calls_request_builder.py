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
    from ....models.phone_calls403_error import PhoneCalls403Error
    from ....models.tns_phone_call_configuration import TnsPhoneCallConfiguration
    from .identify.identify_request_builder import IdentifyRequestBuilder
    from .item.phone_calls_item_request_builder import PhoneCallsItemRequestBuilder
    from .notification.notification_request_builder import NotificationRequestBuilder
    from .phone_calls_put_response import PhoneCallsPutResponse
    from .pop_up.pop_up_request_builder import PopUpRequestBuilder

class PhoneCallsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/phoneCalls
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new PhoneCallsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/phoneCalls", path_parameters)
    
    def by_id(self,id: int) -> PhoneCallsItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.v1.phoneCalls.item collection
        param id: Id of the phone call to be fetched
        Returns: PhoneCallsItemRequestBuilder
        """
        if id is None:
            raise TypeError("id cannot be null.")
        from .item.phone_calls_item_request_builder import PhoneCallsItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["id"] = id
        return PhoneCallsItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def put(self,body: TnsPhoneCallConfiguration, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[PhoneCallsPutResponse]:
        """
        Retrieves a list of phone calls from the database, using misc. filter settings
        param body: This object is used to get phone calls based on this filter settings
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[PhoneCallsPutResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        from ....models.phone_calls403_error import PhoneCalls403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": PhoneCalls403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .phone_calls_put_response import PhoneCallsPutResponse

        return await self.request_adapter.send_async(request_info, PhoneCallsPutResponse, error_mapping)
    
    def to_put_request_information(self,body: TnsPhoneCallConfiguration, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Retrieves a list of phone calls from the database, using misc. filter settings
        param body: This object is used to get phone calls based on this filter settings
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
    
    def with_url(self,raw_url: str) -> PhoneCallsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: PhoneCallsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return PhoneCallsRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def identify(self) -> IdentifyRequestBuilder:
        """
        The identify property
        """
        from .identify.identify_request_builder import IdentifyRequestBuilder

        return IdentifyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def notification(self) -> NotificationRequestBuilder:
        """
        The notification property
        """
        from .notification.notification_request_builder import NotificationRequestBuilder

        return NotificationRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def pop_up(self) -> PopUpRequestBuilder:
        """
        The popUp property
        """
        from .pop_up.pop_up_request_builder import PopUpRequestBuilder

        return PopUpRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class PhoneCallsRequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

