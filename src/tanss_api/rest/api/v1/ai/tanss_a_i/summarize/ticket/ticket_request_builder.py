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
    from .stream.stream_request_builder import StreamRequestBuilder
    from .ticket_post_response import TicketPostResponse

class TicketRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/ai/tanssAI/summarize/ticket
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new TicketRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/ai/tanssAI/summarize/ticket?promptId={promptId}&ticketId={ticketId}", path_parameters)
    
    async def post(self,request_configuration: Optional[RequestConfiguration[TicketRequestBuilderPostQueryParameters]] = None) -> Optional[TicketPostResponse]:
        """
        Erzeugt (oder liefert die gecachte) KI-Zusammenfassung eines Tickets mit dem angegebenen Prompt über TANSS AI (nicht-streamend). Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft. Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId. Rechte: licModule tanssAI/ACTIVE_SUBSCRIPTION (45), TANSS-AI-Konfiguration vorhanden/gültig, interner Benutzer, Firmenzugriff auf das Ticket. Hinweise: Existiert bereits eine aktuelle Summary für ticketId+promptId (keine neuen Mails/Kommentare/Supports), wird sie ohne KI-Aufruf zurückgegeben (model = createdByModel). Sonst inkrementelle Zusammenfassung (nur neue Einträge + alte Summary als Systemprompt), Ergebnis wird als TnsTanssAITicketSummary gespeichert. Fehler TANSS_AI_SUMMARY_IS_ALREADY_IN_PROGRESS bei parallelem Aufruf für dasselbe Ticket, TANSS_AI_TOO_MANY_PARALLEL_REQUESTS (mehr als 5 gleichzeitig), PROMPT_NOT_FOUND bei unbekanntem promptId. Modell fest TANSS_AI_MISTRAL_SMALL_3_2_24_B.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[TicketPostResponse]
        """
        request_info = self.to_post_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .ticket_post_response import TicketPostResponse

        return await self.request_adapter.send_async(request_info, TicketPostResponse, None)
    
    def to_post_request_information(self,request_configuration: Optional[RequestConfiguration[TicketRequestBuilderPostQueryParameters]] = None) -> RequestInformation:
        """
        Erzeugt (oder liefert die gecachte) KI-Zusammenfassung eines Tickets mit dem angegebenen Prompt über TANSS AI (nicht-streamend). Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft. Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId. Rechte: licModule tanssAI/ACTIVE_SUBSCRIPTION (45), TANSS-AI-Konfiguration vorhanden/gültig, interner Benutzer, Firmenzugriff auf das Ticket. Hinweise: Existiert bereits eine aktuelle Summary für ticketId+promptId (keine neuen Mails/Kommentare/Supports), wird sie ohne KI-Aufruf zurückgegeben (model = createdByModel). Sonst inkrementelle Zusammenfassung (nur neue Einträge + alte Summary als Systemprompt), Ergebnis wird als TnsTanssAITicketSummary gespeichert. Fehler TANSS_AI_SUMMARY_IS_ALREADY_IN_PROGRESS bei parallelem Aufruf für dasselbe Ticket, TANSS_AI_TOO_MANY_PARALLEL_REQUESTS (mehr als 5 gleichzeitig), PROMPT_NOT_FOUND bei unbekanntem promptId. Modell fest TANSS_AI_MISTRAL_SMALL_3_2_24_B.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.POST, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> TicketRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: TicketRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return TicketRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def stream(self) -> StreamRequestBuilder:
        """
        The stream property
        """
        from .stream.stream_request_builder import StreamRequestBuilder

        return StreamRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class TicketRequestBuilderPostQueryParameters():
        """
        Erzeugt (oder liefert die gecachte) KI-Zusammenfassung eines Tickets mit dem angegebenen Prompt über TANSS AI (nicht-streamend). Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft. Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId. Rechte: licModule tanssAI/ACTIVE_SUBSCRIPTION (45), TANSS-AI-Konfiguration vorhanden/gültig, interner Benutzer, Firmenzugriff auf das Ticket. Hinweise: Existiert bereits eine aktuelle Summary für ticketId+promptId (keine neuen Mails/Kommentare/Supports), wird sie ohne KI-Aufruf zurückgegeben (model = createdByModel). Sonst inkrementelle Zusammenfassung (nur neue Einträge + alte Summary als Systemprompt), Ergebnis wird als TnsTanssAITicketSummary gespeichert. Fehler TANSS_AI_SUMMARY_IS_ALREADY_IN_PROGRESS bei parallelem Aufruf für dasselbe Ticket, TANSS_AI_TOO_MANY_PARALLEL_REQUESTS (mehr als 5 gleichzeitig), PROMPT_NOT_FOUND bei unbekanntem promptId. Modell fest TANSS_AI_MISTRAL_SMALL_3_2_24_B.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "prompt_id":
                return "promptId"
            if original_name == "ticket_id":
                return "ticketId"
            return original_name
        
        prompt_id: Optional[int] = None

        ticket_id: Optional[int] = None

    
    @dataclass
    class TicketRequestBuilderPostRequestConfiguration(RequestConfiguration[TicketRequestBuilderPostQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

