from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.with_configuration_item_request_builder import WithConfigurationItemRequestBuilder

class FetchRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/ical/fetch
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new FetchRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/ical/fetch", path_parameters)
    
    def by_configuration_id(self,configuration_id: int) -> WithConfigurationItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.v1.ical.fetch.item collection
        param configuration_id: Id of the iCal feed configuration to export.
        Returns: WithConfigurationItemRequestBuilder
        """
        if configuration_id is None:
            raise TypeError("configuration_id cannot be null.")
        from .item.with_configuration_item_request_builder import WithConfigurationItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["configurationId"] = configuration_id
        return WithConfigurationItemRequestBuilder(self.request_adapter, url_tpl_params)
    

