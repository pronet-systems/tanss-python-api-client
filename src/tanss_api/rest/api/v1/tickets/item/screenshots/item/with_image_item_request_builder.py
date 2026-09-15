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
    from .......models.with_image403_error import WithImage403Error
    from .with_image_delete_response import WithImageDeleteResponse
    from .with_image_get_response import WithImageGetResponse
    from .with_image_put_request_body import WithImagePutRequestBody
    from .with_image_put_response import WithImagePutResponse

class WithImageItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/tickets/{-id}/screenshots/{imageId}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new WithImageItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/tickets/{%2Did}/screenshots/{imageId}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[WithImageDeleteResponse]:
        """
        Löscht einen Ticket-Screenshot (Bilddatei + Datensatz) und schreibt einen Ticket-Log-Eintrag.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId.Rechte: Firmenzugriff auf das Ticket; Screenshot-Eigentümer (employeeId == Benutzer) ODER Recht EDIT_AND_DELETE_ALL_COMMENTS.Hinweise: 400 OBJECT_NOT_FOUND, wenn der Screenshot nicht zum Ticket gehört; 400 ID_MUST_BE_POSITIVE; FORBIDDEN CANT_MODIFY_SCREENSHOT; CANNOT_DELETE_FILES bei Fehlschlag. Antwort-Status DELETED. In der Basis-Spezifikation heißt der Pfadparameter imageId.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[WithImageDeleteResponse]
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .with_image_delete_response import WithImageDeleteResponse

        return await self.request_adapter.send_async(request_info, WithImageDeleteResponse, None)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[WithImageGetResponse]:
        """
        This call will produce a direct download link for downloading this image.The generated url can only be used once withing 15 minutes.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[WithImageGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .......models.with_image403_error import WithImage403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": WithImage403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .with_image_get_response import WithImageGetResponse

        return await self.request_adapter.send_async(request_info, WithImageGetResponse, error_mapping)
    
    async def put(self,body: WithImagePutRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[WithImagePutResponse]:
        """
        Aktualisiert Metadaten eines Ticket-Screenshots (z.B. Beschreibung, intern-Flag).Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId.Rechte: Firmenzugriff auf das Ticket.Hinweise: JSON wird per Jackson in das bestehende Bild gemergt; id, ticketId, fileName, date, employeeId dürfen nicht abweichen (Fehler TnsCantModifyJsonFieldException). 400 JSON_IS_NULL / ID_MUST_BE_POSITIVE; 404 DATA_NOT_FOUND. Kein Eigentümer-Check beim Update. Antwort-Status UPDATED. In der Basis-Spezifikation heißt der Pfadparameter imageId.
        param body: Änderbare Felder des Screenshots (JSON-Merge)
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[WithImagePutResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .with_image_put_response import WithImagePutResponse

        return await self.request_adapter.send_async(request_info, WithImagePutResponse, None)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Löscht einen Ticket-Screenshot (Bilddatei + Datensatz) und schreibt einen Ticket-Log-Eintrag.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId.Rechte: Firmenzugriff auf das Ticket; Screenshot-Eigentümer (employeeId == Benutzer) ODER Recht EDIT_AND_DELETE_ALL_COMMENTS.Hinweise: 400 OBJECT_NOT_FOUND, wenn der Screenshot nicht zum Ticket gehört; 400 ID_MUST_BE_POSITIVE; FORBIDDEN CANT_MODIFY_SCREENSHOT; CANNOT_DELETE_FILES bei Fehlschlag. Antwort-Status DELETED. In der Basis-Spezifikation heißt der Pfadparameter imageId.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        This call will produce a direct download link for downloading this image.The generated url can only be used once withing 15 minutes.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_put_request_information(self,body: WithImagePutRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Aktualisiert Metadaten eines Ticket-Screenshots (z.B. Beschreibung, intern-Flag).Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId.Rechte: Firmenzugriff auf das Ticket.Hinweise: JSON wird per Jackson in das bestehende Bild gemergt; id, ticketId, fileName, date, employeeId dürfen nicht abweichen (Fehler TnsCantModifyJsonFieldException). 400 JSON_IS_NULL / ID_MUST_BE_POSITIVE; 404 DATA_NOT_FOUND. Kein Eigentümer-Check beim Update. Antwort-Status UPDATED. In der Basis-Spezifikation heißt der Pfadparameter imageId.
        param body: Änderbare Felder des Screenshots (JSON-Merge)
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
    
    def with_url(self,raw_url: str) -> WithImageItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: WithImageItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return WithImageItemRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class WithImageItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class WithImageItemRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class WithImageItemRequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

