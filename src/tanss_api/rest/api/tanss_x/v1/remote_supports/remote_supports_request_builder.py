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
    from .remote_supports_post_request_body import RemoteSupportsPostRequestBody
    from .remote_supports_post_response import RemoteSupportsPostResponse
    from .systems.systems_request_builder import SystemsRequestBuilder

class RemoteSupportsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/tanss.x/v1/remoteSupports
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new RemoteSupportsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/tanss.x/v1/remoteSupports", path_parameters)
    
    async def post(self,body: RemoteSupportsPostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[RemoteSupportsPostResponse]:
        """
        Legt einen Fernwartungs-Datensatz (TnsRemoteMaintenance) an.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: module, Rollen TANSS_APP.Rechte: Lizenz REMOTE.Hinweis: Auch unter /api/tanss.app/v1. Enthält das JWT eine Bindung an ein externes Remote-System, wird typeId aus dem Token überschrieben; ist extProgram nicht TANSS_APP, muss typeId zum Token passen (403 TOKEN_IS_FOR_OTHER_REMOTE_SUPPORT_API). 403 TYPE_GREATER_1000 / TYPE_DOESNT_EXIST. Ist companyId=0 und deviceId gesetzt, werden companyId/linkTypeId/linkId aus der Geräte-Zuordnung ermittelt; ist employeeId=0 und userId gesetzt, wird employeeId aus der Benutzer-Zuordnung ermittelt. Verknüpfte Entitäten in meta.linkedEntities. Status CREATED.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[RemoteSupportsPostResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .remote_supports_post_response import RemoteSupportsPostResponse

        return await self.request_adapter.send_async(request_info, RemoteSupportsPostResponse, None)
    
    def to_post_request_information(self,body: RemoteSupportsPostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Legt einen Fernwartungs-Datensatz (TnsRemoteMaintenance) an.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: module, Rollen TANSS_APP.Rechte: Lizenz REMOTE.Hinweis: Auch unter /api/tanss.app/v1. Enthält das JWT eine Bindung an ein externes Remote-System, wird typeId aus dem Token überschrieben; ist extProgram nicht TANSS_APP, muss typeId zum Token passen (403 TOKEN_IS_FOR_OTHER_REMOTE_SUPPORT_API). 403 TYPE_GREATER_1000 / TYPE_DOESNT_EXIST. Ist companyId=0 und deviceId gesetzt, werden companyId/linkTypeId/linkId aus der Geräte-Zuordnung ermittelt; ist employeeId=0 und userId gesetzt, wird employeeId aus der Benutzer-Zuordnung ermittelt. Verknüpfte Entitäten in meta.linkedEntities. Status CREATED.
        param body: The request body
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
    
    def with_url(self,raw_url: str) -> RemoteSupportsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: RemoteSupportsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return RemoteSupportsRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def systems(self) -> SystemsRequestBuilder:
        """
        The systems property
        """
        from .systems.systems_request_builder import SystemsRequestBuilder

        return SystemsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class RemoteSupportsRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

