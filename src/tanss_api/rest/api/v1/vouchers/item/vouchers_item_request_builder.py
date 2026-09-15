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
    from .....models.vouchers403_error import Vouchers403Error
    from .vouchers_get_response import VouchersGetResponse
    from .vouchers_post_response import VouchersPostResponse

class VouchersItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/vouchers/{id}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new VouchersItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/vouchers/{id}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[VouchersGetResponse]:
        """
        Returns a single object (invoice/voucher created from billed supports) by its id. Standard access checks apply — vouchers are an internal billing artefact, so customer users do not reach this endpoint; technicians or freelancers need access to the voucher's company.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[VouchersGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .....models.vouchers403_error import Vouchers403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Vouchers403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .vouchers_get_response import VouchersGetResponse

        return await self.request_adapter.send_async(request_info, VouchersGetResponse, error_mapping)
    
    async def post(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[VouchersPostResponse]:
        """
        Resets the voucher's export state to `NONE`, allowing it to be re-exported (e.g. re-sent to an accounting system). The voucher itself is not regenerated. Same access constraints as the GET — a technician with access to the voucher's company.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[VouchersPostResponse]
        """
        request_info = self.to_post_request_information(
            request_configuration
        )
        from .....models.vouchers403_error import Vouchers403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Vouchers403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .vouchers_post_response import VouchersPostResponse

        return await self.request_adapter.send_async(request_info, VouchersPostResponse, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Returns a single object (invoice/voucher created from billed supports) by its id. Standard access checks apply — vouchers are an internal billing artefact, so customer users do not reach this endpoint; technicians or freelancers need access to the voucher's company.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Resets the voucher's export state to `NONE`, allowing it to be re-exported (e.g. re-sent to an accounting system). The voucher itself is not regenerated. Same access constraints as the GET — a technician with access to the voucher's company.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.POST, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> VouchersItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: VouchersItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return VouchersItemRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class VouchersItemRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class VouchersItemRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

