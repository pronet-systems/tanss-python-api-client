from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.with_condition_type_item_request_builder import WithConditionTypeItemRequestBuilder

class ConditionsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/escalations/frontend/conditions
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new ConditionsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/escalations/frontend/conditions", path_parameters)
    
    def by_condition_type(self,condition_type: str) -> WithConditionTypeItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.v1.escalations.frontend.conditions.item collection
        param condition_type: Escalation rule condition type whose frontend form definition is requested.
        Returns: WithConditionTypeItemRequestBuilder
        """
        if condition_type is None:
            raise TypeError("condition_type cannot be null.")
        from .item.with_condition_type_item_request_builder import WithConditionTypeItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["conditionType"] = condition_type
        return WithConditionTypeItemRequestBuilder(self.request_adapter, url_tpl_params)
    

