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
    from .....models.configuration403_error import Configuration403Error
    from .check.check_request_builder import CheckRequestBuilder
    from .configuration_put_request_body import ConfigurationPutRequestBody
    from .configuration_put_response import ConfigurationPutResponse
    from .item.with_type_item_request_builder import WithTypeItemRequestBuilder

class ConfigurationRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/remoteSupports/configuration
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new ConfigurationRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/remoteSupports/configuration", path_parameters)
    
    def by_type(self,type: str) -> WithTypeItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.v1.remoteSupports.configuration.item collection
        param type: Remote-support provider type, e.g. TEAMVIEWER, ANYDESK, ISL_ONLINE.
        Returns: WithTypeItemRequestBuilder
        """
        if type is None:
            raise TypeError("type cannot be null.")
        from .item.with_type_item_request_builder import WithTypeItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["type"] = type
        return WithTypeItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def put(self,body: ConfigurationPutRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[ConfigurationPutResponse]:
        """
        Persists the configuration for a remote-support provider (endpoint, token, fetching flags). Typically called after a successful`configuration/check`. Restricted to users with the `ONLINE_SYSTEM_CONFIGURATION` permission or technician/freelancer role(OSK admin scope).
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ConfigurationPutResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        from .....models.configuration403_error import Configuration403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Configuration403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .configuration_put_response import ConfigurationPutResponse

        return await self.request_adapter.send_async(request_info, ConfigurationPutResponse, error_mapping)
    
    def to_put_request_information(self,body: ConfigurationPutRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Persists the configuration for a remote-support provider (endpoint, token, fetching flags). Typically called after a successful`configuration/check`. Restricted to users with the `ONLINE_SYSTEM_CONFIGURATION` permission or technician/freelancer role(OSK admin scope).
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
    
    def with_url(self,raw_url: str) -> ConfigurationRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: ConfigurationRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return ConfigurationRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def check(self) -> CheckRequestBuilder:
        """
        The check property
        """
        from .check.check_request_builder import CheckRequestBuilder

        return CheckRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class ConfigurationRequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

