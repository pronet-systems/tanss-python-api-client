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
    from ......models.company_post import CompanyPost
    from .companies_delete_response import CompaniesDeleteResponse
    from .companies_get_response import CompaniesGetResponse
    from .companies_put_response import CompaniesPutResponse

class CompaniesItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/systemhaus_one/v1/companies/{id}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new CompaniesItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/systemhaus_one/v1/companies/{id}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[CompaniesDeleteResponse]:
        """
        Löscht eine Firma (delegiert an offiziellen Handler DELETE /api/v1/companies/{id}).Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: module, Rollen SYSTEMHAUS_ONE.Rechte: MANAGE_COMPANIES, Zugriffstyp COMPANY_ADMIN.Hinweise: Keine SAP_ONE-Lizenzprüfung. Eigene Firma nicht löschbar (FORBIDDEN_NO_COMPANY_ACCESS); bei verknüpften Datensätzen TnsCannotDeleteException.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[CompaniesDeleteResponse]
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .companies_delete_response import CompaniesDeleteResponse

        return await self.request_adapter.send_async(request_info, CompaniesDeleteResponse, None)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[CompaniesGetResponse]:
        """
        Liefert eine Firma per ID (delegiert an offiziellen Handler GET /api/v1/companies/{id}).Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: module, Rollen SYSTEMHAUS_ONE.Rechte: Firmenzugriff auf die Firma.Hinweise: Keine SAP_ONE-Lizenzprüfung. Nicht gefunden -> OBJECT_NOT_FOUND.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[CompaniesGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .companies_get_response import CompaniesGetResponse

        return await self.request_adapter.send_async(request_info, CompaniesGetResponse, None)
    
    async def put(self,body: CompanyPost, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[CompaniesPutResponse]:
        """
        Aktualisiert eine Firma per JSON-Merge (delegiert an offiziellen Handler PUT /api/v1/companies/{id}).Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: module, Rollen SYSTEMHAUS_ONE.Rechte: MANAGE_COMPANIES, Firmenzugriff; feldabhängig MANAGE_TICKET_OPTIONS, MANAGE_MAINTENANCE_CONTRACT_OPTIONS, EDIT_INTERNAL_INFORMATION, CHANGE_PDF_OPTIONS, ASSIGN_HEADQUARTERS, ASSIGN_CUSTOMER_LOCK, MANAGE_SERVICE_OPTIONS, SET_COMPANY_INACTIVE.Hinweise: Keine SAP_ONE-Lizenzprüfung. Teilobjekt; "id" wird ignoriert, username, personalCustomer, personalCustomerEmployeeId, deliveryId, modified werden entfernt. Feldgruppen ohne entsprechendes Recht werden stillschweigend verworfen.
        param body: Company object to be saved.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[CompaniesPutResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .companies_put_response import CompaniesPutResponse

        return await self.request_adapter.send_async(request_info, CompaniesPutResponse, None)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Löscht eine Firma (delegiert an offiziellen Handler DELETE /api/v1/companies/{id}).Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: module, Rollen SYSTEMHAUS_ONE.Rechte: MANAGE_COMPANIES, Zugriffstyp COMPANY_ADMIN.Hinweise: Keine SAP_ONE-Lizenzprüfung. Eigene Firma nicht löschbar (FORBIDDEN_NO_COMPANY_ACCESS); bei verknüpften Datensätzen TnsCannotDeleteException.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Liefert eine Firma per ID (delegiert an offiziellen Handler GET /api/v1/companies/{id}).Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: module, Rollen SYSTEMHAUS_ONE.Rechte: Firmenzugriff auf die Firma.Hinweise: Keine SAP_ONE-Lizenzprüfung. Nicht gefunden -> OBJECT_NOT_FOUND.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_put_request_information(self,body: CompanyPost, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Aktualisiert eine Firma per JSON-Merge (delegiert an offiziellen Handler PUT /api/v1/companies/{id}).Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: module, Rollen SYSTEMHAUS_ONE.Rechte: MANAGE_COMPANIES, Firmenzugriff; feldabhängig MANAGE_TICKET_OPTIONS, MANAGE_MAINTENANCE_CONTRACT_OPTIONS, EDIT_INTERNAL_INFORMATION, CHANGE_PDF_OPTIONS, ASSIGN_HEADQUARTERS, ASSIGN_CUSTOMER_LOCK, MANAGE_SERVICE_OPTIONS, SET_COMPANY_INACTIVE.Hinweise: Keine SAP_ONE-Lizenzprüfung. Teilobjekt; "id" wird ignoriert, username, personalCustomer, personalCustomerEmployeeId, deliveryId, modified werden entfernt. Feldgruppen ohne entsprechendes Recht werden stillschweigend verworfen.
        param body: Company object to be saved.
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
    
    def with_url(self,raw_url: str) -> CompaniesItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: CompaniesItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return CompaniesItemRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class CompaniesItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class CompaniesItemRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class CompaniesItemRequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

