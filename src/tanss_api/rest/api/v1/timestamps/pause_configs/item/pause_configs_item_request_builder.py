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
    from ......models.pause_configs403_error import PauseConfigs403Error
    from ......models.timestamp_pause_config import TimestampPauseConfig
    from .pause_configs_get_response import PauseConfigsGetResponse
    from .pause_configs_put_response import PauseConfigsPutResponse

class PauseConfigsItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/timestamps/pauseConfigs/{id}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new PauseConfigsItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/timestamps/pauseConfigs/{id}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        deletes a pause config
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ......models.pause_configs403_error import PauseConfigs403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": PauseConfigs403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[PauseConfigsGetResponse]:
        """
        Liefert eine Pausen-Konfiguration (Mindestpause ab X Minuten Arbeitszeit) der Zeiterfassung.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId.Rechte: TIMESTAMP_STATISTICS_EMPLOYEES_OF_OWN_DEPARTMENTS, TIMESTAMP_PAUSE_CONFIG.Hinweise: Unbekannte ID -> TnsDataNotFoundException. meta FOUND.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[PauseConfigsGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .pause_configs_get_response import PauseConfigsGetResponse

        return await self.request_adapter.send_async(request_info, PauseConfigsGetResponse, None)
    
    async def put(self,body: TimestampPauseConfig, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[PauseConfigsPutResponse]:
        """
        updates a pause config
        param body: Defines a configuration for automatical pause subtraction.This is needed because longer working periods must contain certain pauses.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[PauseConfigsPutResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        from ......models.pause_configs403_error import PauseConfigs403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": PauseConfigs403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .pause_configs_put_response import PauseConfigsPutResponse

        return await self.request_adapter.send_async(request_info, PauseConfigsPutResponse, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        deletes a pause config
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Liefert eine Pausen-Konfiguration (Mindestpause ab X Minuten Arbeitszeit) der Zeiterfassung.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId.Rechte: TIMESTAMP_STATISTICS_EMPLOYEES_OF_OWN_DEPARTMENTS, TIMESTAMP_PAUSE_CONFIG.Hinweise: Unbekannte ID -> TnsDataNotFoundException. meta FOUND.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_put_request_information(self,body: TimestampPauseConfig, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        updates a pause config
        param body: Defines a configuration for automatical pause subtraction.This is needed because longer working periods must contain certain pauses.
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
    
    def with_url(self,raw_url: str) -> PauseConfigsItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: PauseConfigsItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return PauseConfigsItemRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class PauseConfigsItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class PauseConfigsItemRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class PauseConfigsItemRequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

