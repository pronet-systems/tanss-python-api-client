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
    from ....models.pcs403_error import Pcs403Error
    from ....models.tns_personal_computer_configuration import TnsPersonalComputerConfiguration
    from ....models.tns_personal_computer_with_ip_guarantee import TnsPersonalComputerWithIpGuarantee
    from .company.company_request_builder import CompanyRequestBuilder
    from .item.with_pc_item_request_builder import WithPcItemRequestBuilder
    from .pcs_post_response import PcsPostResponse
    from .pcs_put_response import PcsPutResponse
    from .pdf.pdf_request_builder import PdfRequestBuilder

class PcsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/pcs
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new PcsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/pcs", path_parameters)
    
    def by_pc_id(self,pc_id: int) -> WithPcItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.v1.pcs.item collection
        param pc_id: ID of the pc or server to fetch.
        Returns: WithPcItemRequestBuilder
        """
        if pc_id is None:
            raise TypeError("pc_id cannot be null.")
        from .item.with_pc_item_request_builder import WithPcItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["pcId"] = pc_id
        return WithPcItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def post(self,body: TnsPersonalComputerWithIpGuarantee, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[PcsPostResponse]:
        """
        Creates a pc or server.Will also store attached ip address information or guarantee.
        param body: Describes a pc or server with infos (ip address, guarantee)
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[PcsPostResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ....models.pcs403_error import Pcs403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Pcs403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .pcs_post_response import PcsPostResponse

        return await self.request_adapter.send_async(request_info, PcsPostResponse, error_mapping)
    
    async def put(self,body: TnsPersonalComputerConfiguration, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[PcsPutResponse]:
        """
        Gets a list of pcs or server.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[PcsPutResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        from ....models.pcs403_error import Pcs403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Pcs403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .pcs_put_response import PcsPutResponse

        return await self.request_adapter.send_async(request_info, PcsPutResponse, error_mapping)
    
    def to_post_request_information(self,body: TnsPersonalComputerWithIpGuarantee, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Creates a pc or server.Will also store attached ip address information or guarantee.
        param body: Describes a pc or server with infos (ip address, guarantee)
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
    
    def to_put_request_information(self,body: TnsPersonalComputerConfiguration, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Gets a list of pcs or server.
        param body: The request body
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
    
    def with_url(self,raw_url: str) -> PcsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: PcsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return PcsRequestBuilder(self.request_adapter, raw_url)
    
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
    
    @dataclass
    class PcsRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class PcsRequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

