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
    from .manufacturers_delete_response import ManufacturersDeleteResponse
    from .manufacturers_get_response import ManufacturersGetResponse
    from .manufacturers_put_request_body import ManufacturersPutRequestBody
    from .manufacturers_put_response import ManufacturersPutResponse

class ManufacturersItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/deviceManagement/v1/manufacturers/{id}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new ManufacturersItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/deviceManagement/v1/manufacturers/{id}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[ManufacturersDeleteResponse]:
        """
        Löscht einen Hersteller.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: module, Rollen DEVICE_MANAGEMENT.Rechte: BASE_DATA_MANAGEMENT_TECHNICAL_SECTION; interner Benutzertyp; ROLE_DEVICE_MANAGEMENT (WebSecurity).Hinweise: Alias von DELETE /api/v1/manufacturers/{id}. Verknüpfungs-Check gegen TnsPersonalComputer.manufacturerId/mainboardManufacturerId/cpuManufacturerId, TnsPeriphery.manufacturerId, TnsComponent.manufacturerId = TnsCannotDeleteException CANNOT_DELETE_ENTITY_LINKED_ENTITIES. Unbekannte id 404 ENTITY_NOT_FOUND. meta DELETED.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ManufacturersDeleteResponse]
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .manufacturers_delete_response import ManufacturersDeleteResponse

        return await self.request_adapter.send_async(request_info, ManufacturersDeleteResponse, None)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[ManufacturersGetResponse]:
        """
        Liefert einen Hersteller.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: module, Rollen DEVICE_MANAGEMENT.Rechte: ROLE_DEVICE_MANAGEMENT (WebSecurity); kein Rechte-Check im Service.Hinweise: Alias von GET /api/v1/manufacturers/{id}. Unbekannte id 404 OBJECT_NOT_FOUND. meta FOUND.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ManufacturersGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .manufacturers_get_response import ManufacturersGetResponse

        return await self.request_adapter.send_async(request_info, ManufacturersGetResponse, None)
    
    async def put(self,body: ManufacturersPutRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[ManufacturersPutResponse]:
        """
        Aktualisiert einen Hersteller (Teil-Update per JSON-Merge).Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: module, Rollen DEVICE_MANAGEMENT.Rechte: BASE_DATA_MANAGEMENT_TECHNICAL_SECTION; interner Benutzertyp; ROLE_DEVICE_MANAGEMENT (WebSecurity).Hinweise: Alias von PUT /api/v1/manufacturers/{id}. Nur übergebene Felder werden geändert; keine Duplikat-/Pflichtfeld-Prüfung beim Update. Unbekannte id 404 ENTITY_NOT_FOUND. meta UPDATED.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ManufacturersPutResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .manufacturers_put_response import ManufacturersPutResponse

        return await self.request_adapter.send_async(request_info, ManufacturersPutResponse, None)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Löscht einen Hersteller.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: module, Rollen DEVICE_MANAGEMENT.Rechte: BASE_DATA_MANAGEMENT_TECHNICAL_SECTION; interner Benutzertyp; ROLE_DEVICE_MANAGEMENT (WebSecurity).Hinweise: Alias von DELETE /api/v1/manufacturers/{id}. Verknüpfungs-Check gegen TnsPersonalComputer.manufacturerId/mainboardManufacturerId/cpuManufacturerId, TnsPeriphery.manufacturerId, TnsComponent.manufacturerId = TnsCannotDeleteException CANNOT_DELETE_ENTITY_LINKED_ENTITIES. Unbekannte id 404 ENTITY_NOT_FOUND. meta DELETED.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Liefert einen Hersteller.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: module, Rollen DEVICE_MANAGEMENT.Rechte: ROLE_DEVICE_MANAGEMENT (WebSecurity); kein Rechte-Check im Service.Hinweise: Alias von GET /api/v1/manufacturers/{id}. Unbekannte id 404 OBJECT_NOT_FOUND. meta FOUND.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_put_request_information(self,body: ManufacturersPutRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Aktualisiert einen Hersteller (Teil-Update per JSON-Merge).Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: module, Rollen DEVICE_MANAGEMENT.Rechte: BASE_DATA_MANAGEMENT_TECHNICAL_SECTION; interner Benutzertyp; ROLE_DEVICE_MANAGEMENT (WebSecurity).Hinweise: Alias von PUT /api/v1/manufacturers/{id}. Nur übergebene Felder werden geändert; keine Duplikat-/Pflichtfeld-Prüfung beim Update. Unbekannte id 404 ENTITY_NOT_FOUND. meta UPDATED.
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
    
    def with_url(self,raw_url: str) -> ManufacturersItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: ManufacturersItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return ManufacturersItemRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class ManufacturersItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class ManufacturersItemRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class ManufacturersItemRequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

