from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tns_device_base_configuration import TnsDeviceBaseConfiguration

from .tns_device_base_configuration import TnsDeviceBaseConfiguration

@dataclass
class TnsPeripheryConfiguration(TnsDeviceBaseConfiguration, Parsable):
    """
    Parameters which are used to query for peripheries when displaying a list of peripheries
    """
    # id of the periphery type to be filtered
    periphery_type_id: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsPeripheryConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsPeripheryConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsPeripheryConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .tns_device_base_configuration import TnsDeviceBaseConfiguration

        from .tns_device_base_configuration import TnsDeviceBaseConfiguration

        fields: dict[str, Callable[[Any], None]] = {
            "peripheryTypeId": lambda n : setattr(self, 'periphery_type_id', n.get_int_value()),
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
        writer.write_int_value("peripheryTypeId", self.periphery_type_id)
    

