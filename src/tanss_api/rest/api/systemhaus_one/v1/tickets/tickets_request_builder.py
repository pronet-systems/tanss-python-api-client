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
    from .....models.ticket_save import TicketSave
    from .item.with_ticket_item_request_builder import WithTicketItemRequestBuilder
    from .status.status_request_builder import StatusRequestBuilder
    from .tickets_post_response import TicketsPostResponse
    from .types.types_request_builder import TypesRequestBuilder

class TicketsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/systemhaus_one/v1/tickets
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new TicketsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/systemhaus_one/v1/tickets", path_parameters)
    
    def by_ticket_id(self,ticket_id: int) -> WithTicketItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.systemhaus_one.v1.tickets.item collection
        param ticket_id: ID des Tickets.
        Returns: WithTicketItemRequestBuilder
        """
        if ticket_id is None:
            raise TypeError("ticket_id cannot be null.")
        from .item.with_ticket_item_request_builder import WithTicketItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["ticketId"] = ticket_id
        return WithTicketItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def post(self,body: TicketSave, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[TicketsPostResponse]:
        """
        Legt ein neues Ticket im Namen der ERP-/Systemhaus-One-Schnittstelle an.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: module, Rollen SYSTEMHAUS_ONE.Rechte: Lizenz TICKET (Modul 8), Lizenz PROJECT (Modul 9, nur bei project/projectId), TICKET_CHANGE_DEADLINE (nur wenn deadlineDate < dueDate).Hinweise: Lizenz SAP_ONE erforderlich. Body = TnsTicket-Felder per Jackson-Merge (u.a. companyId, remitterId, remitterEmail, title, content, extTicketId, assignedToEmployeeId, assignedToDepartmentId, statusId, typeId, priority, dueDate, deadlineDate, linkTypeId, linkId, project, projectId, orderNumber, internalContent, estimatedMinutes, tags, massTicketDescription). createdEmployeeId = -3 (SYSTEMHAUS_ONE) bei URI mit 'systemhaus_one', sonst -4 (WEB_API); eingeloggter Benutzer überschreibt dies. Ohne dueDate wird die Fälligkeit berechnet; Defaults typeId/priority aus Admin-Einstellungen, statusId=1; Titel auf 100 Zeichen gekürzt. massTicketDescription -> Massenticket, Ergebnis in meta.extra.massTicketCreationResult. 'id' nicht setzen. Antwort: ungefilterte TnsTicket-Entity.
        param body: ticket model to be saved
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[TicketsPostResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .tickets_post_response import TicketsPostResponse

        return await self.request_adapter.send_async(request_info, TicketsPostResponse, None)
    
    def to_post_request_information(self,body: TicketSave, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Legt ein neues Ticket im Namen der ERP-/Systemhaus-One-Schnittstelle an.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: module, Rollen SYSTEMHAUS_ONE.Rechte: Lizenz TICKET (Modul 8), Lizenz PROJECT (Modul 9, nur bei project/projectId), TICKET_CHANGE_DEADLINE (nur wenn deadlineDate < dueDate).Hinweise: Lizenz SAP_ONE erforderlich. Body = TnsTicket-Felder per Jackson-Merge (u.a. companyId, remitterId, remitterEmail, title, content, extTicketId, assignedToEmployeeId, assignedToDepartmentId, statusId, typeId, priority, dueDate, deadlineDate, linkTypeId, linkId, project, projectId, orderNumber, internalContent, estimatedMinutes, tags, massTicketDescription). createdEmployeeId = -3 (SYSTEMHAUS_ONE) bei URI mit 'systemhaus_one', sonst -4 (WEB_API); eingeloggter Benutzer überschreibt dies. Ohne dueDate wird die Fälligkeit berechnet; Defaults typeId/priority aus Admin-Einstellungen, statusId=1; Titel auf 100 Zeichen gekürzt. massTicketDescription -> Massenticket, Ergebnis in meta.extra.massTicketCreationResult. 'id' nicht setzen. Antwort: ungefilterte TnsTicket-Entity.
        param body: ticket model to be saved
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
    
    def with_url(self,raw_url: str) -> TicketsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: TicketsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return TicketsRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def status(self) -> StatusRequestBuilder:
        """
        The status property
        """
        from .status.status_request_builder import StatusRequestBuilder

        return StatusRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def types(self) -> TypesRequestBuilder:
        """
        The types property
        """
        from .types.types_request_builder import TypesRequestBuilder

        return TypesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class TicketsRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

