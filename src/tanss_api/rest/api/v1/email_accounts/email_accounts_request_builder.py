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
    from ....models.email_accounts403_error import EmailAccounts403Error
    from ....models.tns_email_account import TnsEmailAccount
    from .compamy.compamy_request_builder import CompamyRequestBuilder
    from .company.company_request_builder import CompanyRequestBuilder
    from .email_accounts_post_response import EmailAccountsPostResponse
    from .item.email_accounts_item_request_builder import EmailAccountsItemRequestBuilder
    from .pdf.pdf_request_builder import PdfRequestBuilder
    from .types.types_request_builder import TypesRequestBuilder

class EmailAccountsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/emailAccounts
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new EmailAccountsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/emailAccounts", path_parameters)
    
    def by_id(self,id: int) -> EmailAccountsItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.v1.emailAccounts.item collection
        param id: Id of the E-mail account
        Returns: EmailAccountsItemRequestBuilder
        """
        if id is None:
            raise TypeError("id cannot be null.")
        from .item.email_accounts_item_request_builder import EmailAccountsItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["id"] = id
        return EmailAccountsItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def post(self,body: TnsEmailAccount, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[EmailAccountsPostResponse]:
        """
        Creates an email account
        param body: describes an email account (mailbox)
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[EmailAccountsPostResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ....models.email_accounts403_error import EmailAccounts403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": EmailAccounts403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .email_accounts_post_response import EmailAccountsPostResponse

        return await self.request_adapter.send_async(request_info, EmailAccountsPostResponse, error_mapping)
    
    def to_post_request_information(self,body: TnsEmailAccount, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Creates an email account
        param body: describes an email account (mailbox)
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
    
    def with_url(self,raw_url: str) -> EmailAccountsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: EmailAccountsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return EmailAccountsRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def compamy(self) -> CompamyRequestBuilder:
        """
        The compamy property
        """
        from .compamy.compamy_request_builder import CompamyRequestBuilder

        return CompamyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def company(self) -> CompanyRequestBuilder:
        """
        The company property
        """
        from .company.company_request_builder import CompanyRequestBuilder

        return CompanyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def pdf(self) -> PdfRequestBuilder:
        """
        The pdf property
        """
        from .pdf.pdf_request_builder import PdfRequestBuilder

        return PdfRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def types(self) -> TypesRequestBuilder:
        """
        The types property
        """
        from .types.types_request_builder import TypesRequestBuilder

        return TypesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class EmailAccountsRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

