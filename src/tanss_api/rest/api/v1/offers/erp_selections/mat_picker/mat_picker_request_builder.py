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
    from ......models.mat_picker403_error import MatPicker403Error
    from ......models.tns_offer_erp_selection_material_source import TnsOfferErpSelectionMaterialSource
    from .item.with_erp_selection_item_request_builder import WithErpSelectionItemRequestBuilder
    from .mat_picker_get_response import MatPickerGetResponse

class MatPickerRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/offers/erpSelections/matPicker
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new MatPickerRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/offers/erpSelections/matPicker?source={source}{&searchText*}", path_parameters)
    
    def by_erp_selection_id(self,erp_selection_id: int) -> WithErpSelectionItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.v1.offers.erpSelections.matPicker.item collection
        param erp_selection_id: Id of the erp selection
        Returns: WithErpSelectionItemRequestBuilder
        """
        if erp_selection_id is None:
            raise TypeError("erp_selection_id cannot be null.")
        from .item.with_erp_selection_item_request_builder import WithErpSelectionItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["erpSelectionId"] = erp_selection_id
        return WithErpSelectionItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[MatPickerRequestBuilderGetQueryParameters]] = None) -> Optional[MatPickerGetResponse]:
        """
        This route gets a list of materials for the "material picker" which is used to fill material in an "erp selection"
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[MatPickerGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ......models.mat_picker403_error import MatPicker403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": MatPicker403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .mat_picker_get_response import MatPickerGetResponse

        return await self.request_adapter.send_async(request_info, MatPickerGetResponse, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[MatPickerRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        This route gets a list of materials for the "material picker" which is used to fill material in an "erp selection"
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> MatPickerRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: MatPickerRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return MatPickerRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class MatPickerRequestBuilderGetQueryParameters():
        """
        This route gets a list of materials for the "material picker" which is used to fill material in an "erp selection"
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "search_text":
                return "searchText"
            if original_name == "source":
                return "source"
            return original_name
        
        # if result should be filtered, the search text goes here
        search_text: Optional[str] = None

        # determines the source for this picker
        source: Optional[TnsOfferErpSelectionMaterialSource] = None

    
    @dataclass
    class MatPickerRequestBuilderGetRequestConfiguration(RequestConfiguration[MatPickerRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

