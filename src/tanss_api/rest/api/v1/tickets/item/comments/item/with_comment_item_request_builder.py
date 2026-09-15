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
    from .......models.with_comment403_error import WithComment403Error
    from .with_comment_put_request_body import WithCommentPutRequestBody
    from .with_comment_put_response import WithCommentPutResponse

class WithCommentItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/tickets/{-id}/comments/{commentId}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new WithCommentItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/tickets/{%2Did}/comments/{commentId}{?pinned*}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Removes a comment from a ticket. The service-layer `deleteComment` enforcesthat the caller is allowed to delete the specific comment (typically theauthor or an admin) and triggers history bookkeeping.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from .......models.with_comment403_error import WithComment403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": WithComment403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def put(self,body: WithCommentPutRequestBody, request_configuration: Optional[RequestConfiguration[WithCommentItemRequestBuilderPutQueryParameters]] = None) -> Optional[WithCommentPutResponse]:
        """
        Edits an existing comment on a ticket. The optional `pinned` flag re-pins orun-pins the comment to the ticket. Permission is enforced: only the comment's author or an admin may edit it.
        param body: Request body.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[WithCommentPutResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        from .......models.with_comment403_error import WithComment403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": WithComment403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .with_comment_put_response import WithCommentPutResponse

        return await self.request_adapter.send_async(request_info, WithCommentPutResponse, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Removes a comment from a ticket. The service-layer `deleteComment` enforcesthat the caller is allowed to delete the specific comment (typically theauthor or an admin) and triggers history bookkeeping.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_put_request_information(self,body: WithCommentPutRequestBody, request_configuration: Optional[RequestConfiguration[WithCommentItemRequestBuilderPutQueryParameters]] = None) -> RequestInformation:
        """
        Edits an existing comment on a ticket. The optional `pinned` flag re-pins orun-pins the comment to the ticket. Permission is enforced: only the comment's author or an admin may edit it.
        param body: Request body.
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
    
    def with_url(self,raw_url: str) -> WithCommentItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: WithCommentItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return WithCommentItemRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class WithCommentItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class WithCommentItemRequestBuilderPutQueryParameters():
        """
        Edits an existing comment on a ticket. The optional `pinned` flag re-pins orun-pins the comment to the ticket. Permission is enforced: only the comment's author or an admin may edit it.
        """
        # When true, (re-)pin the comment to the ticket; when false, unpin it.
        pinned: Optional[bool] = None

    
    @dataclass
    class WithCommentItemRequestBuilderPutRequestConfiguration(RequestConfiguration[WithCommentItemRequestBuilderPutQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

