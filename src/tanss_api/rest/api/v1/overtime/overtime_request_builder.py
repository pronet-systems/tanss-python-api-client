from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .approve.approve_request_builder import ApproveRequestBuilder
    from .balance.balance_request_builder import BalanceRequestBuilder
    from .history.history_request_builder import HistoryRequestBuilder
    from .open.open_request_builder import OpenRequestBuilder
    from .pay_out.pay_out_request_builder import PayOutRequestBuilder
    from .request.request_request_builder import RequestRequestBuilder
    from .supports.supports_request_builder import SupportsRequestBuilder
    from .to_be_paid_out.to_be_paid_out_request_builder import ToBePaidOutRequestBuilder

class OvertimeRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/overtime
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new OvertimeRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/overtime", path_parameters)
    
    @property
    def approve(self) -> ApproveRequestBuilder:
        """
        The approve property
        """
        from .approve.approve_request_builder import ApproveRequestBuilder

        return ApproveRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def balance(self) -> BalanceRequestBuilder:
        """
        The balance property
        """
        from .balance.balance_request_builder import BalanceRequestBuilder

        return BalanceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def history(self) -> HistoryRequestBuilder:
        """
        The history property
        """
        from .history.history_request_builder import HistoryRequestBuilder

        return HistoryRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def open(self) -> OpenRequestBuilder:
        """
        The open property
        """
        from .open.open_request_builder import OpenRequestBuilder

        return OpenRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def pay_out(self) -> PayOutRequestBuilder:
        """
        The payOut property
        """
        from .pay_out.pay_out_request_builder import PayOutRequestBuilder

        return PayOutRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def request(self) -> RequestRequestBuilder:
        """
        The request property
        """
        from .request.request_request_builder import RequestRequestBuilder

        return RequestRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def supports(self) -> SupportsRequestBuilder:
        """
        The supports property
        """
        from .supports.supports_request_builder import SupportsRequestBuilder

        return SupportsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def to_be_paid_out(self) -> ToBePaidOutRequestBuilder:
        """
        The toBePaidOut property
        """
        from .to_be_paid_out.to_be_paid_out_request_builder import ToBePaidOutRequestBuilder

        return ToBePaidOutRequestBuilder(self.request_adapter, self.path_parameters)
    

