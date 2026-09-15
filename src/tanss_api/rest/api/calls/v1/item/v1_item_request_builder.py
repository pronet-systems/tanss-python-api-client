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
    from .....models.tns_phone_call import TnsPhoneCall
    from .....models.v1403_error import V1403Error
    from .v1_get_response import V1GetResponse
    from .v1_put_response import V1PutResponse

class V1ItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/calls/v1/{id}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new V1ItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/calls/v1/{id}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[V1GetResponse]:
        """
        Gets a specific phone call from the database based on the phone call id
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[V1GetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .....models.v1403_error import V1403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": V1403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .v1_get_response import V1GetResponse

        return await self.request_adapter.send_async(request_info, V1GetResponse, error_mapping)
    
    async def put(self,body: TnsPhoneCall, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[V1PutResponse]:
        """
        This api call updates an existing phone call
        param body: This object represents a phone call
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[V1PutResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        from .....models.v1403_error import V1403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": V1403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .v1_put_response import V1PutResponse

        return await self.request_adapter.send_async(request_info, V1PutResponse, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Gets a specific phone call from the database based on the phone call id
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_put_request_information(self,body: TnsPhoneCall, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        This api call updates an existing phone call
        param body: This object represents a phone call
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
    
    def with_url(self,raw_url: str) -> V1ItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: V1ItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return V1ItemRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class V1ItemRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class V1ItemRequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

