from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .configs.configs_request_builder import ConfigsRequestBuilder
    from .start_workflow.start_workflow_request_builder import StartWorkflowRequestBuilder

class WorkflowContractsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/workflowContracts
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new WorkflowContractsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/workflowContracts", path_parameters)
    
    @property
    def configs(self) -> ConfigsRequestBuilder:
        """
        The configs property
        """
        from .configs.configs_request_builder import ConfigsRequestBuilder

        return ConfigsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def start_workflow(self) -> StartWorkflowRequestBuilder:
        """
        The startWorkflow property
        """
        from .start_workflow.start_workflow_request_builder import StartWorkflowRequestBuilder

        return StartWorkflowRequestBuilder(self.request_adapter, self.path_parameters)
    

