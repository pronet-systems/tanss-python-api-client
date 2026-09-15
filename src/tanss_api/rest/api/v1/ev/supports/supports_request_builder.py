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
    from .....models.tns_ev_appointment import TnsEvAppointment
    from .item.supports_item_request_builder import SupportsItemRequestBuilder
    from .supports_delete_response import SupportsDeleteResponse
    from .supports_post_response import SupportsPostResponse
    from .supports_put_response import SupportsPutResponse

class SupportsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/ev/supports
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new SupportsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/ev/supports", path_parameters)
    
    def by_id(self,id: int) -> SupportsItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.v1.ev.supports.item collection
        param id: Support-ID
        Returns: SupportsItemRequestBuilder
        """
        if id is None:
            raise TypeError("id cannot be null.")
        from .item.supports_item_request_builder import SupportsItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["id"] = id
        return SupportsItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[SupportsRequestBuilderDeleteQueryParameters]] = None) -> Optional[SupportsDeleteResponse]:
        """
        Löscht die EV-Termine zu den angegebenen Supports in Coero und entfernt die Verknüpfungen.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId.Rechte: Firmenzugriff auf Support-Firma je supportId; interner Support nur mit securityManager.void().Hinweise: Für jede ID Support-Check, dann lokale Link-Löschung und Coero DELETE /api/v1/tns/supports. Antwort-Status FOUND. Fehler -> TnsCoeroBadRequestException (400).
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[SupportsDeleteResponse]
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .supports_delete_response import SupportsDeleteResponse

        return await self.request_adapter.send_async(request_info, SupportsDeleteResponse, None)
    
    async def post(self,body: list[TnsEvAppointment], request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[SupportsPostResponse]:
        """
        Legt EV-Termine (Raumbuchungen) für Supports in Coero an und verknüpft sie mit den Supports.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId.Rechte: Firmenzugriff auf Support-Firma je tnsSupport; interner Support nur mit securityManager.void().Hinweise: Status ist FOUND (200), nicht CREATED. appointment wird auf 0 gesetzt, creatorTnsUserId = aktueller User. Coero POST /api/v1/tns/supports/; danach je Termin Link zum Support (Support muss existieren, sonst TnsBadRequestException). Fehler -> TnsCoeroBadRequestException (400).
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[SupportsPostResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .supports_post_response import SupportsPostResponse

        return await self.request_adapter.send_async(request_info, SupportsPostResponse, None)
    
    async def put(self,body: list[TnsEvAppointment], request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[SupportsPutResponse]:
        """
        Aktualisiert bestehende EV-Termine (Raumbuchungen) der Supports in Coero.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId.Rechte: Firmenzugriff auf Support-Firma je tnsSupport; interner Support nur mit securityManager.void().Hinweise: appointment = Coero-Termin-ID. Proxy auf Coero PUT /api/v1/tns/supports/. Keine lokale Link-Aktualisierung. Fehler -> TnsCoeroBadRequestException (400).
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[SupportsPutResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .supports_put_response import SupportsPutResponse

        return await self.request_adapter.send_async(request_info, SupportsPutResponse, None)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[SupportsRequestBuilderDeleteQueryParameters]] = None) -> RequestInformation:
        """
        Löscht die EV-Termine zu den angegebenen Supports in Coero und entfernt die Verknüpfungen.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId.Rechte: Firmenzugriff auf Support-Firma je supportId; interner Support nur mit securityManager.void().Hinweise: Für jede ID Support-Check, dann lokale Link-Löschung und Coero DELETE /api/v1/tns/supports. Antwort-Status FOUND. Fehler -> TnsCoeroBadRequestException (400).
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, '{+baseurl}/api/v1/ev/supports{?supportIds*}', self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: list[TnsEvAppointment], request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Legt EV-Termine (Raumbuchungen) für Supports in Coero an und verknüpft sie mit den Supports.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId.Rechte: Firmenzugriff auf Support-Firma je tnsSupport; interner Support nur mit securityManager.void().Hinweise: Status ist FOUND (200), nicht CREATED. appointment wird auf 0 gesetzt, creatorTnsUserId = aktueller User. Coero POST /api/v1/tns/supports/; danach je Termin Link zum Support (Support muss existieren, sonst TnsBadRequestException). Fehler -> TnsCoeroBadRequestException (400).
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
    
    def to_put_request_information(self,body: list[TnsEvAppointment], request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Aktualisiert bestehende EV-Termine (Raumbuchungen) der Supports in Coero.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId.Rechte: Firmenzugriff auf Support-Firma je tnsSupport; interner Support nur mit securityManager.void().Hinweise: appointment = Coero-Termin-ID. Proxy auf Coero PUT /api/v1/tns/supports/. Keine lokale Link-Aktualisierung. Fehler -> TnsCoeroBadRequestException (400).
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
    
    def with_url(self,raw_url: str) -> SupportsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: SupportsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return SupportsRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class SupportsRequestBuilderDeleteQueryParameters():
        """
        Löscht die EV-Termine zu den angegebenen Supports in Coero und entfernt die Verknüpfungen.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId.Rechte: Firmenzugriff auf Support-Firma je supportId; interner Support nur mit securityManager.void().Hinweise: Für jede ID Support-Check, dann lokale Link-Löschung und Coero DELETE /api/v1/tns/supports. Antwort-Status FOUND. Fehler -> TnsCoeroBadRequestException (400).
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "support_ids":
                return "supportIds"
            return original_name
        
        # Support-IDs (mehrfach oder kommagetrennt)
        support_ids: Optional[list[int]] = None

    
    @dataclass
    class SupportsRequestBuilderDeleteRequestConfiguration(RequestConfiguration[SupportsRequestBuilderDeleteQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class SupportsRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class SupportsRequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

