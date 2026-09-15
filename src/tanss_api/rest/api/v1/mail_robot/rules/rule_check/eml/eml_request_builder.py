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
    from .eml_put_response import EmlPutResponse

class EmlRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/mailRobot/rules/ruleCheck/eml
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new EmlRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/mailRobot/rules/ruleCheck/eml{?testMode*}", path_parameters)
    
    async def put(self,body: str, request_configuration: Optional[RequestConfiguration[EmlRequestBuilderPutQueryParameters]] = None) -> Optional[EmlPutResponse]:
        """
        Wie /api/v1/mailRobot/rules/ruleCheck, aber die Mail wird als roher EML-String übergeben und serverseitig geparst. Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft. Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId. Rechte: licModule(MAILROBOT), companyAccess(-1) (eigene Firma), bet.MANAGE_MAIL_ROBOT_RULES. Hinweise: Query testMode (default true); bei false ist content null. mailSettingsId aus dem geparsten Objekt (meist null, dann 0). Gleiche Vorbehalte zur realen Ausführung von Aktionen wie bei /ruleCheck.
        param body: Roher EML-Text
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[EmlPutResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .eml_put_response import EmlPutResponse

        return await self.request_adapter.send_async(request_info, EmlPutResponse, None)
    
    def to_put_request_information(self,body: str, request_configuration: Optional[RequestConfiguration[EmlRequestBuilderPutQueryParameters]] = None) -> RequestInformation:
        """
        Wie /api/v1/mailRobot/rules/ruleCheck, aber die Mail wird als roher EML-String übergeben und serverseitig geparst. Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft. Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId. Rechte: licModule(MAILROBOT), companyAccess(-1) (eigene Firma), bet.MANAGE_MAIL_ROBOT_RULES. Hinweise: Query testMode (default true); bei false ist content null. mailSettingsId aus dem geparsten Objekt (meist null, dann 0). Gleiche Vorbehalte zur realen Ausführung von Aktionen wie bei /ruleCheck.
        param body: Roher EML-Text
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.PUT, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_scalar(self.request_adapter, "text/plain", body)
        return request_info
    
    def with_url(self,raw_url: str) -> EmlRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: EmlRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return EmlRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class EmlRequestBuilderPutQueryParameters():
        """
        Wie /api/v1/mailRobot/rules/ruleCheck, aber die Mail wird als roher EML-String übergeben und serverseitig geparst. Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft. Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId. Rechte: licModule(MAILROBOT), companyAccess(-1) (eigene Firma), bet.MANAGE_MAIL_ROBOT_RULES. Hinweise: Query testMode (default true); bei false ist content null. mailSettingsId aus dem geparsten Objekt (meist null, dann 0). Gleiche Vorbehalte zur realen Ausführung von Aktionen wie bei /ruleCheck.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "test_mode":
                return "testMode"
            return original_name
        
        test_mode: Optional[bool] = None

    
    @dataclass
    class EmlRequestBuilderPutRequestConfiguration(RequestConfiguration[EmlRequestBuilderPutQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

