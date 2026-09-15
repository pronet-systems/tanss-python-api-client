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
    from ....models.employee import Employee
    from .avatars.avatars_request_builder import AvatarsRequestBuilder
    from .birthdays.birthdays_request_builder import BirthdaysRequestBuilder
    from .departments.departments_request_builder import DepartmentsRequestBuilder
    from .employees_post_response import EmployeesPostResponse
    from .item.employees_item_request_builder import EmployeesItemRequestBuilder
    from .links.links_request_builder import LinksRequestBuilder
    from .not_wanted_technician_and_vacation_infos.not_wanted_technician_and_vacation_infos_request_builder import NotWantedTechnicianAndVacationInfosRequestBuilder
    from .own_state.own_state_request_builder import OwnStateRequestBuilder
    from .salutations.salutations_request_builder import SalutationsRequestBuilder
    from .technicians.technicians_request_builder import TechniciansRequestBuilder
    from .titles.titles_request_builder import TitlesRequestBuilder

class EmployeesRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/employees
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new EmployeesRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/employees", path_parameters)
    
    def by_id(self,id: int) -> EmployeesItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.v1.employees.item collection
        param id: Id of the employee to return.
        Returns: EmployeesItemRequestBuilder
        """
        if id is None:
            raise TypeError("id cannot be null.")
        from .item.employees_item_request_builder import EmployeesItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["id"] = id
        return EmployeesItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def post(self,body: Employee, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[EmployeesPostResponse]:
        """
        Legt vermutlich einen neuen Mitarbeiter an (Gegenstück zu PUT /api/v1/employees/{id}). Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft. Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId. Keine Analyse vorhanden; Body und Antwort aus dem Schema Employee abgeleitet.
        param body: object representing an employee
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[EmployeesPostResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .employees_post_response import EmployeesPostResponse

        return await self.request_adapter.send_async(request_info, EmployeesPostResponse, None)
    
    def to_post_request_information(self,body: Employee, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Legt vermutlich einen neuen Mitarbeiter an (Gegenstück zu PUT /api/v1/employees/{id}). Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft. Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId. Keine Analyse vorhanden; Body und Antwort aus dem Schema Employee abgeleitet.
        param body: object representing an employee
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.POST, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
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
    def avatars(self) -> AvatarsRequestBuilder:
        """
        The avatars property
        """
        from .avatars.avatars_request_builder import AvatarsRequestBuilder

        return AvatarsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def birthdays(self) -> BirthdaysRequestBuilder:
        """
        The birthdays property
        """
        from .birthdays.birthdays_request_builder import BirthdaysRequestBuilder

        return BirthdaysRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def departments(self) -> DepartmentsRequestBuilder:
        """
        The departments property
        """
        from .departments.departments_request_builder import DepartmentsRequestBuilder

        return DepartmentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def links(self) -> LinksRequestBuilder:
        """
        The links property
        """
        from .links.links_request_builder import LinksRequestBuilder

        return LinksRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def not_wanted_technician_and_vacation_infos(self) -> NotWantedTechnicianAndVacationInfosRequestBuilder:
        """
        The notWantedTechnicianAndVacationInfos property
        """
        from .not_wanted_technician_and_vacation_infos.not_wanted_technician_and_vacation_infos_request_builder import NotWantedTechnicianAndVacationInfosRequestBuilder

        return NotWantedTechnicianAndVacationInfosRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def own_state(self) -> OwnStateRequestBuilder:
        """
        The ownState property
        """
        from .own_state.own_state_request_builder import OwnStateRequestBuilder

        return OwnStateRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def salutations(self) -> SalutationsRequestBuilder:
        """
        The salutations property
        """
        from .salutations.salutations_request_builder import SalutationsRequestBuilder

        return SalutationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def technicians(self) -> TechniciansRequestBuilder:
        """
        The technicians property
        """
        from .technicians.technicians_request_builder import TechniciansRequestBuilder

        return TechniciansRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def titles(self) -> TitlesRequestBuilder:
        """
        The titles property
        """
        from .titles.titles_request_builder import TitlesRequestBuilder

        return TitlesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class EmployeesRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

