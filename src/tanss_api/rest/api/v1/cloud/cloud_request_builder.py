from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .is_token_valid.is_token_valid_request_builder import IsTokenValidRequestBuilder
    from .receivers.receivers_request_builder import ReceiversRequestBuilder
    from .upload.upload_request_builder import UploadRequestBuilder

class CloudRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/cloud
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new CloudRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/cloud", path_parameters)
    
    @property
    def is_token_valid(self) -> IsTokenValidRequestBuilder:
        """
        The isTokenValid property
        """
        from .is_token_valid.is_token_valid_request_builder import IsTokenValidRequestBuilder

        return IsTokenValidRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def receivers(self) -> ReceiversRequestBuilder:
        """
        The receivers property
        """
        from .receivers.receivers_request_builder import ReceiversRequestBuilder

        return ReceiversRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def upload(self) -> UploadRequestBuilder:
        """
        The upload property
        """
        from .upload.upload_request_builder import UploadRequestBuilder

        return UploadRequestBuilder(self.request_adapter, self.path_parameters)
    

