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
    from .accounting_types_get_response import AccountingTypesGetResponse
    from .accounting_types_put_request_body import AccountingTypesPutRequestBody
    from .accounting_types_put_response import AccountingTypesPutResponse

class AccountingTypesItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/accountingTypes/{id}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new AccountingTypesItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/accountingTypes/{id}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Generic admin delete endpoint. Used by accounting types, currencies, payment methods, etc.; Requires the corresponding admin permission (e.g. `MANAGE_ACCOUNTING_TYPES` or `BASE_DATA_MANAGEMENT_SYSTEM_TABLES`) and checks for blocking references before the row is removed.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from .....models.accountingtypes403_error import Accountingtypes403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Accountingtypes403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[AccountingTypesGetResponse]:
        """
        Generic admin read endpoint. Returns the single configured entity (accounting type, currency, payment method, etc.) addressed by `id`. Standard admin access checks apply.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[AccountingTypesGetResponse]
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
        from .accounting_types_get_response import AccountingTypesGetResponse

        return await self.request_adapter.send_async(request_info, AccountingTypesGetResponse, error_mapping)
    
    async def put(self,body: AccountingTypesPutRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[AccountingTypesPutResponse]:
        """
        Generic admin update endpoint. Applies the JSON patch to the entity addressed by `id` and persists it. Requires the corresponding admin permission (e.g. `MANAGE_ACCOUNTING_TYPES`, `BASE_DATA_MANAGEMENT_SYSTEM_TABLES`).
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[AccountingTypesPutResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        from .....models.accountingtypes403_error import Accountingtypes403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Accountingtypes403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .accounting_types_put_response import AccountingTypesPutResponse

        return await self.request_adapter.send_async(request_info, AccountingTypesPutResponse, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Generic admin delete endpoint. Used by accounting types, currencies, payment methods, etc.; Requires the corresponding admin permission (e.g. `MANAGE_ACCOUNTING_TYPES` or `BASE_DATA_MANAGEMENT_SYSTEM_TABLES`) and checks for blocking references before the row is removed.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Generic admin read endpoint. Returns the single configured entity (accounting type, currency, payment method, etc.) addressed by `id`. Standard admin access checks apply.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_put_request_information(self,body: AccountingTypesPutRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Generic admin update endpoint. Applies the JSON patch to the entity addressed by `id` and persists it. Requires the corresponding admin permission (e.g. `MANAGE_ACCOUNTING_TYPES`, `BASE_DATA_MANAGEMENT_SYSTEM_TABLES`).
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.PUT, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> AccountingTypesItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: AccountingTypesItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return AccountingTypesItemRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class AccountingTypesItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class AccountingTypesItemRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class AccountingTypesItemRequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

