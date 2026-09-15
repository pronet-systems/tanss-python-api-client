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
    from ....models.peripheries403_error import Peripheries403Error
    from ....models.tns_periphery_configuration import TnsPeripheryConfiguration
    from ....models.tns_periphery_with_ip_guarantee import TnsPeripheryWithIpGuarantee
    from .company.company_request_builder import CompanyRequestBuilder
    from .item.with_periphery_item_request_builder import WithPeripheryItemRequestBuilder
    from .pdf.pdf_request_builder import PdfRequestBuilder
    from .peripheries_post_response import PeripheriesPostResponse
    from .peripheries_put_response import PeripheriesPutResponse
    from .types.types_request_builder import TypesRequestBuilder

class PeripheriesRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/peripheries
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new PeripheriesRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/peripheries", path_parameters)
    
    def by_periphery_id(self,periphery_id: int) -> WithPeripheryItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.v1.peripheries.item collection
        param periphery_id: ID of the periphery to fetch.
        Returns: WithPeripheryItemRequestBuilder
        """
        if periphery_id is None:
            raise TypeError("periphery_id cannot be null.")
        from .item.with_periphery_item_request_builder import WithPeripheryItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["peripheryId"] = periphery_id
        return WithPeripheryItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def post(self,body: TnsPeripheryWithIpGuarantee, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[PeripheriesPostResponse]:
        """
        Creates a peripheryWill also store attached ip address information or guarantee.
        param body: Describes a periphery with all "attached" infos
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[PeripheriesPostResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ....models.peripheries403_error import Peripheries403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Peripheries403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .peripheries_post_response import PeripheriesPostResponse

        return await self.request_adapter.send_async(request_info, PeripheriesPostResponse, error_mapping)
    
    async def put(self,body: TnsPeripheryConfiguration, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[PeripheriesPutResponse]:
        """
        Gets a list of peripheries
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[PeripheriesPutResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        from ....models.peripheries403_error import Peripheries403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Peripheries403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .peripheries_put_response import PeripheriesPutResponse

        return await self.request_adapter.send_async(request_info, PeripheriesPutResponse, error_mapping)
    
    def to_post_request_information(self,body: TnsPeripheryWithIpGuarantee, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Creates a peripheryWill also store attached ip address information or guarantee.
        param body: Describes a periphery with all "attached" infos
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
    
    def to_put_request_information(self,body: TnsPeripheryConfiguration, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Gets a list of peripheries
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
    
    def with_url(self,raw_url: str) -> PeripheriesRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: PeripheriesRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return PeripheriesRequestBuilder(self.request_adapter, raw_url)
    
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
    class PeripheriesRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class PeripheriesRequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

