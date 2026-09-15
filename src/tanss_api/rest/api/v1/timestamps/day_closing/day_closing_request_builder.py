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
    from .....models.day_closing403_error import DayClosing403Error
    from .....models.timestamp_day_closing_id import TimestampDayClosingId
    from .day_closing403_error import DayClosing403Error
    from .day_closing_post_response import DayClosingPostResponse
    from .till_date.till_date_request_builder import TillDateRequestBuilder

class DayClosingRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/timestamps/dayClosing
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new DayClosingRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/timestamps/dayClosing", path_parameters)
    
    async def delete(self,body: list[TimestampDayClosingId], request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        if calculations have to be re-done (i.e. values have changed), then the "day closing"objects have to be re-reated. They have to be deleted first, which can be done via this route.After this, they can be created again (via the POST route)
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_delete_request_information(
            body, request_configuration
        )
        from .....models.day_closing403_error import DayClosing403Error
        from .day_closing403_error import DayClosing403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": DayClosing403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def post(self,body: list[TimestampDayClosingId], request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[DayClosingPostResponse]:
        """
        "closes" a day by storing the calculated values into the database. This can onlybe done by employees who have access to the selected employee and therefore can executea "day closing" for the timestamp module
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[DayClosingPostResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from .....models.day_closing403_error import DayClosing403Error
        from .day_closing403_error import DayClosing403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": DayClosing403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .day_closing_post_response import DayClosingPostResponse

        return await self.request_adapter.send_async(request_info, DayClosingPostResponse, error_mapping)
    
    def to_delete_request_information(self,body: list[TimestampDayClosingId], request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        if calculations have to be re-done (i.e. values have changed), then the "day closing"objects have to be re-reated. They have to be deleted first, which can be done via this route.After this, they can be created again (via the POST route)
        param body: The request body
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
    
    def to_post_request_information(self,body: list[TimestampDayClosingId], request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        "closes" a day by storing the calculated values into the database. This can onlybe done by employees who have access to the selected employee and therefore can executea "day closing" for the timestamp module
        param body: The request body
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
    
    def with_url(self,raw_url: str) -> DayClosingRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: DayClosingRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return DayClosingRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def till_date(self) -> TillDateRequestBuilder:
        """
        The tillDate property
        """
        from .till_date.till_date_request_builder import TillDateRequestBuilder

        return TillDateRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class DayClosingRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class DayClosingRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

