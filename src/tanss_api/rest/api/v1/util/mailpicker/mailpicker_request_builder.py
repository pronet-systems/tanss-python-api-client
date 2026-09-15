from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.with_company_item_request_builder import WithCompanyItemRequestBuilder

class MailpickerRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/util/mailpicker
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new MailpickerRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/util/mailpicker", path_parameters)
    
    def by_company_id(self,company_id: int) -> WithCompanyItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.v1.util.mailpicker.item collection
        param company_id: Id of the company whose mail addresses should be collected.
        Returns: WithCompanyItemRequestBuilder
        """
        if company_id is None:
            raise TypeError("company_id cannot be null.")
        from .item.with_company_item_request_builder import WithCompanyItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["companyId"] = company_id
        return WithCompanyItemRequestBuilder(self.request_adapter, url_tpl_params)
    

