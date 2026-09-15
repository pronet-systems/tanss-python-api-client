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
    from .....models.not_charged_reason403_error import NotChargedReason403Error
    from .item.not_charged_reason_item_request_builder import NotChargedReasonItemRequestBuilder
    from .not_charged_reason_get_response import NotChargedReasonGetResponse
    from .not_charged_reason_post_request_body import NotChargedReasonPostRequestBody
    from .not_charged_reason_post_response import NotChargedReasonPostResponse

class NotChargedReasonRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/supports/notChargedReason
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new NotChargedReasonRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/supports/notChargedReason", path_parameters)
    
    def by_id(self,id: int) -> NotChargedReasonItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.v1.supports.notChargedReason.item collection
        param id: Id of the not-charged reason to delete.
        Returns: NotChargedReasonItemRequestBuilder
        """
        if id is None:
            raise TypeError("id cannot be null.")
        from .item.not_charged_reason_item_request_builder import NotChargedReasonItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["id"] = id
        return NotChargedReasonItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[NotChargedReasonGetResponse]:
        """
        Returns all "not charged" reasons used by supports. When a support is fully or partially not billed, one of these reasons can be referenced (`reasonNotChargedId` / `reasonPartialNotChargedId`) and its `longText` is appended to the support's `reasonNotChargedText`. Inherited admin CRUD route — requires technician/freelancer status and `BASE_DATA_MANAGEMENT_SYSTEM_TABLES` permission.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[NotChargedReasonGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .....models.not_charged_reason403_error import NotChargedReason403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": NotChargedReason403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .not_charged_reason_get_response import NotChargedReasonGetResponse

        return await self.request_adapter.send_async(request_info, NotChargedReasonGetResponse, error_mapping)
    
    async def post(self,body: NotChargedReasonPostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[NotChargedReasonPostResponse]:
        """
        Creates a new not-charged reason. `shortText` is shown in dropdowns/lists; `longText` is the explanatory text appended to a support's not-charged-reason text. Requires technician/freelancer status and `BASE_DATA_MANAGEMENT_SYSTEM_TABLES` permission.
        param body: Request body.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[NotChargedReasonPostResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from .....models.not_charged_reason403_error import NotChargedReason403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": NotChargedReason403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .not_charged_reason_post_response import NotChargedReasonPostResponse

        return await self.request_adapter.send_async(request_info, NotChargedReasonPostResponse, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Returns all "not charged" reasons used by supports. When a support is fully or partially not billed, one of these reasons can be referenced (`reasonNotChargedId` / `reasonPartialNotChargedId`) and its `longText` is appended to the support's `reasonNotChargedText`. Inherited admin CRUD route — requires technician/freelancer status and `BASE_DATA_MANAGEMENT_SYSTEM_TABLES` permission.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: NotChargedReasonPostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Creates a new not-charged reason. `shortText` is shown in dropdowns/lists; `longText` is the explanatory text appended to a support's not-charged-reason text. Requires technician/freelancer status and `BASE_DATA_MANAGEMENT_SYSTEM_TABLES` permission.
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
    
    def with_url(self,raw_url: str) -> NotChargedReasonRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: NotChargedReasonRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return NotChargedReasonRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class NotChargedReasonRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class NotChargedReasonRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

