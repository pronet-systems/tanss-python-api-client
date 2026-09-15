from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.with_with_entity_item_request_builder import WithWithEntityItemRequestBuilder

class WithRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/templates/update/{updateTemplateId}/with
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new WithRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/templates/update/{updateTemplateId}/with", path_parameters)
    
    def by_with_entity_id(self,with_entity_id: int) -> WithWithEntityItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.v1.templates.update.item.with.item collection
        param with_entity_id: Id of the source entity to refresh the template from.
        Returns: WithWithEntityItemRequestBuilder
        """
        if with_entity_id is None:
            raise TypeError("with_entity_id cannot be null.")
        from .item.with_with_entity_item_request_builder import WithWithEntityItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["withEntityId"] = with_entity_id
        return WithWithEntityItemRequestBuilder(self.request_adapter, url_tpl_params)
    

