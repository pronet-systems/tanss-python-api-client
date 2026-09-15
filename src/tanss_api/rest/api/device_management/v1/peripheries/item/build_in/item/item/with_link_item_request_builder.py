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
    from .with_link_delete_response import WithLinkDeleteResponse
    from .with_link_post_response import WithLinkPostResponse

class WithLinkItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/deviceManagement/v1/peripheries/{id}/buildIn/{linkTypeId}/{linkId}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new WithLinkItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/deviceManagement/v1/peripheries/{id}/buildIn/{linkTypeId}/{linkId}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[WithLinkDeleteResponse]:
        """
        Entfernt die Einbau-Zuordnung eines Peripheriegeräts zu einem PC (linkTypeId 1) oder einem anderen Peripheriegerät (linkTypeId 4).Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt (dort nur der Alias /api/v1/peripheries/{peripheryId}/buildIn/...); vom Server so umgesetzt, gegen 10.10 geprueft.Token: module, Rollen DEVICE_MANAGEMENT.Rechte: Lizenz DEVICEMANAGEMENT; VIEW_DEVICE_LISTS(1); MANAGE_DEVICES(2); Firmenzugriff auf companyId des Geräts.Hinweise: Nur linkTypeId 1 (PC) und 4 (Peripherie) werden verarbeitet, andere Werte sind No-Op mit Erfolg. Peripherie {id} nicht vorhanden -> 404 DATA_NOT_FOUND.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[WithLinkDeleteResponse]
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .with_link_delete_response import WithLinkDeleteResponse

        return await self.request_adapter.send_async(request_info, WithLinkDeleteResponse, None)
    
    async def post(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[WithLinkPostResponse]:
        """
        Legt eine Einbau-Zuordnung des Peripheriegeräts {id} in einen PC (linkTypeId 1) oder ein anderes Peripheriegerät (linkTypeId 4) mit ID {linkId} an.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt (dort nur der Alias /api/v1/peripheries/{peripheryId}/buildIn/...); vom Server so umgesetzt, gegen 10.10 geprueft.Token: module, Rollen DEVICE_MANAGEMENT.Rechte: Lizenz DEVICEMANAGEMENT; VIEW_DEVICE_LISTS(1); MANAGE_DEVICES(2); Firmenzugriff auf companyId des Geräts.Hinweise: Nur linkTypeId 1 und 4; andere Werte No-Op mit CREATED. Existenz/Zugriff von {linkId} wird nicht geprüft. Peripherie nicht vorhanden -> 404.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[WithLinkPostResponse]
        """
        request_info = self.to_post_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .with_link_post_response import WithLinkPostResponse

        return await self.request_adapter.send_async(request_info, WithLinkPostResponse, None)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Entfernt die Einbau-Zuordnung eines Peripheriegeräts zu einem PC (linkTypeId 1) oder einem anderen Peripheriegerät (linkTypeId 4).Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt (dort nur der Alias /api/v1/peripheries/{peripheryId}/buildIn/...); vom Server so umgesetzt, gegen 10.10 geprueft.Token: module, Rollen DEVICE_MANAGEMENT.Rechte: Lizenz DEVICEMANAGEMENT; VIEW_DEVICE_LISTS(1); MANAGE_DEVICES(2); Firmenzugriff auf companyId des Geräts.Hinweise: Nur linkTypeId 1 (PC) und 4 (Peripherie) werden verarbeitet, andere Werte sind No-Op mit Erfolg. Peripherie {id} nicht vorhanden -> 404 DATA_NOT_FOUND.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Legt eine Einbau-Zuordnung des Peripheriegeräts {id} in einen PC (linkTypeId 1) oder ein anderes Peripheriegerät (linkTypeId 4) mit ID {linkId} an.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt (dort nur der Alias /api/v1/peripheries/{peripheryId}/buildIn/...); vom Server so umgesetzt, gegen 10.10 geprueft.Token: module, Rollen DEVICE_MANAGEMENT.Rechte: Lizenz DEVICEMANAGEMENT; VIEW_DEVICE_LISTS(1); MANAGE_DEVICES(2); Firmenzugriff auf companyId des Geräts.Hinweise: Nur linkTypeId 1 und 4; andere Werte No-Op mit CREATED. Existenz/Zugriff von {linkId} wird nicht geprüft. Peripherie nicht vorhanden -> 404.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.POST, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> WithLinkItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: WithLinkItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return WithLinkItemRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class WithLinkItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class WithLinkItemRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

