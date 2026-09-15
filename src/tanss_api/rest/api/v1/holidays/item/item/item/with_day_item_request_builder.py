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
    from .......models.with_day403_error import WithDay403Error
    from .with_day_get_response import WithDayGetResponse
    from .with_day_put_request_body import WithDayPutRequestBody
    from .with_day_put_response import WithDayPutResponse

class WithDayItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/holidays/{year}/{month}/{day}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new WithDayItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/holidays/{year}/{month}/{day}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Removes the holiday entry identified by the composite key `(day, month, year)`. Pass `year = 0` to delete a recurring entry. Requires a user from the own company with `MANAGE_HOLIDAYS`.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from .......models.with_day403_error import WithDay403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": WithDay403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[WithDayGetResponse]:
        """
        Loads a single holiday entry identified by the composite key `(day, month, year)`. Pass `year = 0` for recurring entries. Returns 404 if nothing is found. Requires the caller to be a user from the own company; no extra permission for read.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[WithDayGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .......models.with_day403_error import WithDay403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": WithDay403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .with_day_get_response import WithDayGetResponse

        return await self.request_adapter.send_async(request_info, WithDayGetResponse, error_mapping)
    
    async def put(self,body: WithDayPutRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[WithDayPutResponse]:
        """
        Updates the holiday entry identified by the composite key `(day, month, year)`; the request body carries the new field values. Requires a user from the own company with `MANAGE_HOLIDAYS`; description trimming and validation rules from create also apply.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[WithDayPutResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        from .......models.with_day403_error import WithDay403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": WithDay403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .with_day_put_response import WithDayPutResponse

        return await self.request_adapter.send_async(request_info, WithDayPutResponse, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Removes the holiday entry identified by the composite key `(day, month, year)`. Pass `year = 0` to delete a recurring entry. Requires a user from the own company with `MANAGE_HOLIDAYS`.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Loads a single holiday entry identified by the composite key `(day, month, year)`. Pass `year = 0` for recurring entries. Returns 404 if nothing is found. Requires the caller to be a user from the own company; no extra permission for read.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_put_request_information(self,body: WithDayPutRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Updates the holiday entry identified by the composite key `(day, month, year)`; the request body carries the new field values. Requires a user from the own company with `MANAGE_HOLIDAYS`; description trimming and validation rules from create also apply.
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
    
    def with_url(self,raw_url: str) -> WithDayItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: WithDayItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return WithDayItemRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class WithDayItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class WithDayItemRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class WithDayItemRequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

