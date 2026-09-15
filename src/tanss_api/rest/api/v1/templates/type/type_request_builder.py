from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.with_template_type_item_request_builder import WithTemplateTypeItemRequestBuilder

class TypeRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/templates/type
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new TypeRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/templates/type", path_parameters)
    
    def by_template_type(self,template_type: str) -> WithTemplateTypeItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.v1.templates.type.item collection
        param template_type: Template type to list persisted templates for (e.g. TICKET).
        Returns: WithTemplateTypeItemRequestBuilder
        """
        if template_type is None:
            raise TypeError("template_type cannot be null.")
        from .item.with_template_type_item_request_builder import WithTemplateTypeItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["templateType"] = template_type
        return WithTemplateTypeItemRequestBuilder(self.request_adapter, url_tpl_params)
    

