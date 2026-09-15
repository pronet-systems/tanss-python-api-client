from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.with_checklist_item_request_builder import WithChecklistItemRequestBuilder

class WithLinkItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/erp/v1/checklists/assignment/{linkTypeId}/{linkId}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new WithLinkItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/erp/v1/checklists/assignment/{linkTypeId}/{linkId}", path_parameters)
    
    def by_checklist_id(self,checklist_id: int) -> WithChecklistItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.erp.v1.checklists.assignment.item.item.item collection
        param checklist_id: id of the checklist
        Returns: WithChecklistItemRequestBuilder
        """
        if checklist_id is None:
            raise TypeError("checklist_id cannot be null.")
        from .item.with_checklist_item_request_builder import WithChecklistItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["checklistId"] = checklist_id
        return WithChecklistItemRequestBuilder(self.request_adapter, url_tpl_params)
    

