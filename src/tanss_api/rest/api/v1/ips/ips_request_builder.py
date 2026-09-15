from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.assignment_type_item_request_builder import AssignmentTypeItemRequestBuilder

class IpsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/ips
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new IpsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/ips", path_parameters)
    
    def by_assignment_type_id(self,assignment_type_id: int) -> AssignmentTypeItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.v1.ips.item collection
        param assignment_type_id: id of ip address
        Returns: AssignmentTypeItemRequestBuilder
        """
        if assignment_type_id is None:
            raise TypeError("assignment_type_id cannot be null.")
        from .item.assignment_type_item_request_builder import AssignmentTypeItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["assignmentType%2Did"] = assignment_type_id
        return AssignmentTypeItemRequestBuilder(self.request_adapter, url_tpl_params)
    

