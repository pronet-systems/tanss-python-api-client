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
    from .....models.softwarelicenses403_error import Softwarelicenses403Error
    from .....models.tns_softwarelicense import TnsSoftwarelicense
    from .assignments.assignments_request_builder import AssignmentsRequestBuilder
    from .contracts.contracts_request_builder import ContractsRequestBuilder
    from .copy.copy_request_builder import CopyRequestBuilder
    from .pdf.pdf_request_builder import PdfRequestBuilder
    from .properties.properties_request_builder import PropertiesRequestBuilder
    from .softwarelicenses_get_response import SoftwarelicensesGetResponse
    from .softwarelicenses_put_response import SoftwarelicensesPutResponse

class SoftwarelicensesItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/softwarelicenses/{id}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new SoftwarelicensesItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/softwarelicenses/{id}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Deletes a software license
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from .....models.softwarelicenses403_error import Softwarelicenses403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Softwarelicenses403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[SoftwarelicensesGetResponse]:
        """
        Gets a single software license by id
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[SoftwarelicensesGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .....models.softwarelicenses403_error import Softwarelicenses403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Softwarelicenses403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .softwarelicenses_get_response import SoftwarelicensesGetResponse

        return await self.request_adapter.send_async(request_info, SoftwarelicensesGetResponse, error_mapping)
    
    async def put(self,body: TnsSoftwarelicense, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[SoftwarelicensesPutResponse]:
        """
        Updates a software license
        param body: Describes a software license
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[SoftwarelicensesPutResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        from .....models.softwarelicenses403_error import Softwarelicenses403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Softwarelicenses403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .softwarelicenses_put_response import SoftwarelicensesPutResponse

        return await self.request_adapter.send_async(request_info, SoftwarelicensesPutResponse, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Deletes a software license
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Gets a single software license by id
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_put_request_information(self,body: TnsSoftwarelicense, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Updates a software license
        param body: Describes a software license
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
    
    def with_url(self,raw_url: str) -> SoftwarelicensesItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: SoftwarelicensesItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return SoftwarelicensesItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def assignments(self) -> AssignmentsRequestBuilder:
        """
        The assignments property
        """
        from .assignments.assignments_request_builder import AssignmentsRequestBuilder

        return AssignmentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def contracts(self) -> ContractsRequestBuilder:
        """
        The contracts property
        """
        from .contracts.contracts_request_builder import ContractsRequestBuilder

        return ContractsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def copy(self) -> CopyRequestBuilder:
        """
        The copy property
        """
        from .copy.copy_request_builder import CopyRequestBuilder

        return CopyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def pdf(self) -> PdfRequestBuilder:
        """
        The pdf property
        """
        from .pdf.pdf_request_builder import PdfRequestBuilder

        return PdfRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def properties(self) -> PropertiesRequestBuilder:
        """
        The properties property
        """
        from .properties.properties_request_builder import PropertiesRequestBuilder

        return PropertiesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class SoftwarelicensesItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class SoftwarelicensesItemRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class SoftwarelicensesItemRequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

