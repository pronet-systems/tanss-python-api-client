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
    from ....models.checklists404_error import Checklists404Error
    from .action.action_request_builder import ActionRequestBuilder
    from .assignment.assignment_request_builder import AssignmentRequestBuilder
    from .check.check_request_builder import CheckRequestBuilder
    from .checklists_get_response import ChecklistsGetResponse
    from .copy.copy_request_builder import CopyRequestBuilder
    from .create_new_version.create_new_version_request_builder import CreateNewVersionRequestBuilder
    from .item.checklist_item_request_builder import ChecklistItemRequestBuilder

class ChecklistsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/checklists
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new ChecklistsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/checklists{?companyId*,departmentId*}", path_parameters)
    
    def by_checklist_id(self,checklist_id: int) -> ChecklistItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.v1.checklists.item collection
        param checklist_id: ID of the checklist.
        Returns: ChecklistItemRequestBuilder
        """
        if checklist_id is None:
            raise TypeError("checklist_id cannot be null.")
        from .item.checklist_item_request_builder import ChecklistItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["checklist%2Did"] = checklist_id
        return ChecklistItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[ChecklistsRequestBuilderGetQueryParameters]] = None) -> Optional[ChecklistsGetResponse]:
        """
        This route will get all checklists that can be selected i.e. to be assigned to a ticket
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ChecklistsGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ....models.checklists404_error import Checklists404Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "404": Checklists404Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .checklists_get_response import ChecklistsGetResponse

        return await self.request_adapter.send_async(request_info, ChecklistsGetResponse, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[ChecklistsRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        This route will get all checklists that can be selected i.e. to be assigned to a ticket
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> ChecklistsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: ChecklistsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return ChecklistsRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def action(self) -> ActionRequestBuilder:
        """
        The action property
        """
        from .action.action_request_builder import ActionRequestBuilder

        return ActionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def assignment(self) -> AssignmentRequestBuilder:
        """
        The assignment property
        """
        from .assignment.assignment_request_builder import AssignmentRequestBuilder

        return AssignmentRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def check(self) -> CheckRequestBuilder:
        """
        The check property
        """
        from .check.check_request_builder import CheckRequestBuilder

        return CheckRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def copy(self) -> CopyRequestBuilder:
        """
        The copy property
        """
        from .copy.copy_request_builder import CopyRequestBuilder

        return CopyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def create_new_version(self) -> CreateNewVersionRequestBuilder:
        """
        The createNewVersion property
        """
        from .create_new_version.create_new_version_request_builder import CreateNewVersionRequestBuilder

        return CreateNewVersionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class ChecklistsRequestBuilderGetQueryParameters():
        """
        This route will get all checklists that can be selected i.e. to be assigned to a ticket
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "company_id":
                return "companyId"
            if original_name == "department_id":
                return "departmentId"
            return original_name
        
        # (optional) company id to filter the checklists
        company_id: Optional[int] = None

        # (optional) department id to filter the checklists
        department_id: Optional[int] = None

    
    @dataclass
    class ChecklistsRequestBuilderGetRequestConfiguration(RequestConfiguration[ChecklistsRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

