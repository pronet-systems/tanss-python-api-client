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
    from .....models.invoices403_error import Invoices403Error
    from .invoices_get_response import InvoicesGetResponse

class InvoicesRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/systemhaus_one/invoices
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new InvoicesRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/systemhaus_one/invoices{?customer*}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[InvoicesRequestBuilderGetQueryParameters]] = None) -> Optional[InvoicesGetResponse]:
        """
        Returns the invoices and credit notes of **one** customer from the connected SAP Business Onesystem. The customer is addressed by its SAP `CardCode`, passed in `customer`. Cancelled documentsare left out and the list is sorted by document date, newest first. Credit notes come back with anegative `DocTotal` and always count as paid.This is a user-facing route inside TANSS: it is called with a normal user login token, not withone of the token-bound `/api/erp/v1/...` integration routes. Do not confuse it with`GET /api/erp/v1/invoices`, which exports the vouchers flagged for export in TANSS and knows nocustomer filter. The `SAP_ONE` module must be licensed.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[InvoicesGetResponse]
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
        from .invoices_get_response import InvoicesGetResponse

        return await self.request_adapter.send_async(request_info, InvoicesGetResponse, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[InvoicesRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Returns the invoices and credit notes of **one** customer from the connected SAP Business Onesystem. The customer is addressed by its SAP `CardCode`, passed in `customer`. Cancelled documentsare left out and the list is sorted by document date, newest first. Credit notes come back with anegative `DocTotal` and always count as paid.This is a user-facing route inside TANSS: it is called with a normal user login token, not withone of the token-bound `/api/erp/v1/...` integration routes. Do not confuse it with`GET /api/erp/v1/invoices`, which exports the vouchers flagged for export in TANSS and knows nocustomer filter. The `SAP_ONE` module must be licensed.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
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
        Returns the invoices and credit notes of **one** customer from the connected SAP Business Onesystem. The customer is addressed by its SAP `CardCode`, passed in `customer`. Cancelled documentsare left out and the list is sorted by document date, newest first. Credit notes come back with anegative `DocTotal` and always count as paid.This is a user-facing route inside TANSS: it is called with a normal user login token, not withone of the token-bound `/api/erp/v1/...` integration routes. Do not confuse it with`GET /api/erp/v1/invoices`, which exports the vouchers flagged for export in TANSS and knows nocustomer filter. The `SAP_ONE` module must be licensed.
        """
        # SAP `CardCode` of the customer whose documents are returned. Effectively mandatory — theunderlying query matches this value exactly, so leaving it empty yields an empty list.
        customer: Optional[str] = None

    
    @dataclass
    class InvoicesRequestBuilderGetRequestConfiguration(RequestConfiguration[InvoicesRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

