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
    from .....models.planning_additional_types403_error import PlanningAdditionalTypes403Error
    from .item.planning_additional_types_item_request_builder import PlanningAdditionalTypesItemRequestBuilder
    from .planning_additional_types_get_response import PlanningAdditionalTypesGetResponse

class PlanningAdditionalTypesRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/vacationRequests/planningAdditionalTypes
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new PlanningAdditionalTypesRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/vacationRequests/planningAdditionalTypes", path_parameters)
    
    def by_id(self,id: str) -> PlanningAdditionalTypesItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.v1.vacationRequests.planningAdditionalTypes.item collection
        param id: Id of the planning additional type
        Returns: PlanningAdditionalTypesItemRequestBuilder
        """
        if id is None:
            raise TypeError("id cannot be null.")
        from .item.planning_additional_types_item_request_builder import PlanningAdditionalTypesItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["id"] = id
        return PlanningAdditionalTypesItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[PlanningAdditionalTypesGetResponse]:
        """
        Gets a list of absence/custom types
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[PlanningAdditionalTypesGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .....models.planning_additional_types403_error import PlanningAdditionalTypes403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": PlanningAdditionalTypes403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .planning_additional_types_get_response import PlanningAdditionalTypesGetResponse

        return await self.request_adapter.send_async(request_info, PlanningAdditionalTypesGetResponse, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Gets a list of absence/custom types
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> PlanningAdditionalTypesRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: PlanningAdditionalTypesRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return PlanningAdditionalTypesRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class PlanningAdditionalTypesRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

