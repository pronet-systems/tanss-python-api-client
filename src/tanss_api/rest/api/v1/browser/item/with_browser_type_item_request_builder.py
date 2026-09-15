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
    from .....models.tns_browser_item import TnsBrowserItem
    from .item.browser_type_item_request_builder import BrowserTypeItemRequestBuilder
    from .with_browser_type_post_response import WithBrowserTypePostResponse

class WithBrowserTypeItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/browser/{browserType}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new WithBrowserTypeItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/browser/{browserType}", path_parameters)
    
    def by_id(self,id: int) -> BrowserTypeItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.v1.browser.item.item collection
        param id: ID des Elements (Softwarelizenz-Kategorie)
        Returns: BrowserTypeItemRequestBuilder
        """
        if id is None:
            raise TypeError("id cannot be null.")
        from .item.browser_type_item_request_builder import BrowserTypeItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["id"] = id
        return BrowserTypeItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def post(self,body: TnsBrowserItem, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[WithBrowserTypePostResponse]:
        """
        Legt im Kategorie-Browser ein neues Element an; praktisch nur für browserType SOFTWARELICENSE implementiert (erzeugt eine Softwarelizenz-Kategorie/TnsSoftwarelicenseType).Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId.Rechte: Lizenzmodul LICENSE_MANAGEMENT; SOFTWARELICENSES_CATEGORY_ADMINISTRATION; Benutzertyp TECHNICAN|COMPANY_ADMIN|RESTRICTED_USER|FREELANCER.Hinweise: browserType ist ein Enum; KNOWLEDGE_BASE, FILE_LINKS, DOCUMENT liefern TnsNotImplementedException, alle anderen INVALID_TYPE. Felder id, linkType, itemType, count, items werden ignoriert. Neue Kategorie wird active=true gesetzt. Antwort ist das unveränderte Request-Objekt (keine id). Filterstrategie STANDARD, Status CREATED.
        param body: Element des Kategorie-Browsers; derzeit nur für Softwarelizenz-Kategorien genutzt.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[WithBrowserTypePostResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .with_browser_type_post_response import WithBrowserTypePostResponse

        return await self.request_adapter.send_async(request_info, WithBrowserTypePostResponse, None)
    
    def to_post_request_information(self,body: TnsBrowserItem, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Legt im Kategorie-Browser ein neues Element an; praktisch nur für browserType SOFTWARELICENSE implementiert (erzeugt eine Softwarelizenz-Kategorie/TnsSoftwarelicenseType).Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId.Rechte: Lizenzmodul LICENSE_MANAGEMENT; SOFTWARELICENSES_CATEGORY_ADMINISTRATION; Benutzertyp TECHNICAN|COMPANY_ADMIN|RESTRICTED_USER|FREELANCER.Hinweise: browserType ist ein Enum; KNOWLEDGE_BASE, FILE_LINKS, DOCUMENT liefern TnsNotImplementedException, alle anderen INVALID_TYPE. Felder id, linkType, itemType, count, items werden ignoriert. Neue Kategorie wird active=true gesetzt. Antwort ist das unveränderte Request-Objekt (keine id). Filterstrategie STANDARD, Status CREATED.
        param body: Element des Kategorie-Browsers; derzeit nur für Softwarelizenz-Kategorien genutzt.
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
    
    def with_url(self,raw_url: str) -> WithBrowserTypeItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: WithBrowserTypeItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return WithBrowserTypeItemRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class WithBrowserTypeItemRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

