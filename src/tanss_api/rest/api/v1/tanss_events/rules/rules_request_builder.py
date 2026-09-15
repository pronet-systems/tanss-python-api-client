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
    from .....models.rules403_error import Rules403Error
    from .....models.tns_tanss_event_rule import TnsTanssEventRule
    from .....models.tns_tanss_event_rule_configuration import TnsTanssEventRuleConfiguration
    from .item.item_request_builder import ItemRequestBuilder
    from .rules_post_response import RulesPostResponse
    from .rules_put_response import RulesPutResponse
    from .test.test_request_builder import TestRequestBuilder

class RulesRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/tanssEvents/rules
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new RulesRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/tanssEvents/rules", path_parameters)
    
    def by_id(self,id: int) -> ItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.v1.tanssEvents.rules.item collection
        param id: id of the rule
        Returns: ItemRequestBuilder
        """
        if id is None:
            raise TypeError("id cannot be null.")
        from .item.item_request_builder import ItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["%2Did"] = id
        return ItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def post(self,body: TnsTanssEventRule, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[RulesPostResponse]:
        """
        This route will create a "TANSS event rule", which is primarily used for webhhok notifications.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[RulesPostResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from .....models.rules403_error import Rules403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Rules403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .rules_post_response import RulesPostResponse

        return await self.request_adapter.send_async(request_info, RulesPostResponse, error_mapping)
    
    async def put(self,body: TnsTanssEventRuleConfiguration, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[RulesPutResponse]:
        """
        This route will return a list of rules, matching a filter, which is sent in the body
        param body: defines the filter for the event rule list
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[RulesPutResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        from .....models.rules403_error import Rules403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Rules403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .rules_put_response import RulesPutResponse

        return await self.request_adapter.send_async(request_info, RulesPutResponse, error_mapping)
    
    def to_post_request_information(self,body: TnsTanssEventRule, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        This route will create a "TANSS event rule", which is primarily used for webhhok notifications.
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
    
    def to_put_request_information(self,body: TnsTanssEventRuleConfiguration, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        This route will return a list of rules, matching a filter, which is sent in the body
        param body: defines the filter for the event rule list
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
    
    def with_url(self,raw_url: str) -> RulesRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: RulesRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return RulesRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def test(self) -> TestRequestBuilder:
        """
        The test property
        """
        from .test.test_request_builder import TestRequestBuilder

        return TestRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class RulesRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class RulesRequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

