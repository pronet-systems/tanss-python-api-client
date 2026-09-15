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
    from ....models.timeline403_error import Timeline403Error
    from .outlook_sync.outlook_sync_request_builder import OutlookSyncRequestBuilder
    from .timeline_put_request_body import TimelinePutRequestBody
    from .timeline_put_response import TimelinePutResponse

class TimelineRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/timeline
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new TimelineRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/timeline", path_parameters)
    
    async def put(self,body: TimelinePutRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[TimelinePutResponse]:
        """
        Returns the technician timeline used by the capacity-planning view: per-employee, per-day buckets showing absences, scheduled supports and free capacity in minutes for the requested timeframe. Only technicians or freelancers may call it; other roles receive `403`.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[TimelinePutResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        from ....models.timeline403_error import Timeline403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Timeline403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .timeline_put_response import TimelinePutResponse

        return await self.request_adapter.send_async(request_info, TimelinePutResponse, error_mapping)
    
    def to_put_request_information(self,body: TimelinePutRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Returns the technician timeline used by the capacity-planning view: per-employee, per-day buckets showing absences, scheduled supports and free capacity in minutes for the requested timeframe. Only technicians or freelancers may call it; other roles receive `403`.
        param body: The request body
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
    
    def with_url(self,raw_url: str) -> TimelineRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: TimelineRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return TimelineRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def outlook_sync(self) -> OutlookSyncRequestBuilder:
        """
        The outlookSync property
        """
        from .outlook_sync.outlook_sync_request_builder import OutlookSyncRequestBuilder

        return OutlookSyncRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class TimelineRequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

