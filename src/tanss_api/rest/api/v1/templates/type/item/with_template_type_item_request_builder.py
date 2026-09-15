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
    from ......models.with_template_type403_error import WithTemplateType403Error
    from .fields.fields_request_builder import FieldsRequestBuilder
    from .with_template_type_get_response import WithTemplateTypeGetResponse

class WithTemplateTypeItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/templates/type/{templateType}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new WithTemplateTypeItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/templates/type/{templateType}{?showAll*}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[WithTemplateTypeItemRequestBuilderGetQueryParameters]] = None) -> Optional[WithTemplateTypeGetResponse]:
        """
        Returns the list of persisted templates for `templateType`, sized down to the small filter (no full bodycontent). Permissions control who can list them, and visibility-filteredpersist-template rows are decorated with their list-properties (e.g. category names).When `showAll=true`, visibility / assignment filters are skipped — used by admin views (notably forcontract templates) that need to see every template regardless of assignment.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[WithTemplateTypeGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ......models.with_template_type403_error import WithTemplateType403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": WithTemplateType403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .with_template_type_get_response import WithTemplateTypeGetResponse

        return await self.request_adapter.send_async(request_info, WithTemplateTypeGetResponse, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[WithTemplateTypeItemRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Returns the list of persisted templates for `templateType`, sized down to the small filter (no full bodycontent). Permissions control who can list them, and visibility-filteredpersist-template rows are decorated with their list-properties (e.g. category names).When `showAll=true`, visibility / assignment filters are skipped — used by admin views (notably forcontract templates) that need to see every template regardless of assignment.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> WithTemplateTypeItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: WithTemplateTypeItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return WithTemplateTypeItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def fields(self) -> FieldsRequestBuilder:
        """
        The fields property
        """
        from .fields.fields_request_builder import FieldsRequestBuilder

        return FieldsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class WithTemplateTypeItemRequestBuilderGetQueryParameters():
        """
        Returns the list of persisted templates for `templateType`, sized down to the small filter (no full bodycontent). Permissions control who can list them, and visibility-filteredpersist-template rows are decorated with their list-properties (e.g. category names).When `showAll=true`, visibility / assignment filters are skipped — used by admin views (notably forcontract templates) that need to see every template regardless of assignment.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "show_all":
                return "showAll"
            return original_name
        
        # When true, skips visibility/assignment filters (admin views).
        show_all: Optional[bool] = None

    
    @dataclass
    class WithTemplateTypeItemRequestBuilderGetRequestConfiguration(RequestConfiguration[WithTemplateTypeItemRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

