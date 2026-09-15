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
    from ....models.tasks403_error import Tasks403Error
    from .item.tasks_item_request_builder import TasksItemRequestBuilder
    from .series.series_request_builder import SeriesRequestBuilder
    from .tasks_get_response import TasksGetResponse
    from .tasks_post_request_body import TasksPostRequestBody
    from .tasks_post_response import TasksPostResponse
    from .tasks_put_request_body import TasksPutRequestBody
    from .tasks_put_response import TasksPutResponse

class TasksRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/tasks
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new TasksRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/tasks", path_parameters)
    
    def by_id(self,id: int) -> TasksItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.v1.tasks.item collection
        param id: ID of the contract task.
        Returns: TasksItemRequestBuilder
        """
        if id is None:
            raise TypeError("id cannot be null.")
        from .item.tasks_item_request_builder import TasksItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["id"] = id
        return TasksItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[TasksGetResponse]:
        """
        Returns every contract task the caller is allowed to see. Contract tasks are recurring jobs attached to maintenance contracts (e.g. "quarterly server check"). Requires technician/freelancer role plus MAINTENANCE_CONTRACT_SHOW_TASKS and TASK_ADMINISTRATION.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[TasksGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ....models.tasks403_error import Tasks403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Tasks403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .tasks_get_response import TasksGetResponse

        return await self.request_adapter.send_async(request_info, TasksGetResponse, error_mapping)
    
    async def post(self,body: TasksPostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[TasksPostResponse]:
        """
        Creates a new contract task. Requires MAINTENANCE_CONTRACT_ADMINISTRATION and that the parent contract is not currently locked or edited by someone else.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[TasksPostResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ....models.tasks403_error import Tasks403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Tasks403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .tasks_post_response import TasksPostResponse

        return await self.request_adapter.send_async(request_info, TasksPostResponse, error_mapping)
    
    async def put(self,body: TasksPutRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[TasksPutResponse]:
        """
        Returns contract tasks filtered/paginated/sorted using the configuration in the request body. Permission checks are always forced to `true` server-side, so each row in the response respects the caller's actual rights.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[TasksPutResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        from ....models.tasks403_error import Tasks403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Tasks403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .tasks_put_response import TasksPutResponse

        return await self.request_adapter.send_async(request_info, TasksPutResponse, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Returns every contract task the caller is allowed to see. Contract tasks are recurring jobs attached to maintenance contracts (e.g. "quarterly server check"). Requires technician/freelancer role plus MAINTENANCE_CONTRACT_SHOW_TASKS and TASK_ADMINISTRATION.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: TasksPostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Creates a new contract task. Requires MAINTENANCE_CONTRACT_ADMINISTRATION and that the parent contract is not currently locked or edited by someone else.
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
    
    def to_put_request_information(self,body: TasksPutRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Returns contract tasks filtered/paginated/sorted using the configuration in the request body. Permission checks are always forced to `true` server-side, so each row in the response respects the caller's actual rights.
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
    
    def with_url(self,raw_url: str) -> TasksRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: TasksRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return TasksRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def series(self) -> SeriesRequestBuilder:
        """
        The series property
        """
        from .series.series_request_builder import SeriesRequestBuilder

        return SeriesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class TasksRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class TasksRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class TasksRequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

