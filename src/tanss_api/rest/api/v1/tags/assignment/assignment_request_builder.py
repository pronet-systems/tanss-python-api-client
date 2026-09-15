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
    from .....models.assignment403_error import Assignment403Error
    from .....models.tns_tag_assignment import TnsTagAssignment
    from .assignment_get_response import AssignmentGetResponse
    from .assignment_post_response import AssignmentPostResponse
    from .assignment_put_response import AssignmentPutResponse
    from .log.log_request_builder import LogRequestBuilder

class AssignmentRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/tags/assignment
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new AssignmentRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/tags/assignment", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[AssignmentRequestBuilderDeleteQueryParameters]] = None) -> None:
        """
        Removes a tag from an assignment.Must be technician/freelancer and have access to the assignment!
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, None)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[AssignmentRequestBuilderGetQueryParameters]] = None) -> Optional[AssignmentGetResponse]:
        """
        Gets alist of all tags who are assigned to an entity (for example ticket).Must be technician/freelancer and have access to the assignment!
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[AssignmentGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .....models.assignment403_error import Assignment403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Assignment403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .assignment_get_response import AssignmentGetResponse

        return await self.request_adapter.send_async(request_info, AssignmentGetResponse, error_mapping)
    
    async def post(self,body: TnsTagAssignment, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[AssignmentPostResponse]:
        """
        Assigns a tag to an entity.Must be technician/freelancer and have access to the assignment!
        param body: represents a tag assigned to an assignment (ticket, pc, server)
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[AssignmentPostResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from .....models.assignment403_error import Assignment403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Assignment403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .assignment_post_response import AssignmentPostResponse

        return await self.request_adapter.send_async(request_info, AssignmentPostResponse, error_mapping)
    
    async def put(self,body: list[int], request_configuration: Optional[RequestConfiguration[AssignmentRequestBuilderPutQueryParameters]] = None) -> Optional[AssignmentPutResponse]:
        """
        Assigns multiplke tags at one for a specific device/assignment. All tag ids are given.The system automatically determines wbhich of those tags shall be created or removed.Must be technician/freelancer and have access to the assignment!
        param body: ids of all tags in for this device/assignment
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[AssignmentPutResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        from .....models.assignment403_error import Assignment403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Assignment403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .assignment_put_response import AssignmentPutResponse

        return await self.request_adapter.send_async(request_info, AssignmentPutResponse, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[AssignmentRequestBuilderDeleteQueryParameters]] = None) -> RequestInformation:
        """
        Removes a tag from an assignment.Must be technician/freelancer and have access to the assignment!
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, '{+baseurl}/api/v1/tags/assignment?linkId={linkId}&linkTypeId={linkTypeId}&tagId={tagId}', self.path_parameters)
        request_info.configure(request_configuration)
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[AssignmentRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Gets alist of all tags who are assigned to an entity (for example ticket).Must be technician/freelancer and have access to the assignment!
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, '{+baseurl}/api/v1/tags/assignment?linkId={linkId}&linkTypeId={linkTypeId}', self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: TnsTagAssignment, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Assigns a tag to an entity.Must be technician/freelancer and have access to the assignment!
        param body: represents a tag assigned to an assignment (ticket, pc, server)
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
    
    def to_put_request_information(self,body: list[int], request_configuration: Optional[RequestConfiguration[AssignmentRequestBuilderPutQueryParameters]] = None) -> RequestInformation:
        """
        Assigns multiplke tags at one for a specific device/assignment. All tag ids are given.The system automatically determines wbhich of those tags shall be created or removed.Must be technician/freelancer and have access to the assignment!
        param body: ids of all tags in for this device/assignment
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.PUT, '{+baseurl}/api/v1/tags/assignment?linkId={linkId}&linkTypeId={linkTypeId}', self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_scalar(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> AssignmentRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: AssignmentRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return AssignmentRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def log(self) -> LogRequestBuilder:
        """
        The log property
        """
        from .log.log_request_builder import LogRequestBuilder

        return LogRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class AssignmentRequestBuilderDeleteQueryParameters():
        """
        Removes a tag from an assignment.Must be technician/freelancer and have access to the assignment!
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
            if original_name == "tag_id":
                return "tagId"
            return original_name
        
        # id of the assignment
        link_id: Optional[int] = None

        # linkType of the assignment
        link_type_id: Optional[int] = None

        # id of the tag
        tag_id: Optional[int] = None

    
    @dataclass
    class AssignmentRequestBuilderDeleteRequestConfiguration(RequestConfiguration[AssignmentRequestBuilderDeleteQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class AssignmentRequestBuilderGetQueryParameters():
        """
        Gets alist of all tags who are assigned to an entity (for example ticket).Must be technician/freelancer and have access to the assignment!
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
        
        # id of the assignment
        link_id: Optional[int] = None

        # linkType of the assignment
        link_type_id: Optional[int] = None

    
    @dataclass
    class AssignmentRequestBuilderGetRequestConfiguration(RequestConfiguration[AssignmentRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class AssignmentRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class AssignmentRequestBuilderPutQueryParameters():
        """
        Assigns multiplke tags at one for a specific device/assignment. All tag ids are given.The system automatically determines wbhich of those tags shall be created or removed.Must be technician/freelancer and have access to the assignment!
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
        
        # id of the assignment
        link_id: Optional[int] = None

        # linkType of the assignment
        link_type_id: Optional[int] = None

    
    @dataclass
    class AssignmentRequestBuilderPutRequestConfiguration(RequestConfiguration[AssignmentRequestBuilderPutQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

