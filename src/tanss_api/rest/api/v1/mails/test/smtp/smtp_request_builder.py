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
    from ......models.smtp403_error import Smtp403Error
    from ......models.smtp500_error import Smtp500Error
    from ......models.tns_email_settings_smtp import TnsEmailSettingsSmtp
    from .smtp_post_response import SmtpPostResponse

class SmtpRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/mails/test/smtp
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new SmtpRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/mails/test/smtp?receiver={receiver}", path_parameters)
    
    async def post(self,body: TnsEmailSettingsSmtp, request_configuration: Optional[RequestConfiguration[SmtpRequestBuilderPostQueryParameters]] = None) -> Optional[SmtpPostResponse]:
        """
        Route for testing smtp server settings. This route sends a mail to the specified receiver.Need the permission to access the OSK in order to use this route.
        param body: configuration of smtp server settings (for sending mails)
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[SmtpPostResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ......models.smtp403_error import Smtp403Error
        from ......models.smtp500_error import Smtp500Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": Smtp403Error,
            "500": Smtp500Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .smtp_post_response import SmtpPostResponse

        return await self.request_adapter.send_async(request_info, SmtpPostResponse, error_mapping)
    
    def to_post_request_information(self,body: TnsEmailSettingsSmtp, request_configuration: Optional[RequestConfiguration[SmtpRequestBuilderPostQueryParameters]] = None) -> RequestInformation:
        """
        Route for testing smtp server settings. This route sends a mail to the specified receiver.Need the permission to access the OSK in order to use this route.
        param body: configuration of smtp server settings (for sending mails)
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
    
    def with_url(self,raw_url: str) -> SmtpRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: SmtpRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return SmtpRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class SmtpRequestBuilderPostQueryParameters():
        """
        Route for testing smtp server settings. This route sends a mail to the specified receiver.Need the permission to access the OSK in order to use this route.
        """
        # receiver of the test message
        receiver: Optional[str] = None

    
    @dataclass
    class SmtpRequestBuilderPostRequestConfiguration(RequestConfiguration[SmtpRequestBuilderPostQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

