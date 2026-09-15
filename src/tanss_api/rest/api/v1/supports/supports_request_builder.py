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
    from ....models.supports403_error import Supports403Error
    from ....models.tns_support_create import TnsSupportCreate
    from .appointments.appointments_request_builder import AppointmentsRequestBuilder
    from .appointment_wizard.appointment_wizard_request_builder import AppointmentWizardRequestBuilder
    from .book_directly.book_directly_request_builder import BookDirectlyRequestBuilder
    from .clear.clear_request_builder import ClearRequestBuilder
    from .item.with_support_item_request_builder import WithSupportItemRequestBuilder
    from .list_.list_request_builder import ListRequestBuilder
    from .mat_picker.mat_picker_request_builder import MatPickerRequestBuilder
    from .not_charged_reason.not_charged_reason_request_builder import NotChargedReasonRequestBuilder
    from .properties.properties_request_builder import PropertiesRequestBuilder
    from .signature.signature_request_builder import SignatureRequestBuilder
    from .split.split_request_builder import SplitRequestBuilder
    from .statistics.statistics_request_builder import StatisticsRequestBuilder
    from .summary.summary_request_builder import SummaryRequestBuilder
    from .supports_post_response import SupportsPostResponse
    from .unclear.unclear_request_builder import UnclearRequestBuilder

class SupportsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/supports
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new SupportsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/supports", path_parameters)
    
    def by_support_id(self,support_id: int) -> WithSupportItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.v1.supports.item collection
        param support_id: id of the support that shall be fetched
        Returns: WithSupportItemRequestBuilder
        """
        if support_id is None:
            raise TypeError("support_id cannot be null.")
        from .item.with_support_item_request_builder import WithSupportItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["supportId"] = support_id
        return WithSupportItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def post(self,body: TnsSupportCreate, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[SupportsPostResponse]:
        """
        Creates a support/appointment
        param body: model for creating a new support
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[SupportsPostResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ....models.supports403_error import Supports403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Supports403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .supports_post_response import SupportsPostResponse

        return await self.request_adapter.send_async(request_info, SupportsPostResponse, error_mapping)
    
    def to_post_request_information(self,body: TnsSupportCreate, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Creates a support/appointment
        param body: model for creating a new support
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
    
    def with_url(self,raw_url: str) -> SupportsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: SupportsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return SupportsRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def appointment_wizard(self) -> AppointmentWizardRequestBuilder:
        """
        The appointmentWizard property
        """
        from .appointment_wizard.appointment_wizard_request_builder import AppointmentWizardRequestBuilder

        return AppointmentWizardRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def appointments(self) -> AppointmentsRequestBuilder:
        """
        The appointments property
        """
        from .appointments.appointments_request_builder import AppointmentsRequestBuilder

        return AppointmentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def book_directly(self) -> BookDirectlyRequestBuilder:
        """
        The bookDirectly property
        """
        from .book_directly.book_directly_request_builder import BookDirectlyRequestBuilder

        return BookDirectlyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def clear(self) -> ClearRequestBuilder:
        """
        The clear property
        """
        from .clear.clear_request_builder import ClearRequestBuilder

        return ClearRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def list_(self) -> ListRequestBuilder:
        """
        The list property
        """
        from .list_.list_request_builder import ListRequestBuilder

        return ListRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def mat_picker(self) -> MatPickerRequestBuilder:
        """
        The matPicker property
        """
        from .mat_picker.mat_picker_request_builder import MatPickerRequestBuilder

        return MatPickerRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def not_charged_reason(self) -> NotChargedReasonRequestBuilder:
        """
        The notChargedReason property
        """
        from .not_charged_reason.not_charged_reason_request_builder import NotChargedReasonRequestBuilder

        return NotChargedReasonRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def properties(self) -> PropertiesRequestBuilder:
        """
        The properties property
        """
        from .properties.properties_request_builder import PropertiesRequestBuilder

        return PropertiesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def signature(self) -> SignatureRequestBuilder:
        """
        The signature property
        """
        from .signature.signature_request_builder import SignatureRequestBuilder

        return SignatureRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def split(self) -> SplitRequestBuilder:
        """
        The split property
        """
        from .split.split_request_builder import SplitRequestBuilder

        return SplitRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def statistics(self) -> StatisticsRequestBuilder:
        """
        The statistics property
        """
        from .statistics.statistics_request_builder import StatisticsRequestBuilder

        return StatisticsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def summary(self) -> SummaryRequestBuilder:
        """
        The summary property
        """
        from .summary.summary_request_builder import SummaryRequestBuilder

        return SummaryRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def unclear(self) -> UnclearRequestBuilder:
        """
        The unclear property
        """
        from .unclear.unclear_request_builder import UnclearRequestBuilder

        return UnclearRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class SupportsRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

