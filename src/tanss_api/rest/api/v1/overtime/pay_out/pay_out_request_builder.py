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
    from .....models.pay_out403_error import PayOut403Error
    from .item.pay_out_item_request_builder import PayOutItemRequestBuilder
    from .pay_out_post_request_body import PayOutPostRequestBody
    from .pay_out_post_response import PayOutPostResponse

class PayOutRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/overtime/payOut
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new PayOutRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/overtime/payOut", path_parameters)
    
    def by_id(self,id: int) -> PayOutItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.v1.overtime.payOut.item collection
        param id: Id of the overtime pay out request
        Returns: PayOutItemRequestBuilder
        """
        if id is None:
            raise TypeError("id cannot be null.")
        from .item.pay_out_item_request_builder import PayOutItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["id"] = id
        return PayOutItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def post(self,body: PayOutPostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[PayOutPostResponse]:
        """
        Creates a new overtime pay-out request for the caller.
        param body: Request body.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[PayOutPostResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from .....models.pay_out403_error import PayOut403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": PayOut403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .pay_out_post_response import PayOutPostResponse

        return await self.request_adapter.send_async(request_info, PayOutPostResponse, error_mapping)
    
    def to_post_request_information(self,body: PayOutPostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Creates a new overtime pay-out request for the caller.
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
    
    def with_url(self,raw_url: str) -> PayOutRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: PayOutRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return PayOutRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class PayOutRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

