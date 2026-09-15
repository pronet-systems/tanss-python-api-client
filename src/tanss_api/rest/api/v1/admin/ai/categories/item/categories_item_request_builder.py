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
    from .categories_delete_response import CategoriesDeleteResponse
    from .categories_get_response import CategoriesGetResponse
    from .categories_put_request_body import CategoriesPutRequestBody
    from .categories_put_response import CategoriesPutResponse

class CategoriesItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/admin/ai/categories/{id}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new CategoriesItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/admin/ai/categories/{id}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[CategoriesDeleteResponse]:
        """
        Löscht eine KI-Prompt-Kategorie, rückt die Ränge nach und entfernt die Kategorie-Zuordnung bei betroffenen Prompts. Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft. Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId. Rechte: licModule ACTIVE_SUBSCRIPTION (45), interner Benutzer, EDIT_AI_SETTINGS (531). Hinweise: ENTITY_NOT_FOUND wenn unbekannt. Prompts mit dieser categoryId erhalten categoryId=null (werden nicht gelöscht). Antwort meta DELETED.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[CategoriesDeleteResponse]
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .categories_delete_response import CategoriesDeleteResponse

        return await self.request_adapter.send_async(request_info, CategoriesDeleteResponse, None)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[CategoriesGetResponse]:
        """
        Liefert eine einzelne KI-Prompt-Kategorie. Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft. Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId. Rechte: licModule ACTIVE_SUBSCRIPTION (45). Hinweise: EDIT_AI_SETTINGS wird hier NICHT geprüft. OBJECT_NOT_FOUND wenn unbekannt. Status FOUND.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[CategoriesGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .categories_get_response import CategoriesGetResponse

        return await self.request_adapter.send_async(request_info, CategoriesGetResponse, None)
    
    async def put(self,body: CategoriesPutRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[CategoriesPutResponse]:
        """
        Aktualisiert eine KI-Prompt-Kategorie (Name) und/oder verschiebt ihren Rang relativ. Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft. Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId. Rechte: licModule ACTIVE_SUBSCRIPTION (45), interner Benutzer, EDIT_AI_SETTINGS (531). Hinweise: Keys id und rank werden entfernt. adjustRank: neuer rank = alter rank + adjustRank, begrenzt auf 1..Anzahl; andere Kategorien werden nachgerückt; adjustRank wird danach auf null gesetzt. ENTITY_NOT_FOUND wenn unbekannt. Antwort meta UPDATED.
        param body: Zu ändernde Felder (Merge)
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[CategoriesPutResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .categories_put_response import CategoriesPutResponse

        return await self.request_adapter.send_async(request_info, CategoriesPutResponse, None)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Löscht eine KI-Prompt-Kategorie, rückt die Ränge nach und entfernt die Kategorie-Zuordnung bei betroffenen Prompts. Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft. Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId. Rechte: licModule ACTIVE_SUBSCRIPTION (45), interner Benutzer, EDIT_AI_SETTINGS (531). Hinweise: ENTITY_NOT_FOUND wenn unbekannt. Prompts mit dieser categoryId erhalten categoryId=null (werden nicht gelöscht). Antwort meta DELETED.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Liefert eine einzelne KI-Prompt-Kategorie. Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft. Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId. Rechte: licModule ACTIVE_SUBSCRIPTION (45). Hinweise: EDIT_AI_SETTINGS wird hier NICHT geprüft. OBJECT_NOT_FOUND wenn unbekannt. Status FOUND.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_put_request_information(self,body: CategoriesPutRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Aktualisiert eine KI-Prompt-Kategorie (Name) und/oder verschiebt ihren Rang relativ. Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft. Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId. Rechte: licModule ACTIVE_SUBSCRIPTION (45), interner Benutzer, EDIT_AI_SETTINGS (531). Hinweise: Keys id und rank werden entfernt. adjustRank: neuer rank = alter rank + adjustRank, begrenzt auf 1..Anzahl; andere Kategorien werden nachgerückt; adjustRank wird danach auf null gesetzt. ENTITY_NOT_FOUND wenn unbekannt. Antwort meta UPDATED.
        param body: Zu ändernde Felder (Merge)
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
    
    def with_url(self,raw_url: str) -> CategoriesItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: CategoriesItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return CategoriesItemRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class CategoriesItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class CategoriesItemRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class CategoriesItemRequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

