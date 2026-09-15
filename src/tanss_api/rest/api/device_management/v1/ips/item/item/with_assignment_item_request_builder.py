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
    from .with_assignment_get_response import WithAssignmentGetResponse
    from .with_assignment_post_request_body import WithAssignmentPostRequestBody
    from .with_assignment_post_response import WithAssignmentPostResponse

class WithAssignmentItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/deviceManagement/v1/ips/{id}/{assignmentId}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new WithAssignmentItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/deviceManagement/v1/ips/{id}/{assignmentId}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[WithAssignmentGetResponse]:
        """
        Liefert alle IP/MAC-Einträge eines PCs oder Peripheriegeräts.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: module, Rollen DEVICE_MANAGEMENT.Rechte: Entity-Zugriff auf PC (Linktyp 1) bzw. Peripherie (Linktyp 4); kein MANAGE_DEVICES nötig.Hinweise: Alias-Pfad /api/v1/ips/{assignmentType}/{assignmentId}. assignmentType PC|PERIPHERY; andere Werte 403 IPMAC_HAS_INVALID_ASSIGNMENT_TYPE. Keine Filterstrategie.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[WithAssignmentGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .with_assignment_get_response import WithAssignmentGetResponse

        return await self.request_adapter.send_async(request_info, WithAssignmentGetResponse, None)
    
    async def post(self,body: WithAssignmentPostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[WithAssignmentPostResponse]:
        """
        Legt einen neuen IP/MAC-Eintrag für einen PC oder ein Peripheriegerät an.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: module, Rollen DEVICE_MANAGEMENT.Rechte: MANAGE_DEVICES; Entity-Zugriff auf PC (Linktyp 1) bzw. Peripherie (Linktyp 4).Hinweise: Alias-Pfad /api/v1/ips/{assignmentType}/{assignmentId}. id, assignmentId, assignmentType im Body werden entfernt (Zuordnung kommt aus dem Pfad). Anlage wird im PC-/Peripherie-Log protokolliert. Status CREATED.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[WithAssignmentPostResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .with_assignment_post_response import WithAssignmentPostResponse

        return await self.request_adapter.send_async(request_info, WithAssignmentPostResponse, None)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Liefert alle IP/MAC-Einträge eines PCs oder Peripheriegeräts.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: module, Rollen DEVICE_MANAGEMENT.Rechte: Entity-Zugriff auf PC (Linktyp 1) bzw. Peripherie (Linktyp 4); kein MANAGE_DEVICES nötig.Hinweise: Alias-Pfad /api/v1/ips/{assignmentType}/{assignmentId}. assignmentType PC|PERIPHERY; andere Werte 403 IPMAC_HAS_INVALID_ASSIGNMENT_TYPE. Keine Filterstrategie.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: WithAssignmentPostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Legt einen neuen IP/MAC-Eintrag für einen PC oder ein Peripheriegerät an.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: module, Rollen DEVICE_MANAGEMENT.Rechte: MANAGE_DEVICES; Entity-Zugriff auf PC (Linktyp 1) bzw. Peripherie (Linktyp 4).Hinweise: Alias-Pfad /api/v1/ips/{assignmentType}/{assignmentId}. id, assignmentId, assignmentType im Body werden entfernt (Zuordnung kommt aus dem Pfad). Anlage wird im PC-/Peripherie-Log protokolliert. Status CREATED.
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
    
    def with_url(self,raw_url: str) -> WithAssignmentItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: WithAssignmentItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return WithAssignmentItemRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class WithAssignmentItemRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class WithAssignmentItemRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

