from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .clear.clear_request_builder import ClearRequestBuilder
    from .trigger_task.trigger_task_request_builder import TriggerTaskRequestBuilder

class CacheRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/cache
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new CacheRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/cache", path_parameters)
    
    @property
    def clear(self) -> ClearRequestBuilder:
        """
        The clear property
        """
        from .clear.clear_request_builder import ClearRequestBuilder

        return ClearRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def trigger_task(self) -> TriggerTaskRequestBuilder:
        """
        The triggerTask property
        """
        from .trigger_task.trigger_task_request_builder import TriggerTaskRequestBuilder

        return TriggerTaskRequestBuilder(self.request_adapter, self.path_parameters)
    

