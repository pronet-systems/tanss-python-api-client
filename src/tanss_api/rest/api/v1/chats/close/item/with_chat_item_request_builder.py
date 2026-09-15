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
    from ......models.with_chat403_error import WithChat403Error
    from .with_chat_post_response import WithChatPostResponse
    from .with_chat_put_response import WithChatPutResponse

class WithChatItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/chats/close/{chatId}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new WithChatItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/chats/close/{chatId}", path_parameters)
    
    async def post(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[WithChatPostResponse]:
        """
        Closes a chat. If the chat is not created by yourself, a close requests is create at first
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[WithChatPostResponse]
        """
        request_info = self.to_post_request_information(
            request_configuration
        )
        from ......models.with_chat403_error import WithChat403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": WithChat403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .with_chat_post_response import WithChatPostResponse

        return await self.request_adapter.send_async(request_info, WithChatPostResponse, error_mapping)
    
    async def put(self,request_configuration: Optional[RequestConfiguration[WithChatItemRequestBuilderPutQueryParameters]] = None) -> Optional[WithChatPutResponse]:
        """
        This routes accepts or declines a chat closing request.This can only be done for own chats (created by yourself)
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[WithChatPutResponse]
        """
        request_info = self.to_put_request_information(
            request_configuration
        )
        from ......models.with_chat403_error import WithChat403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": WithChat403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .with_chat_put_response import WithChatPutResponse

        return await self.request_adapter.send_async(request_info, WithChatPutResponse, error_mapping)
    
    def to_post_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Closes a chat. If the chat is not created by yourself, a close requests is create at first
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.POST, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_put_request_information(self,request_configuration: Optional[RequestConfiguration[WithChatItemRequestBuilderPutQueryParameters]] = None) -> RequestInformation:
        """
        This routes accepts or declines a chat closing request.This can only be done for own chats (created by yourself)
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.PUT, '{+baseurl}/api/v1/chats/close/{chatId}?accept={accept}', self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
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
    class WithChatItemRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class WithChatItemRequestBuilderPutQueryParameters():
        """
        This routes accepts or declines a chat closing request.This can only be done for own chats (created by yourself)
        """
        # true = accept cloe request / false = decline close request
        accept: Optional[bool] = None

    
    @dataclass
    class WithChatItemRequestBuilderPutRequestConfiguration(RequestConfiguration[WithChatItemRequestBuilderPutQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

