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
    from ......models.tns_browser_item import TnsBrowserItem
    from .browser_type_delete_response import BrowserTypeDeleteResponse
    from .browser_type_get_response import BrowserTypeGetResponse
    from .browser_type_put_response import BrowserTypePutResponse

class BrowserTypeItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/browser/{browserType}/{id}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new BrowserTypeItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/browser/{browserType}/{id}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[BrowserTypeDeleteResponse]:
        """
        Löscht ein Element im Kategorie-Browser; nur für browserType SOFTWARELICENSE implementiert (löscht eine Softwarelizenz-Kategorie).Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId.Rechte: Lizenzmodul LICENSE_MANAGEMENT; SOFTWARELICENSES_CATEGORY_ADMINISTRATION; Benutzertyp TECHNICAN|COMPANY_ADMIN|RESTRICTED_USER|FREELANCER.Hinweise: KNOWLEDGE_BASE/FILE_LINKS/DOCUMENT liefern TnsNotImplementedException, andere INVALID_TYPE. Status DELETED ohne content.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[BrowserTypeDeleteResponse]
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .browser_type_delete_response import BrowserTypeDeleteResponse

        return await self.request_adapter.send_async(request_info, BrowserTypeDeleteResponse, None)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[BrowserTypeGetResponse]:
        """
        Liefert ein einzelnes Element des Kategorie-Browsers; nur für browserType SOFTWARELICENSE implementiert (Softwarelizenz-Kategorie).Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId.Rechte: Lizenzmodul LICENSE_MANAGEMENT; SOFTWARELICENSES_CATEGORY_ADMINISTRATION; Benutzertyp TECHNICAN|COMPANY_ADMIN|RESTRICTED_USER|FREELANCER.Hinweise: KNOWLEDGE_BASE/FILE_LINKS/DOCUMENT liefern TnsNotImplementedException, andere INVALID_TYPE. 404 OBJECT_WITH_ID_CANT_FOUND. Filterstrategie DETAIL.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[BrowserTypeGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .browser_type_get_response import BrowserTypeGetResponse

        return await self.request_adapter.send_async(request_info, BrowserTypeGetResponse, None)
    
    async def put(self,body: TnsBrowserItem, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[BrowserTypePutResponse]:
        """
        Aktualisiert ein Element im Kategorie-Browser; nur für browserType SOFTWARELICENSE implementiert (Softwarelizenz-Kategorie).Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId.Rechte: Lizenzmodul LICENSE_MANAGEMENT; SOFTWARELICENSES_CATEGORY_ADMINISTRATION; Benutzertyp TECHNICAN|COMPANY_ADMIN|RESTRICTED_USER|FREELANCER.Hinweise: Kein Teil-Update: es wird ein neues TnsSoftwarelicenseType mit id aus dem Pfad, active=true und den Body-Werten gespeichert (nicht gesendete Felder werden überschrieben). Andere Typen NotImplemented/INVALID_TYPE. Antwort ist das Request-Objekt. Filterstrategie STANDARD, Status UPDATED.
        param body: Element des Kategorie-Browsers; derzeit nur für Softwarelizenz-Kategorien genutzt.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[BrowserTypePutResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .browser_type_put_response import BrowserTypePutResponse

        return await self.request_adapter.send_async(request_info, BrowserTypePutResponse, None)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Löscht ein Element im Kategorie-Browser; nur für browserType SOFTWARELICENSE implementiert (löscht eine Softwarelizenz-Kategorie).Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId.Rechte: Lizenzmodul LICENSE_MANAGEMENT; SOFTWARELICENSES_CATEGORY_ADMINISTRATION; Benutzertyp TECHNICAN|COMPANY_ADMIN|RESTRICTED_USER|FREELANCER.Hinweise: KNOWLEDGE_BASE/FILE_LINKS/DOCUMENT liefern TnsNotImplementedException, andere INVALID_TYPE. Status DELETED ohne content.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Liefert ein einzelnes Element des Kategorie-Browsers; nur für browserType SOFTWARELICENSE implementiert (Softwarelizenz-Kategorie).Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId.Rechte: Lizenzmodul LICENSE_MANAGEMENT; SOFTWARELICENSES_CATEGORY_ADMINISTRATION; Benutzertyp TECHNICAN|COMPANY_ADMIN|RESTRICTED_USER|FREELANCER.Hinweise: KNOWLEDGE_BASE/FILE_LINKS/DOCUMENT liefern TnsNotImplementedException, andere INVALID_TYPE. 404 OBJECT_WITH_ID_CANT_FOUND. Filterstrategie DETAIL.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_put_request_information(self,body: TnsBrowserItem, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Aktualisiert ein Element im Kategorie-Browser; nur für browserType SOFTWARELICENSE implementiert (Softwarelizenz-Kategorie).Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId.Rechte: Lizenzmodul LICENSE_MANAGEMENT; SOFTWARELICENSES_CATEGORY_ADMINISTRATION; Benutzertyp TECHNICAN|COMPANY_ADMIN|RESTRICTED_USER|FREELANCER.Hinweise: Kein Teil-Update: es wird ein neues TnsSoftwarelicenseType mit id aus dem Pfad, active=true und den Body-Werten gespeichert (nicht gesendete Felder werden überschrieben). Andere Typen NotImplemented/INVALID_TYPE. Antwort ist das Request-Objekt. Filterstrategie STANDARD, Status UPDATED.
        param body: Element des Kategorie-Browsers; derzeit nur für Softwarelizenz-Kategorien genutzt.
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
    
    def with_url(self,raw_url: str) -> BrowserTypeItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: BrowserTypeItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return BrowserTypeItemRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class BrowserTypeItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class BrowserTypeItemRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class BrowserTypeItemRequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

