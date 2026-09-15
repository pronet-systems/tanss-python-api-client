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
    from .services_delete_response import ServicesDeleteResponse
    from .services_get_response import ServicesGetResponse
    from .services_put_request_body import ServicesPutRequestBody
    from .services_put_response import ServicesPutResponse

class ServicesItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/deviceManagement/v1/services/{id}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new ServicesItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/deviceManagement/v1/services/{id}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[ServicesDeleteResponse]:
        """
        Löscht einen Dienst (Service-Definition für IP/MAC-Zuordnungen).Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: module, Rollen DEVICE_MANAGEMENT.Rechte: BASE_DATA_MANAGEMENT_SYSTEM_TABLES, interner Benutzertyp, ROLE_DEVICE_MANAGEMENT (WebSecurity).Hinweise: Alias von DELETE /api/v1/services/{id}, abweichendes Recht (SYSTEM_TABLES statt TECHNICAL_SECTION). Noch von TnsIpMacServiceAssignment referenziert -> CANNOT_DELETE_ENTITY_LINKED_ENTITIES. Unbekannte id -> 404 ENTITY_NOT_FOUND. meta DELETED.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ServicesDeleteResponse]
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .services_delete_response import ServicesDeleteResponse

        return await self.request_adapter.send_async(request_info, ServicesDeleteResponse, None)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[ServicesGetResponse]:
        """
        Liefert einen Dienst.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: module, Rollen DEVICE_MANAGEMENT.Rechte: ROLE_DEVICE_MANAGEMENT (WebSecurity); kein Rechte-Check im Service.Hinweise: Alias von GET /api/v1/services/{id}. Unbekannte id -> 404 OBJECT_NOT_FOUND. meta FOUND.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ServicesGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .services_get_response import ServicesGetResponse

        return await self.request_adapter.send_async(request_info, ServicesGetResponse, None)
    
    async def put(self,body: ServicesPutRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[ServicesPutResponse]:
        """
        Aktualisiert einen Dienst (Teil-Update per JSON-Merge).Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: module, Rollen DEVICE_MANAGEMENT.Rechte: BASE_DATA_MANAGEMENT_SYSTEM_TABLES, interner Benutzertyp, ROLE_DEVICE_MANAGEMENT (WebSecurity).Hinweise: Alias von PUT /api/v1/services/{id}. Nur übergebene Felder werden geändert; keine Duplikat-/Pflichtfeldprüfung beim Update. Unbekannte id -> 404 ENTITY_NOT_FOUND. meta UPDATED.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ServicesPutResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .services_put_response import ServicesPutResponse

        return await self.request_adapter.send_async(request_info, ServicesPutResponse, None)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Löscht einen Dienst (Service-Definition für IP/MAC-Zuordnungen).Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: module, Rollen DEVICE_MANAGEMENT.Rechte: BASE_DATA_MANAGEMENT_SYSTEM_TABLES, interner Benutzertyp, ROLE_DEVICE_MANAGEMENT (WebSecurity).Hinweise: Alias von DELETE /api/v1/services/{id}, abweichendes Recht (SYSTEM_TABLES statt TECHNICAL_SECTION). Noch von TnsIpMacServiceAssignment referenziert -> CANNOT_DELETE_ENTITY_LINKED_ENTITIES. Unbekannte id -> 404 ENTITY_NOT_FOUND. meta DELETED.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Liefert einen Dienst.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: module, Rollen DEVICE_MANAGEMENT.Rechte: ROLE_DEVICE_MANAGEMENT (WebSecurity); kein Rechte-Check im Service.Hinweise: Alias von GET /api/v1/services/{id}. Unbekannte id -> 404 OBJECT_NOT_FOUND. meta FOUND.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_put_request_information(self,body: ServicesPutRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Aktualisiert einen Dienst (Teil-Update per JSON-Merge).Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: module, Rollen DEVICE_MANAGEMENT.Rechte: BASE_DATA_MANAGEMENT_SYSTEM_TABLES, interner Benutzertyp, ROLE_DEVICE_MANAGEMENT (WebSecurity).Hinweise: Alias von PUT /api/v1/services/{id}. Nur übergebene Felder werden geändert; keine Duplikat-/Pflichtfeldprüfung beim Update. Unbekannte id -> 404 ENTITY_NOT_FOUND. meta UPDATED.
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
    
    def with_url(self,raw_url: str) -> ServicesItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: ServicesItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return ServicesItemRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class ServicesItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class ServicesItemRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class ServicesItemRequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

