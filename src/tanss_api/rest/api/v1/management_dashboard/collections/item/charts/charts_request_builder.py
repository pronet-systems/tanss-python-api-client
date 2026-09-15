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
    from .charts_post_request_body import ChartsPostRequestBody
    from .charts_post_response import ChartsPostResponse
    from .item.with_chart_item_request_builder import WithChartItemRequestBuilder

class ChartsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/managementDashboard/collections/{collectionId}/charts
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new ChartsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/managementDashboard/collections/{collectionId}/charts", path_parameters)
    
    def by_chart_id(self,chart_id: int) -> WithChartItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.v1.managementDashboard.collections.item.charts.item collection
        param chart_id: ID des Charts
        Returns: WithChartItemRequestBuilder
        """
        if chart_id is None:
            raise TypeError("chart_id cannot be null.")
        from .item.with_chart_item_request_builder import WithChartItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["chartId"] = chart_id
        return WithChartItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def post(self,body: ChartsPostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[ChartsPostResponse]:
        """
        Legt ein neues Chart in einer eigenen Dashboard-Collection an (inkl. Filter).Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId.Rechte: interner Benutzer; Recht MANAGEMENT_DASHBOARD; Modul-Feature managementDashboard/DASHBOARD; Eigentümer-Check der Collection.Hinweise: id (→0) und collectionId (→Pfad) werden überschrieben. 404 bei unbekannter Collection. Ungültige Enum-Werte werden ignoriert; Filter wird nur geparst, wenn type gesetzt ist. Antwort-Status CREATED.
        param body: Gelesene Keys des neuen Charts
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ChartsPostResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .charts_post_response import ChartsPostResponse

        return await self.request_adapter.send_async(request_info, ChartsPostResponse, None)
    
    def to_post_request_information(self,body: ChartsPostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Legt ein neues Chart in einer eigenen Dashboard-Collection an (inkl. Filter).Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId.Rechte: interner Benutzer; Recht MANAGEMENT_DASHBOARD; Modul-Feature managementDashboard/DASHBOARD; Eigentümer-Check der Collection.Hinweise: id (→0) und collectionId (→Pfad) werden überschrieben. 404 bei unbekannter Collection. Ungültige Enum-Werte werden ignoriert; Filter wird nur geparst, wenn type gesetzt ist. Antwort-Status CREATED.
        param body: Gelesene Keys des neuen Charts
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
    
    def with_url(self,raw_url: str) -> ChartsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: ChartsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return ChartsRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class ChartsRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

