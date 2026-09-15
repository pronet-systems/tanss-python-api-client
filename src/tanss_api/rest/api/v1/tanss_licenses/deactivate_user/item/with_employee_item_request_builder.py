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
    from .with_employee_put_response import WithEmployeePutResponse

class WithEmployeeItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/tanssLicenses/deactivateUser/{employeeId}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new WithEmployeeItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/tanssLicenses/deactivateUser/{employeeId}", path_parameters)
    
    async def put(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[WithEmployeePutResponse]:
        """
        Deaktiviert einen Mitarbeiter, um eine Lizenzüberschreitung (User- bzw. Freelancer-Lizenzen) zu beheben.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId.Rechte: Zugriff auf eigene Systemhaus-Firma.Hinweise: Kein Body. Ergebnis ist ein Status-String, kein Fehler: eigener User -> CANT_DEACTIVATE_OWN_USER; employeeId 0 -> CANT_DEACTIVATE_THIS_USER; nur bei Lizenzfehler NUMBER_OF_USER_LICENSES_EXCEEDED bzw. NUMBER_OF_FREELANCER_LICENSES_EXCEEDED wird active=false gesetzt und die Lizenz neu geladen (USER_DEACTIVATED); sonst NO_LICENSE_ERROR_PRESENT. meta FOUND.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[WithEmployeePutResponse]
        """
        request_info = self.to_put_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .with_employee_put_response import WithEmployeePutResponse

        return await self.request_adapter.send_async(request_info, WithEmployeePutResponse, None)
    
    def to_put_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Deaktiviert einen Mitarbeiter, um eine Lizenzüberschreitung (User- bzw. Freelancer-Lizenzen) zu beheben.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId.Rechte: Zugriff auf eigene Systemhaus-Firma.Hinweise: Kein Body. Ergebnis ist ein Status-String, kein Fehler: eigener User -> CANT_DEACTIVATE_OWN_USER; employeeId 0 -> CANT_DEACTIVATE_THIS_USER; nur bei Lizenzfehler NUMBER_OF_USER_LICENSES_EXCEEDED bzw. NUMBER_OF_FREELANCER_LICENSES_EXCEEDED wird active=false gesetzt und die Lizenz neu geladen (USER_DEACTIVATED); sonst NO_LICENSE_ERROR_PRESENT. meta FOUND.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.PUT, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> WithEmployeeItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: WithEmployeeItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return WithEmployeeItemRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class WithEmployeeItemRequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

