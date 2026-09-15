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
    from .info.info_request_builder import InfoRequestBuilder
    from .timestamp_post_request_body import TimestampPostRequestBody
    from .timestamp_post_response import TimestampPostResponse

class TimestampRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/coero/v1/timestamp
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new TimestampRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/coero/v1/timestamp", path_parameters)
    
    async def post(self,body: TimestampPostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[TimestampPostResponse]:
        """
        Erstellt einen Zeitstempel (Kommen/Gehen/Pause) für einen Mitarbeiter über die Coero-Schnittstelle.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: module, Rollen COERO.Rechte: Lizenzmodul TIMESTAMP (sonst TnsModuleNotLicensedException); ROLE_COERO (WebSecurity); ROLE_COERO/ROLE_TIMESTAMP umgehen TIMESTAMP_MODULE_ACCESS / TIMESTAMP_STATISTICS_EMPLOYEES_OF_OWN_DEPARTMENTS.Hinweise: employeeId bleibt nur bei ROLE_COERO/ROLE_TIMESTAMP oder Recht EDIT_TIMESTAMPS_WITH_ACCESS erhalten, sonst wird der Request-User gesetzt; employeeId==0 = EMLOYEE_ID_MUST_BE_SET. date 0 = jetzt (Unix-Sekunden). Key creationDate wird immer entfernt. Reihenfolge-Prüfung gegen alle Stempel des Tages (TnsTimestampWrongOrderException); Tagesabschluss vorhanden = 403 CANT_MODIFY_TIMESTAMP_DAYCLOSING_EXISTS. creationMode=COERO_API. Nach dem Speichern Auto-Pausen-Logik. meta CREATED.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[TimestampPostResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .timestamp_post_response import TimestampPostResponse

        return await self.request_adapter.send_async(request_info, TimestampPostResponse, None)
    
    def to_post_request_information(self,body: TimestampPostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Erstellt einen Zeitstempel (Kommen/Gehen/Pause) für einen Mitarbeiter über die Coero-Schnittstelle.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: module, Rollen COERO.Rechte: Lizenzmodul TIMESTAMP (sonst TnsModuleNotLicensedException); ROLE_COERO (WebSecurity); ROLE_COERO/ROLE_TIMESTAMP umgehen TIMESTAMP_MODULE_ACCESS / TIMESTAMP_STATISTICS_EMPLOYEES_OF_OWN_DEPARTMENTS.Hinweise: employeeId bleibt nur bei ROLE_COERO/ROLE_TIMESTAMP oder Recht EDIT_TIMESTAMPS_WITH_ACCESS erhalten, sonst wird der Request-User gesetzt; employeeId==0 = EMLOYEE_ID_MUST_BE_SET. date 0 = jetzt (Unix-Sekunden). Key creationDate wird immer entfernt. Reihenfolge-Prüfung gegen alle Stempel des Tages (TnsTimestampWrongOrderException); Tagesabschluss vorhanden = 403 CANT_MODIFY_TIMESTAMP_DAYCLOSING_EXISTS. creationMode=COERO_API. Nach dem Speichern Auto-Pausen-Logik. meta CREATED.
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
    
    def with_url(self,raw_url: str) -> TimestampRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: TimestampRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return TimestampRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def info(self) -> InfoRequestBuilder:
        """
        The info property
        """
        from .info.info_request_builder import InfoRequestBuilder

        return InfoRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class TimestampRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

