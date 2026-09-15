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
    from .....models.companies403_error import Companies403Error
    from .companies_post_request_body import CompaniesPostRequestBody
    from .companies_post_response import CompaniesPostResponse
    from .departments.departments_request_builder import DepartmentsRequestBuilder
    from .employees.employees_request_builder import EmployeesRequestBuilder
    from .item.companies_item_request_builder import CompaniesItemRequestBuilder
    from .search_id.search_id_request_builder import SearchIdRequestBuilder

class CompaniesRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/erp/v1/companies
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new CompaniesRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/erp/v1/companies", path_parameters)
    
    def by_id(self,id: int) -> CompaniesItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.erp.v1.companies.item collection
        param id: ID of the company to delete.
        Returns: CompaniesItemRequestBuilder
        """
        if id is None:
            raise TypeError("id cannot be null.")
        from .item.companies_item_request_builder import CompaniesItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["id"] = id
        return CompaniesItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def post(self,body: CompaniesPostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[CompaniesPostResponse]:
        """
        Creates a new company (customer) record in TANSS from the supplied master data, so an ERP system can push newly onboarded customers into TANSS. Intended for ERP integrations — must be called with the dedicated API token bound to the role `ERP`, not a normal user login.
        param body: Request body.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[CompaniesPostResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from .....models.companies403_error import Companies403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Companies403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .companies_post_response import CompaniesPostResponse

        return await self.request_adapter.send_async(request_info, CompaniesPostResponse, error_mapping)
    
    def to_post_request_information(self,body: CompaniesPostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Creates a new company (customer) record in TANSS from the supplied master data, so an ERP system can push newly onboarded customers into TANSS. Intended for ERP integrations — must be called with the dedicated API token bound to the role `ERP`, not a normal user login.
        param body: Request body.
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
    def departments(self) -> DepartmentsRequestBuilder:
        """
        The departments property
        """
        from .departments.departments_request_builder import DepartmentsRequestBuilder

        return DepartmentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def employees(self) -> EmployeesRequestBuilder:
        """
        The employees property
        """
        from .employees.employees_request_builder import EmployeesRequestBuilder

        return EmployeesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def search_id(self) -> SearchIdRequestBuilder:
        """
        The searchId property
        """
        from .search_id.search_id_request_builder import SearchIdRequestBuilder

        return SearchIdRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class CompaniesRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

