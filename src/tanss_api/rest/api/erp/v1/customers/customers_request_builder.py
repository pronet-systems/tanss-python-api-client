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
    from .....models.customers403_error import Customers403Error
    from .....models.customers_combine import CustomersCombine
    from .....models.customers_combine403_error import CustomersCombine403Error
    from .....models.customer_post import CustomerPost
    from .....models.customer_post_response import CustomerPostResponse

class CustomersRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/erp/v1/customers
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new CustomersRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/erp/v1/customers{?modified*,preferredCustomers*}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[CustomersRequestBuilderGetQueryParameters]] = None) -> Optional[CustomersCombine]:
        """
        Returns companies **and** their employees as two separate lists, restricted to the recordschanged since the timestamp given in `modified`. Both lists cover all companies — there is nofilter for a single customer.`modified` is the switch that decides how much is returned: `0` (the default) returns two emptylists, a Unix timestamp returns everything changed since then, and `-1` returns the completemaster data. The full export can take very long, so the backend drops its execution time limitfor this call.Delegates to the legacy PHP ERP backend (`api/v1/erp/customers`) and passes its answer throughunchanged: unlike the other TANSS routes the body is the bare object, **without** the`meta`/`content` envelope. A problem on the PHP side also arrives with HTTP 200 and a body of`{"message": "…"}`.Intended for ERP integrations — must be called with the dedicated API token bound to the role`ERP`, not a normal user login.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[CustomersCombine]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .....models.customers403_error import Customers403Error
        from .....models.customers_combine403_error import CustomersCombine403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": CustomersCombine403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.customers_combine import CustomersCombine

        return await self.request_adapter.send_async(request_info, CustomersCombine, error_mapping)
    
    async def post(self,body: list[CustomerPost], request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[list[CustomerPostResponse]]:
        """
        Imports customer and supplier master data from the ERP system by delegating to the legacy PHP ERPbackend (`api/v1/erp/customers`). The body is a batch: each entry carries one record as the ERP'sown XML export, Base64-encoded.Every entry is answered individually — the response mirrors the entry and adds a `status`, so asingle malformed record does not fail the whole batch. Requires an ERP interface to be selectedand activated in TANSS. The answer of the PHP backend is passed through unchanged, so the body isthe bare list **without** the `meta`/`content` envelope, and a problem on the PHP side arriveswith HTTP 200 and a body of `{"message": "…"}`.Intended for ERP integrations — must be called with the dedicated API token bound to the role`ERP`, not a normal user login.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[list[CustomerPostResponse]]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from .....models.customers403_error import Customers403Error
        from .....models.customers_combine403_error import CustomersCombine403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Customers403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.customer_post_response import CustomerPostResponse

        return await self.request_adapter.send_collection_async(request_info, CustomerPostResponse, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[CustomersRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Returns companies **and** their employees as two separate lists, restricted to the recordschanged since the timestamp given in `modified`. Both lists cover all companies — there is nofilter for a single customer.`modified` is the switch that decides how much is returned: `0` (the default) returns two emptylists, a Unix timestamp returns everything changed since then, and `-1` returns the completemaster data. The full export can take very long, so the backend drops its execution time limitfor this call.Delegates to the legacy PHP ERP backend (`api/v1/erp/customers`) and passes its answer throughunchanged: unlike the other TANSS routes the body is the bare object, **without** the`meta`/`content` envelope. A problem on the PHP side also arrives with HTTP 200 and a body of`{"message": "…"}`.Intended for ERP integrations — must be called with the dedicated API token bound to the role`ERP`, not a normal user login.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: list[CustomerPost], request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Imports customer and supplier master data from the ERP system by delegating to the legacy PHP ERPbackend (`api/v1/erp/customers`). The body is a batch: each entry carries one record as the ERP'sown XML export, Base64-encoded.Every entry is answered individually — the response mirrors the entry and adds a `status`, so asingle malformed record does not fail the whole batch. Requires an ERP interface to be selectedand activated in TANSS. The answer of the PHP backend is passed through unchanged, so the body isthe bare list **without** the `meta`/`content` envelope, and a problem on the PHP side arriveswith HTTP 200 and a body of `{"message": "…"}`.Intended for ERP integrations — must be called with the dedicated API token bound to the role`ERP`, not a normal user login.
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
    
    def with_url(self,raw_url: str) -> CustomersRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: CustomersRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return CustomersRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class CustomersRequestBuilderGetQueryParameters():
        """
        Returns companies **and** their employees as two separate lists, restricted to the recordschanged since the timestamp given in `modified`. Both lists cover all companies — there is nofilter for a single customer.`modified` is the switch that decides how much is returned: `0` (the default) returns two emptylists, a Unix timestamp returns everything changed since then, and `-1` returns the completemaster data. The full export can take very long, so the backend drops its execution time limitfor this call.Delegates to the legacy PHP ERP backend (`api/v1/erp/customers`) and passes its answer throughunchanged: unlike the other TANSS routes the body is the bare object, **without** the`meta`/`content` envelope. A problem on the PHP side also arrives with HTTP 200 and a body of`{"message": "…"}`.Intended for ERP integrations — must be called with the dedicated API token bound to the role`ERP`, not a normal user login.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "preferred_customers":
                return "preferredCustomers"
            if original_name == "modified":
                return "modified"
            return original_name
        
        # Unix timestamp; only companies and employees whose last change is at or after this value arereturned. `0` returns empty lists, `-1` returns all records.
        modified: Optional[int] = None

        # If true, every employee additionally carries its `preferred_customer` block. Sending`false` omits that block and saves one query per employee.
        preferred_customers: Optional[bool] = None

    
    @dataclass
    class CustomersRequestBuilderGetRequestConfiguration(RequestConfiguration[CustomersRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class CustomersRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

