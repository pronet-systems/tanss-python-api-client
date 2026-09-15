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
    from ....models.tns_phone_call import TnsPhoneCall
    from ....models.tns_phone_call_configuration import TnsPhoneCallConfiguration
    from ....models.v1403_error import V1403Error
    from .employee_assignment.employee_assignment_request_builder import EmployeeAssignmentRequestBuilder
    from .identify.identify_request_builder import IdentifyRequestBuilder
    from .item.v1_item_request_builder import V1ItemRequestBuilder
    from .notification.notification_request_builder import NotificationRequestBuilder
    from .v1_post_response import V1PostResponse
    from .v1_put_response import V1PutResponse

class V1RequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/calls/v1
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new V1RequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/calls/v1", path_parameters)
    
    def by_id(self,id: int) -> V1ItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.calls.v1.item collection
        param id: Id of the phone call to be fetched
        Returns: V1ItemRequestBuilder
        """
        if id is None:
            raise TypeError("id cannot be null.")
        from .item.v1_item_request_builder import V1ItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["id"] = id
        return V1ItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def post(self,body: TnsPhoneCall, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[V1PostResponse]:
        """
        This api call is used to import a phone call into the database.
        param body: This object represents a phone call
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[V1PostResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ....models.v1403_error import V1403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": V1403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .v1_post_response import V1PostResponse

        return await self.request_adapter.send_async(request_info, V1PostResponse, error_mapping)
    
    async def put(self,body: TnsPhoneCallConfiguration, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[V1PutResponse]:
        """
        Retrieves a list of phone calls from the database, using misc. filter settings
        param body: This object is used to get phone calls based on this filter settings
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[V1PutResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        from ....models.v1403_error import V1403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": V1403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .v1_put_response import V1PutResponse

        return await self.request_adapter.send_async(request_info, V1PutResponse, error_mapping)
    
    def to_post_request_information(self,body: TnsPhoneCall, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        This api call is used to import a phone call into the database.
        param body: This object represents a phone call
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
    
    def to_put_request_information(self,body: TnsPhoneCallConfiguration, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Retrieves a list of phone calls from the database, using misc. filter settings
        param body: This object is used to get phone calls based on this filter settings
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.PUT, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> V1RequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: V1RequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return V1RequestBuilder(self.request_adapter, raw_url)
    
    @property
    def employee_assignment(self) -> EmployeeAssignmentRequestBuilder:
        """
        The employeeAssignment property
        """
        from .employee_assignment.employee_assignment_request_builder import EmployeeAssignmentRequestBuilder

        return EmployeeAssignmentRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def identify(self) -> IdentifyRequestBuilder:
        """
        The identify property
        """
        from .identify.identify_request_builder import IdentifyRequestBuilder

        return IdentifyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def notification(self) -> NotificationRequestBuilder:
        """
        The notification property
        """
        from .notification.notification_request_builder import NotificationRequestBuilder

        return NotificationRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class V1RequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class V1RequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

