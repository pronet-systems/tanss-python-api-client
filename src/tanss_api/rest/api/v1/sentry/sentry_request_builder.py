from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .activate.activate_request_builder import ActivateRequestBuilder
    from .deactivate.deactivate_request_builder import DeactivateRequestBuilder
    from .status.status_request_builder import StatusRequestBuilder
    from .test.test_request_builder import TestRequestBuilder

class SentryRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/sentry
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new SentryRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/sentry", path_parameters)
    
    @property
    def activate(self) -> ActivateRequestBuilder:
        """
        The activate property
        """
        from .activate.activate_request_builder import ActivateRequestBuilder

        return ActivateRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def deactivate(self) -> DeactivateRequestBuilder:
        """
        The deactivate property
        """
        from .deactivate.deactivate_request_builder import DeactivateRequestBuilder

        return DeactivateRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def status(self) -> StatusRequestBuilder:
        """
        The status property
        """
        from .status.status_request_builder import StatusRequestBuilder

        return StatusRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def test(self) -> TestRequestBuilder:
        """
        The test property
        """
        from .test.test_request_builder import TestRequestBuilder

        return TestRequestBuilder(self.request_adapter, self.path_parameters)
    

