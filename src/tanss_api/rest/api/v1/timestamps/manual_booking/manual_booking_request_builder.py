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
    from .....models.manual_booking403_error import ManualBooking403Error
    from .item.manual_booking_item_request_builder import ManualBookingItemRequestBuilder
    from .manual_booking_post_request_body import ManualBookingPostRequestBody
    from .manual_booking_post_response import ManualBookingPostResponse
    from .manual_booking_put_request_body import ManualBookingPutRequestBody
    from .manual_booking_put_response import ManualBookingPutResponse

class ManualBookingRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/timestamps/manualBooking
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new ManualBookingRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/timestamps/manualBooking", path_parameters)
    
    def by_id(self,id: int) -> ManualBookingItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.v1.timestamps.manualBooking.item collection
        param id: Id of the manual booking to delete
        Returns: ManualBookingItemRequestBuilder
        """
        if id is None:
            raise TypeError("id cannot be null.")
        from .item.manual_booking_item_request_builder import ManualBookingItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["id"] = id
        return ManualBookingItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def post(self,body: ManualBookingPostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[ManualBookingPostResponse]:
        """
        Creates a manual balance correction for an employee — a positive or negative minute value applied to a specificday together with a reason. Used by supervisors to compensate overtime, pay out balance or fix edge cases thatcannot be captured via real punches. The booking shows up alongside regular timestamps in the day statistics.
        param body: Request body.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ManualBookingPostResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from .....models.manual_booking403_error import ManualBooking403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": ManualBooking403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .manual_booking_post_response import ManualBookingPostResponse

        return await self.request_adapter.send_async(request_info, ManualBookingPostResponse, error_mapping)
    
    async def put(self,body: ManualBookingPutRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[ManualBookingPutResponse]:
        """
        Returns a filtered, paginated list of manual balance corrections. Uses PUT (not GET) because the filter shapeis rich enough to require a JSON body — the request carries pagination, sort and field filters in aconfiguration. Requires admin-level timestamp permissions because manual bookingsaffect other employees' balances.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ManualBookingPutResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        from .....models.manual_booking403_error import ManualBooking403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": ManualBooking403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .manual_booking_put_response import ManualBookingPutResponse

        return await self.request_adapter.send_async(request_info, ManualBookingPutResponse, error_mapping)
    
    def to_post_request_information(self,body: ManualBookingPostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Creates a manual balance correction for an employee — a positive or negative minute value applied to a specificday together with a reason. Used by supervisors to compensate overtime, pay out balance or fix edge cases thatcannot be captured via real punches. The booking shows up alongside regular timestamps in the day statistics.
        param body: Request body.
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
    
    def to_put_request_information(self,body: ManualBookingPutRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Returns a filtered, paginated list of manual balance corrections. Uses PUT (not GET) because the filter shapeis rich enough to require a JSON body — the request carries pagination, sort and field filters in aconfiguration. Requires admin-level timestamp permissions because manual bookingsaffect other employees' balances.
        param body: The request body
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
    
    def with_url(self,raw_url: str) -> ManualBookingRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: ManualBookingRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return ManualBookingRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class ManualBookingRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class ManualBookingRequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

