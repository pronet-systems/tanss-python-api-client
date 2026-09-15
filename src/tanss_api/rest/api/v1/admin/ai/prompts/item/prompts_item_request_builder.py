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
    from .prompts_delete_response import PromptsDeleteResponse
    from .prompts_get_response import PromptsGetResponse
    from .prompts_put_request_body import PromptsPutRequestBody
    from .prompts_put_response import PromptsPutResponse

class PromptsItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/admin/ai/prompts/{id}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new PromptsItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/admin/ai/prompts/{id}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[PromptsDeleteResponse]:
        """
        Löscht einen KI-Prompt und schließt die Rang-Lücke innerhalb der Kategorie.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId.Rechte: Lizenzmodul ACTIVE_SUBSCRIPTION; interner Benutzer; Recht EDIT_AI_SETTINGS.Hinweise: ENTITY_NOT_FOUND bei unbekannter ID. Nach dem Löschen werden die rank-Werte der übrigen Prompts derselben Kategorie um 1 verringert. Antwort-Status DELETED.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[PromptsDeleteResponse]
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .prompts_delete_response import PromptsDeleteResponse

        return await self.request_adapter.send_async(request_info, PromptsDeleteResponse, None)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[PromptsGetResponse]:
        """
        Liefert einen einzelnen KI-Prompt inkl. Zuordnungen.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId.Rechte: Lizenzmodul ACTIVE_SUBSCRIPTION; interner Benutzer (EDIT_AI_SETTINGS wird hier NICHT geprüft).Hinweise: OBJECT_NOT_FOUND bei unbekannter ID. linkedEntities werden befüllt. Antwort-Status FOUND.
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
    
    async def put(self,body: PromptsPutRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[PromptsPutResponse]:
        """
        Aktualisiert einen KI-Prompt (Teil-Update per JSON-Merge), inkl. Kategoriewechsel und relativer Rang-Verschiebung.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId.Rechte: Lizenzmodul ACTIVE_SUBSCRIPTION; interner Benutzer; Recht EDIT_AI_SETTINGS.Hinweise: Nur gesendete Felder werden geändert; Keys id und rank werden ignoriert. configId-Änderung: LLM_CONFIG_NOT_FOUND wenn unbekannt. categoryId-Änderung: Prompt bekommt in neuer Kategorie rank=max+1, alte Kategorie wird nachgerückt; categoryId 0/null = ohne Kategorie. adjustRank verschiebt den Rang relativ innerhalb der Kategorie (auf 1..n begrenzt) und wird danach auf null gesetzt. Zuordnungen werden neu gespeichert. Antwort-Status UPDATED.
        param body: Zu ändernde Felder des Prompts (JSON-Merge)
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[PromptsPutResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .prompts_put_response import PromptsPutResponse

        return await self.request_adapter.send_async(request_info, PromptsPutResponse, None)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Löscht einen KI-Prompt und schließt die Rang-Lücke innerhalb der Kategorie.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId.Rechte: Lizenzmodul ACTIVE_SUBSCRIPTION; interner Benutzer; Recht EDIT_AI_SETTINGS.Hinweise: ENTITY_NOT_FOUND bei unbekannter ID. Nach dem Löschen werden die rank-Werte der übrigen Prompts derselben Kategorie um 1 verringert. Antwort-Status DELETED.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Liefert einen einzelnen KI-Prompt inkl. Zuordnungen.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId.Rechte: Lizenzmodul ACTIVE_SUBSCRIPTION; interner Benutzer (EDIT_AI_SETTINGS wird hier NICHT geprüft).Hinweise: OBJECT_NOT_FOUND bei unbekannter ID. linkedEntities werden befüllt. Antwort-Status FOUND.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_put_request_information(self,body: PromptsPutRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Aktualisiert einen KI-Prompt (Teil-Update per JSON-Merge), inkl. Kategoriewechsel und relativer Rang-Verschiebung.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId.Rechte: Lizenzmodul ACTIVE_SUBSCRIPTION; interner Benutzer; Recht EDIT_AI_SETTINGS.Hinweise: Nur gesendete Felder werden geändert; Keys id und rank werden ignoriert. configId-Änderung: LLM_CONFIG_NOT_FOUND wenn unbekannt. categoryId-Änderung: Prompt bekommt in neuer Kategorie rank=max+1, alte Kategorie wird nachgerückt; categoryId 0/null = ohne Kategorie. adjustRank verschiebt den Rang relativ innerhalb der Kategorie (auf 1..n begrenzt) und wird danach auf null gesetzt. Zuordnungen werden neu gespeichert. Antwort-Status UPDATED.
        param body: Zu ändernde Felder des Prompts (JSON-Merge)
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
    
    def with_url(self,raw_url: str) -> PromptsItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: PromptsItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return PromptsItemRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class PromptsItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class PromptsItemRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class PromptsItemRequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

