from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .components.components_request_builder import ComponentsRequestBuilder
    from .cpus.cpus_request_builder import CpusRequestBuilder
    from .hdd_types.hdd_types_request_builder import HddTypesRequestBuilder
    from .ips.ips_request_builder import IpsRequestBuilder
    from .manufacturers.manufacturers_request_builder import ManufacturersRequestBuilder
    from .os.os_request_builder import OsRequestBuilder
    from .pcs.pcs_request_builder import PcsRequestBuilder
    from .peripheries.peripheries_request_builder import PeripheriesRequestBuilder
    from .services.services_request_builder import ServicesRequestBuilder

class V1RequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/deviceManagement/v1
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new V1RequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/deviceManagement/v1", path_parameters)
    
    @property
    def components(self) -> ComponentsRequestBuilder:
        """
        The components property
        """
        from .components.components_request_builder import ComponentsRequestBuilder

        return ComponentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def cpus(self) -> CpusRequestBuilder:
        """
        The cpus property
        """
        from .cpus.cpus_request_builder import CpusRequestBuilder

        return CpusRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def hdd_types(self) -> HddTypesRequestBuilder:
        """
        The hddTypes property
        """
        from .hdd_types.hdd_types_request_builder import HddTypesRequestBuilder

        return HddTypesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def ips(self) -> IpsRequestBuilder:
        """
        The ips property
        """
        from .ips.ips_request_builder import IpsRequestBuilder

        return IpsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def manufacturers(self) -> ManufacturersRequestBuilder:
        """
        The manufacturers property
        """
        from .manufacturers.manufacturers_request_builder import ManufacturersRequestBuilder

        return ManufacturersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def os(self) -> OsRequestBuilder:
        """
        The os property
        """
        from .os.os_request_builder import OsRequestBuilder

        return OsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def pcs(self) -> PcsRequestBuilder:
        """
        The pcs property
        """
        from .pcs.pcs_request_builder import PcsRequestBuilder

        return PcsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def peripheries(self) -> PeripheriesRequestBuilder:
        """
        The peripheries property
        """
        from .peripheries.peripheries_request_builder import PeripheriesRequestBuilder

        return PeripheriesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def services(self) -> ServicesRequestBuilder:
        """
        The services property
        """
        from .services.services_request_builder import ServicesRequestBuilder

        return ServicesRequestBuilder(self.request_adapter, self.path_parameters)
    

