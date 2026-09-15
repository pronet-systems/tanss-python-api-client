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
    from ....models.priorities403_error import Priorities403Error
    from .item.priorities_item_request_builder import PrioritiesItemRequestBuilder
    from .priorities_get_response import PrioritiesGetResponse
    from .priorities_post_request_body import PrioritiesPostRequestBody
    from .priorities_post_response import PrioritiesPostResponse
    from .sort.sort_request_builder import SortRequestBuilder

class PrioritiesRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/priorities
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new PrioritiesRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/priorities", path_parameters)
    
    def by_id(self,id: str) -> PrioritiesItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.v1.priorities.item collection
        param id: Id of the ticket priority.
        Returns: PrioritiesItemRequestBuilder
        """
        if id is None:
            raise TypeError("id cannot be null.")
        from .item.priorities_item_request_builder import PrioritiesItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["id"] = id
        return PrioritiesItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[PrioritiesGetResponse]:
        """
        Returns the full list of ticket priorities ordered by `sortOrder`. Priorities area customer-configurable enum used to flag urgency on tickets and SLAs. Open toany authenticated user — write operations require the`SERVICE_LEVEL_AGREEMENT_ADMINISTRATION` permission.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[PrioritiesGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ....models.priorities403_error import Priorities403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Priorities403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .priorities_get_response import PrioritiesGetResponse

        return await self.request_adapter.send_async(request_info, PrioritiesGetResponse, error_mapping)
    
    async def post(self,body: PrioritiesPostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[PrioritiesPostResponse]:
        """
        Creates a new ticket priority. The new priority is automatically appended atthe end of the `sortOrder` sequence. Requires the`SERVICE_LEVEL_AGREEMENT_ADMINISTRATION` permission; the caller must also be atechnician or freelancer.
        param body: Request body.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[PrioritiesPostResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ....models.priorities403_error import Priorities403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Priorities403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .priorities_post_response import PrioritiesPostResponse

        return await self.request_adapter.send_async(request_info, PrioritiesPostResponse, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Returns the full list of ticket priorities ordered by `sortOrder`. Priorities area customer-configurable enum used to flag urgency on tickets and SLAs. Open toany authenticated user — write operations require the`SERVICE_LEVEL_AGREEMENT_ADMINISTRATION` permission.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: PrioritiesPostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Creates a new ticket priority. The new priority is automatically appended atthe end of the `sortOrder` sequence. Requires the`SERVICE_LEVEL_AGREEMENT_ADMINISTRATION` permission; the caller must also be atechnician or freelancer.
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
    
    def with_url(self,raw_url: str) -> PrioritiesRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: PrioritiesRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return PrioritiesRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def sort(self) -> SortRequestBuilder:
        """
        The sort property
        """
        from .sort.sort_request_builder import SortRequestBuilder

        return SortRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class PrioritiesRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class PrioritiesRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

