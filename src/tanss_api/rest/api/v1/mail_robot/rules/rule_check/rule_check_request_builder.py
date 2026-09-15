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
    from ......models.tns_mail import TnsMail
    from .eml.eml_request_builder import EmlRequestBuilder
    from .item.with_rule_item_request_builder import WithRuleItemRequestBuilder
    from .rule_check_put_response import RuleCheckPutResponse

class RuleCheckRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/mailRobot/rules/ruleCheck
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new RuleCheckRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/mailRobot/rules/ruleCheck{?testMode*}", path_parameters)
    
    def by_rule_id(self,rule_id: int) -> WithRuleItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.v1.mailRobot.rules.ruleCheck.item collection
        param rule_id: Unique identifier of the item
        Returns: WithRuleItemRequestBuilder
        """
        if rule_id is None:
            raise TypeError("rule_id cannot be null.")
        from .item.with_rule_item_request_builder import WithRuleItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["ruleId"] = rule_id
        return WithRuleItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def put(self,body: TnsMail, request_configuration: Optional[RequestConfiguration[RuleCheckRequestBuilderPutQueryParameters]] = None) -> Optional[RuleCheckPutResponse]:
        """
        Lässt den kompletten Mailroboter-Regellauf (Ticket-Erkennung + alle Regeln des Postfachs) für eine als JSON übergebene Mail laufen und liefert das Ergebnis-Protokoll. Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft. Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId. Rechte: licModule(MAILROBOT), companyAccess(-1) (eigene Firma), bet.MANAGE_MAIL_ROBOT_RULES. Hinweise: Query testMode (default true): nur dann wird der Ergebnis-Collector angelegt und Debug-Log geschrieben; bei false ist content null. Ob Aktionen (Ticket anlegen, Mail senden ...) im testMode nur simuliert werden, wurde nicht verifiziert - Aktionen werden evtl. real ausgeführt. mailSettingsId der Mail bestimmt die geprüften Regeln (null=0). DEFAULT-Regeln nur ohne erkanntes Ticket, EXECUTE_AFTER_TICKET_RECOGNITION nur mit. Die Feldnamen des Ergebnisobjekts sind nicht dokumentiert.
        param body: describes a mail object
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[RuleCheckPutResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .rule_check_put_response import RuleCheckPutResponse

        return await self.request_adapter.send_async(request_info, RuleCheckPutResponse, None)
    
    def to_put_request_information(self,body: TnsMail, request_configuration: Optional[RequestConfiguration[RuleCheckRequestBuilderPutQueryParameters]] = None) -> RequestInformation:
        """
        Lässt den kompletten Mailroboter-Regellauf (Ticket-Erkennung + alle Regeln des Postfachs) für eine als JSON übergebene Mail laufen und liefert das Ergebnis-Protokoll. Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft. Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId. Rechte: licModule(MAILROBOT), companyAccess(-1) (eigene Firma), bet.MANAGE_MAIL_ROBOT_RULES. Hinweise: Query testMode (default true): nur dann wird der Ergebnis-Collector angelegt und Debug-Log geschrieben; bei false ist content null. Ob Aktionen (Ticket anlegen, Mail senden ...) im testMode nur simuliert werden, wurde nicht verifiziert - Aktionen werden evtl. real ausgeführt. mailSettingsId der Mail bestimmt die geprüften Regeln (null=0). DEFAULT-Regeln nur ohne erkanntes Ticket, EXECUTE_AFTER_TICKET_RECOGNITION nur mit. Die Feldnamen des Ergebnisobjekts sind nicht dokumentiert.
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
    
    def with_url(self,raw_url: str) -> RuleCheckRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: RuleCheckRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return RuleCheckRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def eml(self) -> EmlRequestBuilder:
        """
        The eml property
        """
        from .eml.eml_request_builder import EmlRequestBuilder

        return EmlRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class RuleCheckRequestBuilderPutQueryParameters():
        """
        Lässt den kompletten Mailroboter-Regellauf (Ticket-Erkennung + alle Regeln des Postfachs) für eine als JSON übergebene Mail laufen und liefert das Ergebnis-Protokoll. Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft. Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId. Rechte: licModule(MAILROBOT), companyAccess(-1) (eigene Firma), bet.MANAGE_MAIL_ROBOT_RULES. Hinweise: Query testMode (default true): nur dann wird der Ergebnis-Collector angelegt und Debug-Log geschrieben; bei false ist content null. Ob Aktionen (Ticket anlegen, Mail senden ...) im testMode nur simuliert werden, wurde nicht verifiziert - Aktionen werden evtl. real ausgeführt. mailSettingsId der Mail bestimmt die geprüften Regeln (null=0). DEFAULT-Regeln nur ohne erkanntes Ticket, EXECUTE_AFTER_TICKET_RECOGNITION nur mit. Die Feldnamen des Ergebnisobjekts sind nicht dokumentiert.
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
    class RuleCheckRequestBuilderPutRequestConfiguration(RequestConfiguration[RuleCheckRequestBuilderPutQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

