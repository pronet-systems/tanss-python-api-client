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
    from .timers_delete_response import TimersDeleteResponse
    from .timers_get_response import TimersGetResponse
    from .timers_put_response import TimersPutResponse

class TimersItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/tanss.app/v1/timers/{id}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new TimersItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/tanss.app/v1/timers/{id}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[TimersDeleteResponse]:
        """
        Löscht einen Timer samt aller Fragmente.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: module, Rollen TANSS_APP.Rechte: eigener Timer oder bet.VIEW_TIMERS_OF_ALL_TECHNICIANS (nur Leseprüfung; DELETE_TIMERS_OF_ALL_TECHNICIANS wird hier nicht geprüft).Hinweis: 404 ENTITY_NOT_FOUND. Status DELETED. Auch unter /api/tanss.x/v1.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[TimersDeleteResponse]
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .timers_delete_response import TimersDeleteResponse

        return await self.request_adapter.send_async(request_info, TimersDeleteResponse, None)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[TimersGetResponse]:
        """
        Liefert einen Timer.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: module, Rollen TANSS_APP.Rechte: eigener Timer oder bet.VIEW_TIMERS_OF_ALL_TECHNICIANS.Hinweis: 404 ENTITY_NOT_FOUND. Auch unter /api/tanss.x/v1.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[TimersGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .timers_get_response import TimersGetResponse

        return await self.request_adapter.send_async(request_info, TimersGetResponse, None)
    
    async def put(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[TimersPutResponse]:
        """
        Toggle Start/Stop eines Timers: läuft er (startTime>0), wird gestoppt (Dauer aufaddiert, letztes Fragment bekommt stopTime); sonst wird er gestartet (startTime=jetzt, neues Fragment).Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: module, Rollen TANSS_APP.Hinweis: Kein Body. Keine Rechteprüfung. 400 OBJECT_NOT_FOUND. Status UPDATED. Auch unter /api/tanss.x/v1.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[TimersPutResponse]
        """
        request_info = self.to_put_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .timers_put_response import TimersPutResponse

        return await self.request_adapter.send_async(request_info, TimersPutResponse, None)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Löscht einen Timer samt aller Fragmente.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: module, Rollen TANSS_APP.Rechte: eigener Timer oder bet.VIEW_TIMERS_OF_ALL_TECHNICIANS (nur Leseprüfung; DELETE_TIMERS_OF_ALL_TECHNICIANS wird hier nicht geprüft).Hinweis: 404 ENTITY_NOT_FOUND. Status DELETED. Auch unter /api/tanss.x/v1.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Liefert einen Timer.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: module, Rollen TANSS_APP.Rechte: eigener Timer oder bet.VIEW_TIMERS_OF_ALL_TECHNICIANS.Hinweis: 404 ENTITY_NOT_FOUND. Auch unter /api/tanss.x/v1.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_put_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Toggle Start/Stop eines Timers: läuft er (startTime>0), wird gestoppt (Dauer aufaddiert, letztes Fragment bekommt stopTime); sonst wird er gestartet (startTime=jetzt, neues Fragment).Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: module, Rollen TANSS_APP.Hinweis: Kein Body. Keine Rechteprüfung. 400 OBJECT_NOT_FOUND. Status UPDATED. Auch unter /api/tanss.x/v1.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.PUT, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> TimersItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: TimersItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return TimersItemRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class TimersItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class TimersItemRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class TimersItemRequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

