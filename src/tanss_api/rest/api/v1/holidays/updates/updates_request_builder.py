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
    from .....models.updates403_error import Updates403Error
    from .item.with_year_item_request_builder import WithYearItemRequestBuilder
    from .updates import Updates
    from .updates_post_response import UpdatesPostResponse

class UpdatesRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/holidays/updates
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new UpdatesRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/holidays/updates", path_parameters)
    
    def by_year(self,year: int) -> WithYearItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.v1.holidays.updates.item collection
        param year: Year for which the public holidays should be computed.
        Returns: WithYearItemRequestBuilder
        """
        if year is None:
            raise TypeError("year cannot be null.")
        from .item.with_year_item_request_builder import WithYearItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["year"] = year
        return WithYearItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def post(self,body: list[Updates], request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[UpdatesPostResponse]:
        """
        Bulk-imports a list of holiday entries — typically the result of one of the `updates/{year}` lookups, after the user has confirmed which entries to take over. Each entry runs through the standard create pipeline (description trim/length check, day/month validation). Requires a user from the own company with `MANAGE_HOLIDAYS`.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[UpdatesPostResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from .....models.updates403_error import Updates403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Updates403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .updates_post_response import UpdatesPostResponse

        return await self.request_adapter.send_async(request_info, UpdatesPostResponse, error_mapping)
    
    def to_post_request_information(self,body: list[Updates], request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Bulk-imports a list of holiday entries — typically the result of one of the `updates/{year}` lookups, after the user has confirmed which entries to take over. Each entry runs through the standard create pipeline (description trim/length check, day/month validation). Requires a user from the own company with `MANAGE_HOLIDAYS`.
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
    
    def with_url(self,raw_url: str) -> UpdatesRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: UpdatesRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return UpdatesRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class UpdatesRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

