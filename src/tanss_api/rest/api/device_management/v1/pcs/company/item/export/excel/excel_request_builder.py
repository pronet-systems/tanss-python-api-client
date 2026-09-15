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
    from .excel_get_response import ExcelGetResponse

class ExcelRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/deviceManagement/v1/pcs/company/{companyId}/export/excel
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new ExcelRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/deviceManagement/v1/pcs/company/{companyId}/export/excel", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[ExcelGetResponse]:
        """
        Exportiert die PC/Server-Liste einer Firma (und ihrer Filialen) als Excel-Arbeitsmappe (ein Sheet pro Firma/Filiale). Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft. Token: module, Rollen DEVICE_MANAGEMENT. Rechte: licModule DEVICEMANAGEMENT (7), VIEW_DEVICE_LISTS (1), EXPORT_PCS_TO_EXCEL (49), Firmenzugriff auf companyId. Hinweise: Alias-Pfad /api/v1/pcs/... existiert ebenfalls. Der Accept-Header steuert die Ausgabeform: application/msexcel liefert rohe XLSX-Bytes (Content-Disposition excel-pc-liste-{companyId}.xlsx), sonst TnsFilePassResponse im meta/content-Envelope. Sheets nur für Firmen, auf die der User Zugriff hat; enthält Server und PCs inkl. IPs/Garantie.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ExcelGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .excel_get_response import ExcelGetResponse

        return await self.request_adapter.send_async(request_info, ExcelGetResponse, None)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Exportiert die PC/Server-Liste einer Firma (und ihrer Filialen) als Excel-Arbeitsmappe (ein Sheet pro Firma/Filiale). Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft. Token: module, Rollen DEVICE_MANAGEMENT. Rechte: licModule DEVICEMANAGEMENT (7), VIEW_DEVICE_LISTS (1), EXPORT_PCS_TO_EXCEL (49), Firmenzugriff auf companyId. Hinweise: Alias-Pfad /api/v1/pcs/... existiert ebenfalls. Der Accept-Header steuert die Ausgabeform: application/msexcel liefert rohe XLSX-Bytes (Content-Disposition excel-pc-liste-{companyId}.xlsx), sonst TnsFilePassResponse im meta/content-Envelope. Sheets nur für Firmen, auf die der User Zugriff hat; enthält Server und PCs inkl. IPs/Garantie.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> ExcelRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: ExcelRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return ExcelRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class ExcelRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

