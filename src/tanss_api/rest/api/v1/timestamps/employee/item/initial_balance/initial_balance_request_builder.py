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
    from .......models.initial_balance403_error import InitialBalance403Error
    from .......models.timestamp_day_closing_only_balance import TimestampDayClosingOnlyBalance
    from .initial_balance_get_response import InitialBalanceGetResponse
    from .initial_balance_post_response import InitialBalancePostResponse

class InitialBalanceRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/timestamps/employee/{employeeId}/initialBalance
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new InitialBalanceRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/timestamps/employee/{employeeId}/initialBalance", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[InitialBalanceGetResponse]:
        """
        Liefert den Anfangssaldo (Initial-Balance-Tagesabschluss) der Zeiterfassung eines Mitarbeiters.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId.Rechte: Lizenzmodul TIMESTAMP; TIMESTAMP_MODULE_ACCESS oder TIMESTAMP_STATISTICS_EMPLOYEES_OF_OWN_DEPARTMENTS; Mitarbeiter-Usertyp plus TIMESTAMP_STATISTICS_EMPLOYEES_OF_OWN_DEPARTMENTS plus TIMESTAMP_INITIAL_BALANCE_CONFIG (sonst FORBIDDEN CANT_EDIT_TIMESTAMP_OF_USER).Hinweise: Existiert kein Eintrag, wird ein leeres Objekt mit employeeId und balance=0 zurückgegeben (kein 404). Filter SMALL. Mitarbeiter als Linked Entity. meta FOUND.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[InitialBalanceGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .initial_balance_get_response import InitialBalanceGetResponse

        return await self.request_adapter.send_async(request_info, InitialBalanceGetResponse, None)
    
    async def post(self,body: TimestampDayClosingOnlyBalance, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[InitialBalancePostResponse]:
        """
        When transferring balances from a foreign system, the balance could have an initialvalue. This can be set by using this call.Requires the permission to change other employees timestamps directly
        param body: Object containing the initial balance (in minutes)
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[InitialBalancePostResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from .......models.initial_balance403_error import InitialBalance403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": InitialBalance403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .initial_balance_post_response import InitialBalancePostResponse

        return await self.request_adapter.send_async(request_info, InitialBalancePostResponse, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Liefert den Anfangssaldo (Initial-Balance-Tagesabschluss) der Zeiterfassung eines Mitarbeiters.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId.Rechte: Lizenzmodul TIMESTAMP; TIMESTAMP_MODULE_ACCESS oder TIMESTAMP_STATISTICS_EMPLOYEES_OF_OWN_DEPARTMENTS; Mitarbeiter-Usertyp plus TIMESTAMP_STATISTICS_EMPLOYEES_OF_OWN_DEPARTMENTS plus TIMESTAMP_INITIAL_BALANCE_CONFIG (sonst FORBIDDEN CANT_EDIT_TIMESTAMP_OF_USER).Hinweise: Existiert kein Eintrag, wird ein leeres Objekt mit employeeId und balance=0 zurückgegeben (kein 404). Filter SMALL. Mitarbeiter als Linked Entity. meta FOUND.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: TimestampDayClosingOnlyBalance, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        When transferring balances from a foreign system, the balance could have an initialvalue. This can be set by using this call.Requires the permission to change other employees timestamps directly
        param body: Object containing the initial balance (in minutes)
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
    
    def with_url(self,raw_url: str) -> InitialBalanceRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: InitialBalanceRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return InitialBalanceRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class InitialBalanceRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class InitialBalanceRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

