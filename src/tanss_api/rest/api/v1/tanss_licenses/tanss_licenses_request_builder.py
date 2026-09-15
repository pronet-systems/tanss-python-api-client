from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .deactivate_user.deactivate_user_request_builder import DeactivateUserRequestBuilder
    from .fetch.fetch_request_builder import FetchRequestBuilder

class TanssLicensesRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/tanssLicenses
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new TanssLicensesRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/tanssLicenses", path_parameters)
    
    @property
    def deactivate_user(self) -> DeactivateUserRequestBuilder:
        """
        The deactivateUser property
        """
        from .deactivate_user.deactivate_user_request_builder import DeactivateUserRequestBuilder

        return DeactivateUserRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def fetch(self) -> FetchRequestBuilder:
        """
        The fetch property
        """
        from .fetch.fetch_request_builder import FetchRequestBuilder

        return FetchRequestBuilder(self.request_adapter, self.path_parameters)
    

