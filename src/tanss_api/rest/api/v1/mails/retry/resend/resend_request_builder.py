from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.with_retry_item_request_builder import WithRetryItemRequestBuilder

class ResendRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/mails/retry/resend
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new ResendRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/mails/retry/resend", path_parameters)
    
    def by_retry_id(self,retry_id: int) -> WithRetryItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.v1.mails.retry.resend.item collection
        param retry_id: Id of the failed outgoing mail retry entry to resend.
        Returns: WithRetryItemRequestBuilder
        """
        if retry_id is None:
            raise TypeError("retry_id cannot be null.")
        from .item.with_retry_item_request_builder import WithRetryItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["retryId"] = retry_id
        return WithRetryItemRequestBuilder(self.request_adapter, url_tpl_params)
    

