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
    from .....models.with_day403_error import WithDay403Error
    from .charts.charts_request_builder import ChartsRequestBuilder
    from .confirm.confirm_request_builder import ConfirmRequestBuilder
    from .statistic_all_services_by_day.statistic_all_services_by_day_request_builder import StatisticAllServicesByDayRequestBuilder
    from .with_day_get_response import WithDayGetResponse

class WithDayItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/ownDailyServices/{day}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new WithDayItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/ownDailyServices/{day}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[WithDayGetResponse]:
        """
        Returns the calling employee's own daily-services view for the given day: booked supports, not-yet-confirmed days, day-confirminfos, older days that still need attention (open appointments/consultations) and the relevant holidays. Requires the caller tobe a technician or freelancer with the `ACCESS_DAILY_SUPPORTS` permission. If the employee still has earlier days to confirm,the returned `day` is silently shifted to the oldest unconfirmed date — the requested `day` is not always echoed back.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[WithDayGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .....models.with_day403_error import WithDay403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": WithDay403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .with_day_get_response import WithDayGetResponse

        return await self.request_adapter.send_async(request_info, WithDayGetResponse, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Returns the calling employee's own daily-services view for the given day: booked supports, not-yet-confirmed days, day-confirminfos, older days that still need attention (open appointments/consultations) and the relevant holidays. Requires the caller tobe a technician or freelancer with the `ACCESS_DAILY_SUPPORTS` permission. If the employee still has earlier days to confirm,the returned `day` is silently shifted to the oldest unconfirmed date — the requested `day` is not always echoed back.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> WithDayItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: WithDayItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return WithDayItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def charts(self) -> ChartsRequestBuilder:
        """
        The charts property
        """
        from .charts.charts_request_builder import ChartsRequestBuilder

        return ChartsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def confirm(self) -> ConfirmRequestBuilder:
        """
        The confirm property
        """
        from .confirm.confirm_request_builder import ConfirmRequestBuilder

        return ConfirmRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def statistic_all_services_by_day(self) -> StatisticAllServicesByDayRequestBuilder:
        """
        The statisticAllServicesByDay property
        """
        from .statistic_all_services_by_day.statistic_all_services_by_day_request_builder import StatisticAllServicesByDayRequestBuilder

        return StatisticAllServicesByDayRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class WithDayItemRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

