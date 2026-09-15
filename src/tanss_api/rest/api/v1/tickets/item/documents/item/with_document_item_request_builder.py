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
    from .......models.with_document403_error import WithDocument403Error
    from .with_document_delete_response import WithDocumentDeleteResponse
    from .with_document_get_response import WithDocumentGetResponse
    from .with_document_put_request_body import WithDocumentPutRequestBody
    from .with_document_put_response import WithDocumentPutResponse

class WithDocumentItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/tickets/{-id}/documents/{documentId}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new WithDocumentItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/tickets/{%2Did}/documents/{documentId}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[WithDocumentDeleteResponse]:
        """
        Löscht ein Ticket-Dokument (Datei + Datensatz) und schreibt einen Ticket-Log-Eintrag.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId.Rechte: Firmenzugriff auf das Ticket; Dokument-Eigentümer (employeeId == Benutzer) ODER Recht EDIT_AND_DELETE_ALL_COMMENTS.Hinweise: 400 OBJECT_NOT_FOUND, wenn das Dokument nicht zum Ticket gehört; 400 ID_MUST_BE_POSITIVE bei IDs <= 0; FORBIDDEN CANT_MODIFY_DOCUMENT bei fehlendem Recht; CANNOT_DELETE_FILES, wenn das Löschen fehlschlägt. Antwort-Status DELETED.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[WithDocumentDeleteResponse]
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .with_document_delete_response import WithDocumentDeleteResponse

        return await self.request_adapter.send_async(request_info, WithDocumentDeleteResponse, None)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[WithDocumentGetResponse]:
        """
        This call will produce a direct download link for downloading this document.The generated url can only be used once withing 15 minutes.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[WithDocumentGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .......models.with_document403_error import WithDocument403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": WithDocument403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .with_document_get_response import WithDocumentGetResponse

        return await self.request_adapter.send_async(request_info, WithDocumentGetResponse, error_mapping)
    
    async def put(self,body: WithDocumentPutRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[WithDocumentPutResponse]:
        """
        Aktualisiert Metadaten eines Ticket-Dokuments (z.B. Beschreibung, intern-Flag).Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId.Rechte: Firmenzugriff auf das Ticket.Hinweise: JSON wird per Jackson in das bestehende Dokument gemergt; id, ticketId, fileName, date, employeeId dürfen nicht abweichen (Fehler TnsCantModifyJsonFieldException). 400 JSON_IS_NULL / ID_MUST_BE_POSITIVE; 404 DATA_NOT_FOUND bei unbekanntem Dokument. Kein Eigentümer-Check beim Update. Antwort-Status UPDATED.
        param body: Änderbare Felder des Dokuments (JSON-Merge)
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[WithDocumentPutResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .with_document_put_response import WithDocumentPutResponse

        return await self.request_adapter.send_async(request_info, WithDocumentPutResponse, None)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Löscht ein Ticket-Dokument (Datei + Datensatz) und schreibt einen Ticket-Log-Eintrag.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId.Rechte: Firmenzugriff auf das Ticket; Dokument-Eigentümer (employeeId == Benutzer) ODER Recht EDIT_AND_DELETE_ALL_COMMENTS.Hinweise: 400 OBJECT_NOT_FOUND, wenn das Dokument nicht zum Ticket gehört; 400 ID_MUST_BE_POSITIVE bei IDs <= 0; FORBIDDEN CANT_MODIFY_DOCUMENT bei fehlendem Recht; CANNOT_DELETE_FILES, wenn das Löschen fehlschlägt. Antwort-Status DELETED.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        This call will produce a direct download link for downloading this document.The generated url can only be used once withing 15 minutes.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_put_request_information(self,body: WithDocumentPutRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Aktualisiert Metadaten eines Ticket-Dokuments (z.B. Beschreibung, intern-Flag).Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId.Rechte: Firmenzugriff auf das Ticket.Hinweise: JSON wird per Jackson in das bestehende Dokument gemergt; id, ticketId, fileName, date, employeeId dürfen nicht abweichen (Fehler TnsCantModifyJsonFieldException). 400 JSON_IS_NULL / ID_MUST_BE_POSITIVE; 404 DATA_NOT_FOUND bei unbekanntem Dokument. Kein Eigentümer-Check beim Update. Antwort-Status UPDATED.
        param body: Änderbare Felder des Dokuments (JSON-Merge)
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
    
    def with_url(self,raw_url: str) -> WithDocumentItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: WithDocumentItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return WithDocumentItemRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class WithDocumentItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class WithDocumentItemRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class WithDocumentItemRequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

