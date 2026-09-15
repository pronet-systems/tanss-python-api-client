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
    from ......models.tns_personal_computer_with_ip_guarantee import TnsPersonalComputerWithIpGuarantee
    from .pcs_delete_response import PcsDeleteResponse
    from .pcs_get_response import PcsGetResponse
    from .pcs_put_response import PcsPutResponse

class PcsItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/deviceManagement/v1/pcs/{id}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new PcsItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/deviceManagement/v1/pcs/{id}{?loadContractAssignments*}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[PcsDeleteResponse]:
        """
        Löscht einen PC/Server, sofern keine verknüpften Objekte existieren; entfernt Zuordnungen und schreibt Log. Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft. Token: module, Rollen DEVICE_MANAGEMENT. Rechte: licModule DEVICEMANAGEMENT (7), VIEW_DEVICE_LISTS (1), MANAGE_DEVICES (2), DELETE_DEVICES (131), Firmenzugriff auf pc.companyId. Hinweise: Alias /api/v1/pcs/{id}. Blockiert (TnsCannotDeleteException mit infos), wenn Komponenten, Supports, Tickets, Aufgaben oder Wartungsvertrags-Zuordnungen am PC hängen. Nach dem Löschen werden Zuordnungen (IPs, Service-Icons, Dokumente etc.) bereinigt und ein Löschlog geschrieben. Antwort meta DELETED.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[PcsDeleteResponse]
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .pcs_delete_response import PcsDeleteResponse

        return await self.request_adapter.send_async(request_info, PcsDeleteResponse, None)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[PcsItemRequestBuilderGetQueryParameters]] = None) -> Optional[PcsGetResponse]:
        """
        Liefert einen PC/Server mit Details (IPs, Garantie, Komponenten, Peripherie, Lizenzen), optional inkl. Wartungsvertrags-Zuordnungen. Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft. Token: module, Rollen DEVICE_MANAGEMENT. Rechte: licModule DEVICEMANAGEMENT (7), VIEW_DEVICE_LISTS (1), Firmenzugriff auf pc.companyId. Hinweise: Alias /api/v1/pcs/{id}. Query loadContractAssignments (default false): true ermittelt maintenanceContractAssignments aus den Verträgen der Firma und befüllt linkedEntities. meta enthält Filter-Strategien (DETAIL für PC/Periphery/Component/Softwarelicense, SMALL für ContractAssignment). OBJECT_NOT_FOUND wenn unbekannt.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[PcsGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .pcs_get_response import PcsGetResponse

        return await self.request_adapter.send_async(request_info, PcsGetResponse, None)
    
    async def put(self,body: TnsPersonalComputerWithIpGuarantee, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[PcsPutResponse]:
        """
        Aktualisiert einen PC/Server per JSON-Merge mit Validierung und Änderungslog. Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft. Token: module, Rollen DEVICE_MANAGEMENT. Rechte: licModule DEVICEMANAGEMENT (7), VIEW_DEVICE_LISTS (1), MANAGE_DEVICES (2), Firmenzugriff auf companyId (alt und neu), MANAGE_DEVICE_PASSWORDS (88) für internalRemark, MANAGE_REMOTE_MAINTENANCE_CONNECTIONS (303) für teamviewerPassword/anydeskPassword. Hinweise: Alias /api/v1/pcs/{id}. Body ist ein Merge aller Felder von TnsPersonalComputer (inkl. ips[] und guarantee); Key id wird entfernt; model ist Pflicht; purchasePrice nur für interne Benutzer, sonst still verworfen. Firmenwechsel verboten bei Vertragszuordnungen (CANT_CHANGE_COMPANY_BECAUSE_ASSIGNED_TO_CONTRACTS), ebenso active-Änderung. Validierung: companyId/assignmentEmployeeId/serviceTechnicianId/manufacturerId/ mainboardManufacturerId/cpuManufacturerId/osId/cpuTypeId müssen existieren, ownageType und model Pflicht (TnsMissingFieldKeyException). hostId > 0 prüft Firmenzugriff auf den Host. Änderungslog wird geschrieben. Antwort meta UPDATED.
        param body: Describes a pc or server with infos (ip address, guarantee)
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[PcsPutResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .pcs_put_response import PcsPutResponse

        return await self.request_adapter.send_async(request_info, PcsPutResponse, None)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Löscht einen PC/Server, sofern keine verknüpften Objekte existieren; entfernt Zuordnungen und schreibt Log. Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft. Token: module, Rollen DEVICE_MANAGEMENT. Rechte: licModule DEVICEMANAGEMENT (7), VIEW_DEVICE_LISTS (1), MANAGE_DEVICES (2), DELETE_DEVICES (131), Firmenzugriff auf pc.companyId. Hinweise: Alias /api/v1/pcs/{id}. Blockiert (TnsCannotDeleteException mit infos), wenn Komponenten, Supports, Tickets, Aufgaben oder Wartungsvertrags-Zuordnungen am PC hängen. Nach dem Löschen werden Zuordnungen (IPs, Service-Icons, Dokumente etc.) bereinigt und ein Löschlog geschrieben. Antwort meta DELETED.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[PcsItemRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Liefert einen PC/Server mit Details (IPs, Garantie, Komponenten, Peripherie, Lizenzen), optional inkl. Wartungsvertrags-Zuordnungen. Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft. Token: module, Rollen DEVICE_MANAGEMENT. Rechte: licModule DEVICEMANAGEMENT (7), VIEW_DEVICE_LISTS (1), Firmenzugriff auf pc.companyId. Hinweise: Alias /api/v1/pcs/{id}. Query loadContractAssignments (default false): true ermittelt maintenanceContractAssignments aus den Verträgen der Firma und befüllt linkedEntities. meta enthält Filter-Strategien (DETAIL für PC/Periphery/Component/Softwarelicense, SMALL für ContractAssignment). OBJECT_NOT_FOUND wenn unbekannt.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_put_request_information(self,body: TnsPersonalComputerWithIpGuarantee, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Aktualisiert einen PC/Server per JSON-Merge mit Validierung und Änderungslog. Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft. Token: module, Rollen DEVICE_MANAGEMENT. Rechte: licModule DEVICEMANAGEMENT (7), VIEW_DEVICE_LISTS (1), MANAGE_DEVICES (2), Firmenzugriff auf companyId (alt und neu), MANAGE_DEVICE_PASSWORDS (88) für internalRemark, MANAGE_REMOTE_MAINTENANCE_CONNECTIONS (303) für teamviewerPassword/anydeskPassword. Hinweise: Alias /api/v1/pcs/{id}. Body ist ein Merge aller Felder von TnsPersonalComputer (inkl. ips[] und guarantee); Key id wird entfernt; model ist Pflicht; purchasePrice nur für interne Benutzer, sonst still verworfen. Firmenwechsel verboten bei Vertragszuordnungen (CANT_CHANGE_COMPANY_BECAUSE_ASSIGNED_TO_CONTRACTS), ebenso active-Änderung. Validierung: companyId/assignmentEmployeeId/serviceTechnicianId/manufacturerId/ mainboardManufacturerId/cpuManufacturerId/osId/cpuTypeId müssen existieren, ownageType und model Pflicht (TnsMissingFieldKeyException). hostId > 0 prüft Firmenzugriff auf den Host. Änderungslog wird geschrieben. Antwort meta UPDATED.
        param body: Describes a pc or server with infos (ip address, guarantee)
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
    
    def with_url(self,raw_url: str) -> PcsItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: PcsItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return PcsItemRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class PcsItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class PcsItemRequestBuilderGetQueryParameters():
        """
        Liefert einen PC/Server mit Details (IPs, Garantie, Komponenten, Peripherie, Lizenzen), optional inkl. Wartungsvertrags-Zuordnungen. Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft. Token: module, Rollen DEVICE_MANAGEMENT. Rechte: licModule DEVICEMANAGEMENT (7), VIEW_DEVICE_LISTS (1), Firmenzugriff auf pc.companyId. Hinweise: Alias /api/v1/pcs/{id}. Query loadContractAssignments (default false): true ermittelt maintenanceContractAssignments aus den Verträgen der Firma und befüllt linkedEntities. meta enthält Filter-Strategien (DETAIL für PC/Periphery/Component/Softwarelicense, SMALL für ContractAssignment). OBJECT_NOT_FOUND wenn unbekannt.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "load_contract_assignments":
                return "loadContractAssignments"
            return original_name
        
        load_contract_assignments: Optional[bool] = None

    
    @dataclass
    class PcsItemRequestBuilderGetRequestConfiguration(RequestConfiguration[PcsItemRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class PcsItemRequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

