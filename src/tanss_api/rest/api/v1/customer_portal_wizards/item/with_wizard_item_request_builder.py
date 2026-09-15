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
    from .....models.tns_customer_portal_wizard import TnsCustomerPortalWizard
    from .with_wizard_delete_response import WithWizardDeleteResponse
    from .with_wizard_get_response import WithWizardGetResponse
    from .with_wizard_put_response import WithWizardPutResponse

class WithWizardItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/customerPortalWizards/{wizardId}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new WithWizardItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/customerPortalWizards/{wizardId}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[WithWizardDeleteResponse]:
        """
        Löscht einen Kundenportal-Wizard. Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft. Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId. Rechte: Benutzertyp TECHNICAN, COMPANY_ADMIN, RESTRICTED_USER oder FREELANCER. Hinweise: Standard-CRUD, 404 ENTITY_NOT_FOUND wenn nicht vorhanden. Status DELETED ohne content.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[WithWizardDeleteResponse]
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .with_wizard_delete_response import WithWizardDeleteResponse

        return await self.request_adapter.send_async(request_info, WithWizardDeleteResponse, None)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[WithWizardGetResponse]:
        """
        Liefert einen Kundenportal-Wizard inkl. Widget-Definition. Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft. Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId. Rechte: Benutzertyp TECHNICAN, COMPANY_ADMIN, RESTRICTED_USER oder FREELANCER. Hinweise: 404 OBJECT_NOT_FOUND wenn nicht vorhanden. Keine Filterstrategie.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[WithWizardGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .with_wizard_get_response import WithWizardGetResponse

        return await self.request_adapter.send_async(request_info, WithWizardGetResponse, None)
    
    async def put(self,body: TnsCustomerPortalWizard, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[WithWizardPutResponse]:
        """
        Aktualisiert einen Kundenportal-Wizard (Name/Widget-Struktur) per Teil-Update. Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft. Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId. Rechte: Benutzertyp TECHNICAN, COMPANY_ADMIN, RESTRICTED_USER oder FREELANCER. Hinweise: Merge nur der gesendeten Felder; id wird ignoriert. Vor dem Speichern werden fehlende widgetId als UUID gesetzt (rekursiv) und fehlende nextWidgetId auf das Folge-Widget; Actions ohne type führen zu ACTION_TYPE_CAN_NOT_BE_NULL. 404 ENTITY_NOT_FOUND. Status UPDATED.
        param body: Kundenportal-Wizard inkl. Widget-Definition
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[WithWizardPutResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .with_wizard_put_response import WithWizardPutResponse

        return await self.request_adapter.send_async(request_info, WithWizardPutResponse, None)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Löscht einen Kundenportal-Wizard. Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft. Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId. Rechte: Benutzertyp TECHNICAN, COMPANY_ADMIN, RESTRICTED_USER oder FREELANCER. Hinweise: Standard-CRUD, 404 ENTITY_NOT_FOUND wenn nicht vorhanden. Status DELETED ohne content.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Liefert einen Kundenportal-Wizard inkl. Widget-Definition. Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft. Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId. Rechte: Benutzertyp TECHNICAN, COMPANY_ADMIN, RESTRICTED_USER oder FREELANCER. Hinweise: 404 OBJECT_NOT_FOUND wenn nicht vorhanden. Keine Filterstrategie.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_put_request_information(self,body: TnsCustomerPortalWizard, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Aktualisiert einen Kundenportal-Wizard (Name/Widget-Struktur) per Teil-Update. Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft. Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId. Rechte: Benutzertyp TECHNICAN, COMPANY_ADMIN, RESTRICTED_USER oder FREELANCER. Hinweise: Merge nur der gesendeten Felder; id wird ignoriert. Vor dem Speichern werden fehlende widgetId als UUID gesetzt (rekursiv) und fehlende nextWidgetId auf das Folge-Widget; Actions ohne type führen zu ACTION_TYPE_CAN_NOT_BE_NULL. 404 ENTITY_NOT_FOUND. Status UPDATED.
        param body: Kundenportal-Wizard inkl. Widget-Definition
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
    
    def with_url(self,raw_url: str) -> WithWizardItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: WithWizardItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return WithWizardItemRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class WithWizardItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class WithWizardItemRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class WithWizardItemRequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

