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
    from .todos_delete_response import TodosDeleteResponse
    from .todos_put_request_body import TodosPutRequestBody
    from .todos_put_response import TodosPutResponse

class TodosItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/todos/{id}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new TodosItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/todos/{id}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[TodosDeleteResponse]:
        """
        Löscht das TnsTodo-Objekt (Wurzelobjekt eines Mitarbeiters) mit der angegebenen ID.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId.Rechte: Besitzerprüfung todo.employeeId == aktueller User (FORBIDDEN_MISSING_PERMISSIONS).Hinweise: ENTITY_NOT_FOUND wenn ID unbekannt. Löscht die Wurzel, nicht ein einzelnes Item. meta DELETED.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[TodosDeleteResponse]
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .todos_delete_response import TodosDeleteResponse

        return await self.request_adapter.send_async(request_info, TodosDeleteResponse, None)
    
    async def put(self,body: TodosPutRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[TodosPutResponse]:
        """
        Aktualisiert das TnsTodo-Objekt (z.B. choosenListId, Listen) per JSON-Merge in die bestehende Entität.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId.Hinweise: ENTITY_NOT_FOUND wenn ID unbekannt; leeres JSON -> TnsJsonException. 'id' wird hier NICHT aus dem JSON entfernt. Keine Besitzerprüfung im Update-Pfad erkennbar. Listen werden nach dem Speichern über den Listen-Service nachgezogen. meta UPDATED.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[TodosPutResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .todos_put_response import TodosPutResponse

        return await self.request_adapter.send_async(request_info, TodosPutResponse, None)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Löscht das TnsTodo-Objekt (Wurzelobjekt eines Mitarbeiters) mit der angegebenen ID.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId.Rechte: Besitzerprüfung todo.employeeId == aktueller User (FORBIDDEN_MISSING_PERMISSIONS).Hinweise: ENTITY_NOT_FOUND wenn ID unbekannt. Löscht die Wurzel, nicht ein einzelnes Item. meta DELETED.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_put_request_information(self,body: TodosPutRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Aktualisiert das TnsTodo-Objekt (z.B. choosenListId, Listen) per JSON-Merge in die bestehende Entität.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId.Hinweise: ENTITY_NOT_FOUND wenn ID unbekannt; leeres JSON -> TnsJsonException. 'id' wird hier NICHT aus dem JSON entfernt. Keine Besitzerprüfung im Update-Pfad erkennbar. Listen werden nach dem Speichern über den Listen-Service nachgezogen. meta UPDATED.
        param body: The request body
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
    
    def with_url(self,raw_url: str) -> TodosItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: TodosItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return TodosItemRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class TodosItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class TodosItemRequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

