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
    from .....models.external_ids403_error import ExternalIds403Error
    from .external_ids_post_request_body import ExternalIdsPostRequestBody
    from .external_ids_post_response import ExternalIdsPostResponse
    from .external_ids_put_request_body import ExternalIdsPutRequestBody
    from .external_ids_put_response import ExternalIdsPutResponse

class ExternalIdsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/systemhaus_one/v1/externalIds
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new ExternalIdsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/systemhaus_one/v1/externalIds", path_parameters)
    
    async def post(self,body: ExternalIdsPostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[ExternalIdsPostResponse]:
        """
        Creates a new mapping between a TANSS entity (identified by `linkTypeId`/`linkId`) and its external identifier in the connected SAP Business One system. Intended for the SAP B1 ERP integration — must be called with the dedicated API token bound to the role `SYSTEMHAUS_ONE`, not a normal user login; the `SAP_ONE` module must be licensed.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ExternalIdsPostResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from .....models.external_ids403_error import ExternalIds403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": ExternalIds403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .external_ids_post_response import ExternalIdsPostResponse

        return await self.request_adapter.send_async(request_info, ExternalIdsPostResponse, error_mapping)
    
    async def put(self,body: ExternalIdsPutRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[ExternalIdsPutResponse]:
        """
        Returns the external identifiers (SAP B1 IDs) for the TANSS entities listed in the request body (link type plus a list of link IDs). Uses `PUT` so that the variable-length list of IDs can be supplied as a JSON body rather than a long query string. Intended for the SAP B1 ERP integration — must be called with the dedicated API token bound to the role `SYSTEMHAUS_ONE`, not a normal user login; the `SAP_ONE` module must be licensed.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ExternalIdsPutResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        from .....models.external_ids403_error import ExternalIds403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": ExternalIds403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .external_ids_put_response import ExternalIdsPutResponse

        return await self.request_adapter.send_async(request_info, ExternalIdsPutResponse, error_mapping)
    
    def to_post_request_information(self,body: ExternalIdsPostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Creates a new mapping between a TANSS entity (identified by `linkTypeId`/`linkId`) and its external identifier in the connected SAP Business One system. Intended for the SAP B1 ERP integration — must be called with the dedicated API token bound to the role `SYSTEMHAUS_ONE`, not a normal user login; the `SAP_ONE` module must be licensed.
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
    
    def to_put_request_information(self,body: ExternalIdsPutRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Returns the external identifiers (SAP B1 IDs) for the TANSS entities listed in the request body (link type plus a list of link IDs). Uses `PUT` so that the variable-length list of IDs can be supplied as a JSON body rather than a long query string. Intended for the SAP B1 ERP integration — must be called with the dedicated API token bound to the role `SYSTEMHAUS_ONE`, not a normal user login; the `SAP_ONE` module must be licensed.
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
    
    def with_url(self,raw_url: str) -> ExternalIdsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: ExternalIdsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return ExternalIdsRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class ExternalIdsRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class ExternalIdsRequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

