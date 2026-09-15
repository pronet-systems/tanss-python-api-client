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
    from ....models.company_categories403_error import CompanyCategories403Error
    from ....models.tns_company_category import TnsCompanyCategory
    from .company_categories_get_response import CompanyCategoriesGetResponse
    from .company_categories_post_response import CompanyCategoriesPostResponse
    from .item.company_categories_item_request_builder import CompanyCategoriesItemRequestBuilder
    from .types.types_request_builder import TypesRequestBuilder

class CompanyCategoriesRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/companyCategories
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new CompanyCategoriesRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/companyCategories", path_parameters)
    
    def by_id(self,id: int) -> CompanyCategoriesItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.v1.companyCategories.item collection
        param id: Id of the company category
        Returns: CompanyCategoriesItemRequestBuilder
        """
        if id is None:
            raise TypeError("id cannot be null.")
        from .item.company_categories_item_request_builder import CompanyCategoriesItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["id"] = id
        return CompanyCategoriesItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[CompanyCategoriesGetResponse]:
        """
        Gets a list of all categories
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[CompanyCategoriesGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ....models.company_categories403_error import CompanyCategories403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": CompanyCategories403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .company_categories_get_response import CompanyCategoriesGetResponse

        return await self.request_adapter.send_async(request_info, CompanyCategoriesGetResponse, error_mapping)
    
    async def post(self,body: TnsCompanyCategory, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[CompanyCategoriesPostResponse]:
        """
        Creates a company category in TANSS.
        param body: defines a company category
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[CompanyCategoriesPostResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ....models.company_categories403_error import CompanyCategories403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": CompanyCategories403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .company_categories_post_response import CompanyCategoriesPostResponse

        return await self.request_adapter.send_async(request_info, CompanyCategoriesPostResponse, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Gets a list of all categories
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: TnsCompanyCategory, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Creates a company category in TANSS.
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
    
    @property
    def types(self) -> TypesRequestBuilder:
        """
        The types property
        """
        from .types.types_request_builder import TypesRequestBuilder

        return TypesRequestBuilder(self.request_adapter, self.path_parameters)
    
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
    

