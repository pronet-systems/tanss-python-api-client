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
    from .....models.four_zero_three_error import FourZeroThreeError
    from .delete_response import DeleteResponse
    from .export.export_request_builder import ExportRequestBuilder
    from .get_response import GetResponse
    from .item.id_item_request_builder import IdItemRequestBuilder
    from .put_request_body import PutRequestBody
    from .put_response import PutResponse

class ItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/templates/{-id}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new ItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/templates/{%2Did}", path_parameters)
    
    def by_id(self,id: int) -> IdItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.v1.templates.item.item collection
        param id: Id of the existing entity to snapshot into a template.
        Returns: IdItemRequestBuilder
        """
        if id is None:
            raise TypeError("id cannot be null.")
        from .item.id_item_request_builder import IdItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["id"] = id
        return IdItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[DeleteResponse]:
        """
        Löscht eine Objektvorlage (TnsObjectTemplatePersist).Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId.Rechte: ADMINISTRATE_ALL_MAINTENANCE_CONTRACT_TEMPLATES oder Ersteller (createdByEmployeeId == aktueller User), sonst FORBIDDEN MUST_BE_CREATOR.Hinweise: id 0 -> BadRequest ID_MUST_BE_GIVEN; unbekannt -> TEMPLATE_DOESNT_EXIST bzw. ENTITY_NOT_FOUND. Löschung wird geloggt. meta DELETED.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[DeleteResponse]
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .delete_response import DeleteResponse

        return await self.request_adapter.send_async(request_info, DeleteResponse, None)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[GetResponse]:
        """
        Returns a single template by its id.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[GetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .....models.four_zero_three_error import FourZeroThreeError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": FourZeroThreeError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .get_response import GetResponse

        return await self.request_adapter.send_async(request_info, GetResponse, error_mapping)
    
    async def put(self,body: PutRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[PutResponse]:
        """
        Aktualisiert eine Objektvorlage: nur umbenennen (wenn nur 'name' gesendet wird) oder Vorlageninhalt inkl. Name/Felder ersetzen.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId.Rechte: typspezifische Prüfung; bei Typ CONTRACT ADMINISTRATE_ALL_MAINTENANCE_CONTRACT_TEMPLATES, sonst nur Ersteller (FORBIDDEN ONLY_CREATOR_CAN_UPDATE_TEMPLATE).Hinweise: Genau 1 Key (name) -> reines Umbenennen. Sonst wird das JSON als Template des vorhandenen Typs geparst und validiert; bei fremder tucId Matching-Prüfung (TnsForeignTemplateMissingMatchingsException) oder BadRequest TEMPLATE_MUST_BE_FROM_ANOTHER_SYSTEM. active/description werden aus dem Template übernommen. meta UPDATED.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[PutResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .put_response import PutResponse

        return await self.request_adapter.send_async(request_info, PutResponse, None)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Löscht eine Objektvorlage (TnsObjectTemplatePersist).Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId.Rechte: ADMINISTRATE_ALL_MAINTENANCE_CONTRACT_TEMPLATES oder Ersteller (createdByEmployeeId == aktueller User), sonst FORBIDDEN MUST_BE_CREATOR.Hinweise: id 0 -> BadRequest ID_MUST_BE_GIVEN; unbekannt -> TEMPLATE_DOESNT_EXIST bzw. ENTITY_NOT_FOUND. Löschung wird geloggt. meta DELETED.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Returns a single template by its id.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_put_request_information(self,body: PutRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Aktualisiert eine Objektvorlage: nur umbenennen (wenn nur 'name' gesendet wird) oder Vorlageninhalt inkl. Name/Felder ersetzen.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId.Rechte: typspezifische Prüfung; bei Typ CONTRACT ADMINISTRATE_ALL_MAINTENANCE_CONTRACT_TEMPLATES, sonst nur Ersteller (FORBIDDEN ONLY_CREATOR_CAN_UPDATE_TEMPLATE).Hinweise: Genau 1 Key (name) -> reines Umbenennen. Sonst wird das JSON als Template des vorhandenen Typs geparst und validiert; bei fremder tucId Matching-Prüfung (TnsForeignTemplateMissingMatchingsException) oder BadRequest TEMPLATE_MUST_BE_FROM_ANOTHER_SYSTEM. active/description werden aus dem Template übernommen. meta UPDATED.
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
    
    def with_url(self,raw_url: str) -> ItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: ItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return ItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def export(self) -> ExportRequestBuilder:
        """
        The export property
        """
        from .export.export_request_builder import ExportRequestBuilder

        return ExportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class ItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class ItemRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class ItemRequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

