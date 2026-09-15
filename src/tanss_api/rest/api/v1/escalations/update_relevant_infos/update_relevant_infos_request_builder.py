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
    from .....models.update_relevant_infos403_error import UpdateRelevantInfos403Error
    from .update_relevant_infos_put_request_body import UpdateRelevantInfosPutRequestBody
    from .update_relevant_infos_put_response import UpdateRelevantInfosPutResponse

class UpdateRelevantInfosRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/escalations/updateRelevantInfos
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new UpdateRelevantInfosRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/escalations/updateRelevantInfos", path_parameters)
    
    async def put(self,body: UpdateRelevantInfosPutRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[UpdateRelevantInfosPutResponse]:
        """
        Rebuilds the cached "relevant info" snapshots used by the escalation engine to evaluate rules quickly (e.g. last status change timestamps, deadlines). Scope can be limited via the body to specific tickets/rules; otherwise everything is refreshed. Requires MANAGE_TICKET_ESCALATION.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[UpdateRelevantInfosPutResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        from .....models.update_relevant_infos403_error import UpdateRelevantInfos403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": UpdateRelevantInfos403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .update_relevant_infos_put_response import UpdateRelevantInfosPutResponse

        return await self.request_adapter.send_async(request_info, UpdateRelevantInfosPutResponse, error_mapping)
    
    def to_put_request_information(self,body: UpdateRelevantInfosPutRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Rebuilds the cached "relevant info" snapshots used by the escalation engine to evaluate rules quickly (e.g. last status change timestamps, deadlines). Scope can be limited via the body to specific tickets/rules; otherwise everything is refreshed. Requires MANAGE_TICKET_ESCALATION.
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
    
    def with_url(self,raw_url: str) -> UpdateRelevantInfosRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: UpdateRelevantInfosRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return UpdateRelevantInfosRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class UpdateRelevantInfosRequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

