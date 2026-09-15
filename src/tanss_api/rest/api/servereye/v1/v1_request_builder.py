from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .bucketitem.bucketitem_request_builder import BucketitemRequestBuilder
    from .fetch.fetch_request_builder import FetchRequestBuilder

class V1RequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/servereye/v1
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new V1RequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/servereye/v1", path_parameters)
    
    @property
    def bucketitem(self) -> BucketitemRequestBuilder:
        """
        The bucketitem property
        """
        from .bucketitem.bucketitem_request_builder import BucketitemRequestBuilder

        return BucketitemRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def fetch(self) -> FetchRequestBuilder:
        """
        The fetch property
        """
        from .fetch.fetch_request_builder import FetchRequestBuilder

        return FetchRequestBuilder(self.request_adapter, self.path_parameters)
    

