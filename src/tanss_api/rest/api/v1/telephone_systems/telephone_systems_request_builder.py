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
    from ....models.telephone_systems403_error import TelephoneSystems403Error
    from .check.check_request_builder import CheckRequestBuilder
    from .intervals.intervals_request_builder import IntervalsRequestBuilder
    from .item.telephone_systems_item_request_builder import TelephoneSystemsItemRequestBuilder
    from .restart.restart_request_builder import RestartRequestBuilder
    from .telephone_systems_get_response import TelephoneSystemsGetResponse
    from .telephone_systems_post_request_body import TelephoneSystemsPostRequestBody
    from .telephone_systems_post_response import TelephoneSystemsPostResponse

class TelephoneSystemsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/telephoneSystems
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new TelephoneSystemsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/telephoneSystems", path_parameters)
    
    def by_id(self,id: int) -> TelephoneSystemsItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.v1.telephoneSystems.item collection
        param id: Id of the telephone system.
        Returns: TelephoneSystemsItemRequestBuilder
        """
        if id is None:
            raise TypeError("id cannot be null.")
        from .item.telephone_systems_item_request_builder import TelephoneSystemsItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["id"] = id
        return TelephoneSystemsItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[TelephoneSystemsGetResponse]:
        """
        Lists every configured telephone system (PBX adapter) used by the call-import background thread. Each entry is read from the `tanss.telephoneSystems.<id>.*` properties file and returned as a flat key/value map; entries are sorted by id. Requires technician/freelancer plus `ONLINE_SYSTEM_CONFIGURATION`.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[TelephoneSystemsGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ....models.telephone_systems403_error import TelephoneSystems403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": TelephoneSystems403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .telephone_systems_get_response import TelephoneSystemsGetResponse

        return await self.request_adapter.send_async(request_info, TelephoneSystemsGetResponse, error_mapping)
    
    async def post(self,body: TelephoneSystemsPostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[TelephoneSystemsPostResponse]:
        """
        Registers a new telephone-system config entry. `type` is mandatory and selects which field set is persisted (host, port, credentials, etc. depend on the PBX vendor). If `id` is omitted, the next free id is auto-assigned; if supplied, it must not collide with an existing entry. Requires technician/freelancer plus `ONLINE_SYSTEM_CONFIGURATION`.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[TelephoneSystemsPostResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ....models.telephone_systems403_error import TelephoneSystems403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": TelephoneSystems403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .telephone_systems_post_response import TelephoneSystemsPostResponse

        return await self.request_adapter.send_async(request_info, TelephoneSystemsPostResponse, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Lists every configured telephone system (PBX adapter) used by the call-import background thread. Each entry is read from the `tanss.telephoneSystems.<id>.*` properties file and returned as a flat key/value map; entries are sorted by id. Requires technician/freelancer plus `ONLINE_SYSTEM_CONFIGURATION`.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: TelephoneSystemsPostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Registers a new telephone-system config entry. `type` is mandatory and selects which field set is persisted (host, port, credentials, etc. depend on the PBX vendor). If `id` is omitted, the next free id is auto-assigned; if supplied, it must not collide with an existing entry. Requires technician/freelancer plus `ONLINE_SYSTEM_CONFIGURATION`.
        param body: The request body
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
    
    def with_url(self,raw_url: str) -> TelephoneSystemsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: TelephoneSystemsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return TelephoneSystemsRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def check(self) -> CheckRequestBuilder:
        """
        The check property
        """
        from .check.check_request_builder import CheckRequestBuilder

        return CheckRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def intervals(self) -> IntervalsRequestBuilder:
        """
        The intervals property
        """
        from .intervals.intervals_request_builder import IntervalsRequestBuilder

        return IntervalsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def restart(self) -> RestartRequestBuilder:
        """
        The restart property
        """
        from .restart.restart_request_builder import RestartRequestBuilder

        return RestartRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class TelephoneSystemsRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class TelephoneSystemsRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

