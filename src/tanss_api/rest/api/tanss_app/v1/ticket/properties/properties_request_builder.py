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
    from ......models.ticket_save import TicketSave
    from .properties_post_response import PropertiesPostResponse

class PropertiesRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/tanss.app/v1/ticket/properties
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new PropertiesRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/tanss.app/v1/ticket/properties{?property*}", path_parameters)
    
    async def post(self,body: TicketSave, request_configuration: Optional[RequestConfiguration[PropertiesRequestBuilderPostQueryParameters]] = None) -> Optional[PropertiesPostResponse]:
        """
        Alias von POST /api/v1/tickets/0/properties (ticketId=0, viewChecks=false) - berechnet abhaengige Felder/Meta-Properties eines neuen Tickets nach Aenderung des Feldes property. Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft. Token: module, Rollen TANSS_APP. Hinweise: Auch unter /api/tanss.x/v1.
        param body: ticket model to be saved
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[PropertiesPostResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .properties_post_response import PropertiesPostResponse

        return await self.request_adapter.send_async(request_info, PropertiesPostResponse, None)
    
    def to_post_request_information(self,body: TicketSave, request_configuration: Optional[RequestConfiguration[PropertiesRequestBuilderPostQueryParameters]] = None) -> RequestInformation:
        """
        Alias von POST /api/v1/tickets/0/properties (ticketId=0, viewChecks=false) - berechnet abhaengige Felder/Meta-Properties eines neuen Tickets nach Aenderung des Feldes property. Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft. Token: module, Rollen TANSS_APP. Hinweise: Auch unter /api/tanss.x/v1.
        param body: ticket model to be saved
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
    class PropertiesRequestBuilderPostQueryParameters():
        """
        Alias von POST /api/v1/tickets/0/properties (ticketId=0, viewChecks=false) - berechnet abhaengige Felder/Meta-Properties eines neuen Tickets nach Aenderung des Feldes property. Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft. Token: module, Rollen TANSS_APP. Hinweise: Auch unter /api/tanss.x/v1.
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
            return original_name
        
        # Name des geaenderten Feldes
        property_: Optional[str] = None

    
    @dataclass
    class PropertiesRequestBuilderPostRequestConfiguration(RequestConfiguration[PropertiesRequestBuilderPostQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

