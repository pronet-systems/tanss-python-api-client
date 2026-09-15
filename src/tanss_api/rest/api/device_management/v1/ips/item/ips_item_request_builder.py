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
    from .ips_delete_response import IpsDeleteResponse
    from .ips_put_request_body import IpsPutRequestBody
    from .ips_put_response import IpsPutResponse
    from .item.with_assignment_item_request_builder import WithAssignmentItemRequestBuilder

class IpsItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/deviceManagement/v1/ips/{id}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new IpsItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/deviceManagement/v1/ips/{id}", path_parameters)
    
    def by_assignment_id(self,assignment_id: int) -> WithAssignmentItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.deviceManagement.v1.ips.item.item collection
        param assignment_id: ID des PCs bzw. Peripheriegeräts
        Returns: WithAssignmentItemRequestBuilder
        """
        if assignment_id is None:
            raise TypeError("assignment_id cannot be null.")
        from .item.with_assignment_item_request_builder import WithAssignmentItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["assignmentId"] = assignment_id
        return WithAssignmentItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[IpsDeleteResponse]:
        """
        Löscht eine IP/MAC-Zuordnung eines PCs oder Peripheriegeräts.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: module, Rollen DEVICE_MANAGEMENT.Rechte: MANAGE_DEVICES; Entity-Zugriff auf zugeordneten PC (Linktyp 1) bzw. Peripherie (Linktyp 4).Hinweise: Alias-Pfad /api/v1/ips/{id}. id ist long. 404 ENTITY_NOT_FOUND wenn nicht vorhanden. Löschung wird im PC-/Peripherie-Log protokolliert. Status DELETED ohne content.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[IpsDeleteResponse]
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .ips_delete_response import IpsDeleteResponse

        return await self.request_adapter.send_async(request_info, IpsDeleteResponse, None)
    
    async def put(self,body: IpsPutRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[IpsPutResponse]:
        """
        Aktualisiert eine IP/MAC-Zuordnung per Teil-Update.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: module, Rollen DEVICE_MANAGEMENT.Rechte: MANAGE_DEVICES; Entity-Zugriff auf zugeordneten PC (Linktyp 1) bzw. Peripherie (Linktyp 4).Hinweise: Alias-Pfad /api/v1/ips/{id}. Zuordnung (assignmentType/-Id) kann nicht umgehängt werden; id, assignmentId, assignmentType im Body werden ignoriert. Änderungen werden im PC-/Peripherie-Log protokolliert. 404 ENTITY_NOT_FOUND. Status UPDATED.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[IpsPutResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .ips_put_response import IpsPutResponse

        return await self.request_adapter.send_async(request_info, IpsPutResponse, None)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Löscht eine IP/MAC-Zuordnung eines PCs oder Peripheriegeräts.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: module, Rollen DEVICE_MANAGEMENT.Rechte: MANAGE_DEVICES; Entity-Zugriff auf zugeordneten PC (Linktyp 1) bzw. Peripherie (Linktyp 4).Hinweise: Alias-Pfad /api/v1/ips/{id}. id ist long. 404 ENTITY_NOT_FOUND wenn nicht vorhanden. Löschung wird im PC-/Peripherie-Log protokolliert. Status DELETED ohne content.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_put_request_information(self,body: IpsPutRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Aktualisiert eine IP/MAC-Zuordnung per Teil-Update.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: module, Rollen DEVICE_MANAGEMENT.Rechte: MANAGE_DEVICES; Entity-Zugriff auf zugeordneten PC (Linktyp 1) bzw. Peripherie (Linktyp 4).Hinweise: Alias-Pfad /api/v1/ips/{id}. Zuordnung (assignmentType/-Id) kann nicht umgehängt werden; id, assignmentId, assignmentType im Body werden ignoriert. Änderungen werden im PC-/Peripherie-Log protokolliert. 404 ENTITY_NOT_FOUND. Status UPDATED.
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
    
    def with_url(self,raw_url: str) -> IpsItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: IpsItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return IpsItemRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class IpsItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class IpsItemRequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

