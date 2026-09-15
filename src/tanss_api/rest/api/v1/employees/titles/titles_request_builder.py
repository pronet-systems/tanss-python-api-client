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
    from .....models.titles403_error import Titles403Error
    from .item.titles_item_request_builder import TitlesItemRequestBuilder
    from .titles_get_response import TitlesGetResponse
    from .titles_post_request_body import TitlesPostRequestBody
    from .titles_post_response import TitlesPostResponse

class TitlesRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/employees/titles
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new TitlesRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/employees/titles", path_parameters)
    
    def by_id(self,id: str) -> TitlesItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.v1.employees.titles.item collection
        param id: Id of the employee title to delete.
        Returns: TitlesItemRequestBuilder
        """
        if id is None:
            raise TypeError("id cannot be null.")
        from .item.titles_item_request_builder import TitlesItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["id"] = id
        return TitlesItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[TitlesGetResponse]:
        """
        Returns all employee titles. Caller must be a technician or freelancerwith the `BASE_DATA_MANAGEMENT_SYSTEM_TABLES` permission.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[TitlesGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .....models.titles403_error import Titles403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Titles403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .titles_get_response import TitlesGetResponse

        return await self.request_adapter.send_async(request_info, TitlesGetResponse, error_mapping)
    
    async def post(self,body: TitlesPostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[TitlesPostResponse]:
        """
        Creates a new employee title. Caller must be a technician or freelancerwith the `BASE_DATA_MANAGEMENT_SYSTEM_TABLES` permission.
        param body: Request body.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[TitlesPostResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from .....models.titles403_error import Titles403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Titles403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .titles_post_response import TitlesPostResponse

        return await self.request_adapter.send_async(request_info, TitlesPostResponse, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Returns all employee titles. Caller must be a technician or freelancerwith the `BASE_DATA_MANAGEMENT_SYSTEM_TABLES` permission.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: TitlesPostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Creates a new employee title. Caller must be a technician or freelancerwith the `BASE_DATA_MANAGEMENT_SYSTEM_TABLES` permission.
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
    
    def with_url(self,raw_url: str) -> TitlesRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: TitlesRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return TitlesRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class TitlesRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class TitlesRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

