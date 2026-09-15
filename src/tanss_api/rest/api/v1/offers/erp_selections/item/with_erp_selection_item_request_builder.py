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
    from ......models.tns_offer_erp_selection import TnsOfferErpSelection
    from ......models.with_erp_selection403_error import WithErpSelection403Error
    from .with_erp_selection_get_response import WithErpSelectionGetResponse
    from .with_erp_selection_put_response import WithErpSelectionPutResponse

class WithErpSelectionItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/offers/erpSelections/{erpSelectionId}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new WithErpSelectionItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/offers/erpSelections/{erpSelectionId}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Deletes an erp selection
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ......models.with_erp_selection403_error import WithErpSelection403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": WithErpSelection403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[WithErpSelectionGetResponse]:
        """
        Fetches information regarding a specific erp selection (including material)
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[WithErpSelectionGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ......models.with_erp_selection403_error import WithErpSelection403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": WithErpSelection403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .with_erp_selection_get_response import WithErpSelectionGetResponse

        return await self.request_adapter.send_async(request_info, WithErpSelectionGetResponse, error_mapping)
    
    async def put(self,body: TnsOfferErpSelection, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[WithErpSelectionPutResponse]:
        """
        Updates an erp selection and saves all attached materials as well
        param body: This object represents an "erp selection" profile to be used in offer templates
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[WithErpSelectionPutResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        from ......models.with_erp_selection403_error import WithErpSelection403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": WithErpSelection403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .with_erp_selection_put_response import WithErpSelectionPutResponse

        return await self.request_adapter.send_async(request_info, WithErpSelectionPutResponse, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Deletes an erp selection
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Fetches information regarding a specific erp selection (including material)
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_put_request_information(self,body: TnsOfferErpSelection, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Updates an erp selection and saves all attached materials as well
        param body: This object represents an "erp selection" profile to be used in offer templates
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
    
    def with_url(self,raw_url: str) -> WithErpSelectionItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: WithErpSelectionItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return WithErpSelectionItemRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class WithErpSelectionItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class WithErpSelectionItemRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class WithErpSelectionItemRequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

