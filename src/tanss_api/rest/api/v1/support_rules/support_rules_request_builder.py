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
    from ....models.support_rules403_error import SupportRules403Error
    from .frontend.frontend_request_builder import FrontendRequestBuilder
    from .item.support_rules_item_request_builder import SupportRulesItemRequestBuilder
    from .support_rules_get_response import SupportRulesGetResponse
    from .support_rules_post_request_body import SupportRulesPostRequestBody
    from .support_rules_post_response import SupportRulesPostResponse
    from .support_rules_put_request_body import SupportRulesPutRequestBody
    from .support_rules_put_response import SupportRulesPutResponse
    from .trigger.trigger_request_builder import TriggerRequestBuilder

class SupportRulesRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/supportRules
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new SupportRulesRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/supportRules", path_parameters)
    
    def by_id(self,id: int) -> SupportRulesItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.v1.supportRules.item collection
        param id: Id of the support rule to delete.
        Returns: SupportRulesItemRequestBuilder
        """
        if id is None:
            raise TypeError("id cannot be null.")
        from .item.support_rules_item_request_builder import SupportRulesItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["id"] = id
        return SupportRulesItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[SupportRulesGetResponse]:
        """
        Returns every configured support rule (`leistungen_regeln` table). A support rule fires on a defined trigger (e.g. a support that exceeds a duration threshold) and runs configured events such as sending notifications. Requires the ESCALATION module licence and technician/freelancer status.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[SupportRulesGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ....models.support_rules403_error import SupportRules403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": SupportRules403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .support_rules_get_response import SupportRulesGetResponse

        return await self.request_adapter.send_async(request_info, SupportRulesGetResponse, error_mapping)
    
    async def post(self,body: SupportRulesPostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[SupportRulesPostResponse]:
        """
        Creates a new support rule. Conditions and events submitted with the rule are persisted by the `afterCreate` hook. Requires the `SUPPORT_RULE_ADMINISTRATION` permission and the ESCALATION module licence.
        param body: Request body.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[SupportRulesPostResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ....models.support_rules403_error import SupportRules403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": SupportRules403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .support_rules_post_response import SupportRulesPostResponse

        return await self.request_adapter.send_async(request_info, SupportRulesPostResponse, error_mapping)
    
    async def put(self,body: SupportRulesPutRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[SupportRulesPutResponse]:
        """
        Loads support rules filtered/sorted/paginated according to object. Used by the rules-administration list views. Requires the ESCALATION module licence and technician/freelancer status.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[SupportRulesPutResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        from ....models.support_rules403_error import SupportRules403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": SupportRules403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .support_rules_put_response import SupportRulesPutResponse

        return await self.request_adapter.send_async(request_info, SupportRulesPutResponse, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Returns every configured support rule (`leistungen_regeln` table). A support rule fires on a defined trigger (e.g. a support that exceeds a duration threshold) and runs configured events such as sending notifications. Requires the ESCALATION module licence and technician/freelancer status.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: SupportRulesPostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Creates a new support rule. Conditions and events submitted with the rule are persisted by the `afterCreate` hook. Requires the `SUPPORT_RULE_ADMINISTRATION` permission and the ESCALATION module licence.
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
    
    def to_put_request_information(self,body: SupportRulesPutRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Loads support rules filtered/sorted/paginated according to object. Used by the rules-administration list views. Requires the ESCALATION module licence and technician/freelancer status.
        param body: The request body
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
    
    def with_url(self,raw_url: str) -> SupportRulesRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: SupportRulesRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return SupportRulesRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def frontend(self) -> FrontendRequestBuilder:
        """
        The frontend property
        """
        from .frontend.frontend_request_builder import FrontendRequestBuilder

        return FrontendRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def trigger(self) -> TriggerRequestBuilder:
        """
        The trigger property
        """
        from .trigger.trigger_request_builder import TriggerRequestBuilder

        return TriggerRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class SupportRulesRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class SupportRulesRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class SupportRulesRequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

