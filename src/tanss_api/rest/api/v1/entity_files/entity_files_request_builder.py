from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.item_request_builder import ItemRequestBuilder

class EntityFilesRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/entityFiles
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new EntityFilesRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/entityFiles", path_parameters)
    
    def by_id(self,id: int) -> ItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.v1.entityFiles.item collection
        param id: Id of the entity file.
        Returns: ItemRequestBuilder
        """
        if id is None:
            raise TypeError("id cannot be null.")
        from .item.item_request_builder import ItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["%2Did"] = id
        return ItemRequestBuilder(self.request_adapter, url_tpl_params)
    

