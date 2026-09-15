from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.with_contract_item_request_builder import WithContractItemRequestBuilder

class PrepaidRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/contracts/prepaid
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new PrepaidRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/contracts/prepaid", path_parameters)
    
    def by_contract_id(self,contract_id: int) -> WithContractItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.v1.contracts.prepaid.item collection
        param contract_id: ID of the contract to calculate the prepaid balance for.
        Returns: WithContractItemRequestBuilder
        """
        if contract_id is None:
            raise TypeError("contract_id cannot be null.")
        from .item.with_contract_item_request_builder import WithContractItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["contractId"] = contract_id
        return WithContractItemRequestBuilder(self.request_adapter, url_tpl_params)
    

