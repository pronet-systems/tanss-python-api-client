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
    from .....models.config403_error import Config403Error
    from .config_get_response import ConfigGetResponse
    from .config_post_request_body import ConfigPostRequestBody
    from .config_post_response import ConfigPostResponse

class ConfigRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/starface/config
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new ConfigRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/starface/config", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Removes the calling user's Starface XML-RPC user settings and tears down the live websocket subscription that pushes incoming-call events to TANSS. Used when an employee unlinks their Starface account. Requires technician/freelancer plus `ONLINE_SYSTEM_CONFIGURATION`.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from .....models.config403_error import Config403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Config403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[ConfigGetResponse]:
        """
        Returns the calling user's stored Starface XML-RPC user settings (host, port, login, etc.) used to register call-event subscriptions. Secrets are masked by the default filter. Requires technician/freelancer plus `ONLINE_SYSTEM_CONFIGURATION`.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ConfigGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .....models.config403_error import Config403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Config403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .config_get_response import ConfigGetResponse

        return await self.request_adapter.send_async(request_info, ConfigGetResponse, error_mapping)
    
    async def post(self,body: ConfigPostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[ConfigPostResponse]:
        """
        Creates or replaces the calling user's Starface XML-RPC settings. The new credentials are stored but the subscription is not automatically restarted — call `subscribe` (or `resubscribeAll`) to reconnect afterwards. Requires technician/freelancer plus `ONLINE_SYSTEM_CONFIGURATION`.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ConfigPostResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from .....models.config403_error import Config403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Config403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .config_post_response import ConfigPostResponse

        return await self.request_adapter.send_async(request_info, ConfigPostResponse, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Removes the calling user's Starface XML-RPC user settings and tears down the live websocket subscription that pushes incoming-call events to TANSS. Used when an employee unlinks their Starface account. Requires technician/freelancer plus `ONLINE_SYSTEM_CONFIGURATION`.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Returns the calling user's stored Starface XML-RPC user settings (host, port, login, etc.) used to register call-event subscriptions. Secrets are masked by the default filter. Requires technician/freelancer plus `ONLINE_SYSTEM_CONFIGURATION`.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: ConfigPostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Creates or replaces the calling user's Starface XML-RPC settings. The new credentials are stored but the subscription is not automatically restarted — call `subscribe` (or `resubscribeAll`) to reconnect afterwards. Requires technician/freelancer plus `ONLINE_SYSTEM_CONFIGURATION`.
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
    
    def with_url(self,raw_url: str) -> ConfigRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: ConfigRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return ConfigRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class ConfigRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class ConfigRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class ConfigRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

