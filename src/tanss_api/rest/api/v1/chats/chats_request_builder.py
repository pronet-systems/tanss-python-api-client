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
    from ....models.chats403_error import Chats403Error
    from ....models.tns_chat_configuration import TnsChatConfiguration
    from ....models.tns_chat_detail import TnsChatDetail
    from .chats_post_response import ChatsPostResponse
    from .chats_put_response import ChatsPutResponse
    from .close.close_request_builder import CloseRequestBuilder
    from .close_requests.close_requests_request_builder import CloseRequestsRequestBuilder
    from .item.with_chat_item_request_builder import WithChatItemRequestBuilder
    from .messages.messages_request_builder import MessagesRequestBuilder
    from .participants.participants_request_builder import ParticipantsRequestBuilder
    from .re_open.re_open_request_builder import ReOpenRequestBuilder

class ChatsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/chats
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new ChatsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/chats", path_parameters)
    
    def by_chat_id(self,chat_id: int) -> WithChatItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.v1.chats.item collection
        param chat_id: Id of the chat to be fetched
        Returns: WithChatItemRequestBuilder
        """
        if chat_id is None:
            raise TypeError("chat_id cannot be null.")
        from .item.with_chat_item_request_builder import WithChatItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["chatId"] = chat_id
        return WithChatItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def post(self,body: TnsChatDetail, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[ChatsPostResponse]:
        """
        Creates a new chat in TANSS. The chat must contain at least one participant and one message
        param body: TANSS chat (including info regarding messages, participants, logs)
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ChatsPostResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ....models.chats403_error import Chats403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Chats403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .chats_post_response import ChatsPostResponse

        return await self.request_adapter.send_async(request_info, ChatsPostResponse, error_mapping)
    
    async def put(self,body: TnsChatConfiguration, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[ChatsPutResponse]:
        """
        Retrieves a list of chats from the database, using misc. filter settings
        param body: Here, the filter settings for the chat list are stored
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ChatsPutResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        from ....models.chats403_error import Chats403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Chats403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .chats_put_response import ChatsPutResponse

        return await self.request_adapter.send_async(request_info, ChatsPutResponse, error_mapping)
    
    def to_post_request_information(self,body: TnsChatDetail, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Creates a new chat in TANSS. The chat must contain at least one participant and one message
        param body: TANSS chat (including info regarding messages, participants, logs)
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
    
    def to_put_request_information(self,body: TnsChatConfiguration, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Retrieves a list of chats from the database, using misc. filter settings
        param body: Here, the filter settings for the chat list are stored
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
    
    def with_url(self,raw_url: str) -> ChatsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: ChatsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return ChatsRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def close(self) -> CloseRequestBuilder:
        """
        The close property
        """
        from .close.close_request_builder import CloseRequestBuilder

        return CloseRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def close_requests(self) -> CloseRequestsRequestBuilder:
        """
        The closeRequests property
        """
        from .close_requests.close_requests_request_builder import CloseRequestsRequestBuilder

        return CloseRequestsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def messages(self) -> MessagesRequestBuilder:
        """
        The messages property
        """
        from .messages.messages_request_builder import MessagesRequestBuilder

        return MessagesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def participants(self) -> ParticipantsRequestBuilder:
        """
        The participants property
        """
        from .participants.participants_request_builder import ParticipantsRequestBuilder

        return ParticipantsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def re_open(self) -> ReOpenRequestBuilder:
        """
        The reOpen property
        """
        from .re_open.re_open_request_builder import ReOpenRequestBuilder

        return ReOpenRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class ChatsRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class ChatsRequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

