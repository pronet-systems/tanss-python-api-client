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
    from .with_rule_delete_response import WithRuleDeleteResponse
    from .with_rule_get_response import WithRuleGetResponse
    from .with_rule_put_request_body import WithRulePutRequestBody
    from .with_rule_put_response import WithRulePutResponse

class WithRuleItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/tanss.x/v1/tanssEvents/rules/{ruleId}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new WithRuleItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/tanss.x/v1/tanssEvents/rules/{ruleId}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[WithRuleDeleteResponse]:
        """
        Löscht eine TANSS-Event-Regel. Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft. Token: module, Rollen TANSS_APP. Rechte: SecurityManager.long(), ADMINISTRATE_TANSS_EVENT_RULES. Hinweise: Auch unter /api/tanss.app/v1. 404 ENTITY_NOT_FOUND. meta.status DELETED.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[WithRuleDeleteResponse]
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .with_rule_delete_response import WithRuleDeleteResponse

        return await self.request_adapter.send_async(request_info, WithRuleDeleteResponse, None)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[WithRuleGetResponse]:
        """
        Liefert eine TANSS-Event-Regel. Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft. Token: module, Rollen TANSS_APP. Rechte: SecurityManager.long(), ADMINISTRATE_TANSS_EVENT_RULES. Hinweise: Auch unter /api/tanss.app/v1. 404 OBJECT_NOT_FOUND.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[WithRuleGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .with_rule_get_response import WithRuleGetResponse

        return await self.request_adapter.send_async(request_info, WithRuleGetResponse, None)
    
    async def put(self,body: WithRulePutRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[WithRulePutResponse]:
        """
        Aktualisiert eine TANSS-Event-Regel per JSON-Merge (Teil-Update). Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft. Token: module, Rollen TANSS_APP. Rechte: SecurityManager.long(), ADMINISTRATE_TANSS_EVENT_RULES. Hinweise: Auch unter /api/tanss.app/v1. 404 ENTITY_NOT_FOUND. meta.status UPDATED.
        param body: TnsTanssEventRule-Felder (Teil-Update); nur gesendete Felder werden gemerged.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[WithRulePutResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .with_rule_put_response import WithRulePutResponse

        return await self.request_adapter.send_async(request_info, WithRulePutResponse, None)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Löscht eine TANSS-Event-Regel. Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft. Token: module, Rollen TANSS_APP. Rechte: SecurityManager.long(), ADMINISTRATE_TANSS_EVENT_RULES. Hinweise: Auch unter /api/tanss.app/v1. 404 ENTITY_NOT_FOUND. meta.status DELETED.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Liefert eine TANSS-Event-Regel. Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft. Token: module, Rollen TANSS_APP. Rechte: SecurityManager.long(), ADMINISTRATE_TANSS_EVENT_RULES. Hinweise: Auch unter /api/tanss.app/v1. 404 OBJECT_NOT_FOUND.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_put_request_information(self,body: WithRulePutRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Aktualisiert eine TANSS-Event-Regel per JSON-Merge (Teil-Update). Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft. Token: module, Rollen TANSS_APP. Rechte: SecurityManager.long(), ADMINISTRATE_TANSS_EVENT_RULES. Hinweise: Auch unter /api/tanss.app/v1. 404 ENTITY_NOT_FOUND. meta.status UPDATED.
        param body: TnsTanssEventRule-Felder (Teil-Update); nur gesendete Felder werden gemerged.
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
    
    def with_url(self,raw_url: str) -> WithRuleItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: WithRuleItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return WithRuleItemRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class WithRuleItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class WithRuleItemRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class WithRuleItemRequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

