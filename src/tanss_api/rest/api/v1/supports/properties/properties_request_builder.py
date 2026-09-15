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
    from .....models.properties403_error import Properties403Error
    from .properties_post_request_body import PropertiesPostRequestBody
    from .properties_post_response import PropertiesPostResponse

class PropertiesRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/supports/properties
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new PropertiesRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/supports/properties{?changedProperty*,initAllFields*}", path_parameters)
    
    async def post(self,body: PropertiesPostRequestBody, request_configuration: Optional[RequestConfiguration[PropertiesRequestBuilderPostQueryParameters]] = None) -> Optional[PropertiesPostResponse]:
        """
        Given a (possibly unsaved) support payload, returns the form properties — which fields are editable, visible, required, plus computed default values and dropdown options — based on the current state. The frontend calls this on every relevant field change (`changedProperty`) so the backend can re-evaluate dependent rules (e.g. setting `internal` may toggle billing fields). Pass `initAllFields=true` on the first call to populate every field.
        param body: Body binds to the property-evaluation payload.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[PropertiesPostResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from .....models.properties403_error import Properties403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Properties403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .properties_post_response import PropertiesPostResponse

        return await self.request_adapter.send_async(request_info, PropertiesPostResponse, error_mapping)
    
    def to_post_request_information(self,body: PropertiesPostRequestBody, request_configuration: Optional[RequestConfiguration[PropertiesRequestBuilderPostQueryParameters]] = None) -> RequestInformation:
        """
        Given a (possibly unsaved) support payload, returns the form properties — which fields are editable, visible, required, plus computed default values and dropdown options — based on the current state. The frontend calls this on every relevant field change (`changedProperty`) so the backend can re-evaluate dependent rules (e.g. setting `internal` may toggle billing fields). Pass `initAllFields=true` on the first call to populate every field.
        param body: Body binds to the property-evaluation payload.
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
    
    def with_url(self,raw_url: str) -> PropertiesRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: PropertiesRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return PropertiesRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class PropertiesRequestBuilderPostQueryParameters():
        """
        Given a (possibly unsaved) support payload, returns the form properties — which fields are editable, visible, required, plus computed default values and dropdown options — based on the current state. The frontend calls this on every relevant field change (`changedProperty`) so the backend can re-evaluate dependent rules (e.g. setting `internal` may toggle billing fields). Pass `initAllFields=true` on the first call to populate every field.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "changed_property":
                return "changedProperty"
            if original_name == "init_all_fields":
                return "initAllFields"
            return original_name
        
        # Name of the field that just changed so dependent rules can be re-evaluated.
        changed_property: Optional[str] = None

        # When true, populate every form field instead of only the changed one (use on the first call).
        init_all_fields: Optional[bool] = None

    
    @dataclass
    class PropertiesRequestBuilderPostRequestConfiguration(RequestConfiguration[PropertiesRequestBuilderPostQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

