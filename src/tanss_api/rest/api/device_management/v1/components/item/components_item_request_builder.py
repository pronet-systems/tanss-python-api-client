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
    from .components_delete_response import ComponentsDeleteResponse
    from .components_get_response import ComponentsGetResponse
    from .components_put_request_body import ComponentsPutRequestBody
    from .components_put_response import ComponentsPutResponse

class ComponentsItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/deviceManagement/v1/components/{id}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new ComponentsItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/deviceManagement/v1/components/{id}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[ComponentsDeleteResponse]:
        """
        Löscht eine Komponente (inkl. Garantie-Datensatz) und loggt die Löschung. Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft. Token: module, Rollen DEVICE_MANAGEMENT. Rechte: Lizenz DEVICEMANAGEMENT, VIEW_DEVICE_LISTS(1), MANAGE_DEVICES(2), DELETE_DEVICES(131), Firmenzugriff auf companyId bzw. Firma des PCs/Peripheriegeräts, in das sie eingebaut ist. Hinweise: Alias /api/v1/components/{id}. Verknüpfte Supports/Tickets/Aufgaben/Wartungsverträge (linkTypeId 5) -> TnsCannotDeleteException. Nicht gefunden -> 404.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ComponentsDeleteResponse]
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .components_delete_response import ComponentsDeleteResponse

        return await self.request_adapter.send_async(request_info, ComponentsDeleteResponse, None)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[ComponentsGetResponse]:
        """
        Liefert eine Komponente inkl. Garantie und Einbau-Zuordnung (builtInto). Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft. Token: module, Rollen DEVICE_MANAGEMENT. Rechte: Lizenz DEVICEMANAGEMENT, VIEW_DEVICE_LISTS(1), Firmenzugriff auf companyId bzw. Firma des PCs/Peripheriegeräts. Hinweise: Alias /api/v1/components/{id}. Nicht gefunden -> 404 OBJECT_NOT_FOUND. PC nicht vorhanden -> 400 COMPONENT_PC_DOESNT_EXIST, Peripherie nicht vorhanden -> 400 COMPONENT_PERIPHERY_DOESNT_EXIST. Verknüpfte Entitäten in meta.linkedEntities.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ComponentsGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .components_get_response import ComponentsGetResponse

        return await self.request_adapter.send_async(request_info, ComponentsGetResponse, None)
    
    async def put(self,body: ComponentsPutRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[ComponentsPutResponse]:
        """
        Aktualisiert eine Komponente per JSON-Merge (inkl. Garantie) und loggt Änderungen. Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft. Token: module, Rollen DEVICE_MANAGEMENT. Rechte: Lizenz DEVICEMANAGEMENT, VIEW_DEVICE_LISTS(1), MANAGE_DEVICES(2), Firmenzugriff auf companyId sowie Firma des PCs (pcId) / Peripheriegeräts (peripheryId). Hinweise: id im Body wird entfernt. purchasePrice wird ohne securityManager.long() stillschweigend entfernt. Validierung: effektive Firma muss >0 sein (400 DEVICE_MUST_HAVE_A_COMPANY_SET), pcId und peripheryId nicht gleichzeitig (400 COMPONENT_CANT_BE_ASSIGNED_TO_PC_AND_PERIPHERY), bei pcId/peripheryId >0 wird companyId auf 0 gesetzt, componentTypeId/manufacturerId/hddTypeId müssen existieren. Nicht gefunden -> 404. Alias /api/v1/components/{id}.
        param body: Beliebige TnsComponent-Felder (JSON-Merge)
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ComponentsPutResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .components_put_response import ComponentsPutResponse

        return await self.request_adapter.send_async(request_info, ComponentsPutResponse, None)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Löscht eine Komponente (inkl. Garantie-Datensatz) und loggt die Löschung. Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft. Token: module, Rollen DEVICE_MANAGEMENT. Rechte: Lizenz DEVICEMANAGEMENT, VIEW_DEVICE_LISTS(1), MANAGE_DEVICES(2), DELETE_DEVICES(131), Firmenzugriff auf companyId bzw. Firma des PCs/Peripheriegeräts, in das sie eingebaut ist. Hinweise: Alias /api/v1/components/{id}. Verknüpfte Supports/Tickets/Aufgaben/Wartungsverträge (linkTypeId 5) -> TnsCannotDeleteException. Nicht gefunden -> 404.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Liefert eine Komponente inkl. Garantie und Einbau-Zuordnung (builtInto). Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft. Token: module, Rollen DEVICE_MANAGEMENT. Rechte: Lizenz DEVICEMANAGEMENT, VIEW_DEVICE_LISTS(1), Firmenzugriff auf companyId bzw. Firma des PCs/Peripheriegeräts. Hinweise: Alias /api/v1/components/{id}. Nicht gefunden -> 404 OBJECT_NOT_FOUND. PC nicht vorhanden -> 400 COMPONENT_PC_DOESNT_EXIST, Peripherie nicht vorhanden -> 400 COMPONENT_PERIPHERY_DOESNT_EXIST. Verknüpfte Entitäten in meta.linkedEntities.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_put_request_information(self,body: ComponentsPutRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Aktualisiert eine Komponente per JSON-Merge (inkl. Garantie) und loggt Änderungen. Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft. Token: module, Rollen DEVICE_MANAGEMENT. Rechte: Lizenz DEVICEMANAGEMENT, VIEW_DEVICE_LISTS(1), MANAGE_DEVICES(2), Firmenzugriff auf companyId sowie Firma des PCs (pcId) / Peripheriegeräts (peripheryId). Hinweise: id im Body wird entfernt. purchasePrice wird ohne securityManager.long() stillschweigend entfernt. Validierung: effektive Firma muss >0 sein (400 DEVICE_MUST_HAVE_A_COMPANY_SET), pcId und peripheryId nicht gleichzeitig (400 COMPONENT_CANT_BE_ASSIGNED_TO_PC_AND_PERIPHERY), bei pcId/peripheryId >0 wird companyId auf 0 gesetzt, componentTypeId/manufacturerId/hddTypeId müssen existieren. Nicht gefunden -> 404. Alias /api/v1/components/{id}.
        param body: Beliebige TnsComponent-Felder (JSON-Merge)
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
    
    def with_url(self,raw_url: str) -> ComponentsItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: ComponentsItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return ComponentsItemRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class ComponentsItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class ComponentsItemRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class ComponentsItemRequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

