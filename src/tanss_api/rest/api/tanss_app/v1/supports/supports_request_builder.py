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
    Builds and executes requests for operations under /api/tanss.app/v1/supports
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new SupportsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/tanss.app/v1/supports{?isOrganizer*}", path_parameters)
    
    def by_support_id(self,support_id: int) -> WithSupportItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.tanssApp.v1.supports.item collection
        param support_id: Id der Taetigkeit
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
        Legt eine Taetigkeit/Termin (TnsSupport) an mit TANSS-App-spezifischen Persist-Optionen: eigene Firma falls keine angegeben, TANSS-X-Duplikatpruefung, Ticket-Id ermitteln, Konflikte automatisch aufloesen; isOrganizer=true unterdrueckt Benachrichtigungen. Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft. Token: module, Rollen TANSS_APP. Rechte (fallabhaengig): bet.ADD_SUPPORT_FOR_OTHER_EMPLOYEES, bet.PLANNING_CREATE_APPOINTMENTS, bet.CREATE_STANDBYS, bet.BOOK_SUPPORTS, bet.CLEAR_SUPPORTS, bet.CHANGE_INVOICE_NUMBER_SUPPORT_IS_BOOKED. Hinweise: Bei recurrenceMasterLinkId wird der Master geklont (id=0, groupId=0); Fehler RECURRENCE_MASTER_CANT_BE_FOUND, RECURRENCE_MASTER_DOESNT_MATCH_RULE_ID, DATE_MUST_BE_GIVEN_WHILE_CONVERTING_A_RECURRING_APPOINTMENT. Key persistOptions wird serverseitig ueberschrieben. Status CREATED. Auch unter /api/tanss.x/v1.
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
        Taetigkeitenliste nach TnsSupportConfiguration - wie PUT /api/v1/supports/list, jedoch OHNE erzwungene Rechtepruefung (alwaysUsePermissionChecks wird nicht gesetzt). Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft. Token: module, Rollen TANSS_APP. Hinweise: Antwort im Filter STANDARD plus relationshipLinkTypeId, relationshipLinkId, percent, consultation, outlookTitle, outlookLocation; meta.properties.extra u.a. truncateTextLength. Nachbearbeitung ergaenzt Ticket-Icon-Infos und Meta-Properties. Auch unter /api/tanss.x/v1.
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
        Legt eine Taetigkeit/Termin (TnsSupport) an mit TANSS-App-spezifischen Persist-Optionen: eigene Firma falls keine angegeben, TANSS-X-Duplikatpruefung, Ticket-Id ermitteln, Konflikte automatisch aufloesen; isOrganizer=true unterdrueckt Benachrichtigungen. Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft. Token: module, Rollen TANSS_APP. Rechte (fallabhaengig): bet.ADD_SUPPORT_FOR_OTHER_EMPLOYEES, bet.PLANNING_CREATE_APPOINTMENTS, bet.CREATE_STANDBYS, bet.BOOK_SUPPORTS, bet.CLEAR_SUPPORTS, bet.CHANGE_INVOICE_NUMBER_SUPPORT_IS_BOOKED. Hinweise: Bei recurrenceMasterLinkId wird der Master geklont (id=0, groupId=0); Fehler RECURRENCE_MASTER_CANT_BE_FOUND, RECURRENCE_MASTER_DOESNT_MATCH_RULE_ID, DATE_MUST_BE_GIVEN_WHILE_CONVERTING_A_RECURRING_APPOINTMENT. Key persistOptions wird serverseitig ueberschrieben. Status CREATED. Auch unter /api/tanss.x/v1.
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
        Taetigkeitenliste nach TnsSupportConfiguration - wie PUT /api/v1/supports/list, jedoch OHNE erzwungene Rechtepruefung (alwaysUsePermissionChecks wird nicht gesetzt). Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft. Token: module, Rollen TANSS_APP. Hinweise: Antwort im Filter STANDARD plus relationshipLinkTypeId, relationshipLinkId, percent, consultation, outlookTitle, outlookLocation; meta.properties.extra u.a. truncateTextLength. Nachbearbeitung ergaenzt Ticket-Icon-Infos und Meta-Properties. Auch unter /api/tanss.x/v1.
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
        Legt eine Taetigkeit/Termin (TnsSupport) an mit TANSS-App-spezifischen Persist-Optionen: eigene Firma falls keine angegeben, TANSS-X-Duplikatpruefung, Ticket-Id ermitteln, Konflikte automatisch aufloesen; isOrganizer=true unterdrueckt Benachrichtigungen. Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft. Token: module, Rollen TANSS_APP. Rechte (fallabhaengig): bet.ADD_SUPPORT_FOR_OTHER_EMPLOYEES, bet.PLANNING_CREATE_APPOINTMENTS, bet.CREATE_STANDBYS, bet.BOOK_SUPPORTS, bet.CLEAR_SUPPORTS, bet.CHANGE_INVOICE_NUMBER_SUPPORT_IS_BOOKED. Hinweise: Bei recurrenceMasterLinkId wird der Master geklont (id=0, groupId=0); Fehler RECURRENCE_MASTER_CANT_BE_FOUND, RECURRENCE_MASTER_DOESNT_MATCH_RULE_ID, DATE_MUST_BE_GIVEN_WHILE_CONVERTING_A_RECURRING_APPOINTMENT. Key persistOptions wird serverseitig ueberschrieben. Status CREATED. Auch unter /api/tanss.x/v1.
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
        
        # true unterdrueckt Benachrichtigungen
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
    

