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
    from ....models.tags403_error import Tags403Error
    from ....models.tns_tag_without_group_tag import TnsTagWithoutGroupTag
    from .assignment.assignment_request_builder import AssignmentRequestBuilder
    from .assignments.assignments_request_builder import AssignmentsRequestBuilder
    from .groups.groups_request_builder import GroupsRequestBuilder
    from .item.tags_item_request_builder import TagsItemRequestBuilder
    from .selection.selection_request_builder import SelectionRequestBuilder
    from .tags_get_response import TagsGetResponse
    from .tags_post_response import TagsPostResponse

class TagsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/tags
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new TagsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/tags", path_parameters)
    
    def by_id(self,id: int) -> TagsItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.v1.tags.item collection
        param id: id of the tag
        Returns: TagsItemRequestBuilder
        """
        if id is None:
            raise TypeError("id cannot be null.")
        from .item.tags_item_request_builder import TagsItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["id"] = id
        return TagsItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[TagsGetResponse]:
        """
        Gets a list of all tagsMust be technician or freelancer in order to use this route!
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[TagsGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ....models.tags403_error import Tags403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Tags403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .tags_get_response import TagsGetResponse

        return await self.request_adapter.send_async(request_info, TagsGetResponse, error_mapping)
    
    async def post(self,body: TnsTagWithoutGroupTag, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[TagsPostResponse]:
        """
        Creates a new tag.Must have the permission to manage tags in the system in order to use this route!
        param body: represents a tag
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[TagsPostResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ....models.tags403_error import Tags403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Tags403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .tags_post_response import TagsPostResponse

        return await self.request_adapter.send_async(request_info, TagsPostResponse, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Gets a list of all tagsMust be technician or freelancer in order to use this route!
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: TnsTagWithoutGroupTag, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Creates a new tag.Must have the permission to manage tags in the system in order to use this route!
        param body: represents a tag
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
    
    def with_url(self,raw_url: str) -> TagsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: TagsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return TagsRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def assignment(self) -> AssignmentRequestBuilder:
        """
        The assignment property
        """
        from .assignment.assignment_request_builder import AssignmentRequestBuilder

        return AssignmentRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def assignments(self) -> AssignmentsRequestBuilder:
        """
        The assignments property
        """
        from .assignments.assignments_request_builder import AssignmentsRequestBuilder

        return AssignmentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def groups(self) -> GroupsRequestBuilder:
        """
        The groups property
        """
        from .groups.groups_request_builder import GroupsRequestBuilder

        return GroupsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def selection(self) -> SelectionRequestBuilder:
        """
        The selection property
        """
        from .selection.selection_request_builder import SelectionRequestBuilder

        return SelectionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class TagsRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class TagsRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

