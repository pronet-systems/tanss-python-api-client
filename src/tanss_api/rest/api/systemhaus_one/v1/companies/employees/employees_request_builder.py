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
    from .departments.departments_request_builder import DepartmentsRequestBuilder
    from .employees_get_response import EmployeesGetResponse

class EmployeesRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/systemhaus_one/v1/companies/employees
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new EmployeesRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/systemhaus_one/v1/companies/employees{?companyId*,companyNumber*}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[EmployeesRequestBuilderGetQueryParameters]] = None) -> Optional[EmployeesGetResponse]:
        """
        Liefert die aktiven Mitarbeiter (inkl. Ansprechpartner) einer oder mehrerer Firmen.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: module, Rollen SYSTEMHAUS_ONE.Hinweise: Lizenz SAP_ONE erforderlich. companyNumber hat Vorrang und wird gegen TnsCompany.displayId gesucht (mehrere Treffer möglich); sonst companyId; bei 0 die eigene Firma. Nur aktive Mitarbeiter; listType je Eintrag (EMPLOYEE/CONTACT_PERSON/TECHNICIAN/FREELANCER ...).
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[EmployeesGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .employees_get_response import EmployeesGetResponse

        return await self.request_adapter.send_async(request_info, EmployeesGetResponse, None)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[EmployeesRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Liefert die aktiven Mitarbeiter (inkl. Ansprechpartner) einer oder mehrerer Firmen.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: module, Rollen SYSTEMHAUS_ONE.Hinweise: Lizenz SAP_ONE erforderlich. companyNumber hat Vorrang und wird gegen TnsCompany.displayId gesucht (mehrere Treffer möglich); sonst companyId; bei 0 die eigene Firma. Nur aktive Mitarbeiter; listType je Eintrag (EMPLOYEE/CONTACT_PERSON/TECHNICIAN/FREELANCER ...).
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> EmployeesRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: EmployeesRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return EmployeesRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def departments(self) -> DepartmentsRequestBuilder:
        """
        The departments property
        """
        from .departments.departments_request_builder import DepartmentsRequestBuilder

        return DepartmentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class EmployeesRequestBuilderGetQueryParameters():
        """
        Liefert die aktiven Mitarbeiter (inkl. Ansprechpartner) einer oder mehrerer Firmen.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: module, Rollen SYSTEMHAUS_ONE.Hinweise: Lizenz SAP_ONE erforderlich. companyNumber hat Vorrang und wird gegen TnsCompany.displayId gesucht (mehrere Treffer möglich); sonst companyId; bei 0 die eigene Firma. Nur aktive Mitarbeiter; listType je Eintrag (EMPLOYEE/CONTACT_PERSON/TECHNICIAN/FREELANCER ...).
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "company_id":
                return "companyId"
            if original_name == "company_number":
                return "companyNumber"
            return original_name
        
        # Firmen-ID; 0 = eigene Firma.
        company_id: Optional[int] = None

        # Kundennummer (TnsCompany.displayId); hat Vorrang vor companyId.
        company_number: Optional[str] = None

    
    @dataclass
    class EmployeesRequestBuilderGetRequestConfiguration(RequestConfiguration[EmployeesRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

