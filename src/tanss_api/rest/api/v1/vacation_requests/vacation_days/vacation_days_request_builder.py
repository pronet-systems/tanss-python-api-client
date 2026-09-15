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
    from .....models.tns_employee_vacation_days import TnsEmployeeVacationDays
    from .....models.vacation_days403_error import VacationDays403Error
    from .vacation_days_post_response import VacationDaysPostResponse
    from .vacation_days_put_response import VacationDaysPutResponse
    from .year.year_request_builder import YearRequestBuilder

class VacationDaysRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/vacationRequests/vacationDays
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new VacationDaysRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/vacationRequests/vacationDays", path_parameters)
    
    async def post(self,body: TnsEmployeeVacationDays, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[VacationDaysPostResponse]:
        """
        Legt vermutlich den Urlaubstage-Datensatz eines Mitarbeiters für ein Jahr an (POST-Variante von PUT /api/v1/vacationRequests/vacationDays). Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft. Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId. Keine Analyse vorhanden.
        param body: gives details on the vacation days of an employee
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[VacationDaysPostResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .vacation_days_post_response import VacationDaysPostResponse

        return await self.request_adapter.send_async(request_info, VacationDaysPostResponse, None)
    
    async def put(self,body: TnsEmployeeVacationDays, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[VacationDaysPutResponse]:
        """
        sets the available vacation days per year
        param body: gives details on the vacation days of an employee
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[VacationDaysPutResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        from .....models.vacation_days403_error import VacationDays403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": VacationDays403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .vacation_days_put_response import VacationDaysPutResponse

        return await self.request_adapter.send_async(request_info, VacationDaysPutResponse, error_mapping)
    
    def to_post_request_information(self,body: TnsEmployeeVacationDays, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Legt vermutlich den Urlaubstage-Datensatz eines Mitarbeiters für ein Jahr an (POST-Variante von PUT /api/v1/vacationRequests/vacationDays). Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft. Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId. Keine Analyse vorhanden.
        param body: gives details on the vacation days of an employee
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
    
    def to_put_request_information(self,body: TnsEmployeeVacationDays, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        sets the available vacation days per year
        param body: gives details on the vacation days of an employee
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
    
    def with_url(self,raw_url: str) -> VacationDaysRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: VacationDaysRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return VacationDaysRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def year(self) -> YearRequestBuilder:
        """
        The year property
        """
        from .year.year_request_builder import YearRequestBuilder

        return YearRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class VacationDaysRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class VacationDaysRequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

