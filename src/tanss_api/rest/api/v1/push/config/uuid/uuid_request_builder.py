from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.with_uu_item_request_builder import WithUuItemRequestBuilder

class UuidRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/push/config/uuid
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new UuidRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/push/config/uuid", path_parameters)
    
    def by_uuid(self,uuid: str) -> WithUuItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.v1.push.config.uuid.item collection
        param uuid: Unique identifier of the item
        Returns: WithUuItemRequestBuilder
        """
        if uuid is None:
            raise TypeError("uuid cannot be null.")
        from .item.with_uu_item_request_builder import WithUuItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["uuid"] = uuid
        return WithUuItemRequestBuilder(self.request_adapter, url_tpl_params)
    

