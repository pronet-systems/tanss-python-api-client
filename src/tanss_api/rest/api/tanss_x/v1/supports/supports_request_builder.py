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
    from .....models.tns_support_configuration import TnsSupportConfiguration
    from .item.with_support_item_request_builder import WithSupportItemRequestBuilder
    from .properties.properties_request_builder import PropertiesRequestBuilder
    from .supports_post_request_body import SupportsPostRequestBody
    from .supports_post_response import SupportsPostResponse
    from .supports_put_response import SupportsPutResponse

class SupportsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/tanss.x/v1/supports
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new SupportsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/tanss.x/v1/supports{?isOrganizer*}", path_parameters)
    
    def by_support_id(self,support_id: int) -> WithSupportItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.tanssX.v1.supports.item collection
        param support_id: Id des Supports
        Returns: WithSupportItemRequestBuilder
        """
        if support_id is None:
            raise TypeError("support_id cannot be null.")
        from .item.with_support_item_request_builder import WithSupportItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["supportId"] = support_id
        return WithSupportItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def post(self,body: SupportsPostRequestBody, request_configuration: Optional[RequestConfiguration[SupportsRequestBuilderPostQueryParameters]] = None) -> Optional[SupportsPostResponse]:
        """
        Erstellt einen Support/Termin mit TANSS.X-spezifischen Persist-Optionen (Duplikatprüfung, Ticket-Ermittlung, automatische Konfliktauflösung).Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: module, Rollen TANSS_APP.Rechte: Firmenzugriff auf companyId (FORBIDDEN_NO_COMPANY_ACCESS); interner Login für interne Supports (internal=true).Hinweis: Auch unter /api/tanss.app/v1. Query isOrganizer (Default false) -> preventNotification. Persist-Optionen fest: useOwnCompanyIfNoneGiven=true, tanssXduplicateChecks=true, determineTicketId=true, automaticallyResolveConflicts=true. 403 COMPANY_IS_INACTIVE bei inaktiver Firma. text auf 65535 Zeichen gekürzt; date=now wenn 0; dateCreated/createdEmployeeId/modified werden gesetzt. Bei Serienumwandlung (recurrenceMasterLinkId + recurrenceRuleSequenceId | recurrenceRuleSequenceTimestamp + date): 400 wenn date fehlt oder Master/Regel nicht passen. Status CREATED.
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
    
    async def put(self,body: TnsSupportConfiguration, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[SupportsPutResponse]:
        """
        Liefert eine Support-/Terminliste anhand einer TnsSupportConfiguration (wie PUT /api/v1/supports/list, aber ohne erzwungene Rechteprüfung).Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: module, Rollen TANSS_APP.Rechte: bei usePermissionChecks=true SUPPORT_LIST_ALL_SUPPORTS (sonst nur eigene); interner Login (sonst nur SUPPORT/APPOINTMENT_FIX/APPOINTMENT_PROPOSAL); interne Supports nur mit internem Login; Firmenzugriff/gesperrte Firmen; CUSTOMER_SEES_SYMBOL_FOR_SERVICE_TYPE (nur meta columnStatusHide).Hinweis: Auch unter /api/tanss.app/v1. Im Gegensatz zu /api/v1/supports/list wird alwaysUsePermissionChecks() NICHT aufgerufen – Rechtefilter greifen nur wenn usePermissionChecks=true im Body. Ohne mindestens einen Filter und itemsPerPage=0 -> leere Liste. meta.properties.extras: truncateTextLength, columnStatusHide, columnDurationHide.
        param body: object containing support list query parameters.When querying support with these parameters, you can only use the filter settings you need (You don't have to specify all)
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
    
    def to_post_request_information(self,body: SupportsPostRequestBody, request_configuration: Optional[RequestConfiguration[SupportsRequestBuilderPostQueryParameters]] = None) -> RequestInformation:
        """
        Erstellt einen Support/Termin mit TANSS.X-spezifischen Persist-Optionen (Duplikatprüfung, Ticket-Ermittlung, automatische Konfliktauflösung).Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: module, Rollen TANSS_APP.Rechte: Firmenzugriff auf companyId (FORBIDDEN_NO_COMPANY_ACCESS); interner Login für interne Supports (internal=true).Hinweis: Auch unter /api/tanss.app/v1. Query isOrganizer (Default false) -> preventNotification. Persist-Optionen fest: useOwnCompanyIfNoneGiven=true, tanssXduplicateChecks=true, determineTicketId=true, automaticallyResolveConflicts=true. 403 COMPANY_IS_INACTIVE bei inaktiver Firma. text auf 65535 Zeichen gekürzt; date=now wenn 0; dateCreated/createdEmployeeId/modified werden gesetzt. Bei Serienumwandlung (recurrenceMasterLinkId + recurrenceRuleSequenceId | recurrenceRuleSequenceTimestamp + date): 400 wenn date fehlt oder Master/Regel nicht passen. Status CREATED.
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
    
    def to_put_request_information(self,body: TnsSupportConfiguration, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Liefert eine Support-/Terminliste anhand einer TnsSupportConfiguration (wie PUT /api/v1/supports/list, aber ohne erzwungene Rechteprüfung).Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: module, Rollen TANSS_APP.Rechte: bei usePermissionChecks=true SUPPORT_LIST_ALL_SUPPORTS (sonst nur eigene); interner Login (sonst nur SUPPORT/APPOINTMENT_FIX/APPOINTMENT_PROPOSAL); interne Supports nur mit internem Login; Firmenzugriff/gesperrte Firmen; CUSTOMER_SEES_SYMBOL_FOR_SERVICE_TYPE (nur meta columnStatusHide).Hinweis: Auch unter /api/tanss.app/v1. Im Gegensatz zu /api/v1/supports/list wird alwaysUsePermissionChecks() NICHT aufgerufen – Rechtefilter greifen nur wenn usePermissionChecks=true im Body. Ohne mindestens einen Filter und itemsPerPage=0 -> leere Liste. meta.properties.extras: truncateTextLength, columnStatusHide, columnDurationHide.
        param body: object containing support list query parameters.When querying support with these parameters, you can only use the filter settings you need (You don't have to specify all)
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
    
    @property
    def properties(self) -> PropertiesRequestBuilder:
        """
        The properties property
        """
        from .properties.properties_request_builder import PropertiesRequestBuilder

        return PropertiesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class SupportsRequestBuilderPostQueryParameters():
        """
        Erstellt einen Support/Termin mit TANSS.X-spezifischen Persist-Optionen (Duplikatprüfung, Ticket-Ermittlung, automatische Konfliktauflösung).Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: module, Rollen TANSS_APP.Rechte: Firmenzugriff auf companyId (FORBIDDEN_NO_COMPANY_ACCESS); interner Login für interne Supports (internal=true).Hinweis: Auch unter /api/tanss.app/v1. Query isOrganizer (Default false) -> preventNotification. Persist-Optionen fest: useOwnCompanyIfNoneGiven=true, tanssXduplicateChecks=true, determineTicketId=true, automaticallyResolveConflicts=true. 403 COMPANY_IS_INACTIVE bei inaktiver Firma. text auf 65535 Zeichen gekürzt; date=now wenn 0; dateCreated/createdEmployeeId/modified werden gesetzt. Bei Serienumwandlung (recurrenceMasterLinkId + recurrenceRuleSequenceId | recurrenceRuleSequenceTimestamp + date): 400 wenn date fehlt oder Master/Regel nicht passen. Status CREATED.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "is_organizer":
                return "isOrganizer"
            return original_name
        
        # true -> preventNotification
        is_organizer: Optional[bool] = None

    
    @dataclass
    class SupportsRequestBuilderPostRequestConfiguration(RequestConfiguration[SupportsRequestBuilderPostQueryParameters]):
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
    

