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
    from ......models.charts403_error import Charts403Error
    from .charts_get_response import ChartsGetResponse
    from .statistic_all_services_by_day.statistic_all_services_by_day_request_builder import StatisticAllServicesByDayRequestBuilder

class ChartsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/ownDailyServices/{day}/charts
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new ChartsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/ownDailyServices/{day}/charts", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[ChartsGetResponse]:
        """
        Returns the chart data (working-schedule minutes, public/internal support minutes, productivity ratio) for the calling employeeon the given day — the "Wie viel habe ich heute gebucht?" doughnut. Requires technician/freelancer with `ACCESS_DAILY_SUPPORTS`.Always restricted to the caller's own user id; for foreign employees use the `statisticAllServicesByDay` variant instead.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ChartsGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ......models.charts403_error import Charts403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Charts403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .charts_get_response import ChartsGetResponse

        return await self.request_adapter.send_async(request_info, ChartsGetResponse, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Returns the chart data (working-schedule minutes, public/internal support minutes, productivity ratio) for the calling employeeon the given day — the "Wie viel habe ich heute gebucht?" doughnut. Requires technician/freelancer with `ACCESS_DAILY_SUPPORTS`.Always restricted to the caller's own user id; for foreign employees use the `statisticAllServicesByDay` variant instead.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> ChartsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: ChartsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return ChartsRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def statistic_all_services_by_day(self) -> StatisticAllServicesByDayRequestBuilder:
        """
        The statisticAllServicesByDay property
        """
        from .statistic_all_services_by_day.statistic_all_services_by_day_request_builder import StatisticAllServicesByDayRequestBuilder

        return StatisticAllServicesByDayRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class ChartsRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

