from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.with_invoice_number_item_request_builder import WithInvoiceNumberItemRequestBuilder

class DocumentRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/mention/pdfExport/document
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new DocumentRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/mention/pdfExport/document", path_parameters)
    
    def by_invoice_number(self,invoice_number: str) -> WithInvoiceNumberItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.v1.mention.pdfExport.document.item collection
        param invoice_number: Invoice number identifying the mention export PDF to load.
        Returns: WithInvoiceNumberItemRequestBuilder
        """
        if invoice_number is None:
            raise TypeError("invoice_number cannot be null.")
        from .item.with_invoice_number_item_request_builder import WithInvoiceNumberItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["invoiceNumber"] = invoice_number
        return WithInvoiceNumberItemRequestBuilder(self.request_adapter, url_tpl_params)
    

