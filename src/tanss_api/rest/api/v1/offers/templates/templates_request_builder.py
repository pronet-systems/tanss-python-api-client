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
    from .....models.templates403_error import Templates403Error
    from .....models.tns_offer_template import TnsOfferTemplate
    from .footer.footer_request_builder import FooterRequestBuilder
    from .global_settings.global_settings_request_builder import GlobalSettingsRequestBuilder
    from .item.with_template_item_request_builder import WithTemplateItemRequestBuilder
    from .templates_get_response import TemplatesGetResponse
    from .templates_post_response import TemplatesPostResponse

class TemplatesRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/offers/templates
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new TemplatesRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/offers/templates", path_parameters)
    
    def by_template_id(self,template_id: int) -> WithTemplateItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.v1.offers.templates.item collection
        param template_id: Id of the offer template
        Returns: WithTemplateItemRequestBuilder
        """
        if template_id is None:
            raise TypeError("template_id cannot be null.")
        from .item.with_template_item_request_builder import WithTemplateItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["templateId"] = template_id
        return WithTemplateItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[TemplatesGetResponse]:
        """
        This route gets a list of all offer termplates
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[TemplatesGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .....models.templates403_error import Templates403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Templates403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .templates_get_response import TemplatesGetResponse

        return await self.request_adapter.send_async(request_info, TemplatesGetResponse, error_mapping)
    
    async def post(self,body: TnsOfferTemplate, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[TemplatesPostResponse]:
        """
        Creates a new offer template
        param body: Describes an offer template
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[TemplatesPostResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from .....models.templates403_error import Templates403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Templates403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .templates_post_response import TemplatesPostResponse

        return await self.request_adapter.send_async(request_info, TemplatesPostResponse, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        This route gets a list of all offer termplates
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: TnsOfferTemplate, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Creates a new offer template
        param body: Describes an offer template
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
    
    def with_url(self,raw_url: str) -> TemplatesRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: TemplatesRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return TemplatesRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def footer(self) -> FooterRequestBuilder:
        """
        The footer property
        """
        from .footer.footer_request_builder import FooterRequestBuilder

        return FooterRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def global_settings(self) -> GlobalSettingsRequestBuilder:
        """
        The globalSettings property
        """
        from .global_settings.global_settings_request_builder import GlobalSettingsRequestBuilder

        return GlobalSettingsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class TemplatesRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class TemplatesRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

