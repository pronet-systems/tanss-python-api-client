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
    from .item.todos_item_request_builder import TodosItemRequestBuilder
    from .todos_get_response import TodosGetResponse

class TodosRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/todos
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new TodosRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/todos", path_parameters)
    
    def by_id(self,id: int) -> TodosItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.v1.todos.item collection
        param id: Id des TnsTodo-Objekts.
        Returns: TodosItemRequestBuilder
        """
        if id is None:
            raise TypeError("id cannot be null.")
        from .item.todos_item_request_builder import TodosItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["id"] = id
        return TodosItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[TodosGetResponse]:
        """
        Liefert die persönliche ToDo-Struktur (TnsTodo) des angemeldeten Mitarbeiters inkl. Listen und Items; legt sie bei Erstaufruf automatisch an.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId.Rechte: Besitzerprüfung todo.employeeId == aktueller User (sonst FORBIDDEN_MISSING_PERMISSIONS).Hinweise: Fehlt das Todo, wird ein neues mit choosenListId=-1 angelegt (Seiteneffekt). Pro Item wird die PopUp-Notification (Typ 30) eingehängt. meta FOUND.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[TodosGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .todos_get_response import TodosGetResponse

        return await self.request_adapter.send_async(request_info, TodosGetResponse, None)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Liefert die persönliche ToDo-Struktur (TnsTodo) des angemeldeten Mitarbeiters inkl. Listen und Items; legt sie bei Erstaufruf automatisch an.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId.Rechte: Besitzerprüfung todo.employeeId == aktueller User (sonst FORBIDDEN_MISSING_PERMISSIONS).Hinweise: Fehlt das Todo, wird ein neues mit choosenListId=-1 angelegt (Seiteneffekt). Pro Item wird die PopUp-Notification (Typ 30) eingehängt. meta FOUND.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> TodosRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: TodosRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return TodosRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class TodosRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

