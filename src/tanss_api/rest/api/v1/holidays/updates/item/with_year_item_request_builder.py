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
    from ......models.with_year403_error import WithYear403Error
    from .item.with_state_item_request_builder import WithStateItemRequestBuilder
    from .with_year_get_response import WithYearGetResponse

class WithYearItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/holidays/updates/{year}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new WithYearItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/holidays/updates/{year}", path_parameters)
    
    def by_state(self,state: str) -> WithStateItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.v1.holidays.updates.item.item collection
        param state: German federal state code to filter the holidays (e.g. BY, BW, NW).
        Returns: WithStateItemRequestBuilder
        """
        if state is None:
            raise TypeError("state cannot be null.")
        from .item.with_state_item_request_builder import WithStateItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["state"] = state
        return WithStateItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[WithYearGetResponse]:
        """
        Returns the canonical list of German public holidays for a given year without any federal-state filter (state defaults to `NONE`). Used by the admin UI to pre-fill the holiday import. Each entry tells whether the date is fixed (always same day/month) or movable (Easter-derived). Requires a user from the own company with `MANAGE_HOLIDAYS`.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[WithYearGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ......models.with_year403_error import WithYear403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": WithYear403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .with_year_get_response import WithYearGetResponse

        return await self.request_adapter.send_async(request_info, WithYearGetResponse, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Returns the canonical list of German public holidays for a given year without any federal-state filter (state defaults to `NONE`). Used by the admin UI to pre-fill the holiday import. Each entry tells whether the date is fixed (always same day/month) or movable (Easter-derived). Requires a user from the own company with `MANAGE_HOLIDAYS`.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> WithYearItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: WithYearItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return WithYearItemRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class WithYearItemRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

