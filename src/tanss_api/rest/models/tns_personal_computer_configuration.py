from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tns_device_base_configuration import TnsDeviceBaseConfiguration
    from .tns_server_filter_type import TnsServerFilterType

from .tns_device_base_configuration import TnsDeviceBaseConfiguration

@dataclass
class TnsPersonalComputerConfiguration(TnsDeviceBaseConfiguration, Parsable):
    # show only there os ids
    os_ids: Optional[list[int]] = None
    # filter settings for the "server" state
    servers: Optional[TnsServerFilterType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsPersonalComputerConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsPersonalComputerConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsPersonalComputerConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .tns_device_base_configuration import TnsDeviceBaseConfiguration
        from .tns_server_filter_type import TnsServerFilterType

        from .tns_device_base_configuration import TnsDeviceBaseConfiguration
        from .tns_server_filter_type import TnsServerFilterType

        fields: dict[str, Callable[[Any], None]] = {
            "osIds": lambda n : setattr(self, 'os_ids', n.get_collection_of_primitive_values(int)),
            "servers": lambda n : setattr(self, 'servers', n.get_enum_value(TnsServerFilterType)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_collection_of_primitive_values("osIds", self.os_ids)
        writer.write_enum_value("servers", self.servers)
    

