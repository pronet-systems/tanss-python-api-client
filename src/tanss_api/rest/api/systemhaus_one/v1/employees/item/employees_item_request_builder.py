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
    from ......models.employee import Employee
    from .departments.departments_request_builder import DepartmentsRequestBuilder
    from .employees_get_response import EmployeesGetResponse
    from .employees_put_response import EmployeesPutResponse

class EmployeesItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/systemhaus_one/v1/employees/{id}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new EmployeesItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/systemhaus_one/v1/employees/{id}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[EmployeesGetResponse]:
        """
        Liefert einen Mitarbeiter per ID (delegiert an offiziellen Handler GET /api/v1/employees/{id}).Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: module, Rollen SYSTEMHAUS_ONE.Rechte: ACCESS_INACTIVE_EMPLOYEES (nur bei inaktivem Mitarbeiter), Firmenzugriff auf eine Firma des Mitarbeiters (sonst COMPANY_ADMIN).Hinweise: Keine SAP_ONE-Lizenzprüfung. Eigener Benutzer immer erlaubt; ohne Benutzerkontext (userId 0) keine Prüfung. Nicht gefunden -> OBJECT_NOT_FOUND.
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
    
    async def put(self,body: Employee, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[EmployeesPutResponse]:
        """
        Aktualisiert einen Mitarbeiter per JSON-Merge (delegiert an offiziellen Handler PUT /api/v1/employees/{id}).Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: module, Rollen SYSTEMHAUS_ONE.Rechte: EMPLOYEE_ADMINISTRATION, ACCESS_INACTIVE_EMPLOYEES (bei inaktivem Mitarbeiter), Firmenzugriff, EMPLOYEE_ADMINISTRATION_OF_OWN_COMPANY (bei Techniker/eigener Firma).Hinweise: Keine SAP_ONE-Lizenzprüfung. Teilobjekt; "id" wird ignoriert. Bearbeitung des eigenen Benutzers ohne Rechteprüfung.
        param body: object representing an employee
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[EmployeesPutResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .employees_put_response import EmployeesPutResponse

        return await self.request_adapter.send_async(request_info, EmployeesPutResponse, None)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Liefert einen Mitarbeiter per ID (delegiert an offiziellen Handler GET /api/v1/employees/{id}).Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: module, Rollen SYSTEMHAUS_ONE.Rechte: ACCESS_INACTIVE_EMPLOYEES (nur bei inaktivem Mitarbeiter), Firmenzugriff auf eine Firma des Mitarbeiters (sonst COMPANY_ADMIN).Hinweise: Keine SAP_ONE-Lizenzprüfung. Eigener Benutzer immer erlaubt; ohne Benutzerkontext (userId 0) keine Prüfung. Nicht gefunden -> OBJECT_NOT_FOUND.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_put_request_information(self,body: Employee, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Aktualisiert einen Mitarbeiter per JSON-Merge (delegiert an offiziellen Handler PUT /api/v1/employees/{id}).Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: module, Rollen SYSTEMHAUS_ONE.Rechte: EMPLOYEE_ADMINISTRATION, ACCESS_INACTIVE_EMPLOYEES (bei inaktivem Mitarbeiter), Firmenzugriff, EMPLOYEE_ADMINISTRATION_OF_OWN_COMPANY (bei Techniker/eigener Firma).Hinweise: Keine SAP_ONE-Lizenzprüfung. Teilobjekt; "id" wird ignoriert. Bearbeitung des eigenen Benutzers ohne Rechteprüfung.
        param body: object representing an employee
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
    
    def with_url(self,raw_url: str) -> EmployeesItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: EmployeesItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return EmployeesItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def departments(self) -> DepartmentsRequestBuilder:
        """
        The departments property
        """
        from .departments.departments_request_builder import DepartmentsRequestBuilder

        return DepartmentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class EmployeesItemRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class EmployeesItemRequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

