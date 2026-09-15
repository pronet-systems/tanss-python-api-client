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
    from ........models.with_checklist404_error import WithChecklist404Error
    from .with_checklist_delete_response import WithChecklistDeleteResponse
    from .with_checklist_post_response import WithChecklistPostResponse
    from .with_checklist_put_response import WithChecklistPutResponse

class WithChecklistItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/checklists/assignment/{linkTypeId}/{linkId}/{checklistId}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new WithChecklistItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/checklists/assignment/{linkTypeId}/{linkId}/{checklistId}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[WithChecklistDeleteResponse]:
        """
        This route will remove a checklist checklist assignment from a ticket
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[WithChecklistDeleteResponse]
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ........models.with_checklist404_error import WithChecklist404Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "404": WithChecklist404Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .with_checklist_delete_response import WithChecklistDeleteResponse

        return await self.request_adapter.send_async(request_info, WithChecklistDeleteResponse, error_mapping)
    
    async def post(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[WithChecklistPostResponse]:
        """
        This route will assign a checklist to a ticket
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[WithChecklistPostResponse]
        """
        request_info = self.to_post_request_information(
            request_configuration
        )
        from ........models.with_checklist404_error import WithChecklist404Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "404": WithChecklist404Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .with_checklist_post_response import WithChecklistPostResponse

        return await self.request_adapter.send_async(request_info, WithChecklistPostResponse, error_mapping)
    
    async def put(self,request_configuration: Optional[RequestConfiguration[WithChecklistItemRequestBuilderPutQueryParameters]] = None) -> Optional[WithChecklistPutResponse]:
        """
        Verschiebt eine Checklisten-Zuordnung in der Reihenfolge (Rang) am verknuepften Objekt, indem sie mit der Zuordnung an Position rank+Offset getauscht wird.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId.Hinweise: Query 'rank' ist ein OFFSET (z.B. 1 oder -1), kein absoluter Rang: neuer Rang = aktueller Rang + rank; existiert an diesem Rang eine andere Zuordnung des gleichen Objekts, tauschen beide, sonst passiert nichts. Unbekannte Zuordnung -> keine Aenderung, trotzdem 200 mit Liste. Keine Rechtepruefung. meta=FOUND.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[WithChecklistPutResponse]
        """
        request_info = self.to_put_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .with_checklist_put_response import WithChecklistPutResponse

        return await self.request_adapter.send_async(request_info, WithChecklistPutResponse, None)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        This route will remove a checklist checklist assignment from a ticket
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        This route will assign a checklist to a ticket
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.POST, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_put_request_information(self,request_configuration: Optional[RequestConfiguration[WithChecklistItemRequestBuilderPutQueryParameters]] = None) -> RequestInformation:
        """
        Verschiebt eine Checklisten-Zuordnung in der Reihenfolge (Rang) am verknuepften Objekt, indem sie mit der Zuordnung an Position rank+Offset getauscht wird.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId.Hinweise: Query 'rank' ist ein OFFSET (z.B. 1 oder -1), kein absoluter Rang: neuer Rang = aktueller Rang + rank; existiert an diesem Rang eine andere Zuordnung des gleichen Objekts, tauschen beide, sonst passiert nichts. Unbekannte Zuordnung -> keine Aenderung, trotzdem 200 mit Liste. Keine Rechtepruefung. meta=FOUND.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.PUT, '{+baseurl}/api/v1/checklists/assignment/{linkTypeId}/{linkId}/{checklistId}?rank={rank}', self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> WithChecklistItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: WithChecklistItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return WithChecklistItemRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class WithChecklistItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class WithChecklistItemRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class WithChecklistItemRequestBuilderPutQueryParameters():
        """
        Verschiebt eine Checklisten-Zuordnung in der Reihenfolge (Rang) am verknuepften Objekt, indem sie mit der Zuordnung an Position rank+Offset getauscht wird.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId.Hinweise: Query 'rank' ist ein OFFSET (z.B. 1 oder -1), kein absoluter Rang: neuer Rang = aktueller Rang + rank; existiert an diesem Rang eine andere Zuordnung des gleichen Objekts, tauschen beide, sonst passiert nichts. Unbekannte Zuordnung -> keine Aenderung, trotzdem 200 mit Liste. Keine Rechtepruefung. meta=FOUND.
        """
        # Offset zum aktuellen Rang (z.B. 1 oder -1)
        rank: Optional[int] = None

    
    @dataclass
    class WithChecklistItemRequestBuilderPutRequestConfiguration(RequestConfiguration[WithChecklistItemRequestBuilderPutQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

