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
    from ......models.process404_error import Process404Error
    from .process_get_response import ProcessGetResponse

class ProcessRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/checklists/{checklist-id}/process
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new ProcessRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/checklists/{checklist%2Did}/process?linkId={linkId}&linkTypeId={linkTypeId}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[ProcessRequestBuilderGetQueryParameters]] = None) -> Optional[ProcessGetResponse]:
        """
        This route will be used for processing a checklist.It will fetch the checklist, along with all the values for the current assignment (i.e. ticket).If you want to process checklist, this is the main part for fetching all neccessary infos.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ProcessGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ......models.process404_error import Process404Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "404": Process404Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .process_get_response import ProcessGetResponse

        return await self.request_adapter.send_async(request_info, ProcessGetResponse, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[ProcessRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        This route will be used for processing a checklist.It will fetch the checklist, along with all the values for the current assignment (i.e. ticket).If you want to process checklist, this is the main part for fetching all neccessary infos.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> ProcessRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: ProcessRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return ProcessRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class ProcessRequestBuilderGetQueryParameters():
        """
        This route will be used for processing a checklist.It will fetch the checklist, along with all the values for the current assignment (i.e. ticket).If you want to process checklist, this is the main part for fetching all neccessary infos.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "link_id":
                return "linkId"
            if original_name == "link_type_id":
                return "linkTypeId"
            return original_name
        
        # id of the ticket
        link_id: Optional[int] = None

        # linkTypeId (11 = ticket)
        link_type_id: Optional[int] = None

    
    @dataclass
    class ProcessRequestBuilderGetRequestConfiguration(RequestConfiguration[ProcessRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

