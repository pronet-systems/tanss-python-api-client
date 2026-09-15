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
    from .summaries_delete_response import SummariesDeleteResponse
    from .summaries_get_response import SummariesGetResponse

class SummariesRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/ai/tanssAI/tickets/{ticketId}/summaries
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new SummariesRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/ai/tanssAI/tickets/{ticketId}/summaries", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[SummariesDeleteResponse]:
        """
        Löscht alle gespeicherten KI-Zusammenfassungen eines Tickets. Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft. Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId. Rechte: licModule tanssAI/ACTIVE_SUBSCRIPTION (45), TANSS-AI-Konfiguration vorhanden/gültig, interner Benutzer. Hinweise: Keine Ticket-Zugriffsprüfung (deleteAllByTicketId direkt). Antwort meta DELETED.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[SummariesDeleteResponse]
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .summaries_delete_response import SummariesDeleteResponse

        return await self.request_adapter.send_async(request_info, SummariesDeleteResponse, None)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[SummariesGetResponse]:
        """
        Liefert alle gespeicherten KI-Zusammenfassungen eines Tickets. Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft. Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId. Rechte: licModule tanssAI/ACTIVE_SUBSCRIPTION (45), TANSS-AI-Konfiguration vorhanden/gültig, interner Benutzer, Firmenzugriff auf das Ticket. Hinweise: Ticket-Zugriffsprüfung nur wenn das Ticket existiert (unbekannte ticketId liefert leere Liste, kein 404). Status FOUND.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[SummariesGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .summaries_get_response import SummariesGetResponse

        return await self.request_adapter.send_async(request_info, SummariesGetResponse, None)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Löscht alle gespeicherten KI-Zusammenfassungen eines Tickets. Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft. Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId. Rechte: licModule tanssAI/ACTIVE_SUBSCRIPTION (45), TANSS-AI-Konfiguration vorhanden/gültig, interner Benutzer. Hinweise: Keine Ticket-Zugriffsprüfung (deleteAllByTicketId direkt). Antwort meta DELETED.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Liefert alle gespeicherten KI-Zusammenfassungen eines Tickets. Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft. Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId. Rechte: licModule tanssAI/ACTIVE_SUBSCRIPTION (45), TANSS-AI-Konfiguration vorhanden/gültig, interner Benutzer, Firmenzugriff auf das Ticket. Hinweise: Ticket-Zugriffsprüfung nur wenn das Ticket existiert (unbekannte ticketId liefert leere Liste, kein 404). Status FOUND.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> SummariesRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: SummariesRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return SummariesRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class SummariesRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class SummariesRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

