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
    from .....models.languages403_error import Languages403Error
    from .languages_post_request_body import LanguagesPostRequestBody
    from .languages_post_response import LanguagesPostResponse
    from .languages_put_response import LanguagesPutResponse

class LanguagesRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/util/languages
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new LanguagesRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/util/languages{?language*}", path_parameters)
    
    async def post(self,body: LanguagesPostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[LanguagesPostResponse]:
        """
        Resolves a batch of language keys: the body lists translation areas as top-level keys, each mapping to an object of key names whose values are placeholders. The response mirrors the structure but replaces every value with the localised string for the caller's currently active language.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[LanguagesPostResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from .....models.languages403_error import Languages403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Languages403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .languages_post_response import LanguagesPostResponse

        return await self.request_adapter.send_async(request_info, LanguagesPostResponse, error_mapping)
    
    async def put(self,request_configuration: Optional[RequestConfiguration[LanguagesRequestBuilderPutQueryParameters]] = None) -> Optional[LanguagesPutResponse]:
        """
        Persists the requested UI language code for the authenticated user. Subsequent language string lookups for the same user use this value. The response carries a simple boolean success flag.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[LanguagesPutResponse]
        """
        request_info = self.to_put_request_information(
            request_configuration
        )
        from .....models.languages403_error import Languages403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Languages403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .languages_put_response import LanguagesPutResponse

        return await self.request_adapter.send_async(request_info, LanguagesPutResponse, error_mapping)
    
    def to_post_request_information(self,body: LanguagesPostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Resolves a batch of language keys: the body lists translation areas as top-level keys, each mapping to an object of key names whose values are placeholders. The response mirrors the structure but replaces every value with the localised string for the caller's currently active language.
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
    
    def to_put_request_information(self,request_configuration: Optional[RequestConfiguration[LanguagesRequestBuilderPutQueryParameters]] = None) -> RequestInformation:
        """
        Persists the requested UI language code for the authenticated user. Subsequent language string lookups for the same user use this value. The response carries a simple boolean success flag.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.PUT, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> LanguagesRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: LanguagesRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return LanguagesRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class LanguagesRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class LanguagesRequestBuilderPutQueryParameters():
        """
        Persists the requested UI language code for the authenticated user. Subsequent language string lookups for the same user use this value. The response carries a simple boolean success flag.
        """
        # UI language code to persist for the authenticated user.
        language: Optional[str] = None

    
    @dataclass
    class LanguagesRequestBuilderPutRequestConfiguration(RequestConfiguration[LanguagesRequestBuilderPutQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

