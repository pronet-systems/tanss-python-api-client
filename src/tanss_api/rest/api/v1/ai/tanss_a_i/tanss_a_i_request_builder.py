from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .chat.chat_request_builder import ChatRequestBuilder
    from .summaries.summaries_request_builder import SummariesRequestBuilder
    from .summarize.summarize_request_builder import SummarizeRequestBuilder
    from .tickets.tickets_request_builder import TicketsRequestBuilder

class TanssAIRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/ai/tanssAI
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new TanssAIRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/ai/tanssAI", path_parameters)
    
    @property
    def chat(self) -> ChatRequestBuilder:
        """
        The chat property
        """
        from .chat.chat_request_builder import ChatRequestBuilder

        return ChatRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def summaries(self) -> SummariesRequestBuilder:
        """
        The summaries property
        """
        from .summaries.summaries_request_builder import SummariesRequestBuilder

        return SummariesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def summarize(self) -> SummarizeRequestBuilder:
        """
        The summarize property
        """
        from .summarize.summarize_request_builder import SummarizeRequestBuilder

        return SummarizeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def tickets(self) -> TicketsRequestBuilder:
        """
        The tickets property
        """
        from .tickets.tickets_request_builder import TicketsRequestBuilder

        return TicketsRequestBuilder(self.request_adapter, self.path_parameters)
    

