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
    from .....models.prices403_error import Prices403Error
    from .....models.tns_accounting_type_price import TnsAccountingTypePrice
    from .item.with_accounting_type_item_request_builder import WithAccountingTypeItemRequestBuilder
    from .prices_post_response import PricesPostResponse

class PricesRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/accountingTypes/prices
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new PricesRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/accountingTypes/prices", path_parameters)
    
    def by_accounting_type_id(self,accounting_type_id: int) -> WithAccountingTypeItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.v1.accountingTypes.prices.item collection
        param accounting_type_id: Id of the accounting type whose price entry should be deleted.
        Returns: WithAccountingTypeItemRequestBuilder
        """
        if accounting_type_id is None:
            raise TypeError("accounting_type_id cannot be null.")
        from .item.with_accounting_type_item_request_builder import WithAccountingTypeItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["accountingTypeId"] = accounting_type_id
        return WithAccountingTypeItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def post(self,body: TnsAccountingTypePrice, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[PricesPostResponse]:
        """
        Upserts the price for an accounting type at a given assignment (company, contract, or ticket). The controller validates the linked accounting type, delegates the access check to the link-type strategy, and returns `201` when the row is created or `202` when an existing one is updated. The accounting type price cache is cleared after persisting.
        param body: This object represents a special accountig type price
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[PricesPostResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from .....models.prices403_error import Prices403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Prices403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .prices_post_response import PricesPostResponse

        return await self.request_adapter.send_async(request_info, PricesPostResponse, error_mapping)
    
    def to_post_request_information(self,body: TnsAccountingTypePrice, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Upserts the price for an accounting type at a given assignment (company, contract, or ticket). The controller validates the linked accounting type, delegates the access check to the link-type strategy, and returns `201` when the row is created or `202` when an existing one is updated. The accounting type price cache is cleared after persisting.
        param body: This object represents a special accountig type price
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
    class PricesRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

