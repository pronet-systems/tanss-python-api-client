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
    from ......models.tns_l_l_m_prompt import TnsLLMPrompt
    from .item.prompts_item_request_builder import PromptsItemRequestBuilder
    from .prompts_get_response import PromptsGetResponse
    from .prompts_post_response import PromptsPostResponse
    from .properties.properties_request_builder import PropertiesRequestBuilder

class PromptsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/admin/ai/prompts
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new PromptsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/admin/ai/prompts", path_parameters)
    
    def by_id(self,id: int) -> PromptsItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.v1.admin.ai.prompts.item collection
        param id: ID des Prompts
        Returns: PromptsItemRequestBuilder
        """
        if id is None:
            raise TypeError("id cannot be null.")
        from .item.prompts_item_request_builder import PromptsItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["id"] = id
        return PromptsItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[PromptsGetResponse]:
        """
        Liefert alle KI-Prompts (Admin-Bereich) inkl. Zuordnungen (Mitarbeiter, Abteilungen, Textbaustein-Typen).Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId.Rechte: Lizenzmodul ACTIVE_SUBSCRIPTION; interner Benutzer; Recht EDIT_AI_SETTINGS.Hinweise: Zuordnungen (employees/employeeDepartments/textModuleTypes) werden nachgeladen; linkedEntities werden in meta befüllt. Antwort-Status FOUND.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[PromptsGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .prompts_get_response import PromptsGetResponse

        return await self.request_adapter.send_async(request_info, PromptsGetResponse, None)
    
    async def post(self,body: TnsLLMPrompt, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[PromptsPostResponse]:
        """
        Legt einen neuen KI-Prompt an; Rang wird automatisch als max+1 innerhalb der Kategorie gesetzt.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId.Rechte: Lizenzmodul ACTIVE_SUBSCRIPTION; interner Benutzer; Recht EDIT_AI_SETTINGS.Hinweise: id/rank im Body werden ignoriert. configId ist Pflicht (LLM_CONFIG_NOT_FOUND wenn unbekannt), categoryId muss existieren, wenn gesetzt (ENTITY_NOT_FOUND). Zuordnungen werden nach dem Speichern separat persistiert. instruction darf den Platzhalter {text} enthalten. Antwort-Status CREATED.
        param body: KI-Prompt inkl. Zuordnungen
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[PromptsPostResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .prompts_post_response import PromptsPostResponse

        return await self.request_adapter.send_async(request_info, PromptsPostResponse, None)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Liefert alle KI-Prompts (Admin-Bereich) inkl. Zuordnungen (Mitarbeiter, Abteilungen, Textbaustein-Typen).Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId.Rechte: Lizenzmodul ACTIVE_SUBSCRIPTION; interner Benutzer; Recht EDIT_AI_SETTINGS.Hinweise: Zuordnungen (employees/employeeDepartments/textModuleTypes) werden nachgeladen; linkedEntities werden in meta befüllt. Antwort-Status FOUND.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: TnsLLMPrompt, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Legt einen neuen KI-Prompt an; Rang wird automatisch als max+1 innerhalb der Kategorie gesetzt.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId.Rechte: Lizenzmodul ACTIVE_SUBSCRIPTION; interner Benutzer; Recht EDIT_AI_SETTINGS.Hinweise: id/rank im Body werden ignoriert. configId ist Pflicht (LLM_CONFIG_NOT_FOUND wenn unbekannt), categoryId muss existieren, wenn gesetzt (ENTITY_NOT_FOUND). Zuordnungen werden nach dem Speichern separat persistiert. instruction darf den Platzhalter {text} enthalten. Antwort-Status CREATED.
        param body: KI-Prompt inkl. Zuordnungen
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
    
    def with_url(self,raw_url: str) -> PromptsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: PromptsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return PromptsRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def properties(self) -> PropertiesRequestBuilder:
        """
        The properties property
        """
        from .properties.properties_request_builder import PropertiesRequestBuilder

        return PropertiesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class PromptsRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class PromptsRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

