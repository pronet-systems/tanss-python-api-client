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
    from ....models.tns_vacation_request import TnsVacationRequest
    from ....models.vacation_requests403_error import VacationRequests403Error
    from .item.vacation_requests_item_request_builder import VacationRequestsItemRequestBuilder
    from .list_.list_request_builder import ListRequestBuilder
    from .planning_additional_types.planning_additional_types_request_builder import PlanningAdditionalTypesRequestBuilder
    from .properties.properties_request_builder import PropertiesRequestBuilder
    from .vacation_days.vacation_days_request_builder import VacationDaysRequestBuilder
    from .vacation_requests_post_response import VacationRequestsPostResponse

class VacationRequestsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/vacationRequests
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new VacationRequestsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/vacationRequests", path_parameters)
    
    def by_id(self,id: int) -> VacationRequestsItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.v1.vacationRequests.item collection
        param id: Id of the vacation request
        Returns: VacationRequestsItemRequestBuilder
        """
        if id is None:
            raise TypeError("id cannot be null.")
        from .item.vacation_requests_item_request_builder import VacationRequestsItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["id"] = id
        return VacationRequestsItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def post(self,body: TnsVacationRequest, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[VacationRequestsPostResponse]:
        """
        creates a vacation request
        param body: vacation request (or illness, absence, custom type, overtime, standBy, custom). If a custom type shall be stored, use the planningAdditionalId property to specify the custom type
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[VacationRequestsPostResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ....models.vacation_requests403_error import VacationRequests403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": VacationRequests403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .vacation_requests_post_response import VacationRequestsPostResponse

        return await self.request_adapter.send_async(request_info, VacationRequestsPostResponse, error_mapping)
    
    def to_post_request_information(self,body: TnsVacationRequest, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        creates a vacation request
        param body: vacation request (or illness, absence, custom type, overtime, standBy, custom). If a custom type shall be stored, use the planningAdditionalId property to specify the custom type
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
    
    def with_url(self,raw_url: str) -> VacationRequestsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: VacationRequestsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return VacationRequestsRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def list_(self) -> ListRequestBuilder:
        """
        The list property
        """
        from .list_.list_request_builder import ListRequestBuilder

        return ListRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def planning_additional_types(self) -> PlanningAdditionalTypesRequestBuilder:
        """
        The planningAdditionalTypes property
        """
        from .planning_additional_types.planning_additional_types_request_builder import PlanningAdditionalTypesRequestBuilder

        return PlanningAdditionalTypesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def properties(self) -> PropertiesRequestBuilder:
        """
        The properties property
        """
        from .properties.properties_request_builder import PropertiesRequestBuilder

        return PropertiesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def vacation_days(self) -> VacationDaysRequestBuilder:
        """
        The vacationDays property
        """
        from .vacation_days.vacation_days_request_builder import VacationDaysRequestBuilder

        return VacationDaysRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class VacationRequestsRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

