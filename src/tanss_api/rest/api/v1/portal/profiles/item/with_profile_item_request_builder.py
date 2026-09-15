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
    from .with_profile_delete_response import WithProfileDeleteResponse
    from .with_profile_put_request_body import WithProfilePutRequestBody
    from .with_profile_put_response import WithProfilePutResponse

class WithProfileItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/portal/profiles/{profileId}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new WithProfileItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/portal/profiles/{profileId}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[WithProfileDeleteResponse]:
        """
        Löscht ein Portal-Profil des angemeldeten Mitarbeiters inkl. aller Items. Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft. Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId. Rechte: Besitzerprüfung, profile.employeeId muss dem aktuellen User entsprechen. Hinweise: ENTITY_NOT_FOUND wenn unbekannt, FORBIDDEN_MISSING_PERMISSIONS bei fremdem Profil. Items werden nach dem Löschen des Profils entfernt. Antwort meta DELETED.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[WithProfileDeleteResponse]
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .with_profile_delete_response import WithProfileDeleteResponse

        return await self.request_adapter.send_async(request_info, WithProfileDeleteResponse, None)
    
    async def put(self,body: WithProfilePutRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[WithProfilePutResponse]:
        """
        Aktualisiert ein Portal-Profil (Name, Spalten, Typ, Timeline, Position) und synchronisiert die Items (neu/geändert/gelöscht). Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft. Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId. Rechte: Besitzerprüfung, profile.employeeId muss dem aktuellen User entsprechen. Hinweise: Keys id und employeeId werden entfernt. ENTITY_NOT_FOUND wenn unbekannt. Item-Sync: Items ohne bekannte id werden angelegt, nicht mehr enthaltene gelöscht, geänderte aktualisiert; danach werden Positionen pro Spalte neu vergeben. name leer führt zu TnsMissingFieldKeyException('name'). Antwort meta UPDATED.
        param body: Zu ändernde Felder des Profils (Merge) inkl. vollständiger Item-Liste
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[WithProfilePutResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .with_profile_put_response import WithProfilePutResponse

        return await self.request_adapter.send_async(request_info, WithProfilePutResponse, None)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Löscht ein Portal-Profil des angemeldeten Mitarbeiters inkl. aller Items. Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft. Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId. Rechte: Besitzerprüfung, profile.employeeId muss dem aktuellen User entsprechen. Hinweise: ENTITY_NOT_FOUND wenn unbekannt, FORBIDDEN_MISSING_PERMISSIONS bei fremdem Profil. Items werden nach dem Löschen des Profils entfernt. Antwort meta DELETED.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_put_request_information(self,body: WithProfilePutRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Aktualisiert ein Portal-Profil (Name, Spalten, Typ, Timeline, Position) und synchronisiert die Items (neu/geändert/gelöscht). Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft. Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId. Rechte: Besitzerprüfung, profile.employeeId muss dem aktuellen User entsprechen. Hinweise: Keys id und employeeId werden entfernt. ENTITY_NOT_FOUND wenn unbekannt. Item-Sync: Items ohne bekannte id werden angelegt, nicht mehr enthaltene gelöscht, geänderte aktualisiert; danach werden Positionen pro Spalte neu vergeben. name leer führt zu TnsMissingFieldKeyException('name'). Antwort meta UPDATED.
        param body: Zu ändernde Felder des Profils (Merge) inkl. vollständiger Item-Liste
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
    
    def with_url(self,raw_url: str) -> WithProfileItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: WithProfileItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return WithProfileItemRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class WithProfileItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class WithProfileItemRequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

