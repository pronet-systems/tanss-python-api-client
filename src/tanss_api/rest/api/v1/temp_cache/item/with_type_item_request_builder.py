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
    from .....models.with_type403_error import WithType403Error
    from .with_type_get_response import WithTypeGetResponse
    from .with_type_post_response import WithTypePostResponse

class WithTypeItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/tempCache/{type}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new WithTypeItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/tempCache/{type}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Removes the temp-cache row of `type` belonging to the logged-in user. Used when the client discards anunsaved draft (form data, search context, ...) backed by the server-side temp cache. Returns `400` ifno temp cache of that type exists for the user.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from .....models.with_type403_error import WithType403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": WithType403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[WithTypeGetResponse]:
        """
        Returns the currently-stored temp-cache value of `type` for the logged-in user, deserialised according toits type. The response also exposes the cache's `modified` timestamp and`ageInSeconds` via `properties.extras` so the client can decide whether the draft is stale.Returns `400` (DATA_NOT_FOUND) when no temp cache of that type exists for the user.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[WithTypeGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .....models.with_type403_error import WithType403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": WithType403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .with_type_get_response import WithTypeGetResponse

        return await self.request_adapter.send_async(request_info, WithTypeGetResponse, error_mapping)
    
    async def post(self,body: str, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[WithTypePostResponse]:
        """
        Persists (or updates) a temp-cache entry of `type` for the logged-in user. The request body is the rawserialised payload (handled as a string and stored verbatim) — it is deserialised according to its typeon read. The endpoint always returns the freshly deserialised content together with the new `modified`timestamp, so the client can confirm the round-trip.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[WithTypePostResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from .....models.with_type403_error import WithType403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": WithType403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .with_type_post_response import WithTypePostResponse

        return await self.request_adapter.send_async(request_info, WithTypePostResponse, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Removes the temp-cache row of `type` belonging to the logged-in user. Used when the client discards anunsaved draft (form data, search context, ...) backed by the server-side temp cache. Returns `400` ifno temp cache of that type exists for the user.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Returns the currently-stored temp-cache value of `type` for the logged-in user, deserialised according toits type. The response also exposes the cache's `modified` timestamp and`ageInSeconds` via `properties.extras` so the client can decide whether the draft is stale.Returns `400` (DATA_NOT_FOUND) when no temp cache of that type exists for the user.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: str, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Persists (or updates) a temp-cache entry of `type` for the logged-in user. The request body is the rawserialised payload (handled as a string and stored verbatim) — it is deserialised according to its typeon read. The endpoint always returns the freshly deserialised content together with the new `modified`timestamp, so the client can confirm the round-trip.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.POST, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_scalar(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> WithTypeItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: WithTypeItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return WithTypeItemRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class WithTypeItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class WithTypeItemRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class WithTypeItemRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

