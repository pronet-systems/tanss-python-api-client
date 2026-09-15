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
    from ......models.tns_offer_template import TnsOfferTemplate
    from ......models.with_template403_error import WithTemplate403Error
    from .footer.footer_request_builder import FooterRequestBuilder
    from .with_template_get_response import WithTemplateGetResponse
    from .with_template_put_response import WithTemplatePutResponse

class WithTemplateItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/offers/templates/{templateId}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new WithTemplateItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/offers/templates/{templateId}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Deletes an offer template
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ......models.with_template403_error import WithTemplate403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": WithTemplate403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[WithTemplateGetResponse]:
        """
        This route gets a detailled view of an offer template
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[WithTemplateGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ......models.with_template403_error import WithTemplate403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": WithTemplate403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .with_template_get_response import WithTemplateGetResponse

        return await self.request_adapter.send_async(request_info, WithTemplateGetResponse, error_mapping)
    
    async def put(self,body: TnsOfferTemplate, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[WithTemplatePutResponse]:
        """
        This route updates an offer template
        param body: Describes an offer template
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[WithTemplatePutResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        from ......models.with_template403_error import WithTemplate403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": WithTemplate403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .with_template_put_response import WithTemplatePutResponse

        return await self.request_adapter.send_async(request_info, WithTemplatePutResponse, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Deletes an offer template
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        This route gets a detailled view of an offer template
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_put_request_information(self,body: TnsOfferTemplate, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        This route updates an offer template
        param body: Describes an offer template
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
    
    def with_url(self,raw_url: str) -> WithTemplateItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: WithTemplateItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return WithTemplateItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def footer(self) -> FooterRequestBuilder:
        """
        The footer property
        """
        from .footer.footer_request_builder import FooterRequestBuilder

        return FooterRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class WithTemplateItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class WithTemplateItemRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class WithTemplateItemRequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

