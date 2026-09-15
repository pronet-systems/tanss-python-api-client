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
    from .with_item_put_request_body import WithItemPutRequestBody
    from .with_item_put_response import WithItemPutResponse

class WithItemItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/portal/profiles/items/{itemId}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new WithItemItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/portal/profiles/items/{itemId}", path_parameters)
    
    async def put(self,body: WithItemPutRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[WithItemPutResponse]:
        """
        Aktualisiert ein einzelnes Item (Box) eines Portal-Profils, z.B. Spalte/Position/Status. Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft. Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId. Rechte: Besitzerprüfung, das Profil muss dem aktuellen User gehören. Hinweise: Keys id und profileId werden entfernt. ENTITY_NOT_FOUND wenn itemId unbekannt. Vor dem Update MISSING_PORTAL_ID / PORTAL_DOESNT_EXIST / Forbidden, wenn das zugehörige Profil nicht existiert oder nicht dem angemeldeten Mitarbeiter gehört. Antwort meta UPDATED.
        param body: Zu ändernde Felder des Items (Merge)
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[WithItemPutResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .with_item_put_response import WithItemPutResponse

        return await self.request_adapter.send_async(request_info, WithItemPutResponse, None)
    
    def to_put_request_information(self,body: WithItemPutRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Aktualisiert ein einzelnes Item (Box) eines Portal-Profils, z.B. Spalte/Position/Status. Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft. Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId. Rechte: Besitzerprüfung, das Profil muss dem aktuellen User gehören. Hinweise: Keys id und profileId werden entfernt. ENTITY_NOT_FOUND wenn itemId unbekannt. Vor dem Update MISSING_PORTAL_ID / PORTAL_DOESNT_EXIST / Forbidden, wenn das zugehörige Profil nicht existiert oder nicht dem angemeldeten Mitarbeiter gehört. Antwort meta UPDATED.
        param body: Zu ändernde Felder des Items (Merge)
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
    
    def with_url(self,raw_url: str) -> WithItemItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: WithItemItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return WithItemItemRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class WithItemItemRequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

