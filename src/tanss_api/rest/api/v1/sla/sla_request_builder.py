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
    from ....models.sla403_error import Sla403Error
    from .conditions.conditions_request_builder import ConditionsRequestBuilder
    from .images.images_request_builder import ImagesRequestBuilder
    from .item.item_request_builder import ItemRequestBuilder
    from .permissions.permissions_request_builder import PermissionsRequestBuilder
    from .sla_get_response import SlaGetResponse
    from .sla_post_request_body import SlaPostRequestBody
    from .sla_post_response import SlaPostResponse
    from .sla_put_request_body import SlaPutRequestBody
    from .sla_put_response import SlaPutResponse
    from .sort.sort_request_builder import SortRequestBuilder

class SlaRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/sla
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new SlaRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/sla", path_parameters)
    
    def by_id(self,id: int) -> ItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.v1.sla.item collection
        param id: ID of the contract task.
        Returns: ItemRequestBuilder
        """
        if id is None:
            raise TypeError("id cannot be null.")
        from .item.item_request_builder import ItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["%2Did"] = id
        return ItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[SlaGetResponse]:
        """
        Returns every Service-Level-Agreement template configured in the system. SLAs are referenced by contracts and tickets to derive reaction and deadline times. Requires the SERVICE_LEVEL_AGREEMENT_ADMINISTRATION permission.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[SlaGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ....models.sla403_error import Sla403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Sla403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .sla_get_response import SlaGetResponse

        return await self.request_adapter.send_async(request_info, SlaGetResponse, error_mapping)
    
    async def post(self,body: SlaPostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[SlaPostResponse]:
        """
        Creates a new SLA template (name, image, reaction/deadline times, conditions are added separately). Requires the SERVICE_LEVEL_AGREEMENT_ADMINISTRATION permission and access to all companies.
        param body: Request body.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[SlaPostResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ....models.sla403_error import Sla403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Sla403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .sla_post_response import SlaPostResponse

        return await self.request_adapter.send_async(request_info, SlaPostResponse, error_mapping)
    
    async def put(self,body: SlaPutRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[SlaPutResponse]:
        """
        Returns SLAs filtered/sorted/paginated according to the configuration in the request body. The route is intended for the SLA administration list view; use GET for an unfiltered dump.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[SlaPutResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        from ....models.sla403_error import Sla403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Sla403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .sla_put_response import SlaPutResponse

        return await self.request_adapter.send_async(request_info, SlaPutResponse, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Returns every Service-Level-Agreement template configured in the system. SLAs are referenced by contracts and tickets to derive reaction and deadline times. Requires the SERVICE_LEVEL_AGREEMENT_ADMINISTRATION permission.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: SlaPostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Creates a new SLA template (name, image, reaction/deadline times, conditions are added separately). Requires the SERVICE_LEVEL_AGREEMENT_ADMINISTRATION permission and access to all companies.
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
    
    def to_put_request_information(self,body: SlaPutRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Returns SLAs filtered/sorted/paginated according to the configuration in the request body. The route is intended for the SLA administration list view; use GET for an unfiltered dump.
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
    
    def with_url(self,raw_url: str) -> SlaRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: SlaRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return SlaRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def conditions(self) -> ConditionsRequestBuilder:
        """
        The conditions property
        """
        from .conditions.conditions_request_builder import ConditionsRequestBuilder

        return ConditionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def images(self) -> ImagesRequestBuilder:
        """
        The images property
        """
        from .images.images_request_builder import ImagesRequestBuilder

        return ImagesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def permissions(self) -> PermissionsRequestBuilder:
        """
        The permissions property
        """
        from .permissions.permissions_request_builder import PermissionsRequestBuilder

        return PermissionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sort(self) -> SortRequestBuilder:
        """
        The sort property
        """
        from .sort.sort_request_builder import SortRequestBuilder

        return SortRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class SlaRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class SlaRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class SlaRequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

