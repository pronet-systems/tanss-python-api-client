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
    from ......models.titles403_error import Titles403Error
    from .titles_get_response import TitlesGetResponse
    from .titles_put_request_body import TitlesPutRequestBody
    from .titles_put_response import TitlesPutResponse

class TitlesItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/employees/titles/{id}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new TitlesItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/employees/titles/{id}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Deletes the employee title (e.g. "Dr.", "Prof.") identified by `id`. Callermust be a technician or freelancer with the `BASE_DATA_MANAGEMENT_SYSTEM_TABLES`permission.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ......models.titles403_error import Titles403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Titles403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[TitlesGetResponse]:
        """
        Returns a single employee title by id. Caller must be a technician orfreelancer with the `BASE_DATA_MANAGEMENT_SYSTEM_TABLES` permission.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[TitlesGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ......models.titles403_error import Titles403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Titles403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .titles_get_response import TitlesGetResponse

        return await self.request_adapter.send_async(request_info, TitlesGetResponse, error_mapping)
    
    async def put(self,body: TitlesPutRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[TitlesPutResponse]:
        """
        Updates an employee title. Caller must be a technician or freelancer withthe `BASE_DATA_MANAGEMENT_SYSTEM_TABLES` permission.
        param body: Request body.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[TitlesPutResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        from ......models.titles403_error import Titles403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Titles403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .titles_put_response import TitlesPutResponse

        return await self.request_adapter.send_async(request_info, TitlesPutResponse, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Deletes the employee title (e.g. "Dr.", "Prof.") identified by `id`. Callermust be a technician or freelancer with the `BASE_DATA_MANAGEMENT_SYSTEM_TABLES`permission.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Returns a single employee title by id. Caller must be a technician orfreelancer with the `BASE_DATA_MANAGEMENT_SYSTEM_TABLES` permission.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_put_request_information(self,body: TitlesPutRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Updates an employee title. Caller must be a technician or freelancer withthe `BASE_DATA_MANAGEMENT_SYSTEM_TABLES` permission.
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
    
    def with_url(self,raw_url: str) -> TitlesItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: TitlesItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return TitlesItemRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class TitlesItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class TitlesItemRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class TitlesItemRequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

