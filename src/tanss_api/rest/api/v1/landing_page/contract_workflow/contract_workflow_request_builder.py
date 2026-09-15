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
    from .....models.contract_workflow403_error import ContractWorkflow403Error
    from .contract_workflow_get_response import ContractWorkflowGetResponse
    from .contract_workflow_post_request_body import ContractWorkflowPostRequestBody
    from .contract_workflow_post_response import ContractWorkflowPostResponse
    from .pdf.pdf_request_builder import PdfRequestBuilder

class ContractWorkflowRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/landingPage/contractWorkflow
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new ContractWorkflowRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/landingPage/contractWorkflow", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[ContractWorkflowGetResponse]:
        """
        Returns the contract workflow landing page payload for the recipient identified by the workflow contract token currently stored in the request storage. The payload bundles the token, the underlying object, additional workflow info, and the filtered landing-page configuration (texts, layout flags, whether authorizators are required). Used by the public contract landing page rendered for the customer.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ContractWorkflowGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .....models.contract_workflow403_error import ContractWorkflow403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": ContractWorkflow403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .contract_workflow_get_response import ContractWorkflowGetResponse

        return await self.request_adapter.send_async(request_info, ContractWorkflowGetResponse, error_mapping)
    
    async def post(self,body: ContractWorkflowPostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[ContractWorkflowPostResponse]:
        """
        Submits the customer's response on the contract workflow landing page (company data, approver details, optional list of authorizator employees, accept type). The server validates the workflow token, persists the response, and returns the updated landing page content including a `landingPageSubmitResult` indicating the outcome (e.g. confirmation step or follow-up screen).
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ContractWorkflowPostResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from .....models.contract_workflow403_error import ContractWorkflow403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": ContractWorkflow403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .contract_workflow_post_response import ContractWorkflowPostResponse

        return await self.request_adapter.send_async(request_info, ContractWorkflowPostResponse, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Returns the contract workflow landing page payload for the recipient identified by the workflow contract token currently stored in the request storage. The payload bundles the token, the underlying object, additional workflow info, and the filtered landing-page configuration (texts, layout flags, whether authorizators are required). Used by the public contract landing page rendered for the customer.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: ContractWorkflowPostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Submits the customer's response on the contract workflow landing page (company data, approver details, optional list of authorizator employees, accept type). The server validates the workflow token, persists the response, and returns the updated landing page content including a `landingPageSubmitResult` indicating the outcome (e.g. confirmation step or follow-up screen).
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
    
    def with_url(self,raw_url: str) -> ContractWorkflowRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: ContractWorkflowRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return ContractWorkflowRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def pdf(self) -> PdfRequestBuilder:
        """
        The pdf property
        """
        from .pdf.pdf_request_builder import PdfRequestBuilder

        return PdfRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class ContractWorkflowRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class ContractWorkflowRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

