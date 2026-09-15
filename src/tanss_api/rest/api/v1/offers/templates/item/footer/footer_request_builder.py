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
    from .......models.footer403_error import Footer403Error
    from .footer_get_response import FooterGetResponse
    from .footer_put_request_body import FooterPutRequestBody
    from .footer_put_response import FooterPutResponse

class FooterRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/offers/templates/{templateId}/footer
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new FooterRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/offers/templates/{templateId}/footer", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Removes the footer block from the given offer template. Future PDFs rendered from this template will then fall back to no footer (or the global default).
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from .......models.footer403_error import Footer403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Footer403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[FooterGetResponse]:
        """
        Returns the footer block configured for the given offer template, used to render the bottom area of generated offer PDFs.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[FooterGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .......models.footer403_error import Footer403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Footer403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .footer_get_response import FooterGetResponse

        return await self.request_adapter.send_async(request_info, FooterGetResponse, error_mapping)
    
    async def put(self,body: FooterPutRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[FooterPutResponse]:
        """
        Updates the footer block of an offer template (HTML/text rendered at the bottom of every PDF generated from this template).
        param body: Request body.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[FooterPutResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        from .......models.footer403_error import Footer403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Footer403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .footer_put_response import FooterPutResponse

        return await self.request_adapter.send_async(request_info, FooterPutResponse, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Removes the footer block from the given offer template. Future PDFs rendered from this template will then fall back to no footer (or the global default).
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Returns the footer block configured for the given offer template, used to render the bottom area of generated offer PDFs.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_put_request_information(self,body: FooterPutRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Updates the footer block of an offer template (HTML/text rendered at the bottom of every PDF generated from this template).
        param body: Request body.
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
    
    def with_url(self,raw_url: str) -> FooterRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: FooterRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return FooterRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class FooterRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class FooterRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class FooterRequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

