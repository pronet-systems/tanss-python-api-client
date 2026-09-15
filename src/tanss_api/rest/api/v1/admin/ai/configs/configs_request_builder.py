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
    from ......models.tns_l_l_m_configuration import TnsLLMConfiguration
    from .configs_get_response import ConfigsGetResponse
    from .configs_post_response import ConfigsPostResponse
    from .item.configs_item_request_builder import ConfigsItemRequestBuilder
    from .providers.providers_request_builder import ProvidersRequestBuilder

class ConfigsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/admin/ai/configs
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new ConfigsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/admin/ai/configs", path_parameters)
    
    def by_id(self,id: int) -> ConfigsItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.v1.admin.ai.configs.item collection
        param id: ID der Konfiguration
        Returns: ConfigsItemRequestBuilder
        """
        if id is None:
            raise TypeError("id cannot be null.")
        from .item.configs_item_request_builder import ConfigsItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["id"] = id
        return ConfigsItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[ConfigsGetResponse]:
        """
        Listet alle KI-/LLM-Konfigurationen (ohne API-Key).Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId.Hinweise: Kein Lizenz-/Rechte-Check (nur Authentifizierung). apiKey wird durch den STANDARD-Filter ausgeblendet; hasKey = apiKey nicht leer. Antwort-Status FOUND.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ConfigsGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .configs_get_response import ConfigsGetResponse

        return await self.request_adapter.send_async(request_info, ConfigsGetResponse, None)
    
    async def post(self,body: TnsLLMConfiguration, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[ConfigsPostResponse]:
        """
        Legt eine neue LLM-Konfiguration (Provider, Modell, API-Key) an.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId.Rechte: Lizenzmodul ACTIVE_SUBSCRIPTION; interner Benutzer; Recht EDIT_AI_SETTINGS.Hinweise: id/hasKey im Body werden ignoriert bzw. berechnet. apiKey wird verschlüsselt gespeichert. Antwort-Status CREATED.
        param body: KI-/LLM-Konfiguration (apiKey wird in Antworten ausgeblendet)
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ConfigsPostResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .configs_post_response import ConfigsPostResponse

        return await self.request_adapter.send_async(request_info, ConfigsPostResponse, None)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Listet alle KI-/LLM-Konfigurationen (ohne API-Key).Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId.Hinweise: Kein Lizenz-/Rechte-Check (nur Authentifizierung). apiKey wird durch den STANDARD-Filter ausgeblendet; hasKey = apiKey nicht leer. Antwort-Status FOUND.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: TnsLLMConfiguration, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Legt eine neue LLM-Konfiguration (Provider, Modell, API-Key) an.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId.Rechte: Lizenzmodul ACTIVE_SUBSCRIPTION; interner Benutzer; Recht EDIT_AI_SETTINGS.Hinweise: id/hasKey im Body werden ignoriert bzw. berechnet. apiKey wird verschlüsselt gespeichert. Antwort-Status CREATED.
        param body: KI-/LLM-Konfiguration (apiKey wird in Antworten ausgeblendet)
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
    
    def with_url(self,raw_url: str) -> ConfigsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: ConfigsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return ConfigsRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def providers(self) -> ProvidersRequestBuilder:
        """
        The providers property
        """
        from .providers.providers_request_builder import ProvidersRequestBuilder

        return ProvidersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class ConfigsRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class ConfigsRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

