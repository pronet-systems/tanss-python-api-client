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
    from .......models.with_source403_error import WithSource403Error
    from .item.with_assignment_type_item_request_builder import WithAssignmentTypeItemRequestBuilder
    from .with_source import WithSource
    from .with_source_get_response import WithSourceGetResponse
    from .with_source_post_response import WithSourcePostResponse

class WithSourceItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/genericAssignments/for/{sourceType}/{sourceId}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new WithSourceItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/genericAssignments/for/{sourceType}/{sourceId}", path_parameters)
    
    def by_assignment_type(self,assignment_type: str) -> WithAssignmentTypeItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.v1.genericAssignments.for.item.item.item collection
        param assignment_type: Generic assignment type to filter by (e.g. VISIBILITY, AFFECTS).
        Returns: WithAssignmentTypeItemRequestBuilder
        """
        if assignment_type is None:
            raise TypeError("assignment_type cannot be null.")
        from .item.with_assignment_type_item_request_builder import WithAssignmentTypeItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["assignmentType"] = assignment_type
        return WithAssignmentTypeItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[WithSourceGetResponse]:
        """
        Convenience wrapper around the typed variant that hard-codes `assignmentType=VISIBILITY` — i.e. it returns who is allowed tosee the given `sourceType`/`sourceId` (employees/departments listed as visibility targets). Inverted assignments are neverincluded here — use the typed variant `/for/{sourceType}/{sourceId}/{assignmentType}` with `withInverted=true` for that. Requires technician/freelancer with access to the source entity.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[WithSourceGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .......models.with_source403_error import WithSource403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": WithSource403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .with_source_get_response import WithSourceGetResponse

        return await self.request_adapter.send_async(request_info, WithSourceGetResponse, error_mapping)
    
    async def post(self,body: list[WithSource], request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[WithSourcePostResponse]:
        """
        Convenience wrapper that hard-codes `assignmentType=VISIBILITY`: replaces the full visibility list for the given`sourceType`/`sourceId` with the body's array (items not in the body are removed). Requires technician/freelancer plussource-entity access and per-target access for every assignment.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[WithSourcePostResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from .......models.with_source403_error import WithSource403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": WithSource403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .with_source_post_response import WithSourcePostResponse

        return await self.request_adapter.send_async(request_info, WithSourcePostResponse, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Convenience wrapper around the typed variant that hard-codes `assignmentType=VISIBILITY` — i.e. it returns who is allowed tosee the given `sourceType`/`sourceId` (employees/departments listed as visibility targets). Inverted assignments are neverincluded here — use the typed variant `/for/{sourceType}/{sourceId}/{assignmentType}` with `withInverted=true` for that. Requires technician/freelancer with access to the source entity.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: list[WithSource], request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Convenience wrapper that hard-codes `assignmentType=VISIBILITY`: replaces the full visibility list for the given`sourceType`/`sourceId` with the body's array (items not in the body are removed). Requires technician/freelancer plussource-entity access and per-target access for every assignment.
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
    
    def with_url(self,raw_url: str) -> WithSourceItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: WithSourceItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return WithSourceItemRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class WithSourceItemRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class WithSourceItemRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

