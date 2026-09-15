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
    from .....models.tns_vacation_request import TnsVacationRequest
    from .....models.vacation_requests403_error import VacationRequests403Error
    from .pdf.pdf_request_builder import PdfRequestBuilder
    from .vacation_requests_get_response import VacationRequestsGetResponse
    from .vacation_requests_put_response import VacationRequestsPutResponse

class VacationRequestsItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/vacationRequests/{id}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new VacationRequestsItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/vacationRequests/{id}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        deletes a vacation request
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from .....models.vacation_requests403_error import VacationRequests403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": VacationRequests403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[VacationRequestsGetResponse]:
        """
        Liefert einen einzelnen Urlaubs-/Abwesenheitsantrag inkl. Tagen und Genehmigungsschritten.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId.Rechte: Benutzertyp TECHNICAN, COMPANY_ADMIN, RESTRICTED_USER oder FREELANCER; Recht VACATION_AND_ABSENCE_STANDARD_ACCESS (166); Lizenzmodul VACATION (sonst TnsModuleNotLicensedException).Hinweise: Nicht gefunden -> OBJECT_NOT_FOUND (vor dem Rechte-Check). Kein Besitzer-/Vorgesetzten-Check: jeder mit Recht 166 kann beliebige Antraege lesen. days werden nachgeladen, next/currentApprovalProcessStep aus processId/processStepId ermittelt. Bei planningType ILLNESS wird der Antrag maskiert (planningType -> ABSENCE, requestReason/supervisorReason leer), wenn der Aufrufer die Krankheitsdaten des Antragstellers nicht sehen darf. Filter TnsSupport/STANDARD. meta=FOUND.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[VacationRequestsGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .vacation_requests_get_response import VacationRequestsGetResponse

        return await self.request_adapter.send_async(request_info, VacationRequestsGetResponse, None)
    
    async def put(self,body: TnsVacationRequest, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[VacationRequestsPutResponse]:
        """
        updates a vacation request
        param body: vacation request (or illness, absence, custom type, overtime, standBy, custom). If a custom type shall be stored, use the planningAdditionalId property to specify the custom type
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[VacationRequestsPutResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        from .....models.vacation_requests403_error import VacationRequests403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": VacationRequests403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .vacation_requests_put_response import VacationRequestsPutResponse

        return await self.request_adapter.send_async(request_info, VacationRequestsPutResponse, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        deletes a vacation request
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Liefert einen einzelnen Urlaubs-/Abwesenheitsantrag inkl. Tagen und Genehmigungsschritten.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId.Rechte: Benutzertyp TECHNICAN, COMPANY_ADMIN, RESTRICTED_USER oder FREELANCER; Recht VACATION_AND_ABSENCE_STANDARD_ACCESS (166); Lizenzmodul VACATION (sonst TnsModuleNotLicensedException).Hinweise: Nicht gefunden -> OBJECT_NOT_FOUND (vor dem Rechte-Check). Kein Besitzer-/Vorgesetzten-Check: jeder mit Recht 166 kann beliebige Antraege lesen. days werden nachgeladen, next/currentApprovalProcessStep aus processId/processStepId ermittelt. Bei planningType ILLNESS wird der Antrag maskiert (planningType -> ABSENCE, requestReason/supervisorReason leer), wenn der Aufrufer die Krankheitsdaten des Antragstellers nicht sehen darf. Filter TnsSupport/STANDARD. meta=FOUND.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_put_request_information(self,body: TnsVacationRequest, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        updates a vacation request
        param body: vacation request (or illness, absence, custom type, overtime, standBy, custom). If a custom type shall be stored, use the planningAdditionalId property to specify the custom type
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
    
    def with_url(self,raw_url: str) -> VacationRequestsItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: VacationRequestsItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return VacationRequestsItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def pdf(self) -> PdfRequestBuilder:
        """
        The pdf property
        """
        from .pdf.pdf_request_builder import PdfRequestBuilder

        return PdfRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class VacationRequestsItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class VacationRequestsItemRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class VacationRequestsItemRequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

