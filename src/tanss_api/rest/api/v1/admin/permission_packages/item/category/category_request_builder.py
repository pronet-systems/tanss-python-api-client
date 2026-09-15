from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.with_category_item_request_builder import WithCategoryItemRequestBuilder

class CategoryRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/admin/permissionPackages/{packageId}/category
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new CategoryRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/admin/permissionPackages/{packageId}/category", path_parameters)
    
    def by_category_id(self,category_id: int) -> WithCategoryItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.v1.admin.permissionPackages.item.category.item collection
        param category_id: Id of the permission category whose permissions should be removed.
        Returns: WithCategoryItemRequestBuilder
        """
        if category_id is None:
            raise TypeError("category_id cannot be null.")
        from .item.with_category_item_request_builder import WithCategoryItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["categoryId"] = category_id
        return WithCategoryItemRequestBuilder(self.request_adapter, url_tpl_params)
    

