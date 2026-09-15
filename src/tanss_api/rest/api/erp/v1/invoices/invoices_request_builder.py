from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from kiota_abstractions.default_query_parameters import QueryParameters
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Optional, TYPE_CHECKING, Union
from warnings import warn

if TYPE_CHECKING:
    from .....models.invoice import Invoice
    from .....models.invoices403_error import Invoices403Error
    from .....models.invoice_post import InvoicePost
    from .....models.invoice_post_response import InvoicePostResponse

class InvoicesRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/erp/v1/invoices
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new InvoicesRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/erp/v1/invoices{?companyTypes*,pdf*}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[InvoicesRequestBuilderGetQueryParameters]] = None) -> Optional[list[Invoice]]:
        """
        Returns **all** vouchers that are currently flagged for export in TANSS — for every customer.There is no restriction to a single customer or customer number; the only available narrowing is`companyTypes`.For each of those vouchers the matching order request XML (`order_req_<voucher_id>.xml`) is readfrom the ERP export directory and returned Base64-encoded in `order_request`. A voucher whoseorder request file is missing or unreadable is still listed, with `status` describing the problemand `order_request` empty.Delegates to the legacy PHP ERP backend (`api/v1/erp/invoices`) and passes its answer throughunchanged: unlike the other TANSS routes the body is the bare list, **without** the`meta`/`content` envelope. A problem on the PHP side (no ERP interface selected, exportdirectory not readable, …) also arrives with HTTP 200 and a body of `{"message": "…"}`.Intended for ERP integrations only — must be called with the dedicated API token bound to therole `ERP`, not a normal user login.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[list[Invoice]]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .....models.invoices403_error import Invoices403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Invoices403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.invoice import Invoice

        return await self.request_adapter.send_collection_async(request_info, Invoice, error_mapping)
    
    async def post(self,body: list[InvoicePost], request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[list[InvoicePostResponse]]:
        """
        Writes invoice numbers back to the given vouchers by delegating to the legacy PHP ERP backend(`api/v1/erp/invoices`); used by ERP integrations to report the invoice number assigned on theERP side back into TANSS after billing. Accepts a batch, so several vouchers can be settled inone call.Per voucher this marks the voucher and all of its services as exported, stores the invoicenumber, takes the voucher out of post-processing and — unless it is a maintenance-contractpayment — renders the voucher PDF and files it in the voucher history; that PDF is returnedBase64-encoded in `pdf`. Every entry is written to the ERP interface log. An entry whose`voucher_id` does not exist is skipped and comes back with the corresponding text in `status`instead of `OK`.Requires an ERP interface to be selected and activated in TANSS. The answer of the PHP backend ispassed through unchanged, so the body is the bare list **without** the `meta`/`content` envelope,and a problem on the PHP side arrives with HTTP 200 and a body of `{"message": "…"}`.Intended for ERP integrations only — must be called with the dedicated API token bound to therole `ERP`, not a normal user login.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[list[InvoicePostResponse]]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from .....models.invoices403_error import Invoices403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Invoices403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.invoice_post_response import InvoicePostResponse

        return await self.request_adapter.send_collection_async(request_info, InvoicePostResponse, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[InvoicesRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Returns **all** vouchers that are currently flagged for export in TANSS — for every customer.There is no restriction to a single customer or customer number; the only available narrowing is`companyTypes`.For each of those vouchers the matching order request XML (`order_req_<voucher_id>.xml`) is readfrom the ERP export directory and returned Base64-encoded in `order_request`. A voucher whoseorder request file is missing or unreadable is still listed, with `status` describing the problemand `order_request` empty.Delegates to the legacy PHP ERP backend (`api/v1/erp/invoices`) and passes its answer throughunchanged: unlike the other TANSS routes the body is the bare list, **without** the`meta`/`content` envelope. A problem on the PHP side (no ERP interface selected, exportdirectory not readable, …) also arrives with HTTP 200 and a body of `{"message": "…"}`.Intended for ERP integrations only — must be called with the dedicated API token bound to therole `ERP`, not a normal user login.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: list[InvoicePost], request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Writes invoice numbers back to the given vouchers by delegating to the legacy PHP ERP backend(`api/v1/erp/invoices`); used by ERP integrations to report the invoice number assigned on theERP side back into TANSS after billing. Accepts a batch, so several vouchers can be settled inone call.Per voucher this marks the voucher and all of its services as exported, stores the invoicenumber, takes the voucher out of post-processing and — unless it is a maintenance-contractpayment — renders the voucher PDF and files it in the voucher history; that PDF is returnedBase64-encoded in `pdf`. Every entry is written to the ERP interface log. An entry whose`voucher_id` does not exist is skipped and comes back with the corresponding text in `status`instead of `OK`.Requires an ERP interface to be selected and activated in TANSS. The answer of the PHP backend ispassed through unchanged, so the body is the bare list **without** the `meta`/`content` envelope,and a problem on the PHP side arrives with HTTP 200 and a body of `{"message": "…"}`.Intended for ERP integrations only — must be called with the dedicated API token bound to therole `ERP`, not a normal user login.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.POST, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> InvoicesRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: InvoicesRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return InvoicesRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class InvoicesRequestBuilderGetQueryParameters():
        """
        Returns **all** vouchers that are currently flagged for export in TANSS — for every customer.There is no restriction to a single customer or customer number; the only available narrowing is`companyTypes`.For each of those vouchers the matching order request XML (`order_req_<voucher_id>.xml`) is readfrom the ERP export directory and returned Base64-encoded in `order_request`. A voucher whoseorder request file is missing or unreadable is still listed, with `status` describing the problemand `order_request` empty.Delegates to the legacy PHP ERP backend (`api/v1/erp/invoices`) and passes its answer throughunchanged: unlike the other TANSS routes the body is the bare list, **without** the`meta`/`content` envelope. A problem on the PHP side (no ERP interface selected, exportdirectory not readable, …) also arrives with HTTP 200 and a body of `{"message": "…"}`.Intended for ERP integrations only — must be called with the dedicated API token bound to therole `ERP`, not a normal user login.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "company_types":
                return "companyTypes"
            if original_name == "pdf":
                return "pdf"
            return original_name
        
        # Comma-separated list of company type ids. If set, only vouchers of customers that carry atleast one of these company types are returned. Without it, the vouchers of all customers arereturned. Entries that are not a positive number are ignored; if no customer matches thegiven types, the result is empty.
        company_types: Optional[str] = None

        # If true, the rendered voucher PDF is additionally returned Base64-encoded in the `pdf` fieldof every entry whose order request file could be read. Off by default, because rendering thePDFs is expensive.
        pdf: Optional[bool] = None

    
    @dataclass
    class InvoicesRequestBuilderGetRequestConfiguration(RequestConfiguration[InvoicesRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class InvoicesRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

