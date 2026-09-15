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
    from ......models.tns_tanss_event_configuration import TnsTanssEventConfiguration
    from .properties_put_response import PropertiesPutResponse

class PropertiesRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/tanssEvents/list/properties
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new PropertiesRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/tanssEvents/list/properties", path_parameters)
    
    async def put(self,body: TnsTanssEventConfiguration, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[PropertiesPutResponse]:
        """
        Liefert die Eigenschaften (Kategorie-Auswahlliste mit Vorauswahl des Users) fuer die TANSS-Events-Liste im angegebenen Kontext.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId.Rechte: Benutzertyp TECHNICAN, COMPANY_ADMIN, RESTRICTED_USER oder FREELANCER (sonst FORBIDDEN_MISSING_PERMISSIONS).Hinweise: Lese-Operation trotz PUT. Aus dem Body wird nur context (FRONTEND | APP) ausgewertet, alle anderen Felder werden ignoriert. Alle Kategorien werden geliefert; die fuer den User im Kontext ausgewaehlten tragen data.selected=true. context=null -> keine Vorauswahl. meta=FOUND.
        param body: defines the filter for the activity feed items
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[PropertiesPutResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .properties_put_response import PropertiesPutResponse

        return await self.request_adapter.send_async(request_info, PropertiesPutResponse, None)
    
    def to_put_request_information(self,body: TnsTanssEventConfiguration, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Liefert die Eigenschaften (Kategorie-Auswahlliste mit Vorauswahl des Users) fuer die TANSS-Events-Liste im angegebenen Kontext.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId.Rechte: Benutzertyp TECHNICAN, COMPANY_ADMIN, RESTRICTED_USER oder FREELANCER (sonst FORBIDDEN_MISSING_PERMISSIONS).Hinweise: Lese-Operation trotz PUT. Aus dem Body wird nur context (FRONTEND | APP) ausgewertet, alle anderen Felder werden ignoriert. Alle Kategorien werden geliefert; die fuer den User im Kontext ausgewaehlten tragen data.selected=true. context=null -> keine Vorauswahl. meta=FOUND.
        param body: defines the filter for the activity feed items
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
    
    def with_url(self,raw_url: str) -> PropertiesRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: PropertiesRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return PropertiesRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class PropertiesRequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

