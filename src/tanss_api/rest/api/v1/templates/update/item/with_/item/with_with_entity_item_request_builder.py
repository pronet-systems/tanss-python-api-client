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
    from ........models.with_with_entity403_error import WithWithEntity403Error
    from .with_with_entity_put_request_body import WithWithEntityPutRequestBody
    from .with_with_entity_put_response import WithWithEntityPutResponse

class WithWithEntityItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/templates/update/{updateTemplateId}/with/{withEntityId}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new WithWithEntityItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/templates/update/{updateTemplateId}/with/{withEntityId}", path_parameters)
    
    async def put(self,body: WithWithEntityPutRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[WithWithEntityPutResponse]:
        """
        Replaces the persisted template `updateTemplateId` with a fresh snapshot taken from entity `withEntityId`,using the body to override the template `name` (optional) and selected `fields`. Useful when a user wantsto "refresh" a template from a more current source entity.The caller must be allowed to update this template (the standard CRUD checks apply).
        param body: Request body.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[WithWithEntityPutResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        from ........models.with_with_entity403_error import WithWithEntity403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": WithWithEntity403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .with_with_entity_put_response import WithWithEntityPutResponse

        return await self.request_adapter.send_async(request_info, WithWithEntityPutResponse, error_mapping)
    
    def to_put_request_information(self,body: WithWithEntityPutRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Replaces the persisted template `updateTemplateId` with a fresh snapshot taken from entity `withEntityId`,using the body to override the template `name` (optional) and selected `fields`. Useful when a user wantsto "refresh" a template from a more current source entity.The caller must be allowed to update this template (the standard CRUD checks apply).
        param body: Request body.
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
    
    def with_url(self,raw_url: str) -> WithWithEntityItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: WithWithEntityItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return WithWithEntityItemRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class WithWithEntityItemRequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

