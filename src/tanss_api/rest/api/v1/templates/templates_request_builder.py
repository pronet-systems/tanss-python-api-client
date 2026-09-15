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
    from ....models.templates403_error import Templates403Error
    from .assignments.assignments_request_builder import AssignmentsRequestBuilder
    from .create_from.create_from_request_builder import CreateFromRequestBuilder
    from .import_.import_request_builder import ImportRequestBuilder
    from .import_matchings.import_matchings_request_builder import ImportMatchingsRequestBuilder
    from .item.item_request_builder import ItemRequestBuilder
    from .pending_import.pending_import_request_builder import PendingImportRequestBuilder
    from .pending_imports.pending_imports_request_builder import PendingImportsRequestBuilder
    from .templates_put_request_body import TemplatesPutRequestBody
    from .templates_put_response import TemplatesPutResponse
    from .type.type_request_builder import TypeRequestBuilder
    from .update.update_request_builder import UpdateRequestBuilder

class TemplatesRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/templates
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new TemplatesRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/templates", path_parameters)
    
    def by_id(self,id: int) -> ItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.v1.templates.item collection
        param id: Id of the template.
        Returns: ItemRequestBuilder
        """
        if id is None:
            raise TypeError("id cannot be null.")
        from .item.item_request_builder import ItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["%2Did"] = id
        return ItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def put(self,body: TemplatesPutRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[TemplatesPutResponse]:
        """
        Returns persisted records filtered by the supplied object(template type, name/text search, sort, paging, ...). The response is filtered through the small variant ofthe template filter so the JSON `content` field is omitted; use `GET /templates/{id}` to load the full body.Visibility is enforced based on the caller's permissions (own templates, assigned templates,admin-of-type templates).
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[TemplatesPutResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        from ....models.templates403_error import Templates403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Templates403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .templates_put_response import TemplatesPutResponse

        return await self.request_adapter.send_async(request_info, TemplatesPutResponse, error_mapping)
    
    def to_put_request_information(self,body: TemplatesPutRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Returns persisted records filtered by the supplied object(template type, name/text search, sort, paging, ...). The response is filtered through the small variant ofthe template filter so the JSON `content` field is omitted; use `GET /templates/{id}` to load the full body.Visibility is enforced based on the caller's permissions (own templates, assigned templates,admin-of-type templates).
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
    
    def with_url(self,raw_url: str) -> TemplatesRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: TemplatesRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return TemplatesRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def assignments(self) -> AssignmentsRequestBuilder:
        """
        The assignments property
        """
        from .assignments.assignments_request_builder import AssignmentsRequestBuilder

        return AssignmentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def create_from(self) -> CreateFromRequestBuilder:
        """
        The createFrom property
        """
        from .create_from.create_from_request_builder import CreateFromRequestBuilder

        return CreateFromRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def import_(self) -> ImportRequestBuilder:
        """
        The import property
        """
        from .import_.import_request_builder import ImportRequestBuilder

        return ImportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def import_matchings(self) -> ImportMatchingsRequestBuilder:
        """
        The importMatchings property
        """
        from .import_matchings.import_matchings_request_builder import ImportMatchingsRequestBuilder

        return ImportMatchingsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def pending_import(self) -> PendingImportRequestBuilder:
        """
        The pendingImport property
        """
        from .pending_import.pending_import_request_builder import PendingImportRequestBuilder

        return PendingImportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def pending_imports(self) -> PendingImportsRequestBuilder:
        """
        The pendingImports property
        """
        from .pending_imports.pending_imports_request_builder import PendingImportsRequestBuilder

        return PendingImportsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def type(self) -> TypeRequestBuilder:
        """
        The type property
        """
        from .type.type_request_builder import TypeRequestBuilder

        return TypeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def update(self) -> UpdateRequestBuilder:
        """
        The update property
        """
        from .update.update_request_builder import UpdateRequestBuilder

        return UpdateRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class TemplatesRequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

