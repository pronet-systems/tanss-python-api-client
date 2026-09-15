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
    from .....models.with_chat403_error import WithChat403Error
    from .with_chat_get_response import WithChatGetResponse
    from .with_chat_put_request_body import WithChatPutRequestBody
    from .with_chat_put_response import WithChatPutResponse

class WithChatItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/chats/{chatId}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new WithChatItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/chats/{chatId}{?withMessages*}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[WithChatItemRequestBuilderGetQueryParameters]] = None) -> Optional[WithChatGetResponse]:
        """
        Gets infos for a given chat (inlcuding messages, logs and participants)
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[WithChatGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .....models.with_chat403_error import WithChat403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": WithChat403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .with_chat_get_response import WithChatGetResponse

        return await self.request_adapter.send_async(request_info, WithChatGetResponse, error_mapping)
    
    async def put(self,body: WithChatPutRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[WithChatPutResponse]:
        """
        Aktualisiert einen Chat (z.B. Beschreibung, erwartete Antwortzeit) per JSON-Teilupdate.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId.Rechte: Lizenzmodul CHAT (sonst TnsModuleNotLicensedException); Chat-Zugriff als Ersteller, Teilnehmer, Mitglied einer Teilnehmer-Abteilung oder (Chat mit Verknuepfung + Recht ACCESS_ALL_CHATS_CONSULTATIONS + Zugriff auf das verknuepfte Objekt), sonst FORBIDDEN_MISSING_PERMISSIONS.Hinweise: ENTITY_NOT_FOUND bei unbekannter chatId; leeres JSON -> TnsJsonException. Status und Verknuepfung (linkTypeId/linkId) sind hier nicht aenderbar; id, createdByEmployeeId, creationDate, closedByEmployeeId, status, lastMessageId, lastMessageDate, linkTypeId, linkId werden ignoriert. Nach dem Speichern werden Teilnehmer, Nachrichten, Logs und ungelesene Nachrichten nachgeladen. meta=UPDATED.
        param body: Teilupdate mit TnsChat-Feldern
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[WithChatPutResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .with_chat_put_response import WithChatPutResponse

        return await self.request_adapter.send_async(request_info, WithChatPutResponse, None)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[WithChatItemRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Gets infos for a given chat (inlcuding messages, logs and participants)
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_put_request_information(self,body: WithChatPutRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Aktualisiert einen Chat (z.B. Beschreibung, erwartete Antwortzeit) per JSON-Teilupdate.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId.Rechte: Lizenzmodul CHAT (sonst TnsModuleNotLicensedException); Chat-Zugriff als Ersteller, Teilnehmer, Mitglied einer Teilnehmer-Abteilung oder (Chat mit Verknuepfung + Recht ACCESS_ALL_CHATS_CONSULTATIONS + Zugriff auf das verknuepfte Objekt), sonst FORBIDDEN_MISSING_PERMISSIONS.Hinweise: ENTITY_NOT_FOUND bei unbekannter chatId; leeres JSON -> TnsJsonException. Status und Verknuepfung (linkTypeId/linkId) sind hier nicht aenderbar; id, createdByEmployeeId, creationDate, closedByEmployeeId, status, lastMessageId, lastMessageDate, linkTypeId, linkId werden ignoriert. Nach dem Speichern werden Teilnehmer, Nachrichten, Logs und ungelesene Nachrichten nachgeladen. meta=UPDATED.
        param body: Teilupdate mit TnsChat-Feldern
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
    
    def with_url(self,raw_url: str) -> WithChatItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: WithChatItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return WithChatItemRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class WithChatItemRequestBuilderGetQueryParameters():
        """
        Gets infos for a given chat (inlcuding messages, logs and participants)
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "with_messages":
                return "withMessages"
            return original_name
        
        # If "false" is given here, no messages will be loaded
        with_messages: Optional[bool] = None

    
    @dataclass
    class WithChatItemRequestBuilderGetRequestConfiguration(RequestConfiguration[WithChatItemRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class WithChatItemRequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

