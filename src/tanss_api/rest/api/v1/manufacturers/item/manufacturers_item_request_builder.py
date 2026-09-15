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
    from .....models.manufacturers403_error import Manufacturers403Error
    from .....models.tns_manufacturer import TnsManufacturer
    from .manufacturers_get_response import ManufacturersGetResponse
    from .manufacturers_put_response import ManufacturersPutResponse

class ManufacturersItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/manufacturers/{id}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new ManufacturersItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/manufacturers/{id}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Deletes a manufacturer
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from .....models.manufacturers403_error import Manufacturers403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Manufacturers403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[ManufacturersGetResponse]:
        """
        Gets a specific manufacturer
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ManufacturersGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .....models.manufacturers403_error import Manufacturers403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Manufacturers403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .manufacturers_get_response import ManufacturersGetResponse

        return await self.request_adapter.send_async(request_info, ManufacturersGetResponse, error_mapping)
    
    async def put(self,body: TnsManufacturer, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[ManufacturersPutResponse]:
        """
        Updates an existing manufacturer
        param body: representing a manufacturer
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ManufacturersPutResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        from .....models.manufacturers403_error import Manufacturers403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Manufacturers403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .manufacturers_put_response import ManufacturersPutResponse

        return await self.request_adapter.send_async(request_info, ManufacturersPutResponse, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Deletes a manufacturer
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Gets a specific manufacturer
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_put_request_information(self,body: TnsManufacturer, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Updates an existing manufacturer
        param body: representing a manufacturer
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
    
    def with_url(self,raw_url: str) -> ManufacturersItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: ManufacturersItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return ManufacturersItemRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class ManufacturersItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class ManufacturersItemRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class ManufacturersItemRequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

