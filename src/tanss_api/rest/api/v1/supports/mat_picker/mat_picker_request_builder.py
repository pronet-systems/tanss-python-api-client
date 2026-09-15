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
    from .....models.mat_picker403_error import MatPicker403Error
    from .mat_picker_get_response import MatPickerGetResponse

class MatPickerRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/supports/matPicker
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new MatPickerRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/supports/matPicker{?carId*,searchText*,source*,type*}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[MatPickerRequestBuilderGetQueryParameters]] = None) -> Optional[MatPickerGetResponse]:
        """
        Returns the materials matching `searchText`, filtered by source (TANSS catalogue vs. external Wawi), type and optionally a car (mobile stock). Used by the material-picker dropdown when techs add materials to a support entry. Optionally includes serial numbers when the `XML_WAWI_MATERIAL_SEARCH_SN` config flag is set. Standard access checks apply.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[MatPickerGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .....models.mat_picker403_error import MatPicker403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": MatPicker403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .mat_picker_get_response import MatPickerGetResponse

        return await self.request_adapter.send_async(request_info, MatPickerGetResponse, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[MatPickerRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Returns the materials matching `searchText`, filtered by source (TANSS catalogue vs. external Wawi), type and optionally a car (mobile stock). Used by the material-picker dropdown when techs add materials to a support entry. Optionally includes serial numbers when the `XML_WAWI_MATERIAL_SEARCH_SN` config flag is set. Standard access checks apply.
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
        Returns the materials matching `searchText`, filtered by source (TANSS catalogue vs. external Wawi), type and optionally a car (mobile stock). Used by the material-picker dropdown when techs add materials to a support entry. Optionally includes serial numbers when the `XML_WAWI_MATERIAL_SEARCH_SN` config flag is set. Standard access checks apply.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "car_id":
                return "carId"
            if original_name == "search_text":
                return "searchText"
            if original_name == "source":
                return "source"
            if original_name == "type":
                return "type"
            return original_name
        
        # Id of the car (mobile stock) to restrict the search to; 0 means no car filter.
        car_id: Optional[int] = None

        # Text the material name/number is matched against.
        search_text: Optional[str] = None

        # Material source to search (e.g. TANSS catalogue or external Wawi).
        source: Optional[str] = None

        # Material type to filter the results by.
        type: Optional[str] = None

    
    @dataclass
    class MatPickerRequestBuilderGetRequestConfiguration(RequestConfiguration[MatPickerRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

