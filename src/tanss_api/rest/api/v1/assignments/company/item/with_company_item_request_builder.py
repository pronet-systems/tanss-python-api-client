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
    from ......models.with_company403_error import WithCompany403Error
    from .with_company_get_response import WithCompanyGetResponse

class WithCompanyItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/assignments/company/{companyId}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new WithCompanyItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/assignments/company/{companyId}{?branches*}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[WithCompanyItemRequestBuilderGetQueryParameters]] = None) -> Optional[WithCompanyGetResponse]:
        """
        Returns the tree of assignments (devices, contracts, locations, custom assignment types) that can be picked when linkingsomething to the given company — used by the assignment-picker dialog in tickets and supports. Pass `branches=true` to includeassignments of the company's child branches in addition to its own.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[WithCompanyGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ......models.with_company403_error import WithCompany403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": WithCompany403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .with_company_get_response import WithCompanyGetResponse

        return await self.request_adapter.send_async(request_info, WithCompanyGetResponse, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[WithCompanyItemRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Returns the tree of assignments (devices, contracts, locations, custom assignment types) that can be picked when linkingsomething to the given company — used by the assignment-picker dialog in tickets and supports. Pass `branches=true` to includeassignments of the company's child branches in addition to its own.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> WithCompanyItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: WithCompanyItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return WithCompanyItemRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class WithCompanyItemRequestBuilderGetQueryParameters():
        """
        Returns the tree of assignments (devices, contracts, locations, custom assignment types) that can be picked when linkingsomething to the given company — used by the assignment-picker dialog in tickets and supports. Pass `branches=true` to includeassignments of the company's child branches in addition to its own.
        """
        # If 'true', also include assignments of the company's child branches.
        branches: Optional[str] = None

    
    @dataclass
    class WithCompanyItemRequestBuilderGetRequestConfiguration(RequestConfiguration[WithCompanyItemRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

