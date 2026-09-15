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
    from .with_employee_get_response import WithEmployeeGetResponse

class WithEmployeeItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/coero/v1/timestamp/info/{employeeId}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new WithEmployeeItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/coero/v1/timestamp/info/{employeeId}{?from*,till*}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[WithEmployeeItemRequestBuilderGetQueryParameters]] = None) -> Optional[WithEmployeeGetResponse]:
        """
        Liefert die Zeitstempel eines Mitarbeiters im Zeitraum, gruppiert pro Tag (TimestampInfo) inkl. berechneter Perioden je Typ.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: module, Rollen COERO.Rechte: ROLE_COERO (WebSecurity).Hinweise: from/till (Unix-Sekunden), Default 0/0 = heutiger Tag. OFF-Stempel exakt bei from und ON-Stempel exakt bei till werden entfernt; Datum wird gerundet. Nur timestamps/types/weekDay befüllt; history, manualBookings, dayClosing, changesRequested bleiben leer. Kein Rechte-/Lizenz-Check im Service. Reihenfolge der Tage undefiniert. meta FOUND.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[WithEmployeeGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .with_employee_get_response import WithEmployeeGetResponse

        return await self.request_adapter.send_async(request_info, WithEmployeeGetResponse, None)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[WithEmployeeItemRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Liefert die Zeitstempel eines Mitarbeiters im Zeitraum, gruppiert pro Tag (TimestampInfo) inkl. berechneter Perioden je Typ.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: module, Rollen COERO.Rechte: ROLE_COERO (WebSecurity).Hinweise: from/till (Unix-Sekunden), Default 0/0 = heutiger Tag. OFF-Stempel exakt bei from und ON-Stempel exakt bei till werden entfernt; Datum wird gerundet. Nur timestamps/types/weekDay befüllt; history, manualBookings, dayClosing, changesRequested bleiben leer. Kein Rechte-/Lizenz-Check im Service. Reihenfolge der Tage undefiniert. meta FOUND.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> WithEmployeeItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: WithEmployeeItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return WithEmployeeItemRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class WithEmployeeItemRequestBuilderGetQueryParameters():
        """
        Liefert die Zeitstempel eines Mitarbeiters im Zeitraum, gruppiert pro Tag (TimestampInfo) inkl. berechneter Perioden je Typ.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: module, Rollen COERO.Rechte: ROLE_COERO (WebSecurity).Hinweise: from/till (Unix-Sekunden), Default 0/0 = heutiger Tag. OFF-Stempel exakt bei from und ON-Stempel exakt bei till werden entfernt; Datum wird gerundet. Nur timestamps/types/weekDay befüllt; history, manualBookings, dayClosing, changesRequested bleiben leer. Kein Rechte-/Lizenz-Check im Service. Reihenfolge der Tage undefiniert. meta FOUND.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "from_":
                return "from"
            if original_name == "till":
                return "till"
            return original_name
        
        # Beginn des Zeitraums (Unix-Sekunden); 0 = heutiger Tagesbeginn
        from_: Optional[int] = None

        # Ende des Zeitraums (Unix-Sekunden); 0 = heutiges Tagesende
        till: Optional[int] = None

    
    @dataclass
    class WithEmployeeItemRequestBuilderGetRequestConfiguration(RequestConfiguration[WithEmployeeItemRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

