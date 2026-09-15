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
    from ......models.with_checklist403_error import WithChecklist403Error
    from .with_checklist_post_response import WithChecklistPostResponse

class WithChecklistItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/checklists/createNewVersion/{checklistId}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new WithChecklistItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/checklists/createNewVersion/{checklistId}{?updateIncludedInChecklists*}", path_parameters)
    
    async def post(self,request_configuration: Optional[RequestConfiguration[WithChecklistItemRequestBuilderPostQueryParameters]] = None) -> Optional[WithChecklistPostResponse]:
        """
        Creates a successor version of an existing checklist. The new checklist is linked to the source via predecessor/successor ids; the source is deactivated so that future ticket assignments pick up the latest version while in-flight processed instances keep referring to the old version. If `updateIncludedInChecklists` is true, parent checklists that embed the source as a sub-checklist are automatically rewired to the new version.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[WithChecklistPostResponse]
        """
        request_info = self.to_post_request_information(
            request_configuration
        )
        from ......models.with_checklist403_error import WithChecklist403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": WithChecklist403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .with_checklist_post_response import WithChecklistPostResponse

        return await self.request_adapter.send_async(request_info, WithChecklistPostResponse, error_mapping)
    
    def to_post_request_information(self,request_configuration: Optional[RequestConfiguration[WithChecklistItemRequestBuilderPostQueryParameters]] = None) -> RequestInformation:
        """
        Creates a successor version of an existing checklist. The new checklist is linked to the source via predecessor/successor ids; the source is deactivated so that future ticket assignments pick up the latest version while in-flight processed instances keep referring to the old version. If `updateIncludedInChecklists` is true, parent checklists that embed the source as a sub-checklist are automatically rewired to the new version.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.POST, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> WithChecklistItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: WithChecklistItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return WithChecklistItemRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class WithChecklistItemRequestBuilderPostQueryParameters():
        """
        Creates a successor version of an existing checklist. The new checklist is linked to the source via predecessor/successor ids; the source is deactivated so that future ticket assignments pick up the latest version while in-flight processed instances keep referring to the old version. If `updateIncludedInChecklists` is true, parent checklists that embed the source as a sub-checklist are automatically rewired to the new version.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "update_included_in_checklists":
                return "updateIncludedInChecklists"
            return original_name
        
        # If true, rewire parent checklists embedding the source to the new version.
        update_included_in_checklists: Optional[bool] = None

    
    @dataclass
    class WithChecklistItemRequestBuilderPostRequestConfiguration(RequestConfiguration[WithChecklistItemRequestBuilderPostQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

