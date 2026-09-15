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
    from .......models.tns_customer_portal_wizard import TnsCustomerPortalWizard
    from .complete_post_response import CompletePostResponse

class CompleteRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/customerPortalWizards/frontend/{wizardId}/complete
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new CompleteRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/customerPortalWizards/frontend/{wizardId}/complete", path_parameters)
    
    async def post(self,body: TnsCustomerPortalWizard, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[CompletePostResponse]:
        """
        Schließt einen Kundenportal-Wizard ab: Body-Auswahlen werden in den gespeicherten Wizard gemergt, Widgets validiert und aus den Widget-Actions ein Ticket erzeugt. Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft. Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId. Hinweise: Kein Rechte-Check sichtbar. Effektiv gelesen wird content.widgets[{widgetId, selections, selected}]. 404 DATA_NOT_FOUND wenn Wizard fehlt. Validierung je Widget-Typ; Fehler als Exception mit Liste TnsCustomerPortalWizardExceptionItem. Ticket-Erzeugung an Action-Strategien delegiert (CREATE_TICKET, CREATE_SUPPORT, TICKET_PRIORITY, TICKET_DUE_DATE, TICKET_DEADLINE_DATE, ADD_CHECKLIST, TAG, ADD_COMMENT, SEND_MAIL). Status CREATED.
        param body: Kundenportal-Wizard inkl. Widget-Definition
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[CompletePostResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .complete_post_response import CompletePostResponse

        return await self.request_adapter.send_async(request_info, CompletePostResponse, None)
    
    def to_post_request_information(self,body: TnsCustomerPortalWizard, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Schließt einen Kundenportal-Wizard ab: Body-Auswahlen werden in den gespeicherten Wizard gemergt, Widgets validiert und aus den Widget-Actions ein Ticket erzeugt. Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft. Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId. Hinweise: Kein Rechte-Check sichtbar. Effektiv gelesen wird content.widgets[{widgetId, selections, selected}]. 404 DATA_NOT_FOUND wenn Wizard fehlt. Validierung je Widget-Typ; Fehler als Exception mit Liste TnsCustomerPortalWizardExceptionItem. Ticket-Erzeugung an Action-Strategien delegiert (CREATE_TICKET, CREATE_SUPPORT, TICKET_PRIORITY, TICKET_DUE_DATE, TICKET_DEADLINE_DATE, ADD_CHECKLIST, TAG, ADD_COMMENT, SEND_MAIL). Status CREATED.
        param body: Kundenportal-Wizard inkl. Widget-Definition
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
    
    def with_url(self,raw_url: str) -> CompleteRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: CompleteRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return CompleteRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class CompleteRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

