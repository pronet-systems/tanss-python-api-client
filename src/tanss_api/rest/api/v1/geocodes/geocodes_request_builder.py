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
    from ....models.geocodes403_error import Geocodes403Error
    from .geocodes_post_request_body import GeocodesPostRequestBody
    from .geocodes_post_response import GeocodesPostResponse

class GeocodesRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/geocodes
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new GeocodesRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/geocodes", path_parameters)
    
    async def post(self,body: GeocodesPostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[GeocodesPostResponse]:
        """
        Stores a geocode (longitude/latitude, accuracy, status) for an assignment — either an employee (`linkTypeId = 3`) or a company (`linkTypeId = 2`). The caller must be a technician or freelancer. If no `linkTypeId`/`linkId` is supplied, the geocode is attached to the currently logged-in user. For company geocodes, the caller additionally needs company access plus one of `CHANGE_COMPANY_ADDRESS`, `MANAGE_COMPANIES` or `COMPANY_MANAGEMENT_FAST_CARE`; for employee geocodes the user may only set their own coordinates. The `date` field is server-controlled and ignored on input.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[GeocodesPostResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ....models.geocodes403_error import Geocodes403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Geocodes403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .geocodes_post_response import GeocodesPostResponse

        return await self.request_adapter.send_async(request_info, GeocodesPostResponse, error_mapping)
    
    def to_post_request_information(self,body: GeocodesPostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Stores a geocode (longitude/latitude, accuracy, status) for an assignment — either an employee (`linkTypeId = 3`) or a company (`linkTypeId = 2`). The caller must be a technician or freelancer. If no `linkTypeId`/`linkId` is supplied, the geocode is attached to the currently logged-in user. For company geocodes, the caller additionally needs company access plus one of `CHANGE_COMPANY_ADDRESS`, `MANAGE_COMPANIES` or `COMPANY_MANAGEMENT_FAST_CARE`; for employee geocodes the user may only set their own coordinates. The `date` field is server-controlled and ignored on input.
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
    
    def with_url(self,raw_url: str) -> GeocodesRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: GeocodesRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return GeocodesRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class GeocodesRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

