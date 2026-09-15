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
    from ......models.conditions403_error import Conditions403Error
    from .conditions_get_response import ConditionsGetResponse
    from .conditions_post_request_body import ConditionsPostRequestBody
    from .conditions_post_response import ConditionsPostResponse

class ConditionsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/sla/{-id}/conditions
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new ConditionsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/sla/{%2Did}/conditions", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[ConditionsGetResponse]:
        """
        Returns all matching conditions configured for the given SLA, ordered by rank. The conditions decide whether the SLA applies to a particular ticket. Requires admin-level SLA permissions.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ConditionsGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ......models.conditions403_error import Conditions403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Conditions403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .conditions_get_response import ConditionsGetResponse

        return await self.request_adapter.send_async(request_info, ConditionsGetResponse, error_mapping)
    
    async def post(self,body: ConditionsPostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[ConditionsPostResponse]:
        """
        Adds a new matching condition (field, operator, value) to the given SLA. The new condition is appended at the end of the rank order; use the sort route to move it. Requires SERVICE_LEVEL_AGREEMENT_ADMINISTRATION.
        param body: Request body.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ConditionsPostResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ......models.conditions403_error import Conditions403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Conditions403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .conditions_post_response import ConditionsPostResponse

        return await self.request_adapter.send_async(request_info, ConditionsPostResponse, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Returns all matching conditions configured for the given SLA, ordered by rank. The conditions decide whether the SLA applies to a particular ticket. Requires admin-level SLA permissions.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: ConditionsPostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Adds a new matching condition (field, operator, value) to the given SLA. The new condition is appended at the end of the rank order; use the sort route to move it. Requires SERVICE_LEVEL_AGREEMENT_ADMINISTRATION.
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
    
    def with_url(self,raw_url: str) -> ConditionsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: ConditionsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return ConditionsRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class ConditionsRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class ConditionsRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

