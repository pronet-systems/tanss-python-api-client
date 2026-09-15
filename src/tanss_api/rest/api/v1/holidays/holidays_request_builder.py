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
    from ....models.holidays403_error import Holidays403Error
    from .holidays_get_response import HolidaysGetResponse
    from .holidays_post_request_body import HolidaysPostRequestBody
    from .holidays_post_response import HolidaysPostResponse
    from .item.with_year_item_request_builder import WithYearItemRequestBuilder
    from .updates.updates_request_builder import UpdatesRequestBuilder

class HolidaysRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/holidays
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new HolidaysRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/holidays", path_parameters)
    
    def by_year(self,year: int) -> WithYearItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.v1.holidays.item collection
        param year: Year part of the holiday key (use 0 for a recurring entry).
        Returns: WithYearItemRequestBuilder
        """
        if year is None:
            raise TypeError("year cannot be null.")
        from .item.with_year_item_request_builder import WithYearItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["year"] = year
        return WithYearItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[HolidaysGetResponse]:
        """
        Returns every stored holiday entry (recurring entries have `year: 0`, year-specific entries carry the actual year). Read access requires the caller to be a user from the own company; no extra permission is needed for view.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[HolidaysGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ....models.holidays403_error import Holidays403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Holidays403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .holidays_get_response import HolidaysGetResponse

        return await self.request_adapter.send_async(request_info, HolidaysGetResponse, error_mapping)
    
    async def post(self,body: HolidaysPostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[HolidaysPostResponse]:
        """
        Creates a new holiday entry. The controller rejects the request if a holiday for the same day/month/year combination already exists. Requires the caller to be a user from the own company with `MANAGE_HOLIDAYS`; the description is trimmed and capped at 40 characters before persisting.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[HolidaysPostResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ....models.holidays403_error import Holidays403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Holidays403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .holidays_post_response import HolidaysPostResponse

        return await self.request_adapter.send_async(request_info, HolidaysPostResponse, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Returns every stored holiday entry (recurring entries have `year: 0`, year-specific entries carry the actual year). Read access requires the caller to be a user from the own company; no extra permission is needed for view.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: HolidaysPostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Creates a new holiday entry. The controller rejects the request if a holiday for the same day/month/year combination already exists. Requires the caller to be a user from the own company with `MANAGE_HOLIDAYS`; the description is trimmed and capped at 40 characters before persisting.
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
    
    def with_url(self,raw_url: str) -> HolidaysRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: HolidaysRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return HolidaysRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def updates(self) -> UpdatesRequestBuilder:
        """
        The updates property
        """
        from .updates.updates_request_builder import UpdatesRequestBuilder

        return UpdatesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class HolidaysRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class HolidaysRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

