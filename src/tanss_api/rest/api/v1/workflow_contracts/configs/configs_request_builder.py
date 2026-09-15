from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.with_contract_type_item_request_builder import WithContractTypeItemRequestBuilder

class ConfigsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/workflowContracts/configs
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new ConfigsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/workflowContracts/configs", path_parameters)
    
    def by_contract_type(self,contract_type: str) -> WithContractTypeItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.v1.workflowContracts.configs.item collection
        param contract_type: Workflow contract type to fetch configs for (e.g. MANAGED_SERVICES).
        Returns: WithContractTypeItemRequestBuilder
        """
        if contract_type is None:
            raise TypeError("contract_type cannot be null.")
        from .item.with_contract_type_item_request_builder import WithContractTypeItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["contractType"] = contract_type
        return WithContractTypeItemRequestBuilder(self.request_adapter, url_tpl_params)
    

