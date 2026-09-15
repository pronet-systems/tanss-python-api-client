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
    from .....models.four_zero_three_error import FourZeroThreeError
    from .cloud.cloud_request_builder import CloudRequestBuilder
    from .comments.comments_request_builder import CommentsRequestBuilder
    from .contract_infos.contract_infos_request_builder import ContractInfosRequestBuilder
    from .documents.documents_request_builder import DocumentsRequestBuilder
    from .favorite.favorite_request_builder import FavoriteRequestBuilder
    from .get_response import GetResponse
    from .hash.hash_request_builder import HashRequestBuilder
    from .mails.mails_request_builder import MailsRequestBuilder
    from .mail_attachments.mail_attachments_request_builder import MailAttachmentsRequestBuilder
    from .menu.menu_request_builder import MenuRequestBuilder
    from .merge.merge_request_builder import MergeRequestBuilder
    from .pdf.pdf_request_builder import PdfRequestBuilder
    from .pinned.pinned_request_builder import PinnedRequestBuilder
    from .properties.properties_request_builder import PropertiesRequestBuilder
    from .put_request_body import PutRequestBody
    from .put_response import PutResponse
    from .screenshots.screenshots_request_builder import ScreenshotsRequestBuilder
    from .service_cap.service_cap_request_builder import ServiceCapRequestBuilder
    from .statistics.statistics_request_builder import StatisticsRequestBuilder
    from .upload.upload_request_builder import UploadRequestBuilder

class ItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/tickets/{-id}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new ItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/tickets/{%2Did}{?remitterCheck*,targetTicketId*}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[ItemRequestBuilderDeleteQueryParameters]] = None) -> None:
        """
        This call will delete a ticket.If the parameter "targetTicketId" is given, will also move entities such as chats or callbacks to a target ticket
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from .....models.four_zero_three_error import FourZeroThreeError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": FourZeroThreeError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[GetResponse]:
        """
        Fetches a ticket by id and returns all aspects of the ticket
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[GetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .....models.four_zero_three_error import FourZeroThreeError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": FourZeroThreeError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .get_response import GetResponse

        return await self.request_adapter.send_async(request_info, GetResponse, error_mapping)
    
    async def put(self,body: PutRequestBody, request_configuration: Optional[RequestConfiguration[ItemRequestBuilderPutQueryParameters]] = None) -> Optional[PutResponse]:
        """
        Updated a ticket
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[PutResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        from .....models.four_zero_three_error import FourZeroThreeError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": FourZeroThreeError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .put_response import PutResponse

        return await self.request_adapter.send_async(request_info, PutResponse, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[ItemRequestBuilderDeleteQueryParameters]] = None) -> RequestInformation:
        """
        This call will delete a ticket.If the parameter "targetTicketId" is given, will also move entities such as chats or callbacks to a target ticket
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Fetches a ticket by id and returns all aspects of the ticket
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_put_request_information(self,body: PutRequestBody, request_configuration: Optional[RequestConfiguration[ItemRequestBuilderPutQueryParameters]] = None) -> RequestInformation:
        """
        Updated a ticket
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
    
    def with_url(self,raw_url: str) -> ItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: ItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return ItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def cloud(self) -> CloudRequestBuilder:
        """
        The cloud property
        """
        from .cloud.cloud_request_builder import CloudRequestBuilder

        return CloudRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def comments(self) -> CommentsRequestBuilder:
        """
        The comments property
        """
        from .comments.comments_request_builder import CommentsRequestBuilder

        return CommentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def contract_infos(self) -> ContractInfosRequestBuilder:
        """
        The contractInfos property
        """
        from .contract_infos.contract_infos_request_builder import ContractInfosRequestBuilder

        return ContractInfosRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def documents(self) -> DocumentsRequestBuilder:
        """
        The documents property
        """
        from .documents.documents_request_builder import DocumentsRequestBuilder

        return DocumentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def favorite(self) -> FavoriteRequestBuilder:
        """
        The favorite property
        """
        from .favorite.favorite_request_builder import FavoriteRequestBuilder

        return FavoriteRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def hash(self) -> HashRequestBuilder:
        """
        The hash property
        """
        from .hash.hash_request_builder import HashRequestBuilder

        return HashRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def mail_attachments(self) -> MailAttachmentsRequestBuilder:
        """
        The mailAttachments property
        """
        from .mail_attachments.mail_attachments_request_builder import MailAttachmentsRequestBuilder

        return MailAttachmentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def mails(self) -> MailsRequestBuilder:
        """
        The mails property
        """
        from .mails.mails_request_builder import MailsRequestBuilder

        return MailsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def menu(self) -> MenuRequestBuilder:
        """
        The menu property
        """
        from .menu.menu_request_builder import MenuRequestBuilder

        return MenuRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def merge(self) -> MergeRequestBuilder:
        """
        The merge property
        """
        from .merge.merge_request_builder import MergeRequestBuilder

        return MergeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def pdf(self) -> PdfRequestBuilder:
        """
        The pdf property
        """
        from .pdf.pdf_request_builder import PdfRequestBuilder

        return PdfRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def pinned(self) -> PinnedRequestBuilder:
        """
        The pinned property
        """
        from .pinned.pinned_request_builder import PinnedRequestBuilder

        return PinnedRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def properties(self) -> PropertiesRequestBuilder:
        """
        The properties property
        """
        from .properties.properties_request_builder import PropertiesRequestBuilder

        return PropertiesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def screenshots(self) -> ScreenshotsRequestBuilder:
        """
        The screenshots property
        """
        from .screenshots.screenshots_request_builder import ScreenshotsRequestBuilder

        return ScreenshotsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def service_cap(self) -> ServiceCapRequestBuilder:
        """
        The serviceCap property
        """
        from .service_cap.service_cap_request_builder import ServiceCapRequestBuilder

        return ServiceCapRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def statistics(self) -> StatisticsRequestBuilder:
        """
        The statistics property
        """
        from .statistics.statistics_request_builder import StatisticsRequestBuilder

        return StatisticsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def upload(self) -> UploadRequestBuilder:
        """
        The upload property
        """
        from .upload.upload_request_builder import UploadRequestBuilder

        return UploadRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class ItemRequestBuilderDeleteQueryParameters():
        """
        This call will delete a ticket.If the parameter "targetTicketId" is given, will also move entities such as chats or callbacks to a target ticket
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "target_ticket_id":
                return "targetTicketId"
            return original_name
        
        # if given, will also move entities such as chats or callbacks to a target ticket
        target_ticket_id: Optional[int] = None

    
    @dataclass
    class ItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[ItemRequestBuilderDeleteQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class ItemRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class ItemRequestBuilderPutQueryParameters():
        """
        Updated a ticket
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "remitter_check":
                return "remitterCheck"
            return original_name
        
        # can be given to omit the check that a remitter is required when storing tickets
        remitter_check: Optional[bool] = None

    
    @dataclass
    class ItemRequestBuilderPutRequestConfiguration(RequestConfiguration[ItemRequestBuilderPutQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

