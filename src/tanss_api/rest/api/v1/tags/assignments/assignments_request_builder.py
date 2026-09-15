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
    from .....models.assignments403_error import Assignments403Error

class AssignmentsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/tags/assignments
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new AssignmentsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/tags/assignments?linkId={linkId}&linkTypeId={linkTypeId}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[AssignmentsRequestBuilderDeleteQueryParameters]] = None) -> None:
        """
        Bulk-removes every tag assignment from the given entity in one call.Use this when you want to clear all tags from a ticket / device / etc.rather than removing individual assignments via`DELETE /api/v1/tags/assignment`.Must be a technician or freelancer with access to the assignment.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from .....models.assignments403_error import Assignments403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Assignments403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[AssignmentsRequestBuilderDeleteQueryParameters]] = None) -> RequestInformation:
        """
        Bulk-removes every tag assignment from the given entity in one call.Use this when you want to clear all tags from a ticket / device / etc.rather than removing individual assignments via`DELETE /api/v1/tags/assignment`.Must be a technician or freelancer with access to the assignment.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> AssignmentsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: AssignmentsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return AssignmentsRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class AssignmentsRequestBuilderDeleteQueryParameters():
        """
        Bulk-removes every tag assignment from the given entity in one call.Use this when you want to clear all tags from a ticket / device / etc.rather than removing individual assignments via`DELETE /api/v1/tags/assignment`.Must be a technician or freelancer with access to the assignment.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "link_id":
                return "linkId"
            if original_name == "link_type_id":
                return "linkTypeId"
            return original_name
        
        # id of the entity whose tag assignments should be cleared
        link_id: Optional[int] = None

        # linkType of the assignment (numeric id, e.g. 1 = ticket)
        link_type_id: Optional[int] = None

    
    @dataclass
    class AssignmentsRequestBuilderDeleteRequestConfiguration(RequestConfiguration[AssignmentsRequestBuilderDeleteQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

