from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.with_file_item_request_builder import WithFileItemRequestBuilder

class FileRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/documents/file
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new FileRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/documents/file", path_parameters)
    
    def by_file_id(self,file_id: int) -> WithFileItemRequestBuilder:
        """
        Gets an item from the tanss_api.rest.api.v1.documents.file.item collection
        param file_id: Id of the document file attachment to delete.
        Returns: WithFileItemRequestBuilder
        """
        if file_id is None:
            raise TypeError("file_id cannot be null.")
        from .item.with_file_item_request_builder import WithFileItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["fileId"] = file_id
        return WithFileItemRequestBuilder(self.request_adapter, url_tpl_params)
    

