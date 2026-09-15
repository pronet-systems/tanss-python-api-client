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
    from ........models.with_assignment_type403_error import WithAssignmentType403Error
    from .with_assignment_type import WithAssignmentType
    from .with_assignment_type_get_response import WithAssignmentTypeGetResponse
    from .with_assignment_type_post_response import WithAssignmentTypePostResponse

class WithAssignmentTypeItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/genericAssignments/for/{sourceType}/{sourceId}/{assignmentType}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new WithAssignmentTypeItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/genericAssignments/for/{sourceType}/{sourceId}/{assignmentType}{?withInverted*}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[WithAssignmentTypeItemRequestBuilderGetQueryParameters]] = None) -> Optional[WithAssignmentTypeGetResponse]:
        """
        Returns all generic assignments where the given `sourceType`/`sourceId` is the source — filtered by the requested`assignmentType` (e.g. `VISIBILITY`, `AFFECTS`). With `withInverted=true` the result also contains assignments where thesame entity is the target instead, useful for showing both sides of bidirectional links. Requires the caller to be atechnician or freelancer and to have access to the source entity (delegated to the matching source strategy).
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[WithAssignmentTypeGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ........models.with_assignment_type403_error import WithAssignmentType403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": WithAssignmentType403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .with_assignment_type_get_response import WithAssignmentTypeGetResponse

        return await self.request_adapter.send_async(request_info, WithAssignmentTypeGetResponse, error_mapping)
    
    async def post(self,body: list[WithAssignmentType], request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[WithAssignmentTypePostResponse]:
        """
        Replaces the full set of generic assignments of the given `assignmentType` for `sourceType`/`sourceId` with the body's array —this is a "set" operation, not an append: assignments not contained in the body are deleted. Requires technician/freelancerplus access to the source entity (and per-target access to every assigned entity). The returned list is the persisted,output-prepared set after the update.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[WithAssignmentTypePostResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ........models.with_assignment_type403_error import WithAssignmentType403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": WithAssignmentType403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .with_assignment_type_post_response import WithAssignmentTypePostResponse

        return await self.request_adapter.send_async(request_info, WithAssignmentTypePostResponse, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[WithAssignmentTypeItemRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Returns all generic assignments where the given `sourceType`/`sourceId` is the source — filtered by the requested`assignmentType` (e.g. `VISIBILITY`, `AFFECTS`). With `withInverted=true` the result also contains assignments where thesame entity is the target instead, useful for showing both sides of bidirectional links. Requires the caller to be atechnician or freelancer and to have access to the source entity (delegated to the matching source strategy).
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: list[WithAssignmentType], request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Replaces the full set of generic assignments of the given `assignmentType` for `sourceType`/`sourceId` with the body's array —this is a "set" operation, not an append: assignments not contained in the body are deleted. Requires technician/freelancerplus access to the source entity (and per-target access to every assigned entity). The returned list is the persisted,output-prepared set after the update.
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
    
    def with_url(self,raw_url: str) -> WithAssignmentTypeItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: WithAssignmentTypeItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return WithAssignmentTypeItemRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class WithAssignmentTypeItemRequestBuilderGetQueryParameters():
        """
        Returns all generic assignments where the given `sourceType`/`sourceId` is the source — filtered by the requested`assignmentType` (e.g. `VISIBILITY`, `AFFECTS`). With `withInverted=true` the result also contains assignments where thesame entity is the target instead, useful for showing both sides of bidirectional links. Requires the caller to be atechnician or freelancer and to have access to the source entity (delegated to the matching source strategy).
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "with_inverted":
                return "withInverted"
            return original_name
        
        # If true, also include assignments where the entity is the target.
        with_inverted: Optional[bool] = None

    
    @dataclass
    class WithAssignmentTypeItemRequestBuilderGetRequestConfiguration(RequestConfiguration[WithAssignmentTypeItemRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class WithAssignmentTypeItemRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

