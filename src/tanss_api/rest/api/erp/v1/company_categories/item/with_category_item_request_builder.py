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
    from ......models.with_category403_error import WithCategory403Error
    from .with_category_get_response import WithCategoryGetResponse
    from .with_category_post_request_body import WithCategoryPostRequestBody
    from .with_category_post_response import WithCategoryPostResponse
    from .with_category_put_request_body import WithCategoryPutRequestBody
    from .with_category_put_response import WithCategoryPutResponse

class WithCategoryItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/erp/v1/companyCategories/{categoryId}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new WithCategoryItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/erp/v1/companyCategories/{categoryId}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Deletes the company category identified by `categoryId`. Intended for ERP integrations that maintain customer classifications from the ERP side — must be called with the dedicated API token bound to the role `ERP`, not a normal user login.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ......models.with_category403_error import WithCategory403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": WithCategory403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[WithCategoryGetResponse]:
        """
        Returns the single company category identified by `categoryId`. Intended for ERP integrations — must be called with the dedicated API token bound to the role `ERP`, not a normal user login.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[WithCategoryGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ......models.with_category403_error import WithCategory403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": WithCategory403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .with_category_get_response import WithCategoryGetResponse

        return await self.request_adapter.send_async(request_info, WithCategoryGetResponse, error_mapping)
    
    async def post(self,body: WithCategoryPostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[WithCategoryPostResponse]:
        """
        Creates a new company category from the supplied payload. Note that creating runs on this URL and not on `/companyCategories` — the `categoryId` in the path is not evaluated, the id of the new category is assigned by TANSS. Intended for ERP integrations that need to maintain customer classifications in TANSS — must be called with the dedicated API token bound to the role `ERP`, not a normal user login.
        param body: Request body.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[WithCategoryPostResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ......models.with_category403_error import WithCategory403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": WithCategory403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .with_category_post_response import WithCategoryPostResponse

        return await self.request_adapter.send_async(request_info, WithCategoryPostResponse, error_mapping)
    
    async def put(self,body: WithCategoryPutRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[WithCategoryPutResponse]:
        """
        Updates the company category identified by `categoryId` with the supplied fields. Intended for ERP integrations — must be called with the dedicated API token bound to the role `ERP`, not a normal user login.
        param body: Request body.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[WithCategoryPutResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        from ......models.with_category403_error import WithCategory403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": WithCategory403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .with_category_put_response import WithCategoryPutResponse

        return await self.request_adapter.send_async(request_info, WithCategoryPutResponse, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Deletes the company category identified by `categoryId`. Intended for ERP integrations that maintain customer classifications from the ERP side — must be called with the dedicated API token bound to the role `ERP`, not a normal user login.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Returns the single company category identified by `categoryId`. Intended for ERP integrations — must be called with the dedicated API token bound to the role `ERP`, not a normal user login.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: WithCategoryPostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Creates a new company category from the supplied payload. Note that creating runs on this URL and not on `/companyCategories` — the `categoryId` in the path is not evaluated, the id of the new category is assigned by TANSS. Intended for ERP integrations that need to maintain customer classifications in TANSS — must be called with the dedicated API token bound to the role `ERP`, not a normal user login.
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
    
    def to_put_request_information(self,body: WithCategoryPutRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Updates the company category identified by `categoryId` with the supplied fields. Intended for ERP integrations — must be called with the dedicated API token bound to the role `ERP`, not a normal user login.
        param body: Request body.
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
    
    def with_url(self,raw_url: str) -> WithCategoryItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: WithCategoryItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return WithCategoryItemRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class WithCategoryItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class WithCategoryItemRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class WithCategoryItemRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class WithCategoryItemRequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

