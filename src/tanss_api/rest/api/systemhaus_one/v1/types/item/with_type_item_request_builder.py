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
    from ......models.tns_company_type import TnsCompanyType
    from .with_type_delete_response import WithTypeDeleteResponse
    from .with_type_get_response import WithTypeGetResponse
    from .with_type_put_response import WithTypePutResponse

class WithTypeItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/systemhaus_one/v1/types/{typeId}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new WithTypeItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/systemhaus_one/v1/types/{typeId}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[WithTypeDeleteResponse]:
        """
        Löscht einen Firmentyp.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: module, Rollen SYSTEMHAUS_ONE.Rechte: Benutzertyp TECHNICAN/COMPANY_ADMIN/RESTRICTED_USER/FREELANCER, BASE_DATA_MANAGEMENT_SYSTEM_TABLES.Hinweise: Lizenz SAP_ONE erforderlich. Nicht löschbar, wenn Firmen diesen Typ zugeordnet haben (TnsCannotDeleteException). Nicht gefunden -> ENTITY_NOT_FOUND. Logeintrag.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[WithTypeDeleteResponse]
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .with_type_delete_response import WithTypeDeleteResponse

        return await self.request_adapter.send_async(request_info, WithTypeDeleteResponse, None)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[WithTypeGetResponse]:
        """
        Liefert einen Firmentyp per ID.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: module, Rollen SYSTEMHAUS_ONE.Rechte: Benutzertyp TECHNICAN/COMPANY_ADMIN/RESTRICTED_USER/FREELANCER.Hinweise: Lizenz SAP_ONE erforderlich. Nicht gefunden -> OBJECT_NOT_FOUND.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[WithTypeGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .with_type_get_response import WithTypeGetResponse

        return await self.request_adapter.send_async(request_info, WithTypeGetResponse, None)
    
    async def put(self,body: TnsCompanyType, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[WithTypePutResponse]:
        """
        Aktualisiert einen Firmentyp per JSON-Merge.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: module, Rollen SYSTEMHAUS_ONE.Rechte: Benutzertyp TECHNICAN/COMPANY_ADMIN/RESTRICTED_USER/FREELANCER, BASE_DATA_MANAGEMENT_SYSTEM_TABLES.Hinweise: Lizenz SAP_ONE erforderlich. Teilobjekt (name, categoryId, icon, hidden); "id" wird ignoriert. Logeintrag mit altem/neuem Namen. Leerer Body -> TnsJsonException; nicht gefunden -> ENTITY_NOT_FOUND.
        param body: defines a company type
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[WithTypePutResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .with_type_put_response import WithTypePutResponse

        return await self.request_adapter.send_async(request_info, WithTypePutResponse, None)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Löscht einen Firmentyp.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: module, Rollen SYSTEMHAUS_ONE.Rechte: Benutzertyp TECHNICAN/COMPANY_ADMIN/RESTRICTED_USER/FREELANCER, BASE_DATA_MANAGEMENT_SYSTEM_TABLES.Hinweise: Lizenz SAP_ONE erforderlich. Nicht löschbar, wenn Firmen diesen Typ zugeordnet haben (TnsCannotDeleteException). Nicht gefunden -> ENTITY_NOT_FOUND. Logeintrag.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Liefert einen Firmentyp per ID.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: module, Rollen SYSTEMHAUS_ONE.Rechte: Benutzertyp TECHNICAN/COMPANY_ADMIN/RESTRICTED_USER/FREELANCER.Hinweise: Lizenz SAP_ONE erforderlich. Nicht gefunden -> OBJECT_NOT_FOUND.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_put_request_information(self,body: TnsCompanyType, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Aktualisiert einen Firmentyp per JSON-Merge.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: module, Rollen SYSTEMHAUS_ONE.Rechte: Benutzertyp TECHNICAN/COMPANY_ADMIN/RESTRICTED_USER/FREELANCER, BASE_DATA_MANAGEMENT_SYSTEM_TABLES.Hinweise: Lizenz SAP_ONE erforderlich. Teilobjekt (name, categoryId, icon, hidden); "id" wird ignoriert. Logeintrag mit altem/neuem Namen. Leerer Body -> TnsJsonException; nicht gefunden -> ENTITY_NOT_FOUND.
        param body: defines a company type
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
    
    def with_url(self,raw_url: str) -> WithTypeItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: WithTypeItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return WithTypeItemRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class WithTypeItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class WithTypeItemRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class WithTypeItemRequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

