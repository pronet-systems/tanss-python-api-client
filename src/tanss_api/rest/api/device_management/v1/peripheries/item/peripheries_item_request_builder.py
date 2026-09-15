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
    from .build_in.build_in_request_builder import BuildInRequestBuilder
    from .peripheries_delete_response import PeripheriesDeleteResponse
    from .peripheries_get_response import PeripheriesGetResponse
    from .peripheries_put_request_body import PeripheriesPutRequestBody
    from .peripheries_put_response import PeripheriesPutResponse

class PeripheriesItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/deviceManagement/v1/peripheries/{id}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new PeripheriesItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/deviceManagement/v1/peripheries/{id}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[PeripheriesDeleteResponse]:
        """
        Löscht ein Peripheriegerät.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt (dort nur der Alias /api/v1/peripheries/{peripheryId}); vom Server so umgesetzt, gegen 10.10 geprueft.Token: module, Rollen DEVICE_MANAGEMENT.Rechte: Lizenz DEVICEMANAGEMENT; VIEW_DEVICE_LISTS(1); MANAGE_DEVICES(2); DELETE_DEVICES(131); Firmenzugriff auf companyId des Geräts.Hinweise: Verknüpfte Supports/Tickets/Aufgaben/Wartungsverträge (linkTypeId 4) -> TnsCannotDeleteException mit Zählern. Nicht gefunden -> 404. Löschung wird geloggt.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[PeripheriesDeleteResponse]
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .peripheries_delete_response import PeripheriesDeleteResponse

        return await self.request_adapter.send_async(request_info, PeripheriesDeleteResponse, None)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[PeripheriesGetResponse]:
        """
        Liefert ein Peripheriegerät inkl. IPs, Garantie und Zusatzfeldern.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt (dort nur der Alias /api/v1/peripheries/{peripheryId}); vom Server so umgesetzt, gegen 10.10 geprueft.Token: module, Rollen DEVICE_MANAGEMENT.Rechte: Lizenz DEVICEMANAGEMENT; VIEW_DEVICE_LISTS(1); Firmenzugriff auf companyId des Geräts.Hinweise: Nicht gefunden -> 404 OBJECT_NOT_FOUND. Verknüpfte Entitäten (Firma, Mitarbeiter, PC ...) in meta.linkedEntities. Zusätzlich zu TnsPeriphery-With-Ip-Guarantee liefert der Server ip, showRemark, loginName, loginPassword, maintenance, mac, isdn, connectionType, eConfigId, eConfigPos, serviceIcons[].
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[PeripheriesGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .peripheries_get_response import PeripheriesGetResponse

        return await self.request_adapter.send_async(request_info, PeripheriesGetResponse, None)
    
    async def put(self,body: PeripheriesPutRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[PeripheriesPutResponse]:
        """
        Aktualisiert ein Peripheriegerät per JSON-Merge (inkl. Garantie, IPs, Zusatzfelder) und loggt die Änderungen.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt (dort nur der Alias /api/v1/peripheries/{peripheryId}); vom Server so umgesetzt, gegen 10.10 geprueft.Token: module, Rollen DEVICE_MANAGEMENT.Rechte: Lizenz DEVICEMANAGEMENT; VIEW_DEVICE_LISTS(1); MANAGE_DEVICES(2); Firmenzugriff (alte und neue companyId); MANAGE_DEVICE_PASSWORDS(88) + securityManager.long() für internalRemark.Hinweise: id im Body wird entfernt. internalRemark wird ohne Recht 88 stillschweigend entfernt, purchasePrice ohne securityManager.long() ebenfalls. Validierung: peripheryTypeId muss existieren; manufacturerId/employeeId/pcId/storageId falls != 0 müssen existieren; ownageType und connectionType Pflicht (sonst TnsInvalidParameterException). Nicht gefunden -> 404.
        param body: Beliebige TnsPeriphery-Felder (JSON-Merge)
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[PeripheriesPutResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .peripheries_put_response import PeripheriesPutResponse

        return await self.request_adapter.send_async(request_info, PeripheriesPutResponse, None)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Löscht ein Peripheriegerät.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt (dort nur der Alias /api/v1/peripheries/{peripheryId}); vom Server so umgesetzt, gegen 10.10 geprueft.Token: module, Rollen DEVICE_MANAGEMENT.Rechte: Lizenz DEVICEMANAGEMENT; VIEW_DEVICE_LISTS(1); MANAGE_DEVICES(2); DELETE_DEVICES(131); Firmenzugriff auf companyId des Geräts.Hinweise: Verknüpfte Supports/Tickets/Aufgaben/Wartungsverträge (linkTypeId 4) -> TnsCannotDeleteException mit Zählern. Nicht gefunden -> 404. Löschung wird geloggt.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Liefert ein Peripheriegerät inkl. IPs, Garantie und Zusatzfeldern.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt (dort nur der Alias /api/v1/peripheries/{peripheryId}); vom Server so umgesetzt, gegen 10.10 geprueft.Token: module, Rollen DEVICE_MANAGEMENT.Rechte: Lizenz DEVICEMANAGEMENT; VIEW_DEVICE_LISTS(1); Firmenzugriff auf companyId des Geräts.Hinweise: Nicht gefunden -> 404 OBJECT_NOT_FOUND. Verknüpfte Entitäten (Firma, Mitarbeiter, PC ...) in meta.linkedEntities. Zusätzlich zu TnsPeriphery-With-Ip-Guarantee liefert der Server ip, showRemark, loginName, loginPassword, maintenance, mac, isdn, connectionType, eConfigId, eConfigPos, serviceIcons[].
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_put_request_information(self,body: PeripheriesPutRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Aktualisiert ein Peripheriegerät per JSON-Merge (inkl. Garantie, IPs, Zusatzfelder) und loggt die Änderungen.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt (dort nur der Alias /api/v1/peripheries/{peripheryId}); vom Server so umgesetzt, gegen 10.10 geprueft.Token: module, Rollen DEVICE_MANAGEMENT.Rechte: Lizenz DEVICEMANAGEMENT; VIEW_DEVICE_LISTS(1); MANAGE_DEVICES(2); Firmenzugriff (alte und neue companyId); MANAGE_DEVICE_PASSWORDS(88) + securityManager.long() für internalRemark.Hinweise: id im Body wird entfernt. internalRemark wird ohne Recht 88 stillschweigend entfernt, purchasePrice ohne securityManager.long() ebenfalls. Validierung: peripheryTypeId muss existieren; manufacturerId/employeeId/pcId/storageId falls != 0 müssen existieren; ownageType und connectionType Pflicht (sonst TnsInvalidParameterException). Nicht gefunden -> 404.
        param body: Beliebige TnsPeriphery-Felder (JSON-Merge)
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
    
    def with_url(self,raw_url: str) -> PeripheriesItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: PeripheriesItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return PeripheriesItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def build_in(self) -> BuildInRequestBuilder:
        """
        The buildIn property
        """
        from .build_in.build_in_request_builder import BuildInRequestBuilder

        return BuildInRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class PeripheriesItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class PeripheriesItemRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class PeripheriesItemRequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

