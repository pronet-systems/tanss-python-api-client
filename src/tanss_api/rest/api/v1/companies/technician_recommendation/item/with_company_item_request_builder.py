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
    Builds and executes requests for operations under /api/v1/companies/technicianRecommendation/{companyId}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new WithCompanyItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/companies/technicianRecommendation/{companyId}{?linkId*,linkTypeId*}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[WithCompanyItemRequestBuilderGetQueryParameters]] = None) -> Optional[WithCompanyGetResponse]:
        """
        Returns object — i.e. the ranked list of technicians most appropriate to handle work for the company (and optionally a specific assignment via `linkTypeId`/`linkId`, e.g. a PC or software license). The recommendation is derived from explicit object assignments, company types and headquarter fallbacks. Requires a technician or freelancer and access to the company — customer users do not get a recommendation.
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
        Returns object — i.e. the ranked list of technicians most appropriate to handle work for the company (and optionally a specific assignment via `linkTypeId`/`linkId`, e.g. a PC or software license). The recommendation is derived from explicit object assignments, company types and headquarter fallbacks. Requires a technician or freelancer and access to the company — customer users do not get a recommendation.
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
        Returns object — i.e. the ranked list of technicians most appropriate to handle work for the company (and optionally a specific assignment via `linkTypeId`/`linkId`, e.g. a PC or software license). The recommendation is derived from explicit object assignments, company types and headquarter fallbacks. Requires a technician or freelancer and access to the company — customer users do not get a recommendation.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "link_id":
                return "linkId"
            if original_name == "link_type_id":
                return "linkTypeId"
            return original_name
        
        # Optional id of the assignment the recommendation should target.
        link_id: Optional[int] = None

        # Optional link type of a specific assignment (e.g. PC or software license) to narrow the recommendation.
        link_type_id: Optional[int] = None

    
    @dataclass
    class WithCompanyItemRequestBuilderGetRequestConfiguration(RequestConfiguration[WithCompanyItemRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

