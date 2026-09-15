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
    from .....models.tns_timer import TnsTimer
    from .item.timers_item_request_builder import TimersItemRequestBuilder
    from .notes.notes_request_builder import NotesRequestBuilder
    from .timers_get_response import TimersGetResponse
    from .timers_post_response import TimersPostResponse

class TimersRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/tanss.app/v1/timers
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new TimersRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/tanss.app/v1/timers", path_parameters)
    
    def by_id(self,id: int) -> TimersItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.tanssApp.v1.timers.item collection
        param id: Id des Timers
        Returns: TimersItemRequestBuilder
        """
        if id is None:
            raise TypeError("id cannot be null.")
        from .item.timers_item_request_builder import TimersItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["id"] = id
        return TimersItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[TimersRequestBuilderGetQueryParameters]] = None) -> Optional[TimersGetResponse]:
        """
        Liefert alle Timer eines Mitarbeiters (ohne Fragmente) inkl. unfolded-Flag aus den Benutzerpräferenzen.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: module, Rollen TANSS_APP.Hinweis: Query employeeId Pflicht (kein Default). Keine Rechteprüfung – Timer beliebiger Mitarbeiter abrufbar. Auch unter /api/tanss.x/v1.
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
    
    async def post(self,body: TnsTimer, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[TimersPostResponse]:
        """
        Startet einen neuen Timer für tnsTimer.employeeId (startTime=jetzt) und legt das erste Zeitfragment an.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: module, Rollen TANSS_APP.Hinweis: employeeId=0 -> TnsInvalidParameterException("employeeId"). Keine Rechteprüfung. Status CREATED. Auch unter /api/tanss.x/v1.
        param body: Timer der TANSS.App/TANSS.X-Routen (Timer plus startTime, note, fragments, unfolded)
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[TimersPostResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .timers_post_response import TimersPostResponse

        return await self.request_adapter.send_async(request_info, TimersPostResponse, None)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[TimersRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Liefert alle Timer eines Mitarbeiters (ohne Fragmente) inkl. unfolded-Flag aus den Benutzerpräferenzen.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: module, Rollen TANSS_APP.Hinweis: Query employeeId Pflicht (kein Default). Keine Rechteprüfung – Timer beliebiger Mitarbeiter abrufbar. Auch unter /api/tanss.x/v1.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, '{+baseurl}/api/tanss.app/v1/timers?employeeId={employeeId}', self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: TnsTimer, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Startet einen neuen Timer für tnsTimer.employeeId (startTime=jetzt) und legt das erste Zeitfragment an.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: module, Rollen TANSS_APP.Hinweis: employeeId=0 -> TnsInvalidParameterException("employeeId"). Keine Rechteprüfung. Status CREATED. Auch unter /api/tanss.x/v1.
        param body: Timer der TANSS.App/TANSS.X-Routen (Timer plus startTime, note, fragments, unfolded)
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
    
    def with_url(self,raw_url: str) -> TimersRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: TimersRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return TimersRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def notes(self) -> NotesRequestBuilder:
        """
        The notes property
        """
        from .notes.notes_request_builder import NotesRequestBuilder

        return NotesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class TimersRequestBuilderGetQueryParameters():
        """
        Liefert alle Timer eines Mitarbeiters (ohne Fragmente) inkl. unfolded-Flag aus den Benutzerpräferenzen.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: module, Rollen TANSS_APP.Hinweis: Query employeeId Pflicht (kein Default). Keine Rechteprüfung – Timer beliebiger Mitarbeiter abrufbar. Auch unter /api/tanss.x/v1.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "employee_id":
                return "employeeId"
            return original_name
        
        # Id des Mitarbeiters
        employee_id: Optional[int] = None

    
    @dataclass
    class TimersRequestBuilderGetRequestConfiguration(RequestConfiguration[TimersRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class TimersRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

