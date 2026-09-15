from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .company.company_request_builder import CompanyRequestBuilder
    from .fields.fields_request_builder import FieldsRequestBuilder
    from .item.peripheries_item_request_builder import PeripheriesItemRequestBuilder
    from .pdf.pdf_request_builder import PdfRequestBuilder
    from .types.types_request_builder import TypesRequestBuilder

class PeripheriesRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/deviceManagement/v1/peripheries
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new PeripheriesRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/deviceManagement/v1/peripheries", path_parameters)
    
    def by_id(self,id: int) -> PeripheriesItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.deviceManagement.v1.peripheries.item collection
        param id: ID des Peripheriegeräts
        Returns: PeripheriesItemRequestBuilder
        """
        if id is None:
            raise TypeError("id cannot be null.")
        from .item.peripheries_item_request_builder import PeripheriesItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["id"] = id
        return PeripheriesItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    @property
    def company(self) -> CompanyRequestBuilder:
        """
        The company property
        """
        from .company.company_request_builder import CompanyRequestBuilder

        return CompanyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def fields(self) -> FieldsRequestBuilder:
        """
        The fields property
        """
        from .fields.fields_request_builder import FieldsRequestBuilder

        return FieldsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def pdf(self) -> PdfRequestBuilder:
        """
        The pdf property
        """
        from .pdf.pdf_request_builder import PdfRequestBuilder

        return PdfRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def types(self) -> TypesRequestBuilder:
        """
        The types property
        """
        from .types.types_request_builder import TypesRequestBuilder

        return TypesRequestBuilder(self.request_adapter, self.path_parameters)
    

