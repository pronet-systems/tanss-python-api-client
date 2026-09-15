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
    from ....models.timestamp import Timestamp
    from ....models.timestamps403_error import Timestamps403Error
    from .change_requests.change_requests_request_builder import ChangeRequestsRequestBuilder
    from .day_closing.day_closing_request_builder import DayClosingRequestBuilder
    from .employee.employee_request_builder import EmployeeRequestBuilder
    from .employees.employees_request_builder import EmployeesRequestBuilder
    from .info.info_request_builder import InfoRequestBuilder
    from .initial_balances.initial_balances_request_builder import InitialBalancesRequestBuilder
    from .item.employee_item_request_builder import EmployeeItemRequestBuilder
    from .manual_booking.manual_booking_request_builder import ManualBookingRequestBuilder
    from .pause_configs.pause_configs_request_builder import PauseConfigsRequestBuilder
    from .statistics.statistics_request_builder import StatisticsRequestBuilder
    from .timestamps_get_response import TimestampsGetResponse
    from .timestamps_post_response import TimestampsPostResponse

class TimestampsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/timestamps
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new TimestampsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/timestamps{?autoPause*,from*,till*}", path_parameters)
    
    def by_employee_id(self,employee_id: int) -> EmployeeItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.v1.timestamps.item collection
        param employee_id: id of the timestamp
        Returns: EmployeeItemRequestBuilder
        """
        if employee_id is None:
            raise TypeError("employee_id cannot be null.")
        from .item.employee_item_request_builder import EmployeeItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["employee%2Did"] = employee_id
        return EmployeeItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[TimestampsRequestBuilderGetQueryParameters]] = None) -> Optional[TimestampsGetResponse]:
        """
        gets a list of timestamps from a given period
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[TimestampsGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ....models.timestamps403_error import Timestamps403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Timestamps403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .timestamps_get_response import TimestampsGetResponse

        return await self.request_adapter.send_async(request_info, TimestampsGetResponse, error_mapping)
    
    async def post(self,body: Timestamp, request_configuration: Optional[RequestConfiguration[TimestampsRequestBuilderPostQueryParameters]] = None) -> Optional[TimestampsPostResponse]:
        """
        writes a timestamp into the database
        param body: ....
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[TimestampsPostResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ....models.timestamps403_error import Timestamps403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Timestamps403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .timestamps_post_response import TimestampsPostResponse

        return await self.request_adapter.send_async(request_info, TimestampsPostResponse, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[TimestampsRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        gets a list of timestamps from a given period
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: Timestamp, request_configuration: Optional[RequestConfiguration[TimestampsRequestBuilderPostQueryParameters]] = None) -> RequestInformation:
        """
        writes a timestamp into the database
        param body: ....
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
    
    def with_url(self,raw_url: str) -> TimestampsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: TimestampsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return TimestampsRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def change_requests(self) -> ChangeRequestsRequestBuilder:
        """
        The changeRequests property
        """
        from .change_requests.change_requests_request_builder import ChangeRequestsRequestBuilder

        return ChangeRequestsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def day_closing(self) -> DayClosingRequestBuilder:
        """
        The dayClosing property
        """
        from .day_closing.day_closing_request_builder import DayClosingRequestBuilder

        return DayClosingRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def employee(self) -> EmployeeRequestBuilder:
        """
        The employee property
        """
        from .employee.employee_request_builder import EmployeeRequestBuilder

        return EmployeeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def employees(self) -> EmployeesRequestBuilder:
        """
        The employees property
        """
        from .employees.employees_request_builder import EmployeesRequestBuilder

        return EmployeesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def info(self) -> InfoRequestBuilder:
        """
        The info property
        """
        from .info.info_request_builder import InfoRequestBuilder

        return InfoRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def initial_balances(self) -> InitialBalancesRequestBuilder:
        """
        The initialBalances property
        """
        from .initial_balances.initial_balances_request_builder import InitialBalancesRequestBuilder

        return InitialBalancesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def manual_booking(self) -> ManualBookingRequestBuilder:
        """
        The manualBooking property
        """
        from .manual_booking.manual_booking_request_builder import ManualBookingRequestBuilder

        return ManualBookingRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def pause_configs(self) -> PauseConfigsRequestBuilder:
        """
        The pauseConfigs property
        """
        from .pause_configs.pause_configs_request_builder import PauseConfigsRequestBuilder

        return PauseConfigsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def statistics(self) -> StatisticsRequestBuilder:
        """
        The statistics property
        """
        from .statistics.statistics_request_builder import StatisticsRequestBuilder

        return StatisticsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class TimestampsRequestBuilderGetQueryParameters():
        """
        gets a list of timestamps from a given period
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "from_":
                return "from"
            if original_name == "till":
                return "till"
            return original_name
        
        # timestamp of start of period. if omitted,the beginning of the current day will be used
        from_: Optional[int] = None

        # timestamp of end of period. if omitted,the end of the current day will be used
        till: Optional[int] = None

    
    @dataclass
    class TimestampsRequestBuilderGetRequestConfiguration(RequestConfiguration[TimestampsRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class TimestampsRequestBuilderPostQueryParameters():
        """
        writes a timestamp into the database
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "auto_pause":
                return "autoPause"
            return original_name
        
        # if true, a pause will automatically be inserted, if the minimum pause is not met for this day (see "pause config" routes)
        auto_pause: Optional[bool] = None

    
    @dataclass
    class TimestampsRequestBuilderPostRequestConfiguration(RequestConfiguration[TimestampsRequestBuilderPostQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

