from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from kiota_abstractions.default_query_parameters import QueryParameters
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.multipart_body import MultipartBody
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Optional, TYPE_CHECKING, Union
from warnings import warn

if TYPE_CHECKING:
    from .with_token_post_response import WithTokenPostResponse

class WithTokenItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/cloud/upload/{token}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new WithTokenItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/cloud/upload/{token}", path_parameters)
    
    async def post(self,body: MultipartBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[WithTokenPostResponse]:
        """
        Lädt Dateien über einen einmal gültigen CloudUpload-Token als interne Ticket-Dateien hoch.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: public, Rollen PUBLIC.Hinweise: permitAll (WebSecurity), Schutz nur durch Token. Fehler: UPLOADED_FILES_ARE_NULL, TOKEN_IS_NULL, NO_FILES_UPLOADED, INVALID_CLOUD_TOKEN (404, auch bei bereits benutztem Token), DUPLICATED_FILES, EMPTY_FILE, Gesamtgröße über Admin-Setting cloudupload.dateien_maximale_groesse -> TnsCloudUploadFileTooBigException. Token wird vor dem Speichern invalidiert. Pro Datei TnsTicketFiles (internal=true, Beschreibung CloudUpload) plus interner Ticket-Kommentar, Ticket attention=YES. meta CREATED.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[WithTokenPostResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .with_token_post_response import WithTokenPostResponse

        return await self.request_adapter.send_async(request_info, WithTokenPostResponse, None)
    
    def to_post_request_information(self,body: MultipartBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Lädt Dateien über einen einmal gültigen CloudUpload-Token als interne Ticket-Dateien hoch.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: public, Rollen PUBLIC.Hinweise: permitAll (WebSecurity), Schutz nur durch Token. Fehler: UPLOADED_FILES_ARE_NULL, TOKEN_IS_NULL, NO_FILES_UPLOADED, INVALID_CLOUD_TOKEN (404, auch bei bereits benutztem Token), DUPLICATED_FILES, EMPTY_FILE, Gesamtgröße über Admin-Setting cloudupload.dateien_maximale_groesse -> TnsCloudUploadFileTooBigException. Token wird vor dem Speichern invalidiert. Pro Datei TnsTicketFiles (internal=true, Beschreibung CloudUpload) plus interner Ticket-Kommentar, Ticket attention=YES. meta CREATED.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.POST, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "multipart/form-data", body)
        return request_info
    
    def with_url(self,raw_url: str) -> WithTokenItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: WithTokenItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return WithTokenItemRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class WithTokenItemRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

