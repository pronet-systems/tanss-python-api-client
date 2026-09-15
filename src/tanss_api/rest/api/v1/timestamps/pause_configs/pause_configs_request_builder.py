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
    from .....models.pause_configs403_error import PauseConfigs403Error
    from .....models.timestamp_pause_config import TimestampPauseConfig
    from .item.pause_configs_item_request_builder import PauseConfigsItemRequestBuilder
    from .pause_configs_get_response import PauseConfigsGetResponse
    from .pause_configs_post_response import PauseConfigsPostResponse

class PauseConfigsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/timestamps/pauseConfigs
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new PauseConfigsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/timestamps/pauseConfigs", path_parameters)
    
    def by_id(self,id: int) -> PauseConfigsItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.v1.timestamps.pauseConfigs.item collection
        param id: id of the pause config
        Returns: PauseConfigsItemRequestBuilder
        """
        if id is None:
            raise TypeError("id cannot be null.")
        from .item.pause_configs_item_request_builder import PauseConfigsItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["id"] = id
        return PauseConfigsItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[PauseConfigsGetResponse]:
        """
        Defines a configuration for automatical pause subtraction.This is needed because longer working periods must contain certain pauses.In this section, those pause config objects are maintained.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[PauseConfigsGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .....models.pause_configs403_error import PauseConfigs403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": PauseConfigs403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .pause_configs_get_response import PauseConfigsGetResponse

        return await self.request_adapter.send_async(request_info, PauseConfigsGetResponse, error_mapping)
    
    async def post(self,body: TimestampPauseConfig, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[PauseConfigsPostResponse]:
        """
        creates a pause config
        param body: Defines a configuration for automatical pause subtraction.This is needed because longer working periods must contain certain pauses.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[PauseConfigsPostResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from .....models.pause_configs403_error import PauseConfigs403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": PauseConfigs403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .pause_configs_post_response import PauseConfigsPostResponse

        return await self.request_adapter.send_async(request_info, PauseConfigsPostResponse, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Defines a configuration for automatical pause subtraction.This is needed because longer working periods must contain certain pauses.In this section, those pause config objects are maintained.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: TimestampPauseConfig, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        creates a pause config
        param body: Defines a configuration for automatical pause subtraction.This is needed because longer working periods must contain certain pauses.
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
    
    def with_url(self,raw_url: str) -> PauseConfigsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: PauseConfigsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return PauseConfigsRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class PauseConfigsRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class PauseConfigsRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

