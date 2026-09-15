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
    from .....models.telephone_systems403_error import TelephoneSystems403Error
    from .telephone_systems_get_response import TelephoneSystemsGetResponse
    from .telephone_systems_put_request_body import TelephoneSystemsPutRequestBody
    from .telephone_systems_put_response import TelephoneSystemsPutResponse

class TelephoneSystemsItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/telephoneSystems/{id}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new TelephoneSystemsItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/telephoneSystems/{id}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Removes the telephone-system entry with the given id from the properties file (all `tanss.telephoneSystems.<id>.*` keys are dropped). The change does not stop the running import thread on its own — call `restart` afterwards to apply it. Requires technician/freelancer plus `ONLINE_SYSTEM_CONFIGURATION`.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from .....models.telephone_systems403_error import TelephoneSystems403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": TelephoneSystems403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[TelephoneSystemsGetResponse]:
        """
        Returns the configuration map for one telephone system, loaded from the `tanss.telephoneSystems.<id>.*` properties. Throws 404 if the id is unknown. Requires technician/freelancer plus `ONLINE_SYSTEM_CONFIGURATION`.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[TelephoneSystemsGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .....models.telephone_systems403_error import TelephoneSystems403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": TelephoneSystems403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .telephone_systems_get_response import TelephoneSystemsGetResponse

        return await self.request_adapter.send_async(request_info, TelephoneSystemsGetResponse, error_mapping)
    
    async def put(self,body: TelephoneSystemsPutRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[TelephoneSystemsPutResponse]:
        """
        Overwrites the configuration of an existing telephone system. The body must include `id` (must match the path) and `type`; the persisted field set is derived from the stored `type` (vendor-specific). Call `restart` afterwards to apply the change to the running import thread. Requires technician/freelancer plus `ONLINE_SYSTEM_CONFIGURATION`.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[TelephoneSystemsPutResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        from .....models.telephone_systems403_error import TelephoneSystems403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": TelephoneSystems403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .telephone_systems_put_response import TelephoneSystemsPutResponse

        return await self.request_adapter.send_async(request_info, TelephoneSystemsPutResponse, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Removes the telephone-system entry with the given id from the properties file (all `tanss.telephoneSystems.<id>.*` keys are dropped). The change does not stop the running import thread on its own — call `restart` afterwards to apply it. Requires technician/freelancer plus `ONLINE_SYSTEM_CONFIGURATION`.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Returns the configuration map for one telephone system, loaded from the `tanss.telephoneSystems.<id>.*` properties. Throws 404 if the id is unknown. Requires technician/freelancer plus `ONLINE_SYSTEM_CONFIGURATION`.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_put_request_information(self,body: TelephoneSystemsPutRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Overwrites the configuration of an existing telephone system. The body must include `id` (must match the path) and `type`; the persisted field set is derived from the stored `type` (vendor-specific). Call `restart` afterwards to apply the change to the running import thread. Requires technician/freelancer plus `ONLINE_SYSTEM_CONFIGURATION`.
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
    
    def with_url(self,raw_url: str) -> TelephoneSystemsItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: TelephoneSystemsItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return TelephoneSystemsItemRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class TelephoneSystemsItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class TelephoneSystemsItemRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class TelephoneSystemsItemRequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

