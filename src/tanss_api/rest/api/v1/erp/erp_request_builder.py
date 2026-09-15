from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .projects.projects_request_builder import ProjectsRequestBuilder
    from .stocks.stocks_request_builder import StocksRequestBuilder

class ErpRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/erp
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new ErpRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/erp", path_parameters)
    
    @property
    def projects(self) -> ProjectsRequestBuilder:
        """
        The projects property
        """
        from .projects.projects_request_builder import ProjectsRequestBuilder

        return ProjectsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def stocks(self) -> StocksRequestBuilder:
        """
        The stocks property
        """
        from .stocks.stocks_request_builder import StocksRequestBuilder

        return StocksRequestBuilder(self.request_adapter, self.path_parameters)
    

