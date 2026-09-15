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
    from ......models.with_company403_error import WithCompany403Error
    from .item.with_ticket_item_request_builder import WithTicketItemRequestBuilder
    from .with_company_get_response import WithCompanyGetResponse

class WithCompanyItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/util/mailpicker/{companyId}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new WithCompanyItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/util/mailpicker/{companyId}", path_parameters)
    
    def by_ticket_id(self,ticket_id: int) -> WithTicketItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.v1.util.mailpicker.item.item collection
        param ticket_id: Id of the ticket whose previous correspondents should be included.
        Returns: WithTicketItemRequestBuilder
        """
        if ticket_id is None:
            raise TypeError("ticket_id cannot be null.")
        from .item.with_ticket_item_request_builder import WithTicketItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["ticketId"] = ticket_id
        return WithTicketItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[WithCompanyGetResponse]:
        """
        Variant of the mail picker lookup that operates only on a company id (no ticket context). Returns employees and companies with their mail addresses, filtered down to `mails`, `name`, and `centralType` so the recipient picker stays compact.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[WithCompanyGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ......models.with_company403_error import WithCompany403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": WithCompany403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .with_company_get_response import WithCompanyGetResponse

        return await self.request_adapter.send_async(request_info, WithCompanyGetResponse, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Variant of the mail picker lookup that operates only on a company id (no ticket context). Returns employees and companies with their mail addresses, filtered down to `mails`, `name`, and `centralType` so the recipient picker stays compact.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> WithCompanyItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: WithCompanyItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return WithCompanyItemRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class WithCompanyItemRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

