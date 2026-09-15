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
    from .item.with_type_item_request_builder import WithTypeItemRequestBuilder
    from .types_get_response import TypesGetResponse
    from .types_post_request_body import TypesPostRequestBody
    from .types_post_response import TypesPostResponse

class TypesRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/deviceManagement/v1/peripheries/types
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new TypesRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/deviceManagement/v1/peripheries/types", path_parameters)
    
    def by_type_id(self,type_id: int) -> WithTypeItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.deviceManagement.v1.peripheries.types.item collection
        param type_id: ID des Peripherie-Typs
        Returns: WithTypeItemRequestBuilder
        """
        if type_id is None:
            raise TypeError("type_id cannot be null.")
        from .item.with_type_item_request_builder import WithTypeItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["typeId"] = type_id
        return WithTypeItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[TypesGetResponse]:
        """
        Liefert alle Peripherie-Typen.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt (dort nur der Alias /api/v1/peripheries/types); vom Server so umgesetzt, gegen 10.10 geprueft.Token: module, Rollen DEVICE_MANAGEMENT.Hinweise: Kein Rechte-/Lizenz-Check. Antwortobjekte enthalten zusätzlich price (float).
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[TypesGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .types_get_response import TypesGetResponse

        return await self.request_adapter.send_async(request_info, TypesGetResponse, None)
    
    async def post(self,body: TypesPostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[TypesPostResponse]:
        """
        Legt einen neuen Peripherie-Typ an.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt (dort nur der Alias /api/v1/peripheries/types); vom Server so umgesetzt, gegen 10.10 geprueft.Token: module, Rollen DEVICE_MANAGEMENT.Rechte: BASE_DATA_MANAGEMENT_TECHNICAL_SECTION(68); securityManager.long() (Benutzertyp TECHNICAN/COMPANY_ADMIN/RESTRICTED_USER/FREELANCER).Hinweise: id im Body wird entfernt. Leerer name -> 400 PERIPHERY_TYPE_EMPTY; name LIKE vorhandener -> 400 PERIPHERY_TYPE_WITH_NAME_ALREADY_EXISTS. Leerer Body -> TnsJsonException.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[TypesPostResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .types_post_response import TypesPostResponse

        return await self.request_adapter.send_async(request_info, TypesPostResponse, None)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Liefert alle Peripherie-Typen.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt (dort nur der Alias /api/v1/peripheries/types); vom Server so umgesetzt, gegen 10.10 geprueft.Token: module, Rollen DEVICE_MANAGEMENT.Hinweise: Kein Rechte-/Lizenz-Check. Antwortobjekte enthalten zusätzlich price (float).
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: TypesPostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Legt einen neuen Peripherie-Typ an.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt (dort nur der Alias /api/v1/peripheries/types); vom Server so umgesetzt, gegen 10.10 geprueft.Token: module, Rollen DEVICE_MANAGEMENT.Rechte: BASE_DATA_MANAGEMENT_TECHNICAL_SECTION(68); securityManager.long() (Benutzertyp TECHNICAN/COMPANY_ADMIN/RESTRICTED_USER/FREELANCER).Hinweise: id im Body wird entfernt. Leerer name -> 400 PERIPHERY_TYPE_EMPTY; name LIKE vorhandener -> 400 PERIPHERY_TYPE_WITH_NAME_ALREADY_EXISTS. Leerer Body -> TnsJsonException.
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
    
    def with_url(self,raw_url: str) -> TypesRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: TypesRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return TypesRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class TypesRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class TypesRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

