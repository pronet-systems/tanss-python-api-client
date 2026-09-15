from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tns_component_built_in_filter_type import TnsComponentBuiltInFilterType
    from .tns_device_base_configuration import TnsDeviceBaseConfiguration

from .tns_device_base_configuration import TnsDeviceBaseConfiguration

@dataclass
class TnsComponentConfiguration(TnsDeviceBaseConfiguration, Parsable):
    """
    Parameters which are used to query for component when displaying a list of component
    """
    # filter settings for "built in" state of the component (i.e. only built into pcs, periphery)
    built_in_filter: Optional[TnsComponentBuiltInFilterType] = None
    # id of the component type to be filtered
    component_type_id: Optional[int] = None
    # if only components of a given pc shall be displayed
    pc_id: Optional[int] = None
    # if only components of a given periphery shall be displayed
    periphery_id: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsComponentConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsComponentConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsComponentConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .tns_component_built_in_filter_type import TnsComponentBuiltInFilterType
        from .tns_device_base_configuration import TnsDeviceBaseConfiguration

        from .tns_component_built_in_filter_type import TnsComponentBuiltInFilterType
        from .tns_device_base_configuration import TnsDeviceBaseConfiguration

        fields: dict[str, Callable[[Any], None]] = {
            "builtInFilter": lambda n : setattr(self, 'built_in_filter', n.get_enum_value(TnsComponentBuiltInFilterType)),
            "componentTypeId": lambda n : setattr(self, 'component_type_id', n.get_int_value()),
            "pcId": lambda n : setattr(self, 'pc_id', n.get_int_value()),
            "peripheryId": lambda n : setattr(self, 'periphery_id', n.get_int_value()),
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
        writer.write_enum_value("builtInFilter", self.built_in_filter)
        writer.write_int_value("componentTypeId", self.component_type_id)
        writer.write_int_value("pcId", self.pc_id)
        writer.write_int_value("peripheryId", self.periphery_id)
    

