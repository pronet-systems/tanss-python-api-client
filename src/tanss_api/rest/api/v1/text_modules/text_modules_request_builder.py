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
    from ....models.text_modules403_error import TextModules403Error
    from .item.text_modules_item_request_builder import TextModulesItemRequestBuilder
    from .properties.properties_request_builder import PropertiesRequestBuilder
    from .text_modules_get_response import TextModulesGetResponse
    from .text_modules_post_request_body import TextModulesPostRequestBody
    from .text_modules_post_response import TextModulesPostResponse
    from .type.type_request_builder import TypeRequestBuilder

class TextModulesRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/textModules
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new TextModulesRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/textModules", path_parameters)
    
    def by_id(self,id: int) -> TextModulesItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.v1.textModules.item collection
        param id: Id of the text module.
        Returns: TextModulesItemRequestBuilder
        """
        if id is None:
            raise TypeError("id cannot be null.")
        from .item.text_modules_item_request_builder import TextModulesItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["id"] = id
        return TextModulesItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[TextModulesGetResponse]:
        """
        Returns every object (text snippet / canned response) visible to the caller. Visibility isenforced per row (assignments to types, departments, or specific employees).Requires a technician or freelancer — customer logins are blocked; standard permission checks apply.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[TextModulesGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ....models.text_modules403_error import TextModules403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": TextModules403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .text_modules_get_response import TextModulesGetResponse

        return await self.request_adapter.send_async(request_info, TextModulesGetResponse, error_mapping)
    
    async def post(self,body: TextModulesPostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[TextModulesPostResponse]:
        """
        Creates a new object. The `creatorId` is set server-side from the logged-in user. After insert,type / department / employee assignments contained in the body are persisted as well.Standard admin permission checks apply.
        param body: Request body.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[TextModulesPostResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ....models.text_modules403_error import TextModules403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": TextModules403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .text_modules_post_response import TextModulesPostResponse

        return await self.request_adapter.send_async(request_info, TextModulesPostResponse, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Returns every object (text snippet / canned response) visible to the caller. Visibility isenforced per row (assignments to types, departments, or specific employees).Requires a technician or freelancer — customer logins are blocked; standard permission checks apply.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: TextModulesPostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Creates a new object. The `creatorId` is set server-side from the logged-in user. After insert,type / department / employee assignments contained in the body are persisted as well.Standard admin permission checks apply.
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
    
    def with_url(self,raw_url: str) -> TextModulesRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: TextModulesRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return TextModulesRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def properties(self) -> PropertiesRequestBuilder:
        """
        The properties property
        """
        from .properties.properties_request_builder import PropertiesRequestBuilder

        return PropertiesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def type(self) -> TypeRequestBuilder:
        """
        The type property
        """
        from .type.type_request_builder import TypeRequestBuilder

        return TypeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class TextModulesRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class TextModulesRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

