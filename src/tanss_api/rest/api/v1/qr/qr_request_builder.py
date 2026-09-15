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
    from ....models.qr403_error import Qr403Error
    from .item.with_link_type_item_request_builder import WithLinkTypeItemRequestBuilder
    from .qr import Qr
    from .qr_put_response import QrPutResponse

class QrRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/qr
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new QrRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/qr", path_parameters)
    
    def by_link_type_id(self,link_type_id: int) -> WithLinkTypeItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.v1.qr.item collection
        param link_type_id: Link type of the device assignment (e.g. 1 = pc).
        Returns: WithLinkTypeItemRequestBuilder
        """
        if link_type_id is None:
            raise TypeError("link_type_id cannot be null.")
        from .item.with_link_type_item_request_builder import WithLinkTypeItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["linkTypeId"] = link_type_id
        return WithLinkTypeItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def put(self,body: list[Qr], request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[QrPutResponse]:
        """
        Generates a single PDF containing QR codes for a batch of device assignments (PC, periphery, component, etc.). When the `Accept` header is `application/pdf` the PDF is streamed directly; otherwise a file-pass key is returned for asynchronous download. Assignments the caller has no access to are silently skipped.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[QrPutResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        from ....models.qr403_error import Qr403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Qr403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .qr_put_response import QrPutResponse

        return await self.request_adapter.send_async(request_info, QrPutResponse, error_mapping)
    
    def to_put_request_information(self,body: list[Qr], request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Generates a single PDF containing QR codes for a batch of device assignments (PC, periphery, component, etc.). When the `Accept` header is `application/pdf` the PDF is streamed directly; otherwise a file-pass key is returned for asynchronous download. Assignments the caller has no access to are silently skipped.
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
    
    def with_url(self,raw_url: str) -> QrRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: QrRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return QrRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class QrRequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

