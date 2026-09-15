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
    from .....models.checklist403_error import Checklist403Error
    from .checklist_get_response import ChecklistGetResponse
    from .checklist_put_request_body import ChecklistPutRequestBody
    from .checklist_put_response import ChecklistPutResponse
    from .convert.convert_request_builder import ConvertRequestBuilder
    from .process.process_request_builder import ProcessRequestBuilder

class ChecklistItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/checklists/{checklist-id}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new ChecklistItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/checklists/{checklist%2Did}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Deletes a checklist template along with its items, multi-select options, events and actions. Requires the DELETE_PROCESSES permission; a checklist that has a successor (i.e. a newer version) cannot be deleted.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from .....models.checklist403_error import Checklist403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Checklist403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[ChecklistGetResponse]:
        """
        Loads a checklist in edit-mode — all fields (including hidden/disabled ones) are returned so that an administrator can modify the template. For the read-only processing view used inside a ticket, use the `/process` endpoint instead.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ChecklistGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .....models.checklist403_error import Checklist403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Checklist403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .checklist_get_response import ChecklistGetResponse

        return await self.request_adapter.send_async(request_info, ChecklistGetResponse, error_mapping)
    
    async def put(self,body: ChecklistPutRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[ChecklistPutResponse]:
        """
        Updates an existing checklist template. The JSON body is merged using the "checked rights" mechanism — only fields the caller is allowed to change will be applied, anything else is silently ignored.
        param body: Request body.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ChecklistPutResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        from .....models.checklist403_error import Checklist403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Checklist403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .checklist_put_response import ChecklistPutResponse

        return await self.request_adapter.send_async(request_info, ChecklistPutResponse, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Deletes a checklist template along with its items, multi-select options, events and actions. Requires the DELETE_PROCESSES permission; a checklist that has a successor (i.e. a newer version) cannot be deleted.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Loads a checklist in edit-mode — all fields (including hidden/disabled ones) are returned so that an administrator can modify the template. For the read-only processing view used inside a ticket, use the `/process` endpoint instead.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_put_request_information(self,body: ChecklistPutRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Updates an existing checklist template. The JSON body is merged using the "checked rights" mechanism — only fields the caller is allowed to change will be applied, anything else is silently ignored.
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
    
    def with_url(self,raw_url: str) -> ChecklistItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: ChecklistItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return ChecklistItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def convert(self) -> ConvertRequestBuilder:
        """
        The convert property
        """
        from .convert.convert_request_builder import ConvertRequestBuilder

        return ConvertRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def process(self) -> ProcessRequestBuilder:
        """
        The process property
        """
        from .process.process_request_builder import ProcessRequestBuilder

        return ProcessRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class ChecklistItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class ChecklistItemRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class ChecklistItemRequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

