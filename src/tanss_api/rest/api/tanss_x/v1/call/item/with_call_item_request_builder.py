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
    from .with_call_put_request_body import WithCallPutRequestBody
    from .with_call_put_response import WithCallPutResponse

class WithCallItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/tanss.x/v1/call/{callId}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new WithCallItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/tanss.x/v1/call/{callId}", path_parameters)
    
    async def put(self,body: WithCallPutRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[WithCallPutResponse]:
        """
        Aktualisiert einen bestehenden Telefonanruf per JSON-Merge (generischer Update).Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: module, Rollen TANSS_APP.Rechte: Lizenz TELEPHONE; PHONE_LIST_COMPANY; PHONE_LIST_ALL_CALLS.Hinweis: {callId} ist die numerische Datensatz-ID, nicht der callId-String. 404 wenn nicht vorhanden. Firmenzugriffs-Check (FORBIDDEN_NO_COMPANY_ACCESS) auf from/toCompanyId. Werden phoneParticipants mitgegeben, werden alle bestehenden Teilnehmer gelöscht und ersetzt. Status UPDATED.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[WithCallPutResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .with_call_put_response import WithCallPutResponse

        return await self.request_adapter.send_async(request_info, WithCallPutResponse, None)
    
    def to_put_request_information(self,body: WithCallPutRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Aktualisiert einen bestehenden Telefonanruf per JSON-Merge (generischer Update).Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: module, Rollen TANSS_APP.Rechte: Lizenz TELEPHONE; PHONE_LIST_COMPANY; PHONE_LIST_ALL_CALLS.Hinweis: {callId} ist die numerische Datensatz-ID, nicht der callId-String. 404 wenn nicht vorhanden. Firmenzugriffs-Check (FORBIDDEN_NO_COMPANY_ACCESS) auf from/toCompanyId. Werden phoneParticipants mitgegeben, werden alle bestehenden Teilnehmer gelöscht und ersetzt. Status UPDATED.
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
    
    def with_url(self,raw_url: str) -> WithCallItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: WithCallItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return WithCallItemRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class WithCallItemRequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

