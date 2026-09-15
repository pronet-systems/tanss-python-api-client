from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.with_rule_item_request_builder import WithRuleItemRequestBuilder
    from .rule_check.rule_check_request_builder import RuleCheckRequestBuilder

class RulesRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/mailRobot/rules
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new RulesRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/mailRobot/rules", path_parameters)
    
    def by_rule_id(self,rule_id: int) -> WithRuleItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.v1.mailRobot.rules.item collection
        param rule_id: Unique identifier of the item
        Returns: WithRuleItemRequestBuilder
        """
        if rule_id is None:
            raise TypeError("rule_id cannot be null.")
        from .item.with_rule_item_request_builder import WithRuleItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["ruleId"] = rule_id
        return WithRuleItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    @property
    def rule_check(self) -> RuleCheckRequestBuilder:
        """
        The ruleCheck property
        """
        from .rule_check.rule_check_request_builder import RuleCheckRequestBuilder

        return RuleCheckRequestBuilder(self.request_adapter, self.path_parameters)
    

