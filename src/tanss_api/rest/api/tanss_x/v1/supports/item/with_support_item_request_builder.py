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
    from ......models.tns_support import TnsSupport
    from .with_support_delete_response import WithSupportDeleteResponse
    from .with_support_get_response import WithSupportGetResponse
    from .with_support_put_response import WithSupportPutResponse

class WithSupportItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/tanss.x/v1/supports/{supportId}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new WithSupportItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/tanss.x/v1/supports/{supportId}{?discardOnSupport*,isOrganizer*}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[WithSupportItemRequestBuilderDeleteQueryParameters]] = None) -> Optional[WithSupportDeleteResponse]:
        """
        Löscht einen Support/Termin; mit discardOnSupport=true wird das Löschen eines echten Supports verweigert.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: module, Rollen TANSS_APP.Rechte: Firmenzugriff auf companyId; interner Login für interne Supports.Hinweis: Auch unter /api/tanss.app/v1. Query discardOnSupport (Default false): ist true und der Datensatz hat planningType=SUPPORT -> 403 CHANGES_WERE_DISCARDED (gedacht zum Verwerfen von Terminen, nicht von Leistungen). Löschen erzeugt Log-/Ticket-Historie, Event SUPPORT_DELETED, entfernt Dateien und Wiederholungsregeln. Status DELETED.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[WithSupportDeleteResponse]
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .with_support_delete_response import WithSupportDeleteResponse

        return await self.request_adapter.send_async(request_info, WithSupportDeleteResponse, None)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[WithSupportGetResponse]:
        """
        Liefert einen Support/Termin inkl. verknüpfter Entitäten (mit Firmenadresse).Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: module, Rollen TANSS_APP.Rechte: Firmenzugriff auf companyId; interner Login für interne Supports.Hinweis: Auch unter /api/tanss.app/v1. Entspricht GET /api/v1/supports/{supportId} ohne sequenceId, zusätzlich LinkedEntities-Option ADD_COMPANY_ADDRESS. 404 OBJECT_NOT_FOUND.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[WithSupportGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .with_support_get_response import WithSupportGetResponse

        return await self.request_adapter.send_async(request_info, WithSupportGetResponse, None)
    
    async def put(self,body: TnsSupport, request_configuration: Optional[RequestConfiguration[WithSupportItemRequestBuilderPutQueryParameters]] = None) -> Optional[WithSupportPutResponse]:
        """
        Aktualisiert einen Support/Termin per JSON-Merge; setzt automatisch automaticallyResolveConflicts und je nach Query preventNotification/discardOnSupport.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: module, Rollen TANSS_APP.Rechte: Firmenzugriff auf companyId; interner Login für interne Supports; Firma darf nicht inaktiv sein (COMPANY_IS_INACTIVE).Hinweis: Auch unter /api/tanss.app/v1. Query isOrganizer (Default false) -> preventNotification=true; discardOnSupport (Default false) -> discardOnSupport=true. Danach generischer Update wie PUT /api/v1/supports/{supportId}. 404 ENTITY_NOT_FOUND. Status UPDATED.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[WithSupportPutResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .with_support_put_response import WithSupportPutResponse

        return await self.request_adapter.send_async(request_info, WithSupportPutResponse, None)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[WithSupportItemRequestBuilderDeleteQueryParameters]] = None) -> RequestInformation:
        """
        Löscht einen Support/Termin; mit discardOnSupport=true wird das Löschen eines echten Supports verweigert.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: module, Rollen TANSS_APP.Rechte: Firmenzugriff auf companyId; interner Login für interne Supports.Hinweis: Auch unter /api/tanss.app/v1. Query discardOnSupport (Default false): ist true und der Datensatz hat planningType=SUPPORT -> 403 CHANGES_WERE_DISCARDED (gedacht zum Verwerfen von Terminen, nicht von Leistungen). Löschen erzeugt Log-/Ticket-Historie, Event SUPPORT_DELETED, entfernt Dateien und Wiederholungsregeln. Status DELETED.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Liefert einen Support/Termin inkl. verknüpfter Entitäten (mit Firmenadresse).Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: module, Rollen TANSS_APP.Rechte: Firmenzugriff auf companyId; interner Login für interne Supports.Hinweis: Auch unter /api/tanss.app/v1. Entspricht GET /api/v1/supports/{supportId} ohne sequenceId, zusätzlich LinkedEntities-Option ADD_COMPANY_ADDRESS. 404 OBJECT_NOT_FOUND.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_put_request_information(self,body: TnsSupport, request_configuration: Optional[RequestConfiguration[WithSupportItemRequestBuilderPutQueryParameters]] = None) -> RequestInformation:
        """
        Aktualisiert einen Support/Termin per JSON-Merge; setzt automatisch automaticallyResolveConflicts und je nach Query preventNotification/discardOnSupport.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: module, Rollen TANSS_APP.Rechte: Firmenzugriff auf companyId; interner Login für interne Supports; Firma darf nicht inaktiv sein (COMPANY_IS_INACTIVE).Hinweis: Auch unter /api/tanss.app/v1. Query isOrganizer (Default false) -> preventNotification=true; discardOnSupport (Default false) -> discardOnSupport=true. Danach generischer Update wie PUT /api/v1/supports/{supportId}. 404 ENTITY_NOT_FOUND. Status UPDATED.
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
    
    def with_url(self,raw_url: str) -> WithSupportItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: WithSupportItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return WithSupportItemRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class WithSupportItemRequestBuilderDeleteQueryParameters():
        """
        Löscht einen Support/Termin; mit discardOnSupport=true wird das Löschen eines echten Supports verweigert.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: module, Rollen TANSS_APP.Rechte: Firmenzugriff auf companyId; interner Login für interne Supports.Hinweis: Auch unter /api/tanss.app/v1. Query discardOnSupport (Default false): ist true und der Datensatz hat planningType=SUPPORT -> 403 CHANGES_WERE_DISCARDED (gedacht zum Verwerfen von Terminen, nicht von Leistungen). Löschen erzeugt Log-/Ticket-Historie, Event SUPPORT_DELETED, entfernt Dateien und Wiederholungsregeln. Status DELETED.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "discard_on_support":
                return "discardOnSupport"
            return original_name
        
        # true -> Löschen echter Supports (planningType=SUPPORT) wird verweigert
        discard_on_support: Optional[bool] = None

    
    @dataclass
    class WithSupportItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[WithSupportItemRequestBuilderDeleteQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class WithSupportItemRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class WithSupportItemRequestBuilderPutQueryParameters():
        """
        Aktualisiert einen Support/Termin per JSON-Merge; setzt automatisch automaticallyResolveConflicts und je nach Query preventNotification/discardOnSupport.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: module, Rollen TANSS_APP.Rechte: Firmenzugriff auf companyId; interner Login für interne Supports; Firma darf nicht inaktiv sein (COMPANY_IS_INACTIVE).Hinweis: Auch unter /api/tanss.app/v1. Query isOrganizer (Default false) -> preventNotification=true; discardOnSupport (Default false) -> discardOnSupport=true. Danach generischer Update wie PUT /api/v1/supports/{supportId}. 404 ENTITY_NOT_FOUND. Status UPDATED.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "discard_on_support":
                return "discardOnSupport"
            if original_name == "is_organizer":
                return "isOrganizer"
            return original_name
        
        # true -> Änderungen an echten Supports werden verworfen
        discard_on_support: Optional[bool] = None

        # true -> preventNotification
        is_organizer: Optional[bool] = None

    
    @dataclass
    class WithSupportItemRequestBuilderPutRequestConfiguration(RequestConfiguration[WithSupportItemRequestBuilderPutQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

