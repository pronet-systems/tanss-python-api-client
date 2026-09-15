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
    from .assignment_post_request_body import AssignmentPostRequestBody
    from .assignment_post_response import AssignmentPostResponse
    from .item.with_rule_item_request_builder import WithRuleItemRequestBuilder

class AssignmentRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/recurrence/assignment
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new AssignmentRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/recurrence/assignment", path_parameters)
    
    def by_rule_id(self,rule_id: int) -> WithRuleItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.v1.recurrence.assignment.item collection
        param rule_id: Id of the recurrence rule.
        Returns: WithRuleItemRequestBuilder
        """
        if rule_id is None:
            raise TypeError("rule_id cannot be null.")
        from .item.with_rule_item_request_builder import WithRuleItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["ruleId"] = rule_id
        return WithRuleItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def post(self,body: AssignmentPostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[AssignmentPostResponse]:
        """
        Links an existing entity (typically a support) to a recurrence rule, so the occurrence is treated as "converted" into that concrete entity. Caller needs access both to the rule and to the target assignment.
        param body: Request body.
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
    
    def to_post_request_information(self,body: AssignmentPostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Links an existing entity (typically a support) to a recurrence rule, so the occurrence is treated as "converted" into that concrete entity. Caller needs access both to the rule and to the target assignment.
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
    
    def with_url(self,raw_url: str) -> AssignmentRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: AssignmentRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return AssignmentRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class AssignmentRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

