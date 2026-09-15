from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.with_ext_program_item_request_builder import WithExt_programItemRequestBuilder
    from .log.log_request_builder import LogRequestBuilder

class JwtsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/jwts
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new JwtsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/jwts", path_parameters)
    
    def by_ext_program(self,ext_program: str) -> WithExt_programItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.v1.jwts.item collection
        param ext_program: Identifier of the external program the JWT is minted for.
        Returns: WithExt_programItemRequestBuilder
        """
        if ext_program is None:
            raise TypeError("ext_program cannot be null.")
        from .item.with_ext_program_item_request_builder import WithExt_programItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["ext_program"] = ext_program
        return WithExt_programItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    @property
    def log(self) -> LogRequestBuilder:
        """
        The log property
        """
        from .log.log_request_builder import LogRequestBuilder

        return LogRequestBuilder(self.request_adapter, self.path_parameters)
    

