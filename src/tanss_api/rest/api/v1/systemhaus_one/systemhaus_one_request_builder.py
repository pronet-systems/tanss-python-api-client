from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .articles.articles_request_builder import ArticlesRequestBuilder
    from .invoices.invoices_request_builder import InvoicesRequestBuilder
    from .price_lists.price_lists_request_builder import PriceListsRequestBuilder
    from .warehouses.warehouses_request_builder import WarehousesRequestBuilder

class Systemhaus_oneRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/systemhaus_one
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new Systemhaus_oneRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/systemhaus_one", path_parameters)
    
    @property
    def articles(self) -> ArticlesRequestBuilder:
        """
        The articles property
        """
        from .articles.articles_request_builder import ArticlesRequestBuilder

        return ArticlesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def invoices(self) -> InvoicesRequestBuilder:
        """
        The invoices property
        """
        from .invoices.invoices_request_builder import InvoicesRequestBuilder

        return InvoicesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def price_lists(self) -> PriceListsRequestBuilder:
        """
        The priceLists property
        """
        from .price_lists.price_lists_request_builder import PriceListsRequestBuilder

        return PriceListsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def warehouses(self) -> WarehousesRequestBuilder:
        """
        The warehouses property
        """
        from .warehouses.warehouses_request_builder import WarehousesRequestBuilder

        return WarehousesRequestBuilder(self.request_adapter, self.path_parameters)
    

