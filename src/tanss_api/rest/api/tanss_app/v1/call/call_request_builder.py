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
    from .call_post_request_body import CallPostRequestBody
    from .call_post_response import CallPostResponse
    from .item.with_call_item_request_builder import WithCallItemRequestBuilder

class CallRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/tanss.app/v1/call
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new CallRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/tanss.app/v1/call", path_parameters)
    
    def by_call_id(self,call_id: int) -> WithCallItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.tanssApp.v1.call.item collection
        param call_id: Numerische TANSS-id des Anrufs
        Returns: WithCallItemRequestBuilder
        """
        if call_id is None:
            raise TypeError("call_id cannot be null.")
        from .item.with_call_item_request_builder import WithCallItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["callId"] = call_id
        return WithCallItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def post(self,body: CallPostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[CallPostResponse]:
        """
        Legt einen Telefonanruf (TnsPhoneCall) an, fest vorbelegt mit group="TEAMS", telephoneSystemId=TELEPHONE_SYSTEM_TEAMS und aktivierter Duplikatpruefung der callId. Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft. Token: module, Rollen TANSS_APP. Rechte: Lizenz adl.TELEPHONE; bet.PHONE_LIST_COMPANY oder bet.PHONE_LIST_ALL_CALLS. Hinweise: Status CREATED. Doppelte callId im Telefonsystem TEAMS -> TnsDuplicateCallIdException. numberIdentifyState=UNIDENTIFIED -> automatische Rufnummern-Identifikation; IDENTIFIED -> Firmenzugriffspruefung (FORBIDDEN_NO_COMPANY_ACCESS). Rufnummern werden auf 50 Zeichen gekuerzt. id/group/telephoneSystemId werden serverseitig ueberschrieben. Auch unter /api/tanss.x/v1.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[CallPostResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .call_post_response import CallPostResponse

        return await self.request_adapter.send_async(request_info, CallPostResponse, None)
    
    def to_post_request_information(self,body: CallPostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Legt einen Telefonanruf (TnsPhoneCall) an, fest vorbelegt mit group="TEAMS", telephoneSystemId=TELEPHONE_SYSTEM_TEAMS und aktivierter Duplikatpruefung der callId. Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft. Token: module, Rollen TANSS_APP. Rechte: Lizenz adl.TELEPHONE; bet.PHONE_LIST_COMPANY oder bet.PHONE_LIST_ALL_CALLS. Hinweise: Status CREATED. Doppelte callId im Telefonsystem TEAMS -> TnsDuplicateCallIdException. numberIdentifyState=UNIDENTIFIED -> automatische Rufnummern-Identifikation; IDENTIFIED -> Firmenzugriffspruefung (FORBIDDEN_NO_COMPANY_ACCESS). Rufnummern werden auf 50 Zeichen gekuerzt. id/group/telephoneSystemId werden serverseitig ueberschrieben. Auch unter /api/tanss.x/v1.
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
    
    def with_url(self,raw_url: str) -> CallRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: CallRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return CallRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class CallRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

