from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .company.company_request_builder import CompanyRequestBuilder
    from .flags.flags_request_builder import FlagsRequestBuilder

class AssignmentsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/assignments
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new AssignmentsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/assignments", path_parameters)
    
    @property
    def company(self) -> CompanyRequestBuilder:
        """
        The company property
        """
        from .company.company_request_builder import CompanyRequestBuilder

        return CompanyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def flags(self) -> FlagsRequestBuilder:
        """
        The flags property
        """
        from .flags.flags_request_builder import FlagsRequestBuilder

        return FlagsRequestBuilder(self.request_adapter, self.path_parameters)
    

