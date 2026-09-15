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
    from .....models.email_settings403_error import EmailSettings403Error
    from .auth_url.auth_url_request_builder import AuthUrlRequestBuilder
    from .email_settings_get_response import EmailSettingsGetResponse
    from .email_settings_put_request_body import EmailSettingsPutRequestBody
    from .email_settings_put_response import EmailSettingsPutResponse
    from .mail_folders.mail_folders_request_builder import MailFoldersRequestBuilder
    from .messages.messages_request_builder import MessagesRequestBuilder
    from .smtp_auth_url.smtp_auth_url_request_builder import SmtpAuthUrlRequestBuilder

class EmailSettingsItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/emailSettings/{id}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new EmailSettingsItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/emailSettings/{id}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Removes a mailbox configuration. After deletion that inbox is no longer available for sending/receiving mail from tickets.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from .....models.email_settings403_error import EmailSettings403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": EmailSettings403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[EmailSettingsGetResponse]:
        """
        Returns the full object for a single mailbox so the configuration view can edit POP3/IMAP/SMTP credentials or Microsoft Graph linkage.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[EmailSettingsGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .....models.email_settings403_error import EmailSettings403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": EmailSettings403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .email_settings_get_response import EmailSettingsGetResponse

        return await self.request_adapter.send_async(request_info, EmailSettingsGetResponse, error_mapping)
    
    async def put(self,body: EmailSettingsPutRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[EmailSettingsPutResponse]:
        """
        Updates an existing mailbox configuration (credentials, encryption, sender name, reply template, assignment etc.). The body is a object object.
        param body: Request body.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[EmailSettingsPutResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        from .....models.email_settings403_error import EmailSettings403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": EmailSettings403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .email_settings_put_response import EmailSettingsPutResponse

        return await self.request_adapter.send_async(request_info, EmailSettingsPutResponse, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Removes a mailbox configuration. After deletion that inbox is no longer available for sending/receiving mail from tickets.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Returns the full object for a single mailbox so the configuration view can edit POP3/IMAP/SMTP credentials or Microsoft Graph linkage.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_put_request_information(self,body: EmailSettingsPutRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Updates an existing mailbox configuration (credentials, encryption, sender name, reply template, assignment etc.). The body is a object object.
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
    
    def with_url(self,raw_url: str) -> EmailSettingsItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: EmailSettingsItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return EmailSettingsItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def auth_url(self) -> AuthUrlRequestBuilder:
        """
        The authUrl property
        """
        from .auth_url.auth_url_request_builder import AuthUrlRequestBuilder

        return AuthUrlRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def mail_folders(self) -> MailFoldersRequestBuilder:
        """
        The mailFolders property
        """
        from .mail_folders.mail_folders_request_builder import MailFoldersRequestBuilder

        return MailFoldersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def messages(self) -> MessagesRequestBuilder:
        """
        The messages property
        """
        from .messages.messages_request_builder import MessagesRequestBuilder

        return MessagesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def smtp_auth_url(self) -> SmtpAuthUrlRequestBuilder:
        """
        The smtpAuthUrl property
        """
        from .smtp_auth_url.smtp_auth_url_request_builder import SmtpAuthUrlRequestBuilder

        return SmtpAuthUrlRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class EmailSettingsItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class EmailSettingsItemRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class EmailSettingsItemRequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

