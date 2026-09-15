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
    from ......models.pdf403_error import Pdf403Error
    from .mail.mail_request_builder import MailRequestBuilder
    from .pdf_get_response import PdfGetResponse

class PdfRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/tickets/{-id}/pdf
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new PdfRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/tickets/{%2Did}/pdf{?internal*}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[PdfRequestBuilderGetQueryParameters]] = None) -> Optional[PdfGetResponse]:
        """
        Generates and streams a PDF rendering of the ticket detail page. With`internal=true` the PDF includes internal-only fields and comments (technicianview); with `internal=false` the customer view is produced. The response`Content-Type` is determined by the `Accept` header (binary PDF or JSONwrapper). The caller must have access to the ticket.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[PdfGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ......models.pdf403_error import Pdf403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Pdf403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .pdf_get_response import PdfGetResponse

        return await self.request_adapter.send_async(request_info, PdfGetResponse, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[PdfRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Generates and streams a PDF rendering of the ticket detail page. With`internal=true` the PDF includes internal-only fields and comments (technicianview); with `internal=false` the customer view is produced. The response`Content-Type` is determined by the `Accept` header (binary PDF or JSONwrapper). The caller must have access to the ticket.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> PdfRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: PdfRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return PdfRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def mail(self) -> MailRequestBuilder:
        """
        The mail property
        """
        from .mail.mail_request_builder import MailRequestBuilder

        return MailRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class PdfRequestBuilderGetQueryParameters():
        """
        Generates and streams a PDF rendering of the ticket detail page. With`internal=true` the PDF includes internal-only fields and comments (technicianview); with `internal=false` the customer view is produced. The response`Content-Type` is determined by the `Accept` header (binary PDF or JSONwrapper). The caller must have access to the ticket.
        """
        # When true, include internal-only fields and comments (technician view); when false, produce the customer view.
        internal: Optional[bool] = None

    
    @dataclass
    class PdfRequestBuilderGetRequestConfiguration(RequestConfiguration[PdfRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

