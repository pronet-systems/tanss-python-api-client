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
    from ....models.recurrence403_error import Recurrence403Error
    from .assignment.assignment_request_builder import AssignmentRequestBuilder
    from .exclude.exclude_request_builder import ExcludeRequestBuilder
    from .item.with_rule_item_request_builder import WithRuleItemRequestBuilder
    from .query.query_request_builder import QueryRequestBuilder
    from .readable_text.readable_text_request_builder import ReadableTextRequestBuilder
    from .recurrence_post_request_body import RecurrencePostRequestBody
    from .recurrence_post_response import RecurrencePostResponse

class RecurrenceRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/recurrence
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new RecurrenceRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/recurrence", path_parameters)
    
    def by_rule_id(self,rule_id: int) -> WithRuleItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.v1.recurrence.item collection
        param rule_id: Id of the recurrence rule.
        Returns: WithRuleItemRequestBuilder
        """
        if rule_id is None:
            raise TypeError("rule_id cannot be null.")
        from .item.with_rule_item_request_builder import WithRuleItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["ruleId"] = rule_id
        return WithRuleItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def post(self,body: RecurrencePostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[RecurrencePostResponse]:
        """
        Stores a new RRULE-based recurrence definition that drives repeating appointments / supports. Requires a start date and a valid assignment (linkTypeId/linkId) that the caller has access to; only technicians or freelancers may create rules. After persisting, the calculated occurrences are pre-computed for the rule.
        param body: Request body.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[RecurrencePostResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ....models.recurrence403_error import Recurrence403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Recurrence403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .recurrence_post_response import RecurrencePostResponse

        return await self.request_adapter.send_async(request_info, RecurrencePostResponse, error_mapping)
    
    def to_post_request_information(self,body: RecurrencePostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Stores a new RRULE-based recurrence definition that drives repeating appointments / supports. Requires a start date and a valid assignment (linkTypeId/linkId) that the caller has access to; only technicians or freelancers may create rules. After persisting, the calculated occurrences are pre-computed for the rule.
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
    
    def with_url(self,raw_url: str) -> RecurrenceRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: RecurrenceRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return RecurrenceRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def assignment(self) -> AssignmentRequestBuilder:
        """
        The assignment property
        """
        from .assignment.assignment_request_builder import AssignmentRequestBuilder

        return AssignmentRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def exclude(self) -> ExcludeRequestBuilder:
        """
        The exclude property
        """
        from .exclude.exclude_request_builder import ExcludeRequestBuilder

        return ExcludeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def query(self) -> QueryRequestBuilder:
        """
        The query property
        """
        from .query.query_request_builder import QueryRequestBuilder

        return QueryRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def readable_text(self) -> ReadableTextRequestBuilder:
        """
        The readableText property
        """
        from .readable_text.readable_text_request_builder import ReadableTextRequestBuilder

        return ReadableTextRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class RecurrenceRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

