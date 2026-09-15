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
    from ......models.with_phase403_error import WithPhase403Error
    from .with_phase_put_request_body import WithPhasePutRequestBody
    from .with_phase_put_response import WithPhasePutResponse

class WithPhaseItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/projects/phases/{phaseId}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new WithPhaseItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/projects/phases/{phaseId}{?adjustEnd*,adjustStart*}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Removes a phase from a project. The deletion fails if the phase still has child tickets linked.Permissions are checked against the parent project's access rules.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ......models.with_phase403_error import WithPhase403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": WithPhase403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def put(self,body: WithPhasePutRequestBody, request_configuration: Optional[RequestConfiguration[WithPhaseItemRequestBuilderPutQueryParameters]] = None) -> Optional[WithPhasePutResponse]:
        """
        Updates a project phase (name, dates, billing/clearance settings, rank). When`adjustStart` / `adjustEnd` are set, neighbouring phases are automaticallyshifted to keep the project timeline consistent. The caller must have access tothe parent project.
        param body: Request body.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[WithPhasePutResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        from ......models.with_phase403_error import WithPhase403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": WithPhase403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .with_phase_put_response import WithPhasePutResponse

        return await self.request_adapter.send_async(request_info, WithPhasePutResponse, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Removes a phase from a project. The deletion fails if the phase still has child tickets linked.Permissions are checked against the parent project's access rules.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_put_request_information(self,body: WithPhasePutRequestBody, request_configuration: Optional[RequestConfiguration[WithPhaseItemRequestBuilderPutQueryParameters]] = None) -> RequestInformation:
        """
        Updates a project phase (name, dates, billing/clearance settings, rank). When`adjustStart` / `adjustEnd` are set, neighbouring phases are automaticallyshifted to keep the project timeline consistent. The caller must have access tothe parent project.
        param body: Request body.
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
    
    def with_url(self,raw_url: str) -> WithPhaseItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: WithPhaseItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return WithPhaseItemRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class WithPhaseItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class WithPhaseItemRequestBuilderPutQueryParameters():
        """
        Updates a project phase (name, dates, billing/clearance settings, rank). When`adjustStart` / `adjustEnd` are set, neighbouring phases are automaticallyshifted to keep the project timeline consistent. The caller must have access tothe parent project.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "adjust_end":
                return "adjustEnd"
            if original_name == "adjust_start":
                return "adjustStart"
            return original_name
        
        # When true, shift neighbouring phases to keep the timeline consistent after changing this phase's end.
        adjust_end: Optional[bool] = None

        # When true, shift neighbouring phases to keep the timeline consistent after changing this phase's start.
        adjust_start: Optional[bool] = None

    
    @dataclass
    class WithPhaseItemRequestBuilderPutRequestConfiguration(RequestConfiguration[WithPhaseItemRequestBuilderPutQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

