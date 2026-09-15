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
    from .......models.tns_mail import TnsMail
    from .condition_check_put_response import ConditionCheckPutResponse

class ConditionCheckRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/mailRobot/rules/{ruleId}/conditionCheck
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new ConditionCheckRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/mailRobot/rules/{ruleId}/conditionCheck", path_parameters)
    
    async def put(self,body: TnsMail, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[ConditionCheckPutResponse]:
        """
        Prüft nur die Bedingungen einer Regel gegen eine JSON-Mail (keine Aktionen). Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft. Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId. Rechte: licModule(MAILROBOT), companyAccess(-1) (eigene Firma), bet.MANAGE_MAIL_ROBOT_RULES. Hinweise: 404 'Rule was not found!'. Keine Ticket-Erkennung vorab, daher liefern Bedingungen, die auf erkanntes Ticket/Firma angewiesen sind, evtl. false. Antwort-Status FOUND.
        param body: describes a mail object
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ConditionCheckPutResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .condition_check_put_response import ConditionCheckPutResponse

        return await self.request_adapter.send_async(request_info, ConditionCheckPutResponse, None)
    
    def to_put_request_information(self,body: TnsMail, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Prüft nur die Bedingungen einer Regel gegen eine JSON-Mail (keine Aktionen). Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft. Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId. Rechte: licModule(MAILROBOT), companyAccess(-1) (eigene Firma), bet.MANAGE_MAIL_ROBOT_RULES. Hinweise: 404 'Rule was not found!'. Keine Ticket-Erkennung vorab, daher liefern Bedingungen, die auf erkanntes Ticket/Firma angewiesen sind, evtl. false. Antwort-Status FOUND.
        param body: describes a mail object
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
    
    def with_url(self,raw_url: str) -> ConditionCheckRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: ConditionCheckRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return ConditionCheckRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class ConditionCheckRequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

