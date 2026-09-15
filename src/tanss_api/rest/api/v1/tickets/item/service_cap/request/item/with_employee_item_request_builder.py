from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.with_new_amount_item_request_builder import WithNewAmountItemRequestBuilder

class WithEmployeeItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/tickets/{-id}/serviceCap/request/{employeeId}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new WithEmployeeItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/tickets/{%2Did}/serviceCap/request/{employeeId}", path_parameters)
    
    def by_new_amount(self,new_amount: float) -> WithNewAmountItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.v1.tickets.item.serviceCap.request.item.item collection
        param new_amount: Requested new service cap (budget ceiling) amount.
        Returns: WithNewAmountItemRequestBuilder
        """
        if new_amount is None:
            raise TypeError("new_amount cannot be null.")
        from .item.with_new_amount_item_request_builder import WithNewAmountItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["newAmount"] = new_amount
        return WithNewAmountItemRequestBuilder(self.request_adapter, url_tpl_params)
    

