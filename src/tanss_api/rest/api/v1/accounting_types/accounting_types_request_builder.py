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
    from ....models.accountingtypes403_error import Accountingtypes403Error
    from .accounting_types_get_response import AccountingTypesGetResponse
    from .accounting_types_post_request_body import AccountingTypesPostRequestBody
    from .accounting_types_post_response import AccountingTypesPostResponse
    from .item.accounting_types_item_request_builder import AccountingTypesItemRequestBuilder
    from .prices.prices_request_builder import PricesRequestBuilder

class AccountingTypesRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/accountingTypes
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new AccountingTypesRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/accountingTypes", path_parameters)
    
    def by_id(self,id: str) -> AccountingTypesItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.v1.accountingTypes.item collection
        param id: Id of the accounting type.
        Returns: AccountingTypesItemRequestBuilder
        """
        if id is None:
            raise TypeError("id cannot be null.")
        from .item.accounting_types_item_request_builder import AccountingTypesItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["id"] = id
        return AccountingTypesItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[AccountingTypesGetResponse]:
        """
        Returns every accounting type configured in the system, including inactive ones. Standard admin list filters are applied before the payload is built. Callable by technicians and freelancers; modifying operations additionally require `MANAGE_ACCOUNTING_TYPES`.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[AccountingTypesGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ....models.accountingtypes403_error import Accountingtypes403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Accountingtypes403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .accounting_types_get_response import AccountingTypesGetResponse

        return await self.request_adapter.send_async(request_info, AccountingTypesGetResponse, error_mapping)
    
    async def post(self,body: AccountingTypesPostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[AccountingTypesPostResponse]:
        """
        Creates a new accounting type entry that can later be referenced from services, contracts, and tickets. Requires `MANAGE_ACCOUNTING_TYPES`; the entry is validated and persisted via the default CRUD lifecycle.
        param body: Request body.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[AccountingTypesPostResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ....models.accountingtypes403_error import Accountingtypes403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Accountingtypes403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .accounting_types_post_response import AccountingTypesPostResponse

        return await self.request_adapter.send_async(request_info, AccountingTypesPostResponse, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Returns every accounting type configured in the system, including inactive ones. Standard admin list filters are applied before the payload is built. Callable by technicians and freelancers; modifying operations additionally require `MANAGE_ACCOUNTING_TYPES`.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: AccountingTypesPostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Creates a new accounting type entry that can later be referenced from services, contracts, and tickets. Requires `MANAGE_ACCOUNTING_TYPES`; the entry is validated and persisted via the default CRUD lifecycle.
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
    
    def with_url(self,raw_url: str) -> AccountingTypesRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: AccountingTypesRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return AccountingTypesRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def prices(self) -> PricesRequestBuilder:
        """
        The prices property
        """
        from .prices.prices_request_builder import PricesRequestBuilder

        return PricesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class AccountingTypesRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class AccountingTypesRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

