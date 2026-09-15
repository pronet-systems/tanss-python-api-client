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
    from .......models.status403_error import Status403Error
    from .status_get_response import StatusGetResponse
    from .status_put_request_body import StatusPutRequestBody
    from .status_put_response import StatusPutResponse

class StatusItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/companies/relations/status/{id}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new StatusItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/companies/relations/status/{id}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Removes a single object definition (a configurable label like "active", "expired", "planned") that can be attached to company relationships. Requires a technician or freelancer and the `MANAGE_COMPANY_RELATIONS` permission.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from .......models.status403_error import Status403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Status403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[StatusGetResponse]:
        """
        Returns a single object (id + name) by id. Used by the relationship editor to render the status dropdown.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[StatusGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .......models.status403_error import Status403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Status403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .status_get_response import StatusGetResponse

        return await self.request_adapter.send_async(request_info, StatusGetResponse, error_mapping)
    
    async def put(self,body: StatusPutRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[StatusPutResponse]:
        """
        Renames object. Requires a technician or freelancer and the `MANAGE_COMPANY_RELATIONS` permission.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[StatusPutResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        from .......models.status403_error import Status403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Status403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .status_put_response import StatusPutResponse

        return await self.request_adapter.send_async(request_info, StatusPutResponse, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Removes a single object definition (a configurable label like "active", "expired", "planned") that can be attached to company relationships. Requires a technician or freelancer and the `MANAGE_COMPANY_RELATIONS` permission.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Returns a single object (id + name) by id. Used by the relationship editor to render the status dropdown.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_put_request_information(self,body: StatusPutRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Renames object. Requires a technician or freelancer and the `MANAGE_COMPANY_RELATIONS` permission.
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
    
    def with_url(self,raw_url: str) -> StatusItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: StatusItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return StatusItemRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class StatusItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class StatusItemRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class StatusItemRequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

