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
    from ......models.mails403_error import Mails403Error
    from .item.with_mail_item_request_builder import WithMailItemRequestBuilder
    from .mails_post_request_body import MailsPostRequestBody
    from .mails_post_response import MailsPostResponse

class MailsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/tickets/{-id}/mails
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new MailsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/tickets/{%2Did}/mails{?pinned*}", path_parameters)
    
    def by_mail_id(self,mail_id: int) -> WithMailItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.v1.tickets.item.mails.item collection
        param mail_id: Id of the mail to return.
        Returns: WithMailItemRequestBuilder
        """
        if mail_id is None:
            raise TypeError("mail_id cannot be null.")
        from .item.with_mail_item_request_builder import WithMailItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["mailId"] = mail_id
        return WithMailItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def post(self,body: MailsPostRequestBody, request_configuration: Optional[RequestConfiguration[MailsRequestBuilderPostQueryParameters]] = None) -> Optional[MailsPostResponse]:
        """
        Composes and sends an outbound mail from the ticket (to customer, to assignee,to free-text recipients) and stores it in the ticket history. With`pinned=true` the resulting mail entry is pinned to the ticket. Throws 500 onSMTP failure.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[MailsPostResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ......models.mails403_error import Mails403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Mails403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .mails_post_response import MailsPostResponse

        return await self.request_adapter.send_async(request_info, MailsPostResponse, error_mapping)
    
    def to_post_request_information(self,body: MailsPostRequestBody, request_configuration: Optional[RequestConfiguration[MailsRequestBuilderPostQueryParameters]] = None) -> RequestInformation:
        """
        Composes and sends an outbound mail from the ticket (to customer, to assignee,to free-text recipients) and stores it in the ticket history. With`pinned=true` the resulting mail entry is pinned to the ticket. Throws 500 onSMTP failure.
        param body: The request body
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
    
    def with_url(self,raw_url: str) -> MailsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: MailsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return MailsRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class MailsRequestBuilderPostQueryParameters():
        """
        Composes and sends an outbound mail from the ticket (to customer, to assignee,to free-text recipients) and stores it in the ticket history. With`pinned=true` the resulting mail entry is pinned to the ticket. Throws 500 onSMTP failure.
        """
        # When true, pin the resulting mail entry to the ticket.
        pinned: Optional[bool] = None

    
    @dataclass
    class MailsRequestBuilderPostRequestConfiguration(RequestConfiguration[MailsRequestBuilderPostQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

