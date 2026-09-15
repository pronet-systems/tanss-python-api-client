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
    from .....models.participants403_error import Participants403Error
    from .....models.participants404_error import Participants404Error
    from .....models.tns_chat_participant import TnsChatParticipant
    from .participants_post_response import ParticipantsPostResponse

class ParticipantsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/chats/participants
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new ParticipantsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/chats/participants{?departmentId*}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[ParticipantsRequestBuilderDeleteQueryParameters]] = None) -> None:
        """
        Deletes a participant (employee or department) from a chat
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from .....models.participants403_error import Participants403Error
        from .....models.participants404_error import Participants404Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "404": Participants404Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def post(self,body: TnsChatParticipant, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[ParticipantsPostResponse]:
        """
        Adds a participant (employee or department) to a chat
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ParticipantsPostResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from .....models.participants403_error import Participants403Error
        from .....models.participants404_error import Participants404Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Participants403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .participants_post_response import ParticipantsPostResponse

        return await self.request_adapter.send_async(request_info, ParticipantsPostResponse, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[ParticipantsRequestBuilderDeleteQueryParameters]] = None) -> RequestInformation:
        """
        Deletes a participant (employee or department) from a chat
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, '{+baseurl}/api/v1/chats/participants?chatId={chatId}&employeeId={employeeId}{&departmentId*}', self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: TnsChatParticipant, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Adds a participant (employee or department) to a chat
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
    
    def with_url(self,raw_url: str) -> ParticipantsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: ParticipantsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return ParticipantsRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class ParticipantsRequestBuilderDeleteQueryParameters():
        """
        Deletes a participant (employee or department) from a chat
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "chat_id":
                return "chatId"
            if original_name == "department_id":
                return "departmentId"
            if original_name == "employee_id":
                return "employeeId"
            return original_name
        
        # Id of the chat
        chat_id: Optional[int] = None

        # ... or the id of the department
        department_id: Optional[int] = None

        # Either the id of the employee ...
        employee_id: Optional[int] = None

    
    @dataclass
    class ParticipantsRequestBuilderDeleteRequestConfiguration(RequestConfiguration[ParticipantsRequestBuilderDeleteQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class ParticipantsRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

