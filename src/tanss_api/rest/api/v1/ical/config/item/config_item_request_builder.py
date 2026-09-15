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
    from ......models.config403_error import Config403Error
    from .config_get_response import ConfigGetResponse
    from .config_put_request_body import ConfigPutRequestBody
    from .config_put_response import ConfigPutResponse

class ConfigItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/ical/config/{id}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new ConfigItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/ical/config/{id}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Removes an iCal feed configuration by id. Existing calendar subscribers using that configuration id will subsequently receive an error response on `/api/v1/ical/fetch/{configurationId}`, so this effectively revokes the external feed.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ......models.config403_error import Config403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Config403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[ConfigGetResponse]:
        """
        Returns the stored iCal feed configuration identified by `id` (filters such as included employees and planning types). The bcrypt-hashed password used by calendar clients is not exposed in plain text.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ConfigGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ......models.config403_error import Config403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Config403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .config_get_response import ConfigGetResponse

        return await self.request_adapter.send_async(request_info, ConfigGetResponse, error_mapping)
    
    async def put(self,body: ConfigPutRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[ConfigPutResponse]:
        """
        Updates an existing iCal feed configuration. If the body carries a new `password`, it is bcrypt-hashed before being persisted; the `id` in the body is ignored in favour of the path parameter.
        param body: Request body.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ConfigPutResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        from ......models.config403_error import Config403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Config403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .config_put_response import ConfigPutResponse

        return await self.request_adapter.send_async(request_info, ConfigPutResponse, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Removes an iCal feed configuration by id. Existing calendar subscribers using that configuration id will subsequently receive an error response on `/api/v1/ical/fetch/{configurationId}`, so this effectively revokes the external feed.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Returns the stored iCal feed configuration identified by `id` (filters such as included employees and planning types). The bcrypt-hashed password used by calendar clients is not exposed in plain text.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_put_request_information(self,body: ConfigPutRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Updates an existing iCal feed configuration. If the body carries a new `password`, it is bcrypt-hashed before being persisted; the `id` in the body is ignored in favour of the path parameter.
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
    
    def with_url(self,raw_url: str) -> ConfigItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: ConfigItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return ConfigItemRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class ConfigItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class ConfigItemRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class ConfigItemRequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

