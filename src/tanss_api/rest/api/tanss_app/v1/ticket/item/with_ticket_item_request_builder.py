from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .comments.comments_request_builder import CommentsRequestBuilder
    from .mail.mail_request_builder import MailRequestBuilder

class WithTicketItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/tanss.app/v1/ticket/{ticketId}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new WithTicketItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/tanss.app/v1/ticket/{ticketId}", path_parameters)
    
    @property
    def comments(self) -> CommentsRequestBuilder:
        """
        The comments property
        """
        from .comments.comments_request_builder import CommentsRequestBuilder

        return CommentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def mail(self) -> MailRequestBuilder:
        """
        The mail property
        """
        from .mail.mail_request_builder import MailRequestBuilder

        return MailRequestBuilder(self.request_adapter, self.path_parameters)
    

