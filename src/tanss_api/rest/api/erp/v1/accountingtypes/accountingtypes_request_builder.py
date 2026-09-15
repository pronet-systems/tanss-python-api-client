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
    from .....models.accountingtypes403_error import Accountingtypes403Error
    from .accountingtypes_get_response import AccountingtypesGetResponse
    from .accountingtypes_post_request_body import AccountingtypesPostRequestBody
    from .accountingtypes_post_response import AccountingtypesPostResponse
    from .prices.prices_request_builder import PricesRequestBuilder

class AccountingtypesRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/erp/v1/accountingtypes
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new AccountingtypesRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/erp/v1/accountingtypes", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[AccountingtypesGetResponse]:
        """
        Returns the list of all accounting types (Leistungsarten) configured in TANSS, used by the ERP system to map accounting categories during sync. This endpoint is intended for ERP integrations (e.g. Centron) and must be called with the dedicated API token bound to the role `ERP` — it is not exposed to normal user logins.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[AccountingtypesGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .....models.accountingtypes403_error import Accountingtypes403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Accountingtypes403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .accountingtypes_get_response import AccountingtypesGetResponse

        return await self.request_adapter.send_async(request_info, AccountingtypesGetResponse, error_mapping)
    
    async def post(self,body: AccountingtypesPostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[AccountingtypesPostResponse]:
        """
        Creates a new accounting type (Leistungsart) in TANSS so the ERP system can register categories it needs for billing/sync. Intended for ERP integrations (e.g. Centron); callers must authenticate with the dedicated API token bound to the role `ERP`, not with a normal user login.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[AccountingtypesPostResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from .....models.accountingtypes403_error import Accountingtypes403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Accountingtypes403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .accountingtypes_post_response import AccountingtypesPostResponse

        return await self.request_adapter.send_async(request_info, AccountingtypesPostResponse, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Returns the list of all accounting types (Leistungsarten) configured in TANSS, used by the ERP system to map accounting categories during sync. This endpoint is intended for ERP integrations (e.g. Centron) and must be called with the dedicated API token bound to the role `ERP` — it is not exposed to normal user logins.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: AccountingtypesPostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Creates a new accounting type (Leistungsart) in TANSS so the ERP system can register categories it needs for billing/sync. Intended for ERP integrations (e.g. Centron); callers must authenticate with the dedicated API token bound to the role `ERP`, not with a normal user login.
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
    
    def with_url(self,raw_url: str) -> AccountingtypesRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: AccountingtypesRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return AccountingtypesRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def prices(self) -> PricesRequestBuilder:
        """
        The prices property
        """
        from .prices.prices_request_builder import PricesRequestBuilder

        return PricesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class AccountingtypesRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class AccountingtypesRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

