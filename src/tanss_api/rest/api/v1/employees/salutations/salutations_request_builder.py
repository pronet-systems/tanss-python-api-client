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
    from .....models.salutations403_error import Salutations403Error
    from .item.salutations_item_request_builder import SalutationsItemRequestBuilder
    from .salutations_get_response import SalutationsGetResponse
    from .salutations_post_request_body import SalutationsPostRequestBody
    from .salutations_post_response import SalutationsPostResponse

class SalutationsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/employees/salutations
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new SalutationsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/employees/salutations", path_parameters)
    
    def by_id(self,id: str) -> SalutationsItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.v1.employees.salutations.item collection
        param id: Id of the salutation to delete.
        Returns: SalutationsItemRequestBuilder
        """
        if id is None:
            raise TypeError("id cannot be null.")
        from .item.salutations_item_request_builder import SalutationsItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["id"] = id
        return SalutationsItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[SalutationsGetResponse]:
        """
        Returns all salutations. Caller must be a technician or freelancer withthe `BASE_DATA_MANAGEMENT_SYSTEM_TABLES` permission.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[SalutationsGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .....models.salutations403_error import Salutations403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Salutations403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .salutations_get_response import SalutationsGetResponse

        return await self.request_adapter.send_async(request_info, SalutationsGetResponse, error_mapping)
    
    async def post(self,body: SalutationsPostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[SalutationsPostResponse]:
        """
        Creates a new salutation. Caller must be a technician or freelancer withthe `BASE_DATA_MANAGEMENT_SYSTEM_TABLES` permission.
        param body: Request body.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[SalutationsPostResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from .....models.salutations403_error import Salutations403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Salutations403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .salutations_post_response import SalutationsPostResponse

        return await self.request_adapter.send_async(request_info, SalutationsPostResponse, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Returns all salutations. Caller must be a technician or freelancer withthe `BASE_DATA_MANAGEMENT_SYSTEM_TABLES` permission.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: SalutationsPostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Creates a new salutation. Caller must be a technician or freelancer withthe `BASE_DATA_MANAGEMENT_SYSTEM_TABLES` permission.
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
    
    def with_url(self,raw_url: str) -> SalutationsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: SalutationsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return SalutationsRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class SalutationsRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class SalutationsRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

