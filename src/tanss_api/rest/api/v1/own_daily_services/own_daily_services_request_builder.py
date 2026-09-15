from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.with_day_item_request_builder import WithDayItemRequestBuilder

class OwnDailyServicesRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/ownDailyServices
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new OwnDailyServicesRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/ownDailyServices", path_parameters)
    
    def by_day(self,day: str) -> WithDayItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.v1.ownDailyServices.item collection
        param day: Day to fetch the daily-services view for, formatted as YYYY-MM-DD.
        Returns: WithDayItemRequestBuilder
        """
        if day is None:
            raise TypeError("day cannot be null.")
        from .item.with_day_item_request_builder import WithDayItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["day"] = day
        return WithDayItemRequestBuilder(self.request_adapter, url_tpl_params)
    

