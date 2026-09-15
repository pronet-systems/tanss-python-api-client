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
    from .....models.company_categories403_error import CompanyCategories403Error
    from .....models.tns_company_category import TnsCompanyCategory
    from .company_categories_get_response import CompanyCategoriesGetResponse
    from .company_categories_post_response import CompanyCategoriesPostResponse
    from .item.with_category_item_request_builder import WithCategoryItemRequestBuilder

class CompanyCategoriesRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/erp/v1/companyCategories
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new CompanyCategoriesRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/erp/v1/companyCategories", path_parameters)
    
    def by_category_id(self,category_id: int) -> WithCategoryItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.erp.v1.companyCategories.item collection
        param category_id: ID of the company category.
        Returns: WithCategoryItemRequestBuilder
        """
        if category_id is None:
            raise TypeError("category_id cannot be null.")
        from .item.with_category_item_request_builder import WithCategoryItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["categoryId"] = category_id
        return WithCategoryItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[CompanyCategoriesGetResponse]:
        """
        Returns the list of company categories (Firmen-Kategorien) including the company types associated with each category, so an ERP system can map customer classifications during sync. Intended for ERP integrations — must be called with the dedicated API token bound to the role `ERP`, not a normal user login.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[CompanyCategoriesGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .....models.company_categories403_error import CompanyCategories403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": CompanyCategories403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .company_categories_get_response import CompanyCategoriesGetResponse

        return await self.request_adapter.send_async(request_info, CompanyCategoriesGetResponse, error_mapping)
    
    async def post(self,body: TnsCompanyCategory, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[CompanyCategoriesPostResponse]:
        """
        Legt vermutlich eine Firmenkategorie über die ERP-Schnittstelle an (Gegenstück zu GET /api/erp/v1/companyCategories und DELETE /api/erp/v1/companyCategories/{categoryId}). Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft. Token: module, Rollen CENTRON, ERP. Keine Analyse vorhanden; Body und Antwort aus TnsCompanyCategory abgeleitet.
        param body: defines a company category
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[CompanyCategoriesPostResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .company_categories_post_response import CompanyCategoriesPostResponse

        return await self.request_adapter.send_async(request_info, CompanyCategoriesPostResponse, None)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Returns the list of company categories (Firmen-Kategorien) including the company types associated with each category, so an ERP system can map customer classifications during sync. Intended for ERP integrations — must be called with the dedicated API token bound to the role `ERP`, not a normal user login.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: TnsCompanyCategory, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Legt vermutlich eine Firmenkategorie über die ERP-Schnittstelle an (Gegenstück zu GET /api/erp/v1/companyCategories und DELETE /api/erp/v1/companyCategories/{categoryId}). Nicht in der offiziellen Schnittstellenbeschreibung gefuehrt; vom Server so umgesetzt, gegen 10.10 geprueft. Token: module, Rollen CENTRON, ERP. Keine Analyse vorhanden; Body und Antwort aus TnsCompanyCategory abgeleitet.
        param body: defines a company category
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
    
    def with_url(self,raw_url: str) -> CompanyCategoriesRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: CompanyCategoriesRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return CompanyCategoriesRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class CompanyCategoriesRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class CompanyCategoriesRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

