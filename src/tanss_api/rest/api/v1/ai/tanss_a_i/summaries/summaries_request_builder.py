from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.with_summary_item_request_builder import WithSummaryItemRequestBuilder

class SummariesRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/ai/tanssAI/summaries
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new SummariesRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/ai/tanssAI/summaries", path_parameters)
    
    def by_summary_id(self,summary_id: int) -> WithSummaryItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.v1.ai.tanssAI.summaries.item collection
        param summary_id: Unique identifier of the item
        Returns: WithSummaryItemRequestBuilder
        """
        if summary_id is None:
            raise TypeError("summary_id cannot be null.")
        from .item.with_summary_item_request_builder import WithSummaryItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["summaryId"] = summary_id
        return WithSummaryItemRequestBuilder(self.request_adapter, url_tpl_params)
    

