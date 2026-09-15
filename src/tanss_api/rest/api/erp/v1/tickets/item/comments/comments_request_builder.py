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
    from .......models.comments403_error import Comments403Error
    from .......models.tns_comment import TnsComment
    from .comments_post_response import CommentsPostResponse

class CommentsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/erp/v1/tickets/{ticketId}/comments
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new CommentsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/erp/v1/tickets/{ticketId}/comments{?pinned*}", path_parameters)
    
    async def post(self,body: TnsComment, request_configuration: Optional[RequestConfiguration[CommentsRequestBuilderPostQueryParameters]] = None) -> Optional[CommentsPostResponse]:
        """
        Creates a comment on the given ticket. Same behaviour as the user-token route`POST /api/v1/tickets/{ticketId}/comments`, but callable with an ERP integration token — must becalled with the dedicated API token bound to the role `ERP`, not a normal user login.
        param body: Defines a ticket comment
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[CommentsPostResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from .......models.comments403_error import Comments403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Comments403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .comments_post_response import CommentsPostResponse

        return await self.request_adapter.send_async(request_info, CommentsPostResponse, error_mapping)
    
    def to_post_request_information(self,body: TnsComment, request_configuration: Optional[RequestConfiguration[CommentsRequestBuilderPostQueryParameters]] = None) -> RequestInformation:
        """
        Creates a comment on the given ticket. Same behaviour as the user-token route`POST /api/v1/tickets/{ticketId}/comments`, but callable with an ERP integration token — must becalled with the dedicated API token bound to the role `ERP`, not a normal user login.
        param body: Defines a ticket comment
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
    
    def with_url(self,raw_url: str) -> CommentsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: CommentsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return CommentsRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class CommentsRequestBuilderPostQueryParameters():
        """
        Creates a comment on the given ticket. Same behaviour as the user-token route`POST /api/v1/tickets/{ticketId}/comments`, but callable with an ERP integration token — must becalled with the dedicated API token bound to the role `ERP`, not a normal user login.
        """
        # comment can optionally be "pinned" to the ticket
        pinned: Optional[bool] = None

    
    @dataclass
    class CommentsRequestBuilderPostRequestConfiguration(RequestConfiguration[CommentsRequestBuilderPostQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

