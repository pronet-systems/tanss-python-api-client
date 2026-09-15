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
    from ....models.offers403_error import Offers403Error
    from ....models.tns_offer_configuration import TnsOfferConfiguration
    from ....models.tns_offer_details import TnsOfferDetails
    from .duplicate.duplicate_request_builder import DuplicateRequestBuilder
    from .erp_selections.erp_selections_request_builder import ErpSelectionsRequestBuilder
    from .item.with_offer_item_request_builder import WithOfferItemRequestBuilder
    from .offers_post_response import OffersPostResponse
    from .offers_put_response import OffersPutResponse
    from .pdf.pdf_request_builder import PdfRequestBuilder
    from .templates.templates_request_builder import TemplatesRequestBuilder

class OffersRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/offers
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new OffersRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/offers", path_parameters)
    
    def by_offer_id(self,offer_id: int) -> WithOfferItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.v1.offers.item collection
        param offer_id: Id of the offer
        Returns: WithOfferItemRequestBuilder
        """
        if offer_id is None:
            raise TypeError("offer_id cannot be null.")
        from .item.with_offer_item_request_builder import WithOfferItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["offerId"] = offer_id
        return WithOfferItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def post(self,body: TnsOfferDetails, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[OffersPostResponse]:
        """
        This route creates a new offer
        param body: Describes an offer, including variables and material
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[OffersPostResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ....models.offers403_error import Offers403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Offers403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .offers_post_response import OffersPostResponse

        return await self.request_adapter.send_async(request_info, OffersPostResponse, error_mapping)
    
    async def put(self,body: TnsOfferConfiguration, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[OffersPutResponse]:
        """
        This route gets a list of offers (by a given filter, trasmitted in the request body)
        param body: Filter, which offers shall be loaded
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[OffersPutResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        from ....models.offers403_error import Offers403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Offers403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .offers_put_response import OffersPutResponse

        return await self.request_adapter.send_async(request_info, OffersPutResponse, error_mapping)
    
    def to_post_request_information(self,body: TnsOfferDetails, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        This route creates a new offer
        param body: Describes an offer, including variables and material
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
    
    def to_put_request_information(self,body: TnsOfferConfiguration, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        This route gets a list of offers (by a given filter, trasmitted in the request body)
        param body: Filter, which offers shall be loaded
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
    
    def with_url(self,raw_url: str) -> OffersRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: OffersRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return OffersRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def duplicate(self) -> DuplicateRequestBuilder:
        """
        The duplicate property
        """
        from .duplicate.duplicate_request_builder import DuplicateRequestBuilder

        return DuplicateRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def erp_selections(self) -> ErpSelectionsRequestBuilder:
        """
        The erpSelections property
        """
        from .erp_selections.erp_selections_request_builder import ErpSelectionsRequestBuilder

        return ErpSelectionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def pdf(self) -> PdfRequestBuilder:
        """
        The pdf property
        """
        from .pdf.pdf_request_builder import PdfRequestBuilder

        return PdfRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def templates(self) -> TemplatesRequestBuilder:
        """
        The templates property
        """
        from .templates.templates_request_builder import TemplatesRequestBuilder

        return TemplatesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class OffersRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class OffersRequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

