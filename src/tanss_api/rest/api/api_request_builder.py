from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .calls.calls_request_builder import CallsRequestBuilder
    from .coero.coero_request_builder import CoeroRequestBuilder
    from .device_management.device_management_request_builder import DeviceManagementRequestBuilder
    from .erp.erp_request_builder import ErpRequestBuilder
    from .monitoring.monitoring_request_builder import MonitoringRequestBuilder
    from .remote_supports.remote_supports_request_builder import RemoteSupportsRequestBuilder
    from .servereye.servereye_request_builder import ServereyeRequestBuilder
    from .systemhaus_one.systemhaus_one_request_builder import Systemhaus_oneRequestBuilder
    from .tanss_app.tanss_app_request_builder import TanssAppRequestBuilder
    from .tanss_x.tanss_x_request_builder import TanssXRequestBuilder
    from .timestamps.timestamps_request_builder import TimestampsRequestBuilder
    from .v1.v1_request_builder import V1RequestBuilder

class ApiRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new ApiRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api", path_parameters)
    
    @property
    def calls(self) -> CallsRequestBuilder:
        """
        The calls property
        """
        from .calls.calls_request_builder import CallsRequestBuilder

        return CallsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def coero(self) -> CoeroRequestBuilder:
        """
        The coero property
        """
        from .coero.coero_request_builder import CoeroRequestBuilder

        return CoeroRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_management(self) -> DeviceManagementRequestBuilder:
        """
        The deviceManagement property
        """
        from .device_management.device_management_request_builder import DeviceManagementRequestBuilder

        return DeviceManagementRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def erp(self) -> ErpRequestBuilder:
        """
        The erp property
        """
        from .erp.erp_request_builder import ErpRequestBuilder

        return ErpRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def monitoring(self) -> MonitoringRequestBuilder:
        """
        The monitoring property
        """
        from .monitoring.monitoring_request_builder import MonitoringRequestBuilder

        return MonitoringRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def remote_supports(self) -> RemoteSupportsRequestBuilder:
        """
        The remoteSupports property
        """
        from .remote_supports.remote_supports_request_builder import RemoteSupportsRequestBuilder

        return RemoteSupportsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def servereye(self) -> ServereyeRequestBuilder:
        """
        The servereye property
        """
        from .servereye.servereye_request_builder import ServereyeRequestBuilder

        return ServereyeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def systemhaus_one(self) -> Systemhaus_oneRequestBuilder:
        """
        The systemhaus_one property
        """
        from .systemhaus_one.systemhaus_one_request_builder import Systemhaus_oneRequestBuilder

        return Systemhaus_oneRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def tanss_app(self) -> TanssAppRequestBuilder:
        """
        The tanssApp property
        """
        from .tanss_app.tanss_app_request_builder import TanssAppRequestBuilder

        return TanssAppRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def tanss_x(self) -> TanssXRequestBuilder:
        """
        The tanssX property
        """
        from .tanss_x.tanss_x_request_builder import TanssXRequestBuilder

        return TanssXRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def timestamps(self) -> TimestampsRequestBuilder:
        """
        The timestamps property
        """
        from .timestamps.timestamps_request_builder import TimestampsRequestBuilder

        return TimestampsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def v1(self) -> V1RequestBuilder:
        """
        The v1 property
        """
        from .v1.v1_request_builder import V1RequestBuilder

        return V1RequestBuilder(self.request_adapter, self.path_parameters)
    

