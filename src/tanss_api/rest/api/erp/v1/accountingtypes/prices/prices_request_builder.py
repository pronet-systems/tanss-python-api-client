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
    from ......models.prices403_error import Prices403Error
    from .prices_get_response import PricesGetResponse
    from .prices_post_request_body import PricesPostRequestBody
    from .prices_post_response import PricesPostResponse

class PricesRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/erp/v1/accountingtypes/prices
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new PricesRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/erp/v1/accountingtypes/prices", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[PricesGetResponse]:
        """
        Returns the list of default accounting type prices (system-wide defaults, no company-specific overrides), used by ERP systems to retrieve current rates for billing/sync. Intended for ERP integrations (e.g. Centron) — must be called with the dedicated API token bound to the role `ERP`, not a normal user login.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[PricesGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ......models.prices403_error import Prices403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Prices403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .prices_get_response import PricesGetResponse

        return await self.request_adapter.send_async(request_info, PricesGetResponse, error_mapping)
    
    async def post(self,body: PricesPostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[PricesPostResponse]:
        """
        Creates a new default price entry for an accounting type, optionally scoped to a specific link (company or other entity); returns the persisted record. Intended for ERP integrations (e.g. Centron) — must be called with the dedicated API token bound to the role `ERP`, not a normal user login.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[PricesPostResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ......models.prices403_error import Prices403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Prices403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .prices_post_response import PricesPostResponse

        return await self.request_adapter.send_async(request_info, PricesPostResponse, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Returns the list of default accounting type prices (system-wide defaults, no company-specific overrides), used by ERP systems to retrieve current rates for billing/sync. Intended for ERP integrations (e.g. Centron) — must be called with the dedicated API token bound to the role `ERP`, not a normal user login.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: PricesPostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Creates a new default price entry for an accounting type, optionally scoped to a specific link (company or other entity); returns the persisted record. Intended for ERP integrations (e.g. Centron) — must be called with the dedicated API token bound to the role `ERP`, not a normal user login.
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
    
    def with_url(self,raw_url: str) -> PricesRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: PricesRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return PricesRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class PricesRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class PricesRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

