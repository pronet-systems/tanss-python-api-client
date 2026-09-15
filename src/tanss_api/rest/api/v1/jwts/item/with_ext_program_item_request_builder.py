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
    from .....models.with_ext_program403_error import WithExt_program403Error
    from .with_ext_program_get_response import WithExt_programGetResponse

class WithExt_programItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/jwts/{ext_program}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new WithExt_programItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/jwts/{ext_program}{?duration*,info*,isForTesting*}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[WithExt_programItemRequestBuilderGetQueryParameters]] = None) -> Optional[WithExt_programGetResponse]:
        """
        Mints a JWT that lets an external program (e.g. remote-support agent, mobile app, integration bot)authenticate against this API. The token's lifetime is `duration` (milliseconds, default 1 year), the`info` parameter is stored in the token log so the issued token can be tracked / revoked, and`isForTesting=true` skips that log entry. For `REMOTE_SUPPORT` programs, `info` must be a numeric typecode &ge; 1000.Requires the `CREATE_JWT_TOKENS_FOR_EXTERNAL_PROGRAMMS` permission. The external program must also belicensed (`isExternalProgramConfigured`).
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[WithExt_programGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .....models.with_ext_program403_error import WithExt_program403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": WithExt_program403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .with_ext_program_get_response import WithExt_programGetResponse

        return await self.request_adapter.send_async(request_info, WithExt_programGetResponse, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[WithExt_programItemRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Mints a JWT that lets an external program (e.g. remote-support agent, mobile app, integration bot)authenticate against this API. The token's lifetime is `duration` (milliseconds, default 1 year), the`info` parameter is stored in the token log so the issued token can be tracked / revoked, and`isForTesting=true` skips that log entry. For `REMOTE_SUPPORT` programs, `info` must be a numeric typecode &ge; 1000.Requires the `CREATE_JWT_TOKENS_FOR_EXTERNAL_PROGRAMMS` permission. The external program must also belicensed (`isExternalProgramConfigured`).
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> WithExt_programItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: WithExt_programItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return WithExt_programItemRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class WithExt_programItemRequestBuilderGetQueryParameters():
        """
        Mints a JWT that lets an external program (e.g. remote-support agent, mobile app, integration bot)authenticate against this API. The token's lifetime is `duration` (milliseconds, default 1 year), the`info` parameter is stored in the token log so the issued token can be tracked / revoked, and`isForTesting=true` skips that log entry. For `REMOTE_SUPPORT` programs, `info` must be a numeric typecode &ge; 1000.Requires the `CREATE_JWT_TOKENS_FOR_EXTERNAL_PROGRAMMS` permission. The external program must also belicensed (`isExternalProgramConfigured`).
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "is_for_testing":
                return "isForTesting"
            if original_name == "duration":
                return "duration"
            if original_name == "info":
                return "info"
            return original_name
        
        # Token lifetime in milliseconds (defaults to one year).
        duration: Optional[int] = None

        # Free-text or type-code info stored in the token log for tracking.
        info: Optional[str] = None

        # When true, skips creating the token-log entry.
        is_for_testing: Optional[bool] = None

    
    @dataclass
    class WithExt_programItemRequestBuilderGetRequestConfiguration(RequestConfiguration[WithExt_programItemRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

