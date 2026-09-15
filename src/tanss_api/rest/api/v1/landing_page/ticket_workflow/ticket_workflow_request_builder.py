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
    from .....models.ticket_workflow403_error import TicketWorkflow403Error
    from .ticket_workflow_get_response import TicketWorkflowGetResponse
    from .ticket_workflow_post_request_body import TicketWorkflowPostRequestBody
    from .ticket_workflow_post_response import TicketWorkflowPostResponse
    from .upload.upload_request_builder import UploadRequestBuilder

class TicketWorkflowRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/landingPage/ticketWorkflow
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new TicketWorkflowRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/landingPage/ticketWorkflow", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[TicketWorkflowGetResponse]:
        """
        Returns the form definition the public ticket-workflow landing page shouldrender (current step questions, ticket context, allowed inputs). This is theinitial-load call when an external user opens a workflow link.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[TicketWorkflowGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .....models.ticket_workflow403_error import TicketWorkflow403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": TicketWorkflow403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .ticket_workflow_get_response import TicketWorkflowGetResponse

        return await self.request_adapter.send_async(request_info, TicketWorkflowGetResponse, error_mapping)
    
    async def post(self,body: TicketWorkflowPostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[TicketWorkflowPostResponse]:
        """
        Submits the user's answers for the current workflow step. The service advancesthe workflow state machine and returns the next step's content (or thecompletion content if the workflow is finished).
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[TicketWorkflowPostResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from .....models.ticket_workflow403_error import TicketWorkflow403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": TicketWorkflow403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .ticket_workflow_post_response import TicketWorkflowPostResponse

        return await self.request_adapter.send_async(request_info, TicketWorkflowPostResponse, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Returns the form definition the public ticket-workflow landing page shouldrender (current step questions, ticket context, allowed inputs). This is theinitial-load call when an external user opens a workflow link.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: TicketWorkflowPostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Submits the user's answers for the current workflow step. The service advancesthe workflow state machine and returns the next step's content (or thecompletion content if the workflow is finished).
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
    
    def with_url(self,raw_url: str) -> TicketWorkflowRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: TicketWorkflowRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return TicketWorkflowRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def upload(self) -> UploadRequestBuilder:
        """
        The upload property
        """
        from .upload.upload_request_builder import UploadRequestBuilder

        return UploadRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class TicketWorkflowRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class TicketWorkflowRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

