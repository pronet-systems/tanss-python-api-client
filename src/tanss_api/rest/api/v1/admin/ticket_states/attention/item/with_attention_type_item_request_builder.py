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
    from .......models.with_attention_type403_error import WithAttentionType403Error
    from .with_attention_type_post_response import WithAttentionTypePostResponse

class WithAttentionTypeItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/admin/ticketStates/attention/{attentionType}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new WithAttentionTypeItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/admin/ticketStates/attention/{attentionType}{?overwrite*}", path_parameters)
    
    async def post(self,request_configuration: Optional[RequestConfiguration[WithAttentionTypeItemRequestBuilderPostQueryParameters]] = None) -> Optional[WithAttentionTypePostResponse]:
        """
        Uploads an attention icon image for a specific attention type (e.g. urgent,overdue). With `overwrite=true` an existing image is replaced, otherwise thecall fails if an image is already present. Requires admin permission on theattention aspect.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[WithAttentionTypePostResponse]
        """
        request_info = self.to_post_request_information(
            request_configuration
        )
        from .......models.with_attention_type403_error import WithAttentionType403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": WithAttentionType403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .with_attention_type_post_response import WithAttentionTypePostResponse

        return await self.request_adapter.send_async(request_info, WithAttentionTypePostResponse, error_mapping)
    
    def to_post_request_information(self,request_configuration: Optional[RequestConfiguration[WithAttentionTypeItemRequestBuilderPostQueryParameters]] = None) -> RequestInformation:
        """
        Uploads an attention icon image for a specific attention type (e.g. urgent,overdue). With `overwrite=true` an existing image is replaced, otherwise thecall fails if an image is already present. Requires admin permission on theattention aspect.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.POST, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> WithAttentionTypeItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: WithAttentionTypeItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return WithAttentionTypeItemRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class WithAttentionTypeItemRequestBuilderPostQueryParameters():
        """
        Uploads an attention icon image for a specific attention type (e.g. urgent,overdue). With `overwrite=true` an existing image is replaced, otherwise thecall fails if an image is already present. Requires admin permission on theattention aspect.
        """
        # When true, replace an existing attention image; otherwise the call fails if one is present.
        overwrite: Optional[bool] = None

    
    @dataclass
    class WithAttentionTypeItemRequestBuilderPostRequestConfiguration(RequestConfiguration[WithAttentionTypeItemRequestBuilderPostQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

