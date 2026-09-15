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
    from ......models.properties403_error import Properties403Error
    from .properties_get_response import PropertiesGetResponse
    from .properties_post_request_body import PropertiesPostRequestBody
    from .properties_post_response import PropertiesPostResponse

class PropertiesRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/tickets/{-id}/properties
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new PropertiesRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/tickets/{%2Did}/properties{?property*,viewChecks*}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[PropertiesRequestBuilderGetQueryParameters]] = None) -> Optional[PropertiesGetResponse]:
        """
        Returns the form descriptor for displaying / editing a ticket: ticket data,field-level permissions, validation rules, and a fresh content hash. This isthe initial-load endpoint for the ticket form; subsequent re-renders triggeredby field changes go through `POST .../properties`. Returns 404 (or a mergedredirect) if the ticket no longer exists. The caller must have access to theticket.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[PropertiesGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ......models.properties403_error import Properties403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Properties403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .properties_get_response import PropertiesGetResponse

        return await self.request_adapter.send_async(request_info, PropertiesGetResponse, error_mapping)
    
    async def post(self,body: PropertiesPostRequestBody, request_configuration: Optional[RequestConfiguration[PropertiesRequestBuilderPostQueryParameters]] = None) -> Optional[PropertiesPostResponse]:
        """
        Re-renders the ticket form when a field value changes (or when displaying anot-yet-persisted ticket with `ticketId=0`). The body carries the currentin-flight ticket; `property` tells the server which field triggered therefresh so it can compute dependent fields, defaults, and validation messages.With `ticketId=0`, access is checked against the *merged* ticket data.
        param body: Request body.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[PropertiesPostResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ......models.properties403_error import Properties403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Properties403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .properties_post_response import PropertiesPostResponse

        return await self.request_adapter.send_async(request_info, PropertiesPostResponse, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[PropertiesRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Returns the form descriptor for displaying / editing a ticket: ticket data,field-level permissions, validation rules, and a fresh content hash. This isthe initial-load endpoint for the ticket form; subsequent re-renders triggeredby field changes go through `POST .../properties`. Returns 404 (or a mergedredirect) if the ticket no longer exists. The caller must have access to theticket.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: PropertiesPostRequestBody, request_configuration: Optional[RequestConfiguration[PropertiesRequestBuilderPostQueryParameters]] = None) -> RequestInformation:
        """
        Re-renders the ticket form when a field value changes (or when displaying anot-yet-persisted ticket with `ticketId=0`). The body carries the currentin-flight ticket; `property` tells the server which field triggered therefresh so it can compute dependent fields, defaults, and validation messages.With `ticketId=0`, access is checked against the *merged* ticket data.
        param body: Request body.
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
    
    def with_url(self,raw_url: str) -> PropertiesRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: PropertiesRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return PropertiesRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class PropertiesRequestBuilderGetQueryParameters():
        """
        Returns the form descriptor for displaying / editing a ticket: ticket data,field-level permissions, validation rules, and a fresh content hash. This isthe initial-load endpoint for the ticket form; subsequent re-renders triggeredby field changes go through `POST .../properties`. Returns 404 (or a mergedredirect) if the ticket no longer exists. The caller must have access to theticket.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "view_checks":
                return "viewChecks"
            return original_name
        
        # When true, also evaluate view-level visibility checks for the fields.
        view_checks: Optional[bool] = None

    
    @dataclass
    class PropertiesRequestBuilderGetRequestConfiguration(RequestConfiguration[PropertiesRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class PropertiesRequestBuilderPostQueryParameters():
        """
        Re-renders the ticket form when a field value changes (or when displaying anot-yet-persisted ticket with `ticketId=0`). The body carries the currentin-flight ticket; `property` tells the server which field triggered therefresh so it can compute dependent fields, defaults, and validation messages.With `ticketId=0`, access is checked against the *merged* ticket data.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "property_":
                return "property"
            if original_name == "view_checks":
                return "viewChecks"
            return original_name
        
        # Name of the field that triggered the re-render, so dependent fields can be recomputed.
        property_: Optional[str] = None

        # When true, also evaluate view-level visibility checks for the fields.
        view_checks: Optional[bool] = None

    
    @dataclass
    class PropertiesRequestBuilderPostRequestConfiguration(RequestConfiguration[PropertiesRequestBuilderPostQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

