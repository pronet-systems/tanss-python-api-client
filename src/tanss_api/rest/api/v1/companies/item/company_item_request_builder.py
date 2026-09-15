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
    from .....models.company403_error import Company403Error
    from .....models.company_post import CompanyPost
    from .bookable_support.bookable_support_request_builder import BookableSupportRequestBuilder
    from .company_delete_response import CompanyDeleteResponse
    from .company_get_response import CompanyGetResponse
    from .company_put_response import CompanyPutResponse
    from .employees.employees_request_builder import EmployeesRequestBuilder
    from .item.with_company_item_request_builder import WithCompanyItemRequestBuilder
    from .types.types_request_builder import TypesRequestBuilder

class CompanyItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/companies/{company-id}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new CompanyItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/companies/{company%2Did}", path_parameters)
    
    def by_company_id(self,company_id: int) -> WithCompanyItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.v1.companies.item.item collection
        param company_id: Id of the company the info entries belong to.
        Returns: WithCompanyItemRequestBuilder
        """
        if company_id is None:
            raise TypeError("company_id cannot be null.")
        from .item.with_company_item_request_builder import WithCompanyItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["companyId"] = company_id
        return WithCompanyItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[CompanyDeleteResponse]:
        """
        Loescht eine Firma.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId.Rechte: Zugriffstyp >= COMPANY_ADMIN; Recht MANAGE_COMPANIES; die eigene Systemhaus-Firma darf nicht geloescht werden (FORBIDDEN_NO_COMPANY_ACCESS).Hinweise: ENTITY_NOT_FOUND bei unbekannter ID; zusaetzliche Pruefung vor dem Loeschen (vermutlich Verwendungs-/Sperrpruefung). meta=DELETED.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[CompanyDeleteResponse]
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .company_delete_response import CompanyDeleteResponse

        return await self.request_adapter.send_async(request_info, CompanyDeleteResponse, None)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[CompanyGetResponse]:
        """
        Returns a single company by its id, including its master data and assigned company types. The caller needs access to the company; customer users only ever see their own company.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[CompanyGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .....models.company403_error import Company403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Company403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .company_get_response import CompanyGetResponse

        return await self.request_adapter.send_async(request_info, CompanyGetResponse, error_mapping)
    
    async def put(self,body: CompanyPost, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[CompanyPutResponse]:
        """
        Updates an existing company with the supplied master data. Only the fields present in the payload are changed. The caller needs edit access to the company.
        param body: Company object to be saved.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[CompanyPutResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        from .....models.company403_error import Company403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Company403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .company_put_response import CompanyPutResponse

        return await self.request_adapter.send_async(request_info, CompanyPutResponse, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Loescht eine Firma.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId.Rechte: Zugriffstyp >= COMPANY_ADMIN; Recht MANAGE_COMPANIES; die eigene Systemhaus-Firma darf nicht geloescht werden (FORBIDDEN_NO_COMPANY_ACCESS).Hinweise: ENTITY_NOT_FOUND bei unbekannter ID; zusaetzliche Pruefung vor dem Loeschen (vermutlich Verwendungs-/Sperrpruefung). meta=DELETED.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Returns a single company by its id, including its master data and assigned company types. The caller needs access to the company; customer users only ever see their own company.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_put_request_information(self,body: CompanyPost, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Updates an existing company with the supplied master data. Only the fields present in the payload are changed. The caller needs edit access to the company.
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
    
    def with_url(self,raw_url: str) -> CompanyItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: CompanyItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return CompanyItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def bookable_support(self) -> BookableSupportRequestBuilder:
        """
        The bookableSupport property
        """
        from .bookable_support.bookable_support_request_builder import BookableSupportRequestBuilder

        return BookableSupportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def employees(self) -> EmployeesRequestBuilder:
        """
        The employees property
        """
        from .employees.employees_request_builder import EmployeesRequestBuilder

        return EmployeesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def types(self) -> TypesRequestBuilder:
        """
        The types property
        """
        from .types.types_request_builder import TypesRequestBuilder

        return TypesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class CompanyItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class CompanyItemRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class CompanyItemRequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

