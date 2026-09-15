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
    from .check.check_request_builder import CheckRequestBuilder
    from .reserved.reserved_request_builder import ReservedRequestBuilder
    from .rooms_get_response import RoomsGetResponse

class RoomsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/ev/rooms
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new RoomsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/ev/rooms?capacity={capacity}&duration={duration}&start={start}&support={support}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[RoomsRequestBuilderGetQueryParameters]] = None) -> Optional[RoomsGetResponse]:
        """
        Liefert die in Coero verfügbaren Räume für Start/Dauer/Kapazität (optional bezogen auf einen Support).Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId.Rechte: Firmenzugriff auf Support-Firma (nur wenn support != 0).Hinweise: Alle vier Query-Parameter Pflicht; support=0 überspringt den Support-Check. Proxy auf Coero GET /api/v1/tns/rooms/. Bei nicht erreichbarem Coero leere Liste.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[RoomsGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .rooms_get_response import RoomsGetResponse

        return await self.request_adapter.send_async(request_info, RoomsGetResponse, None)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[RoomsRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Liefert die in Coero verfügbaren Räume für Start/Dauer/Kapazität (optional bezogen auf einen Support).Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId.Rechte: Firmenzugriff auf Support-Firma (nur wenn support != 0).Hinweise: Alle vier Query-Parameter Pflicht; support=0 überspringt den Support-Check. Proxy auf Coero GET /api/v1/tns/rooms/. Bei nicht erreichbarem Coero leere Liste.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> RoomsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: RoomsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return RoomsRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def check(self) -> CheckRequestBuilder:
        """
        The check property
        """
        from .check.check_request_builder import CheckRequestBuilder

        return CheckRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def reserved(self) -> ReservedRequestBuilder:
        """
        The reserved property
        """
        from .reserved.reserved_request_builder import ReservedRequestBuilder

        return ReservedRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class RoomsRequestBuilderGetQueryParameters():
        """
        Liefert die in Coero verfügbaren Räume für Start/Dauer/Kapazität (optional bezogen auf einen Support).Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: general, Rollen USER. TANSS_APP-Token nur mit loggedInUserId.Rechte: Firmenzugriff auf Support-Firma (nur wenn support != 0).Hinweise: Alle vier Query-Parameter Pflicht; support=0 überspringt den Support-Check. Proxy auf Coero GET /api/v1/tns/rooms/. Bei nicht erreichbarem Coero leere Liste.
        """
        # Benötigte Kapazität
        capacity: Optional[int] = None

        # Dauer
        duration: Optional[int] = None

        # Startzeitpunkt (Unix-Timestamp)
        start: Optional[int] = None

        # Support-ID (0 = ohne Support-Bezug)
        support: Optional[int] = None

    
    @dataclass
    class RoomsRequestBuilderGetRequestConfiguration(RequestConfiguration[RoomsRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

