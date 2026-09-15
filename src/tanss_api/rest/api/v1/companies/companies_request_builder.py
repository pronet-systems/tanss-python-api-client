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
    from ....models.companies403_error import Companies403Error
    from ....models.company_post import CompanyPost
    from .companies_post_response import CompaniesPostResponse
    from .cost_center.cost_center_request_builder import CostCenterRequestBuilder
    from .departments.departments_request_builder import DepartmentsRequestBuilder
    from .flags.flags_request_builder import FlagsRequestBuilder
    from .item.company_item_request_builder import CompanyItemRequestBuilder
    from .properties.properties_request_builder import PropertiesRequestBuilder
    from .relations.relations_request_builder import RelationsRequestBuilder
    from .search.search_request_builder import SearchRequestBuilder
    from .technician_recommendation.technician_recommendation_request_builder import TechnicianRecommendationRequestBuilder

class CompaniesRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/companies
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new CompaniesRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/companies", path_parameters)
    
    def by_company_id(self,company_id: int) -> CompanyItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.v1.companies.item collection
        param company_id: Unique identifier of the item
        Returns: CompanyItemRequestBuilder
        """
        if company_id is None:
            raise TypeError("company_id cannot be null.")
        from .item.company_item_request_builder import CompanyItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["company%2Did"] = company_id
        return CompanyItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def post(self,body: CompanyPost, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[CompaniesPostResponse]:
        """
        Creates a new company in TANSS. The caller must have the `MANAGE_COMPANIES` permission and access to all companies; if a `headquarterId` is given, access to that headquarter is verified as well. Duplicates by (name, street, city) are rejected and the next free customer id is assigned automatically.To create a "personal customer" (company + single employee modeled as one person), set `personalCustomer: true` and pass a fully populated `personalCustomerEmployee` — the company name is then derived from "Lastname, Firstname" and the employee is persisted and attached to the new company.
        param body: Company object to be saved.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[CompaniesPostResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ....models.companies403_error import Companies403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Companies403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .companies_post_response import CompaniesPostResponse

        return await self.request_adapter.send_async(request_info, CompaniesPostResponse, error_mapping)
    
    def to_post_request_information(self,body: CompanyPost, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Creates a new company in TANSS. The caller must have the `MANAGE_COMPANIES` permission and access to all companies; if a `headquarterId` is given, access to that headquarter is verified as well. Duplicates by (name, street, city) are rejected and the next free customer id is assigned automatically.To create a "personal customer" (company + single employee modeled as one person), set `personalCustomer: true` and pass a fully populated `personalCustomerEmployee` — the company name is then derived from "Lastname, Firstname" and the employee is persisted and attached to the new company.
        param body: Company object to be saved.
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
    
    def with_url(self,raw_url: str) -> CompaniesRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: CompaniesRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return CompaniesRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def cost_center(self) -> CostCenterRequestBuilder:
        """
        The costCenter property
        """
        from .cost_center.cost_center_request_builder import CostCenterRequestBuilder

        return CostCenterRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def departments(self) -> DepartmentsRequestBuilder:
        """
        The departments property
        """
        from .departments.departments_request_builder import DepartmentsRequestBuilder

        return DepartmentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def flags(self) -> FlagsRequestBuilder:
        """
        The flags property
        """
        from .flags.flags_request_builder import FlagsRequestBuilder

        return FlagsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def properties(self) -> PropertiesRequestBuilder:
        """
        The properties property
        """
        from .properties.properties_request_builder import PropertiesRequestBuilder

        return PropertiesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def relations(self) -> RelationsRequestBuilder:
        """
        The relations property
        """
        from .relations.relations_request_builder import RelationsRequestBuilder

        return RelationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def search(self) -> SearchRequestBuilder:
        """
        The search property
        """
        from .search.search_request_builder import SearchRequestBuilder

        return SearchRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def technician_recommendation(self) -> TechnicianRecommendationRequestBuilder:
        """
        The technicianRecommendation property
        """
        from .technician_recommendation.technician_recommendation_request_builder import TechnicianRecommendationRequestBuilder

        return TechnicianRecommendationRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class CompaniesRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

