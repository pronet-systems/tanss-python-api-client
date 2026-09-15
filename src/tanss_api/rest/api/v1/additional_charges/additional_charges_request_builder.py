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
    from ....models.additional_charges403_error import AdditionalCharges403Error
    from .additional_charges_get_response import AdditionalChargesGetResponse
    from .additional_charges_post_request_body import AdditionalChargesPostRequestBody
    from .additional_charges_post_response import AdditionalChargesPostResponse
    from .additional_charges_put_request_body import AdditionalChargesPutRequestBody
    from .additional_charges_put_response import AdditionalChargesPutResponse
    from .delete.delete_request_builder import DeleteRequestBuilder

class AdditionalChargesRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/additionalCharges
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new AdditionalChargesRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/additionalCharges{?companyId*,contractId*}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[AdditionalChargesRequestBuilderGetQueryParameters]] = None) -> Optional[AdditionalChargesGetResponse]:
        """
        Returns all configured overtime additional-charge rules (`zuschlag` table). These rules define percentage surcharges that apply to supports (time entries) booked on specific weekdays/time ranges, scoped by company, contract and link type. Requires the `MANAGE_OVERTIME_DEFINITIONS` permission and technician/freelancer status.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[AdditionalChargesGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ....models.additional_charges403_error import AdditionalCharges403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": AdditionalCharges403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .additional_charges_get_response import AdditionalChargesGetResponse

        return await self.request_adapter.send_async(request_info, AdditionalChargesGetResponse, error_mapping)
    
    async def post(self,body: AdditionalChargesPostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[AdditionalChargesPostResponse]:
        """
        Creates a new overtime additional-charge definition. The composite key consists of `companyId`, `contractId`, `linkTypeId`, `linkId`, `day` and `number`; `number` is auto-assigned when omitted. Overlapping time ranges within the same scope/day are rejected. Requires the `MANAGE_OVERTIME_DEFINITIONS` permission.
        param body: Request body.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[AdditionalChargesPostResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ....models.additional_charges403_error import AdditionalCharges403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": AdditionalCharges403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .additional_charges_post_response import AdditionalChargesPostResponse

        return await self.request_adapter.send_async(request_info, AdditionalChargesPostResponse, error_mapping)
    
    async def put(self,body: AdditionalChargesPutRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[AdditionalChargesPutResponse]:
        """
        Updates an existing overtime additional-charge rule identified by its composite key (`companyId`, `contractId`, `linkTypeId`, `linkId`, `day`, `number`). The service re-validates the timeframe and rejects overlaps with other charges in the same scope. Logs old/new values for the change. Requires the `MANAGE_OVERTIME_DEFINITIONS` permission.
        param body: Request body.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[AdditionalChargesPutResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        from ....models.additional_charges403_error import AdditionalCharges403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": AdditionalCharges403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .additional_charges_put_response import AdditionalChargesPutResponse

        return await self.request_adapter.send_async(request_info, AdditionalChargesPutResponse, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[AdditionalChargesRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Returns all configured overtime additional-charge rules (`zuschlag` table). These rules define percentage surcharges that apply to supports (time entries) booked on specific weekdays/time ranges, scoped by company, contract and link type. Requires the `MANAGE_OVERTIME_DEFINITIONS` permission and technician/freelancer status.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: AdditionalChargesPostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Creates a new overtime additional-charge definition. The composite key consists of `companyId`, `contractId`, `linkTypeId`, `linkId`, `day` and `number`; `number` is auto-assigned when omitted. Overlapping time ranges within the same scope/day are rejected. Requires the `MANAGE_OVERTIME_DEFINITIONS` permission.
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
    
    def to_put_request_information(self,body: AdditionalChargesPutRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Updates an existing overtime additional-charge rule identified by its composite key (`companyId`, `contractId`, `linkTypeId`, `linkId`, `day`, `number`). The service re-validates the timeframe and rejects overlaps with other charges in the same scope. Logs old/new values for the change. Requires the `MANAGE_OVERTIME_DEFINITIONS` permission.
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
    
    def with_url(self,raw_url: str) -> AdditionalChargesRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: AdditionalChargesRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return AdditionalChargesRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def delete_path(self) -> DeleteRequestBuilder:
        """
        The deletePath property
        """
        from .delete.delete_request_builder import DeleteRequestBuilder

        return DeleteRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class AdditionalChargesRequestBuilderGetQueryParameters():
        """
        Returns all configured overtime additional-charge rules (`zuschlag` table). These rules define percentage surcharges that apply to supports (time entries) booked on specific weekdays/time ranges, scoped by company, contract and link type. Requires the `MANAGE_OVERTIME_DEFINITIONS` permission and technician/freelancer status.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "company_id":
                return "companyId"
            if original_name == "contract_id":
                return "contractId"
            return original_name
        
        # Filter the additional-charge rules to a single company.
        company_id: Optional[int] = None

        # Filter the additional-charge rules to a single contract.
        contract_id: Optional[int] = None

    
    @dataclass
    class AdditionalChargesRequestBuilderGetRequestConfiguration(RequestConfiguration[AdditionalChargesRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class AdditionalChargesRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class AdditionalChargesRequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

