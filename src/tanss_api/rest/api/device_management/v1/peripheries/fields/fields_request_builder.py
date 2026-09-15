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
    from ......models.fields403_error import Fields403Error
    from .fields_get_response import FieldsGetResponse
    from .fields_post_request_body import FieldsPostRequestBody
    from .fields_post_response import FieldsPostResponse
    from .item.fields_item_request_builder import FieldsItemRequestBuilder

class FieldsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/deviceManagement/v1/peripheries/fields
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new FieldsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/deviceManagement/v1/peripheries/fields", path_parameters)
    
    def by_id(self,id: int) -> FieldsItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.deviceManagement.v1.peripheries.fields.item collection
        param id: ID of the periphery-type additional field to delete.
        Returns: FieldsItemRequestBuilder
        """
        if id is None:
            raise TypeError("id cannot be null.")
        from .item.fields_item_request_builder import FieldsItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["id"] = id
        return FieldsItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[FieldsGetResponse]:
        """
        Returns all custom additional-field definitions across all periphery types. Used by the device-management admin UI to render the per-type custom field configuration.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[FieldsGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ......models.fields403_error import Fields403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Fields403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .fields_get_response import FieldsGetResponse

        return await self.request_adapter.send_async(request_info, FieldsGetResponse, error_mapping)
    
    async def post(self,body: FieldsPostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[FieldsPostResponse]:
        """
        Adds a new custom additional-field definition (e.g. "Seriennummer", "Garantieende") under a periphery type. The field then becomes available to fill in when editing peripheries of that type.
        param body: Request body.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[FieldsPostResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ......models.fields403_error import Fields403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Fields403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .fields_post_response import FieldsPostResponse

        return await self.request_adapter.send_async(request_info, FieldsPostResponse, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Returns all custom additional-field definitions across all periphery types. Used by the device-management admin UI to render the per-type custom field configuration.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: FieldsPostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Adds a new custom additional-field definition (e.g. "Seriennummer", "Garantieende") under a periphery type. The field then becomes available to fill in when editing peripheries of that type.
        param body: Request body.
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
    
    def with_url(self,raw_url: str) -> FieldsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: FieldsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return FieldsRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class FieldsRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class FieldsRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

