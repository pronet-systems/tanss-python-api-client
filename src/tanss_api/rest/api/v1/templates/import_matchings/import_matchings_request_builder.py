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
    from .....models.import_matchings403_error import ImportMatchings403Error
    from .import_matchings import ImportMatchings
    from .import_matchings_post_response import ImportMatchingsPostResponse
    from .import_matchings_put_response import ImportMatchingsPutResponse

class ImportMatchingsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/templates/importMatchings
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new ImportMatchingsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/templates/importMatchings", path_parameters)
    
    async def post(self,body: list[ImportMatchings], request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[ImportMatchingsPostResponse]:
        """
        Persists the user's choices for resolving foreign-system → local matchings (which foreign company id mapsto which local company id, etc.) so subsequent imports of the same source can be processed withoutprompting. Each row in the body is created individually. Returns the same listback to confirm persistence.Requires the admin-of-imports permission.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ImportMatchingsPostResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from .....models.import_matchings403_error import ImportMatchings403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": ImportMatchings403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .import_matchings_post_response import ImportMatchingsPostResponse

        return await self.request_adapter.send_async(request_info, ImportMatchingsPostResponse, error_mapping)
    
    async def put(self,body: list[ImportMatchings], request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[ImportMatchingsPutResponse]:
        """
        Builds the data used to populate the import-matching pop-up: for each foreign id in the body it returnsthe available local entities to choose from. The result object carries selection listsgrouped by linked-entity type so the UI can render the dropdowns.Requires the same admin-of-imports permission as the POST variant.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ImportMatchingsPutResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        from .....models.import_matchings403_error import ImportMatchings403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": ImportMatchings403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .import_matchings_put_response import ImportMatchingsPutResponse

        return await self.request_adapter.send_async(request_info, ImportMatchingsPutResponse, error_mapping)
    
    def to_post_request_information(self,body: list[ImportMatchings], request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Persists the user's choices for resolving foreign-system → local matchings (which foreign company id mapsto which local company id, etc.) so subsequent imports of the same source can be processed withoutprompting. Each row in the body is created individually. Returns the same listback to confirm persistence.Requires the admin-of-imports permission.
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
    
    def to_put_request_information(self,body: list[ImportMatchings], request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Builds the data used to populate the import-matching pop-up: for each foreign id in the body it returnsthe available local entities to choose from. The result object carries selection listsgrouped by linked-entity type so the UI can render the dropdowns.Requires the same admin-of-imports permission as the POST variant.
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
    
    def with_url(self,raw_url: str) -> ImportMatchingsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: ImportMatchingsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return ImportMatchingsRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class ImportMatchingsRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class ImportMatchingsRequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

