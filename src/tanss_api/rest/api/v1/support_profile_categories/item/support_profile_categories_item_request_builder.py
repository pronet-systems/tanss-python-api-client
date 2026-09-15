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
    from .support_profile_categories_delete_response import SupportProfileCategoriesDeleteResponse
    from .support_profile_categories_get_response import SupportProfileCategoriesGetResponse
    from .support_profile_categories_put_request_body import SupportProfileCategoriesPutRequestBody
    from .support_profile_categories_put_response import SupportProfileCategoriesPutResponse

class SupportProfileCategoriesItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/supportProfileCategories/{id}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new SupportProfileCategoriesItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/supportProfileCategories/{id}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[SupportProfileCategoriesDeleteResponse]:
        """
        Generischer Admin-Endpunkt: löscht die Support-Profil-Kategorie anhand des Schlüssels.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId.Rechte: abhängig von den Hooks der konkreten Service-Klasse.Hinweise: Ablauf akf.long(id): Permission-Hooks, Prüf-Hook auf der Entität, ENTITY_NOT_FOUND wenn unbekannt. meta DELETED.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[SupportProfileCategoriesDeleteResponse]
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .support_profile_categories_delete_response import SupportProfileCategoriesDeleteResponse

        return await self.request_adapter.send_async(request_info, SupportProfileCategoriesDeleteResponse, None)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[SupportProfileCategoriesGetResponse]:
        """
        Generischer Admin-Endpunkt: liefert die Support-Profil-Kategorie anhand des Schlüssels.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId.Rechte: Firmenzugriffsprüfung falls ITnsCompanyAssignable (FORBIDDEN_NO_COMPANY_ACCESS); weitere Hooks der Service-Klasse.Hinweise: OBJECT_NOT_FOUND wenn unbekannt; ggf. Filterstrategien. Felder der Entität nicht dokumentiert. meta FOUND.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[SupportProfileCategoriesGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .support_profile_categories_get_response import SupportProfileCategoriesGetResponse

        return await self.request_adapter.send_async(request_info, SupportProfileCategoriesGetResponse, None)
    
    async def put(self,body: SupportProfileCategoriesPutRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[SupportProfileCategoriesPutResponse]:
        """
        Generischer Admin-Endpunkt: aktualisiert die Support-Profil-Kategorie per JSON-Teilupdate.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId.Rechte: Hooks der Service-Klasse; Standard Firmenzugriffsprüfung bei ITnsCompanyAssignable.Hinweise: 'id' wird vor dem Merge entfernt. ENTITY_NOT_FOUND wenn unbekannt, leeres JSON -> TnsJsonException, Merge via Jackson readerForUpdating, Speichern mit Diff-Logging. meta UPDATED.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[SupportProfileCategoriesPutResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .support_profile_categories_put_response import SupportProfileCategoriesPutResponse

        return await self.request_adapter.send_async(request_info, SupportProfileCategoriesPutResponse, None)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Generischer Admin-Endpunkt: löscht die Support-Profil-Kategorie anhand des Schlüssels.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId.Rechte: abhängig von den Hooks der konkreten Service-Klasse.Hinweise: Ablauf akf.long(id): Permission-Hooks, Prüf-Hook auf der Entität, ENTITY_NOT_FOUND wenn unbekannt. meta DELETED.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Generischer Admin-Endpunkt: liefert die Support-Profil-Kategorie anhand des Schlüssels.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId.Rechte: Firmenzugriffsprüfung falls ITnsCompanyAssignable (FORBIDDEN_NO_COMPANY_ACCESS); weitere Hooks der Service-Klasse.Hinweise: OBJECT_NOT_FOUND wenn unbekannt; ggf. Filterstrategien. Felder der Entität nicht dokumentiert. meta FOUND.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_put_request_information(self,body: SupportProfileCategoriesPutRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Generischer Admin-Endpunkt: aktualisiert die Support-Profil-Kategorie per JSON-Teilupdate.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId.Rechte: Hooks der Service-Klasse; Standard Firmenzugriffsprüfung bei ITnsCompanyAssignable.Hinweise: 'id' wird vor dem Merge entfernt. ENTITY_NOT_FOUND wenn unbekannt, leeres JSON -> TnsJsonException, Merge via Jackson readerForUpdating, Speichern mit Diff-Logging. meta UPDATED.
        param body: The request body
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
    
    def with_url(self,raw_url: str) -> SupportProfileCategoriesItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: SupportProfileCategoriesItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return SupportProfileCategoriesItemRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class SupportProfileCategoriesItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class SupportProfileCategoriesItemRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class SupportProfileCategoriesItemRequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

