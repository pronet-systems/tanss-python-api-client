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
    from .....models.change_requests403_error import ChangeRequests403Error
    from .change_requests_get_response import ChangeRequestsGetResponse
    from .item.with_employee_item_request_builder import WithEmployeeItemRequestBuilder

class ChangeRequestsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/timestamps/changeRequests
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new ChangeRequestsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/timestamps/changeRequests", path_parameters)
    
    def by_employee_id(self,employee_id: int) -> WithEmployeeItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.v1.timestamps.changeRequests.item collection
        param employee_id: Id of the employee whose change requests are cleared
        Returns: WithEmployeeItemRequestBuilder
        """
        if employee_id is None:
            raise TypeError("employee_id cannot be null.")
        from .item.with_employee_item_request_builder import WithEmployeeItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["employeeId"] = employee_id
        return WithEmployeeItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[ChangeRequestsGetResponse]:
        """
        Returns all open timestamp change requests that the caller is permitted to see, grouped per employee and day,with their statistics and day-closing values attached (the running balance is intentionally omitted because therequests are not yet applied). Use this as the inbox for supervisors who approve or reject pending timestampcorrections.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ChangeRequestsGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .....models.change_requests403_error import ChangeRequests403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": ChangeRequests403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .change_requests_get_response import ChangeRequestsGetResponse

        return await self.request_adapter.send_async(request_info, ChangeRequestsGetResponse, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Returns all open timestamp change requests that the caller is permitted to see, grouped per employee and day,with their statistics and day-closing values attached (the running balance is intentionally omitted because therequests are not yet applied). Use this as the inbox for supervisors who approve or reject pending timestampcorrections.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> ChangeRequestsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: ChangeRequestsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return ChangeRequestsRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class ChangeRequestsRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

