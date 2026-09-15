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
    from .customers_get_response import CustomersGetResponse
    from .customers_post_request_body import CustomersPostRequestBody
    from .customers_post_response import CustomersPostResponse

class CustomersRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/systemhaus_one/v1/customers
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new CustomersRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/systemhaus_one/v1/customers", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[CustomersGetResponse]:
        """
        Proxy: leitet die Anfrage an die ERP-Kundenschnittstelle des PHP-Backends (api/v1/erp/customers) weiter.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: module, Rollen SYSTEMHAUS_ONE.Hinweise: Lizenz SAP_ONE erforderlich. Der komplette Query-String wird weitergereicht; Header Api-Key = Admin-Einstellung api.wawi.key. Timeout tanss.timeout (default 60 s); IO-Fehler -> TnsErpServiceCallException. Die Antwort ist die Roh-Antwort des PHP-Backends, NICHT im {meta,content}-Envelope; Parameter und Inhalt werden vom PHP-Backend bestimmt.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[CustomersGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .customers_get_response import CustomersGetResponse

        return await self.request_adapter.send_async(request_info, CustomersGetResponse, None)
    
    async def post(self,body: CustomersPostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[CustomersPostResponse]:
        """
        Proxy: leitet den Request-Body per POST an die ERP-Kundenschnittstelle des PHP-Backends (api/v1/erp/customers) weiter.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: module, Rollen SYSTEMHAUS_ONE.Hinweise: Lizenz SAP_ONE erforderlich. Body wird unverändert weitergereicht (Felder vom PHP-Backend definiert); Header Api-Key = api.wawi.key. Timeout tanss.timeout (default 60 s). Die Antwort ist die Roh-Antwort des PHP-Backends, kein {meta,content}-Envelope.
        param body: Beliebiges JSON, wird unverändert an das PHP-Backend weitergereicht.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[CustomersPostResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .customers_post_response import CustomersPostResponse

        return await self.request_adapter.send_async(request_info, CustomersPostResponse, None)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Proxy: leitet die Anfrage an die ERP-Kundenschnittstelle des PHP-Backends (api/v1/erp/customers) weiter.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: module, Rollen SYSTEMHAUS_ONE.Hinweise: Lizenz SAP_ONE erforderlich. Der komplette Query-String wird weitergereicht; Header Api-Key = Admin-Einstellung api.wawi.key. Timeout tanss.timeout (default 60 s); IO-Fehler -> TnsErpServiceCallException. Die Antwort ist die Roh-Antwort des PHP-Backends, NICHT im {meta,content}-Envelope; Parameter und Inhalt werden vom PHP-Backend bestimmt.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: CustomersPostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Proxy: leitet den Request-Body per POST an die ERP-Kundenschnittstelle des PHP-Backends (api/v1/erp/customers) weiter.Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft.Token: module, Rollen SYSTEMHAUS_ONE.Hinweise: Lizenz SAP_ONE erforderlich. Body wird unverändert weitergereicht (Felder vom PHP-Backend definiert); Header Api-Key = api.wawi.key. Timeout tanss.timeout (default 60 s). Die Antwort ist die Roh-Antwort des PHP-Backends, kein {meta,content}-Envelope.
        param body: Beliebiges JSON, wird unverändert an das PHP-Backend weitergereicht.
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
    
    def with_url(self,raw_url: str) -> CustomersRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: CustomersRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return CustomersRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class CustomersRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class CustomersRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

