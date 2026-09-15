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
    from .assignments_post_request_body import AssignmentsPostRequestBody
    from .assignments_post_response import AssignmentsPostResponse
    from .item.with_template_item_request_builder import WithTemplateItemRequestBuilder

class AssignmentsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/templates/assignments
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new AssignmentsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/templates/assignments", path_parameters)
    
    def by_template_id(self,template_id: int) -> WithTemplateItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.v1.templates.assignments.item collection
        param template_id: Id of the object template whose assignments are requested.
        Returns: WithTemplateItemRequestBuilder
        """
        if template_id is None:
            raise TypeError("template_id cannot be null.")
        from .item.with_template_item_request_builder import WithTemplateItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["templateId"] = template_id
        return WithTemplateItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[AssignmentsRequestBuilderDeleteQueryParameters]] = None) -> None:
        """
        Removes the assignment binding (`templateId`, `linkTypeId`, `linkId`) so the template is no longer offeredto that company / employee / department / ticket type, ... The caller must be allowed to modify theparent template.
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
    
    async def post(self,body: AssignmentsPostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[AssignmentsPostResponse]:
        """
        Binds a template to a target entity (company, employee, department, ticket type, ...) so that it appears asavailable when working with that entity. Standard admin permission checks apply, and the caller must beallowed to modify the parent template.
        param body: Request body.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[AssignmentsPostResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from .....models.assignments403_error import Assignments403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Assignments403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .assignments_post_response import AssignmentsPostResponse

        return await self.request_adapter.send_async(request_info, AssignmentsPostResponse, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[AssignmentsRequestBuilderDeleteQueryParameters]] = None) -> RequestInformation:
        """
        Removes the assignment binding (`templateId`, `linkTypeId`, `linkId`) so the template is no longer offeredto that company / employee / department / ticket type, ... The caller must be allowed to modify theparent template.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, '{+baseurl}/api/v1/templates/assignments?linkId={linkId}&linkTypeId={linkTypeId}&templateId={templateId}', self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: AssignmentsPostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Binds a template to a target entity (company, employee, department, ticket type, ...) so that it appears asavailable when working with that entity. Standard admin permission checks apply, and the caller must beallowed to modify the parent template.
        param body: Request body.
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
        Removes the assignment binding (`templateId`, `linkTypeId`, `linkId`) so the template is no longer offeredto that company / employee / department / ticket type, ... The caller must be allowed to modify theparent template.
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
            if original_name == "template_id":
                return "templateId"
            return original_name
        
        # Id of the linked entity to unbind from the template.
        link_id: Optional[int] = None

        # Type of the linked entity (company, employee, department, ticket type, ...).
        link_type_id: Optional[int] = None

        # Id of the object template the assignment belongs to.
        template_id: Optional[int] = None

    
    @dataclass
    class AssignmentsRequestBuilderDeleteRequestConfiguration(RequestConfiguration[AssignmentsRequestBuilderDeleteQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class AssignmentsRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

