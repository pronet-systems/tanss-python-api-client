from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .phases.phases_request_builder import PhasesRequestBuilder
    from .phase_init.phase_init_request_builder import PhaseInitRequestBuilder
    from .status.status_request_builder import StatusRequestBuilder
    from .tickets.tickets_request_builder import TicketsRequestBuilder

class WithProjectItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/projects/{projectId}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new WithProjectItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/projects/{projectId}", path_parameters)
    
    @property
    def phase_init(self) -> PhaseInitRequestBuilder:
        """
        The phaseInit property
        """
        from .phase_init.phase_init_request_builder import PhaseInitRequestBuilder

        return PhaseInitRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def phases(self) -> PhasesRequestBuilder:
        """
        The phases property
        """
        from .phases.phases_request_builder import PhasesRequestBuilder

        return PhasesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def status(self) -> StatusRequestBuilder:
        """
        The status property
        """
        from .status.status_request_builder import StatusRequestBuilder

        return StatusRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def tickets(self) -> TicketsRequestBuilder:
        """
        The tickets property
        """
        from .tickets.tickets_request_builder import TicketsRequestBuilder

        return TicketsRequestBuilder(self.request_adapter, self.path_parameters)
    

