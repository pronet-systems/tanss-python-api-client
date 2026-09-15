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
    from ....models.escalations403_error import Escalations403Error
    from .categories.categories_request_builder import CategoriesRequestBuilder
    from .check.check_request_builder import CheckRequestBuilder
    from .escalations_get_response import EscalationsGetResponse
    from .escalations_post_request_body import EscalationsPostRequestBody
    from .escalations_post_response import EscalationsPostResponse
    from .escalations_put_request_body import EscalationsPutRequestBody
    from .escalations_put_response import EscalationsPutResponse
    from .frontend.frontend_request_builder import FrontendRequestBuilder
    from .get_rules_for_ticket.get_rules_for_ticket_request_builder import GetRulesForTicketRequestBuilder
    from .get_tickets_for_rule.get_tickets_for_rule_request_builder import GetTicketsForRuleRequestBuilder
    from .is_ticket.is_ticket_request_builder import IsTicketRequestBuilder
    from .item.escalations_item_request_builder import EscalationsItemRequestBuilder
    from .statistics.statistics_request_builder import StatisticsRequestBuilder
    from .update_relevant_infos.update_relevant_infos_request_builder import UpdateRelevantInfosRequestBuilder

class EscalationsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/escalations
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new EscalationsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/escalations", path_parameters)
    
    def by_id(self,id: int) -> EscalationsItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.v1.escalations.item collection
        param id: Id of the escalation rule to delete.
        Returns: EscalationsItemRequestBuilder
        """
        if id is None:
            raise TypeError("id cannot be null.")
        from .item.escalations_item_request_builder import EscalationsItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["id"] = id
        return EscalationsItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[EscalationsGetResponse]:
        """
        Returns the full, unfiltered list of escalation rules configured in the system. Escalation rules drive automated SLA reactions (e-mails, status changes, technician reassignment) when tickets or supports breach a configured threshold. Requires the MANAGE_TICKET_ESCALATION permission and technician/freelancer role.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[EscalationsGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ....models.escalations403_error import Escalations403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Escalations403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .escalations_get_response import EscalationsGetResponse

        return await self.request_adapter.send_async(request_info, EscalationsGetResponse, error_mapping)
    
    async def post(self,body: EscalationsPostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[EscalationsPostResponse]:
        """
        Creates a new escalation rule. After persistence the engine will start considering this rule on every periodic escalation check (and on the manual `/check` route). Requires MANAGE_TICKET_ESCALATION.
        param body: Request body.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[EscalationsPostResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ....models.escalations403_error import Escalations403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Escalations403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .escalations_post_response import EscalationsPostResponse

        return await self.request_adapter.send_async(request_info, EscalationsPostResponse, error_mapping)
    
    async def put(self,body: EscalationsPutRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[EscalationsPutResponse]:
        """
        Returns escalation rules using a paginated/filtered configuration in the body (search text, sort order, category filter, …). Use this variant when the frontend needs to render a list view with filters; for an unconditional dump use GET.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[EscalationsPutResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        from ....models.escalations403_error import Escalations403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Escalations403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .escalations_put_response import EscalationsPutResponse

        return await self.request_adapter.send_async(request_info, EscalationsPutResponse, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Returns the full, unfiltered list of escalation rules configured in the system. Escalation rules drive automated SLA reactions (e-mails, status changes, technician reassignment) when tickets or supports breach a configured threshold. Requires the MANAGE_TICKET_ESCALATION permission and technician/freelancer role.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: EscalationsPostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Creates a new escalation rule. After persistence the engine will start considering this rule on every periodic escalation check (and on the manual `/check` route). Requires MANAGE_TICKET_ESCALATION.
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
    
    def to_put_request_information(self,body: EscalationsPutRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Returns escalation rules using a paginated/filtered configuration in the body (search text, sort order, category filter, …). Use this variant when the frontend needs to render a list view with filters; for an unconditional dump use GET.
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
    
    def with_url(self,raw_url: str) -> EscalationsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: EscalationsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return EscalationsRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def categories(self) -> CategoriesRequestBuilder:
        """
        The categories property
        """
        from .categories.categories_request_builder import CategoriesRequestBuilder

        return CategoriesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def check(self) -> CheckRequestBuilder:
        """
        The check property
        """
        from .check.check_request_builder import CheckRequestBuilder

        return CheckRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def frontend(self) -> FrontendRequestBuilder:
        """
        The frontend property
        """
        from .frontend.frontend_request_builder import FrontendRequestBuilder

        return FrontendRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_rules_for_ticket(self) -> GetRulesForTicketRequestBuilder:
        """
        The getRulesForTicket property
        """
        from .get_rules_for_ticket.get_rules_for_ticket_request_builder import GetRulesForTicketRequestBuilder

        return GetRulesForTicketRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_tickets_for_rule(self) -> GetTicketsForRuleRequestBuilder:
        """
        The getTicketsForRule property
        """
        from .get_tickets_for_rule.get_tickets_for_rule_request_builder import GetTicketsForRuleRequestBuilder

        return GetTicketsForRuleRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def is_ticket(self) -> IsTicketRequestBuilder:
        """
        The isTicket property
        """
        from .is_ticket.is_ticket_request_builder import IsTicketRequestBuilder

        return IsTicketRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def statistics(self) -> StatisticsRequestBuilder:
        """
        The statistics property
        """
        from .statistics.statistics_request_builder import StatisticsRequestBuilder

        return StatisticsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def update_relevant_infos(self) -> UpdateRelevantInfosRequestBuilder:
        """
        The updateRelevantInfos property
        """
        from .update_relevant_infos.update_relevant_infos_request_builder import UpdateRelevantInfosRequestBuilder

        return UpdateRelevantInfosRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class EscalationsRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class EscalationsRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class EscalationsRequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

