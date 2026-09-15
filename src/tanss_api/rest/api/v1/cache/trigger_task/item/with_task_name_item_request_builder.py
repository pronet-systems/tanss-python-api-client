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
    from .with_task_name_get_response import WithTaskNameGetResponse

class WithTaskNameItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/cache/triggerTask/{taskName}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new WithTaskNameItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/cache/triggerTask/{taskName}{?id*}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[WithTaskNameItemRequestBuilderGetQueryParameters]] = None) -> Optional[WithTaskNameGetResponse]:
        """
        Interner Trigger-Endpunkt: stößt benannte Hintergrund-Tasks an (Dokumente verschieben, Ticket-Infos aktualisieren, Lizenzen dekodieren/neu laden, Push senden, Support-gelöscht-Event).Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: mixed, Rollen USER, PHP. TANSS_APP-Token nur mit loggedInUserId.Hinweise: taskName = moveDocuments (id string), ticketRelevantInfoUpdate (id int, asynchron), decodeLicenses, refreshLicenses, sendPush (id int), createSupportDeleteTanssEvent (id int = Support-ID). Unbekannter Name -> ENUM_TYPE_DONT_EXIST; nicht-numerische id bei int-Tasks -> NumberFormatException. Keine Rechteprüfung im Controller (vermutlich für interne PHP-Aufrufe). meta FOUND.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[WithTaskNameGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .with_task_name_get_response import WithTaskNameGetResponse

        return await self.request_adapter.send_async(request_info, WithTaskNameGetResponse, None)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[WithTaskNameItemRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Interner Trigger-Endpunkt: stößt benannte Hintergrund-Tasks an (Dokumente verschieben, Ticket-Infos aktualisieren, Lizenzen dekodieren/neu laden, Push senden, Support-gelöscht-Event).Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: mixed, Rollen USER, PHP. TANSS_APP-Token nur mit loggedInUserId.Hinweise: taskName = moveDocuments (id string), ticketRelevantInfoUpdate (id int, asynchron), decodeLicenses, refreshLicenses, sendPush (id int), createSupportDeleteTanssEvent (id int = Support-ID). Unbekannter Name -> ENUM_TYPE_DONT_EXIST; nicht-numerische id bei int-Tasks -> NumberFormatException. Keine Rechteprüfung im Controller (vermutlich für interne PHP-Aufrufe). meta FOUND.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> WithTaskNameItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: WithTaskNameItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return WithTaskNameItemRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class WithTaskNameItemRequestBuilderGetQueryParameters():
        """
        Interner Trigger-Endpunkt: stößt benannte Hintergrund-Tasks an (Dokumente verschieben, Ticket-Infos aktualisieren, Lizenzen dekodieren/neu laden, Push senden, Support-gelöscht-Event).Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: mixed, Rollen USER, PHP. TANSS_APP-Token nur mit loggedInUserId.Hinweise: taskName = moveDocuments (id string), ticketRelevantInfoUpdate (id int, asynchron), decodeLicenses, refreshLicenses, sendPush (id int), createSupportDeleteTanssEvent (id int = Support-ID). Unbekannter Name -> ENUM_TYPE_DONT_EXIST; nicht-numerische id bei int-Tasks -> NumberFormatException. Keine Rechteprüfung im Controller (vermutlich für interne PHP-Aufrufe). meta FOUND.
        """
        # Task-abhängiger Parameter (Id als String).
        id: Optional[str] = None

    
    @dataclass
    class WithTaskNameItemRequestBuilderGetRequestConfiguration(RequestConfiguration[WithTaskNameItemRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

