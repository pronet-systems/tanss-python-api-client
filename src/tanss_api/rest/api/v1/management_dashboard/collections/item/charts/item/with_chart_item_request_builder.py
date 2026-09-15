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
    from .with_chart_delete_response import WithChartDeleteResponse
    from .with_chart_put_request_body import WithChartPutRequestBody
    from .with_chart_put_response import WithChartPutResponse

class WithChartItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/managementDashboard/collections/{collectionId}/charts/{chartId}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new WithChartItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/managementDashboard/collections/{collectionId}/charts/{chartId}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[WithChartDeleteResponse]:
        """
        Löscht ein Chart samt Filter.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId.Rechte: interner Benutzer; Recht MANAGEMENT_DASHBOARD; Modul-Feature managementDashboard/DASHBOARD; Eigentümer-Check der Collection.Hinweise: 404 bei unbekannter Collection oder Chart. Es wird NICHT geprüft, ob das Chart zur angegebenen Collection gehört. Antwort-Status DELETED.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[WithChartDeleteResponse]
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .with_chart_delete_response import WithChartDeleteResponse

        return await self.request_adapter.send_async(request_info, WithChartDeleteResponse, None)
    
    async def put(self,body: WithChartPutRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[WithChartPutResponse]:
        """
        Aktualisiert (bzw. legt per Upsert an) ein Chart in einer eigenen Collection inkl. Filter.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId.Rechte: interner Benutzer; Recht MANAGEMENT_DASHBOARD; Modul-Feature managementDashboard/DASHBOARD; Eigentümer-Check der Collection.Hinweise: id (→chartId) und collectionId (→Pfad) werden überschrieben. Kein Existenz-Check des Charts: Objekt wird komplett aus dem Body gebaut und gespeichert (nicht gesendete Felder werden null/0). Filter wird ersetzt. Antwort-Status UPDATED.
        param body: Gelesene Keys des Charts (vollständiges Objekt)
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[WithChartPutResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .with_chart_put_response import WithChartPutResponse

        return await self.request_adapter.send_async(request_info, WithChartPutResponse, None)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Löscht ein Chart samt Filter.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId.Rechte: interner Benutzer; Recht MANAGEMENT_DASHBOARD; Modul-Feature managementDashboard/DASHBOARD; Eigentümer-Check der Collection.Hinweise: 404 bei unbekannter Collection oder Chart. Es wird NICHT geprüft, ob das Chart zur angegebenen Collection gehört. Antwort-Status DELETED.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_put_request_information(self,body: WithChartPutRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Aktualisiert (bzw. legt per Upsert an) ein Chart in einer eigenen Collection inkl. Filter.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId.Rechte: interner Benutzer; Recht MANAGEMENT_DASHBOARD; Modul-Feature managementDashboard/DASHBOARD; Eigentümer-Check der Collection.Hinweise: id (→chartId) und collectionId (→Pfad) werden überschrieben. Kein Existenz-Check des Charts: Objekt wird komplett aus dem Body gebaut und gespeichert (nicht gesendete Felder werden null/0). Filter wird ersetzt. Antwort-Status UPDATED.
        param body: Gelesene Keys des Charts (vollständiges Objekt)
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
    
    def with_url(self,raw_url: str) -> WithChartItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: WithChartItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return WithChartItemRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class WithChartItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class WithChartItemRequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

