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
    from .collections_post_request_body import CollectionsPostRequestBody
    from .collections_post_response import CollectionsPostResponse
    from .item.with_collection_item_request_builder import WithCollectionItemRequestBuilder

class CollectionsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/managementDashboard/collections
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new CollectionsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/managementDashboard/collections", path_parameters)
    
    def by_collection_id(self,collection_id: int) -> WithCollectionItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.v1.managementDashboard.collections.item collection
        param collection_id: ID der Collection
        Returns: WithCollectionItemRequestBuilder
        """
        if collection_id is None:
            raise TypeError("collection_id cannot be null.")
        from .item.with_collection_item_request_builder import WithCollectionItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["collectionId"] = collection_id
        return WithCollectionItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def post(self,body: CollectionsPostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[CollectionsPostResponse]:
        """
        Legt eine neue Dashboard-Collection für den aktuellen Benutzer an.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId.Rechte: interner Benutzer; Recht MANAGEMENT_DASHBOARD; Modul-Feature managementDashboard/DASHBOARD.Hinweise: id und userId aus dem Body werden überschrieben (id=0, userId=aktueller Benutzer). Ungültiger visibilityType wird stillschweigend ignoriert. Sichtbarkeiten werden nur bei visibilityType=EVERYBODY gespeichert. Antwort-Status CREATED.
        param body: Gelesene Keys der neuen Collection
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[CollectionsPostResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .collections_post_response import CollectionsPostResponse

        return await self.request_adapter.send_async(request_info, CollectionsPostResponse, None)
    
    def to_post_request_information(self,body: CollectionsPostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Legt eine neue Dashboard-Collection für den aktuellen Benutzer an.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId.Rechte: interner Benutzer; Recht MANAGEMENT_DASHBOARD; Modul-Feature managementDashboard/DASHBOARD.Hinweise: id und userId aus dem Body werden überschrieben (id=0, userId=aktueller Benutzer). Ungültiger visibilityType wird stillschweigend ignoriert. Sichtbarkeiten werden nur bei visibilityType=EVERYBODY gespeichert. Antwort-Status CREATED.
        param body: Gelesene Keys der neuen Collection
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
    
    def with_url(self,raw_url: str) -> CollectionsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: CollectionsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return CollectionsRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class CollectionsRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

