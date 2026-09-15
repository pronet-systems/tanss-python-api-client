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
    from .charts.charts_request_builder import ChartsRequestBuilder
    from .with_collection_delete_response import WithCollectionDeleteResponse
    from .with_collection_put_request_body import WithCollectionPutRequestBody
    from .with_collection_put_response import WithCollectionPutResponse

class WithCollectionItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/managementDashboard/collections/{collectionId}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new WithCollectionItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/managementDashboard/collections/{collectionId}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[WithCollectionDeleteResponse]:
        """
        Löscht eine Dashboard-Collection inkl. aller Charts, Chart-Filter und Sichtbarkeiten.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId.Rechte: interner Benutzer; Recht MANAGEMENT_DASHBOARD; Modul-Feature managementDashboard/DASHBOARD; Eigentümer-Check (collection.userId == aktueller Benutzer, sonst FORBIDDEN).Hinweise: 404 bei unbekannter ID. Antwort-Status DELETED.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[WithCollectionDeleteResponse]
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .with_collection_delete_response import WithCollectionDeleteResponse

        return await self.request_adapter.send_async(request_info, WithCollectionDeleteResponse, None)
    
    async def put(self,body: WithCollectionPutRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[WithCollectionPutResponse]:
        """
        Aktualisiert eine eigene Dashboard-Collection (Name, Sichtbarkeitstyp, Sichtbarkeiten).Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId.Rechte: interner Benutzer; Recht MANAGEMENT_DASHBOARD; Modul-Feature managementDashboard/DASHBOARD; Eigentümer-Check (collection.userId == aktueller Benutzer).Hinweise: id/userId werden aus der bestehenden Collection übernommen. 404 bei unbekannter ID. Bestehende Sichtbarkeiten werden gelöscht und (nur bei EVERYBODY) neu angelegt. Charts bleiben unberührt. Antwort-Status UPDATED.
        param body: Gelesene Keys der Collection
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[WithCollectionPutResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .with_collection_put_response import WithCollectionPutResponse

        return await self.request_adapter.send_async(request_info, WithCollectionPutResponse, None)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Löscht eine Dashboard-Collection inkl. aller Charts, Chart-Filter und Sichtbarkeiten.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId.Rechte: interner Benutzer; Recht MANAGEMENT_DASHBOARD; Modul-Feature managementDashboard/DASHBOARD; Eigentümer-Check (collection.userId == aktueller Benutzer, sonst FORBIDDEN).Hinweise: 404 bei unbekannter ID. Antwort-Status DELETED.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_put_request_information(self,body: WithCollectionPutRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Aktualisiert eine eigene Dashboard-Collection (Name, Sichtbarkeitstyp, Sichtbarkeiten).Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId.Rechte: interner Benutzer; Recht MANAGEMENT_DASHBOARD; Modul-Feature managementDashboard/DASHBOARD; Eigentümer-Check (collection.userId == aktueller Benutzer).Hinweise: id/userId werden aus der bestehenden Collection übernommen. 404 bei unbekannter ID. Bestehende Sichtbarkeiten werden gelöscht und (nur bei EVERYBODY) neu angelegt. Charts bleiben unberührt. Antwort-Status UPDATED.
        param body: Gelesene Keys der Collection
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
    
    def with_url(self,raw_url: str) -> WithCollectionItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: WithCollectionItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return WithCollectionItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def charts(self) -> ChartsRequestBuilder:
        """
        The charts property
        """
        from .charts.charts_request_builder import ChartsRequestBuilder

        return ChartsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class WithCollectionItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class WithCollectionItemRequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

