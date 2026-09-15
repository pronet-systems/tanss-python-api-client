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
    from .....models.pref403_error import Pref403Error
    from .pref_post_request_body import PrefPostRequestBody
    from .pref_post_response import PrefPostResponse
    from .pref_put_request_body import PrefPutRequestBody
    from .pref_put_response import PrefPutResponse

class PrefRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/util/pref
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new PrefRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/util/pref", path_parameters)
    
    async def post(self,body: PrefPostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[PrefPostResponse]:
        """
        Persists a single integer preference value, identified by the triple `sectionId / assignmentId / preferenceId`. An access check based on the section is performed before the row is stored; existing entries with the same key are updated.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[PrefPostResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from .....models.pref403_error import Pref403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Pref403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .pref_post_response import PrefPostResponse

        return await self.request_adapter.send_async(request_info, PrefPostResponse, error_mapping)
    
    async def put(self,body: PrefPutRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[PrefPutResponse]:
        """
        Resolves a batch of integer preferences. The body is a nested map `<sectionId>: { <assignmentId>: { <preferenceId>: <ignored> } }`; the response mirrors that shape with the stored values, returning `null` for entries the caller cannot read.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[PrefPutResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        from .....models.pref403_error import Pref403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Pref403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .pref_put_response import PrefPutResponse

        return await self.request_adapter.send_async(request_info, PrefPutResponse, error_mapping)
    
    def to_post_request_information(self,body: PrefPostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Persists a single integer preference value, identified by the triple `sectionId / assignmentId / preferenceId`. An access check based on the section is performed before the row is stored; existing entries with the same key are updated.
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
    
    def to_put_request_information(self,body: PrefPutRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Resolves a batch of integer preferences. The body is a nested map `<sectionId>: { <assignmentId>: { <preferenceId>: <ignored> } }`; the response mirrors that shape with the stored values, returning `null` for entries the caller cannot read.
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
    
    def with_url(self,raw_url: str) -> PrefRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: PrefRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return PrefRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class PrefRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class PrefRequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

