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
    from ....models.email_settings403_error import EmailSettings403Error
    from .email_settings_get_response import EmailSettingsGetResponse
    from .email_settings_post_request_body import EmailSettingsPostRequestBody
    from .email_settings_post_response import EmailSettingsPostResponse
    from .item.email_settings_item_request_builder import EmailSettingsItemRequestBuilder
    from .properties.properties_request_builder import PropertiesRequestBuilder

class EmailSettingsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/emailSettings
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new EmailSettingsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/emailSettings", path_parameters)
    
    def by_id(self,id: int) -> EmailSettingsItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.v1.emailSettings.item collection
        param id: Id of the mailbox / email settings entry.
        Returns: EmailSettingsItemRequestBuilder
        """
        if id is None:
            raise TypeError("id cannot be null.")
        from .item.email_settings_item_request_builder import EmailSettingsItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["id"] = id
        return EmailSettingsItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[EmailSettingsGetResponse]:
        """
        Returns all configured mailboxes (POP3/IMAP/Microsoft Graph accounts) that the current technician may access, including linked-entity data needed by the mail-settings administration view. Used to populate the list of inboxes a technician can pick when sending mail from a ticket.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[EmailSettingsGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ....models.email_settings403_error import EmailSettings403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": EmailSettings403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .email_settings_get_response import EmailSettingsGetResponse

        return await self.request_adapter.send_async(request_info, EmailSettingsGetResponse, error_mapping)
    
    async def post(self,body: EmailSettingsPostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[EmailSettingsPostResponse]:
        """
        Creates a new mailbox configuration (POP3/IMAP/SMTP credentials or Microsoft Graph link) used by techs to send and receive emails from tickets. The body is a object object.
        param body: Request body.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[EmailSettingsPostResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ....models.email_settings403_error import EmailSettings403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": EmailSettings403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .email_settings_post_response import EmailSettingsPostResponse

        return await self.request_adapter.send_async(request_info, EmailSettingsPostResponse, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Returns all configured mailboxes (POP3/IMAP/Microsoft Graph accounts) that the current technician may access, including linked-entity data needed by the mail-settings administration view. Used to populate the list of inboxes a technician can pick when sending mail from a ticket.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: EmailSettingsPostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Creates a new mailbox configuration (POP3/IMAP/SMTP credentials or Microsoft Graph link) used by techs to send and receive emails from tickets. The body is a object object.
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
    
    def with_url(self,raw_url: str) -> EmailSettingsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: EmailSettingsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return EmailSettingsRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def properties(self) -> PropertiesRequestBuilder:
        """
        The properties property
        """
        from .properties.properties_request_builder import PropertiesRequestBuilder

        return PropertiesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class EmailSettingsRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class EmailSettingsRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

