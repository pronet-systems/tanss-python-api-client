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
    from .generate_post_response import GeneratePostResponse

class GenerateRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/tickets/{-id}/cloud/generate
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new GenerateRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/tickets/{%2Did}/cloud/generate?employeeIds={employeeIds}", path_parameters)
    
    async def post(self,request_configuration: Optional[RequestConfiguration[GenerateRequestBuilderPostQueryParameters]] = None) -> Optional[GeneratePostResponse]:
        """
        Erzeugt ein Cloud-Upload-Token (UUID) für ein Ticket und benachrichtigt die angegebenen Mitarbeiter (Cloud-Upload-Link).Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId.Hinweise: Query employeeIds = kommaseparierte Mitarbeiter-IDs (Pflicht). Fehler: EMPLOYEE_IDS_ARE_NULL, EMPLOYEE_ID_IS_NOT_A_NUMBER, TICKET_NOT_EXISTS (404), NO_EMPLOYEES_GIVEN, DUPLICATED_EMPLOYEE, EMPLOYEE_NOT_FOUND, EMPLOYEE_HAS_NO_EMAIL_ADDRESS. Das erzeugte Token wird nicht zurückgegeben. Kein Rechte-Check im Controller.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[GeneratePostResponse]
        """
        request_info = self.to_post_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .generate_post_response import GeneratePostResponse

        return await self.request_adapter.send_async(request_info, GeneratePostResponse, None)
    
    def to_post_request_information(self,request_configuration: Optional[RequestConfiguration[GenerateRequestBuilderPostQueryParameters]] = None) -> RequestInformation:
        """
        Erzeugt ein Cloud-Upload-Token (UUID) für ein Ticket und benachrichtigt die angegebenen Mitarbeiter (Cloud-Upload-Link).Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId.Hinweise: Query employeeIds = kommaseparierte Mitarbeiter-IDs (Pflicht). Fehler: EMPLOYEE_IDS_ARE_NULL, EMPLOYEE_ID_IS_NOT_A_NUMBER, TICKET_NOT_EXISTS (404), NO_EMPLOYEES_GIVEN, DUPLICATED_EMPLOYEE, EMPLOYEE_NOT_FOUND, EMPLOYEE_HAS_NO_EMAIL_ADDRESS. Das erzeugte Token wird nicht zurückgegeben. Kein Rechte-Check im Controller.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.POST, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> GenerateRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: GenerateRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return GenerateRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class GenerateRequestBuilderPostQueryParameters():
        """
        Erzeugt ein Cloud-Upload-Token (UUID) für ein Ticket und benachrichtigt die angegebenen Mitarbeiter (Cloud-Upload-Link).Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId.Hinweise: Query employeeIds = kommaseparierte Mitarbeiter-IDs (Pflicht). Fehler: EMPLOYEE_IDS_ARE_NULL, EMPLOYEE_ID_IS_NOT_A_NUMBER, TICKET_NOT_EXISTS (404), NO_EMPLOYEES_GIVEN, DUPLICATED_EMPLOYEE, EMPLOYEE_NOT_FOUND, EMPLOYEE_HAS_NO_EMAIL_ADDRESS. Das erzeugte Token wird nicht zurückgegeben. Kein Rechte-Check im Controller.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "employee_ids":
                return "employeeIds"
            return original_name
        
        # Kommaseparierte Mitarbeiter-IDs, die den Upload-Link erhalten
        employee_ids: Optional[str] = None

    
    @dataclass
    class GenerateRequestBuilderPostRequestConfiguration(RequestConfiguration[GenerateRequestBuilderPostQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

