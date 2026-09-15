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
    from ....models.currencies403_error import Currencies403Error
    from .currencies_get_response import CurrenciesGetResponse
    from .currencies_post_request_body import CurrenciesPostRequestBody
    from .currencies_post_response import CurrenciesPostResponse
    from .item.currencies_item_request_builder import CurrenciesItemRequestBuilder

class CurrenciesRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/currencies
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new CurrenciesRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/currencies", path_parameters)
    
    def by_id(self,id: str) -> CurrenciesItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.v1.currencies.item collection
        param id: Id of the currency.
        Returns: CurrenciesItemRequestBuilder
        """
        if id is None:
            raise TypeError("id cannot be null.")
        from .item.currencies_item_request_builder import CurrenciesItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["id"] = id
        return CurrenciesItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[CurrenciesGetResponse]:
        """
        Returns every currency configured in the system together with its conversion factor. Read access uses the default CRUD basic permission check; mutations require a user from the own company with `BASE_DATA_MANAGEMENT_SYSTEM_TABLES`.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[CurrenciesGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ....models.currencies403_error import Currencies403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Currencies403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .currencies_get_response import CurrenciesGetResponse

        return await self.request_adapter.send_async(request_info, CurrenciesGetResponse, error_mapping)
    
    async def post(self,body: CurrenciesPostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[CurrenciesPostResponse]:
        """
        Creates a new currency entry that can be assigned to companies, offers, and invoices. Requires a user from the own company with `BASE_DATA_MANAGEMENT_SYSTEM_TABLES`; the factor is stored as a multiplier relative to the system's leading currency.
        param body: Request body.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[CurrenciesPostResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ....models.currencies403_error import Currencies403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Currencies403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .currencies_post_response import CurrenciesPostResponse

        return await self.request_adapter.send_async(request_info, CurrenciesPostResponse, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Returns every currency configured in the system together with its conversion factor. Read access uses the default CRUD basic permission check; mutations require a user from the own company with `BASE_DATA_MANAGEMENT_SYSTEM_TABLES`.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: CurrenciesPostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Creates a new currency entry that can be assigned to companies, offers, and invoices. Requires a user from the own company with `BASE_DATA_MANAGEMENT_SYSTEM_TABLES`; the factor is stored as a multiplier relative to the system's leading currency.
        param body: Request body.
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
    
    def with_url(self,raw_url: str) -> CurrenciesRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: CurrenciesRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return CurrenciesRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class CurrenciesRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class CurrenciesRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

