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
    from ......models.tns_tanss_event_rule_configuration import TnsTanssEventRuleConfiguration
    from .item.with_rule_item_request_builder import WithRuleItemRequestBuilder
    from .rules_post_request_body import RulesPostRequestBody
    from .rules_post_response import RulesPostResponse
    from .rules_put_response import RulesPutResponse
    from .test.test_request_builder import TestRequestBuilder

class RulesRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/tanss.x/v1/tanssEvents/rules
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new RulesRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/tanss.x/v1/tanssEvents/rules", path_parameters)
    
    def by_rule_id(self,rule_id: int) -> WithRuleItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.tanssX.v1.tanssEvents.rules.item collection
        param rule_id: Unique identifier of the item
        Returns: WithRuleItemRequestBuilder
        """
        if rule_id is None:
            raise TypeError("rule_id cannot be null.")
        from .item.with_rule_item_request_builder import WithRuleItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["ruleId"] = rule_id
        return WithRuleItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def post(self,body: RulesPostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[RulesPostResponse]:
        """
        Erstellt eine TANSS-Event-Regel (Alias zu POST /api/v1/tanssEvents/rules).Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: module, Rollen TANSS_APP.Rechte: interner Mitarbeiter-Login; ADMINISTRATE_TANSS_EVENT_RULES.Hinweis: Auch unter /api/tanss.app/v1. Generischer Create (id wird entfernt). Status CREATED.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[RulesPostResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .rules_post_response import RulesPostResponse

        return await self.request_adapter.send_async(request_info, RulesPostResponse, None)
    
    async def put(self,body: TnsTanssEventRuleConfiguration, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[RulesPutResponse]:
        """
        Liefert Event-Regeln gefiltert nach Konfiguration (Alias zu PUT /api/v1/tanssEvents/rules).Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: module, Rollen TANSS_APP.Rechte: ADMINISTRATE_TANSS_EVENT_RULES.Hinweis: Auch unter /api/tanss.app/v1. 403 FORBIDDEN_MISSING_PERMISSIONS ohne Recht.
        param body: defines the filter for the event rule list
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[RulesPutResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .rules_put_response import RulesPutResponse

        return await self.request_adapter.send_async(request_info, RulesPutResponse, None)
    
    def to_post_request_information(self,body: RulesPostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Erstellt eine TANSS-Event-Regel (Alias zu POST /api/v1/tanssEvents/rules).Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: module, Rollen TANSS_APP.Rechte: interner Mitarbeiter-Login; ADMINISTRATE_TANSS_EVENT_RULES.Hinweis: Auch unter /api/tanss.app/v1. Generischer Create (id wird entfernt). Status CREATED.
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
        Liefert Event-Regeln gefiltert nach Konfiguration (Alias zu PUT /api/v1/tanssEvents/rules).Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: module, Rollen TANSS_APP.Rechte: ADMINISTRATE_TANSS_EVENT_RULES.Hinweis: Auch unter /api/tanss.app/v1. 403 FORBIDDEN_MISSING_PERMISSIONS ohne Recht.
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
    

