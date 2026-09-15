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
    from .....models.tns_push_config import TnsPushConfig
    from .all.all_request_builder import AllRequestBuilder
    from .config_post_response import ConfigPostResponse
    from .id.id_request_builder import IdRequestBuilder
    from .own.own_request_builder import OwnRequestBuilder
    from .uuid.uuid_request_builder import UuidRequestBuilder

class ConfigRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/push/config
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new ConfigRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/push/config", path_parameters)
    
    async def post(self,body: TnsPushConfig, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[ConfigPostResponse]:
        """
        Registriert bzw. aktualisiert die Push-Konfiguration (Gerätetoken) des aktuellen Benutzers, identifiziert durch userId+uuid (Upsert). Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft. Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId. Rechte: CONFIGURE_SMARTPHONE_CLIENTS nur für fremde userId; sonst wird userId auf den aktuellen Benutzer gesetzt. Hinweise: uuid ist Pflicht (MissingFieldKey 'uuid'); id und lastResponse werden ignoriert. 400 CURRENT_USER_NOT_EXISTS wenn kein Benutzer eingeloggt. Existiert (userId, uuid) bereits, wird der Datensatz überschrieben und lastResponse=now. Antwort-Status FOUND (nicht CREATED).
        param body: Push-Konfiguration (Gerätetoken) eines Benutzers
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ConfigPostResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .config_post_response import ConfigPostResponse

        return await self.request_adapter.send_async(request_info, ConfigPostResponse, None)
    
    def to_post_request_information(self,body: TnsPushConfig, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Registriert bzw. aktualisiert die Push-Konfiguration (Gerätetoken) des aktuellen Benutzers, identifiziert durch userId+uuid (Upsert). Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft. Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId. Rechte: CONFIGURE_SMARTPHONE_CLIENTS nur für fremde userId; sonst wird userId auf den aktuellen Benutzer gesetzt. Hinweise: uuid ist Pflicht (MissingFieldKey 'uuid'); id und lastResponse werden ignoriert. 400 CURRENT_USER_NOT_EXISTS wenn kein Benutzer eingeloggt. Existiert (userId, uuid) bereits, wird der Datensatz überschrieben und lastResponse=now. Antwort-Status FOUND (nicht CREATED).
        param body: Push-Konfiguration (Gerätetoken) eines Benutzers
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
    
    def with_url(self,raw_url: str) -> ConfigRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: ConfigRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return ConfigRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def all(self) -> AllRequestBuilder:
        """
        The all property
        """
        from .all.all_request_builder import AllRequestBuilder

        return AllRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def id(self) -> IdRequestBuilder:
        """
        The id property
        """
        from .id.id_request_builder import IdRequestBuilder

        return IdRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def own(self) -> OwnRequestBuilder:
        """
        The own property
        """
        from .own.own_request_builder import OwnRequestBuilder

        return OwnRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def uuid(self) -> UuidRequestBuilder:
        """
        The uuid property
        """
        from .uuid.uuid_request_builder import UuidRequestBuilder

        return UuidRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class ConfigRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

