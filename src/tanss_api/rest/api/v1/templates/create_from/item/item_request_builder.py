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
    from ......models.four_zero_three_error import FourZeroThreeError
    from .item.id_item_request_builder import IdItemRequestBuilder
    from .post_request_body import PostRequestBody
    from .post_response import PostResponse

class ItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/templates/createFrom/{-id}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new ItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/templates/createFrom/{%2Did}", path_parameters)
    
    def by_id(self,id: int) -> IdItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.v1.templates.createFrom.item.item collection
        param id: Id of the persisted template to create a new entity from.
        Returns: IdItemRequestBuilder
        """
        if id is None:
            raise TypeError("id cannot be null.")
        from .item.id_item_request_builder import IdItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["id"] = id
        return IdItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def post(self,body: PostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[PostResponse]:
        """
        Creates a real entity (ticket, contract, document, ...) from the persisted template identified by `id`,using the supplied vars body to fill placeholder fields. Returns a objectwith the template `type` and the id of the newly-created entity.The caller must be permitted to create from this template — assignments and per-type permissions are checked.
        param body: Request body.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[PostResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ......models.four_zero_three_error import FourZeroThreeError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": FourZeroThreeError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .post_response import PostResponse

        return await self.request_adapter.send_async(request_info, PostResponse, error_mapping)
    
    def to_post_request_information(self,body: PostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Creates a real entity (ticket, contract, document, ...) from the persisted template identified by `id`,using the supplied vars body to fill placeholder fields. Returns a objectwith the template `type` and the id of the newly-created entity.The caller must be permitted to create from this template — assignments and per-type permissions are checked.
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
    
    def with_url(self,raw_url: str) -> ItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: ItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return ItemRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class ItemRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

