from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.export_item_request_builder import ExportItemRequestBuilder

class ExportRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/templates/{-id}/export
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new ExportRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/templates/{%2Did}/export", path_parameters)
    
    def by_id(self,id: int) -> ExportItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.v1.templates.item.export.item collection
        param id: Id of the source entity to render the template from.
        Returns: ExportItemRequestBuilder
        """
        if id is None:
            raise TypeError("id cannot be null.")
        from .item.export_item_request_builder import ExportItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["id"] = id
        return ExportItemRequestBuilder(self.request_adapter, url_tpl_params)
    

