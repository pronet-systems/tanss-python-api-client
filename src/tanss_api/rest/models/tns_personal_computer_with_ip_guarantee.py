from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tns_guarantee import TnsGuarantee
    from .tns_ip_mac_with_service_assignments import TnsIpMacWithServiceAssignments
    from .tns_personal_computer import TnsPersonalComputer

from .tns_personal_computer import TnsPersonalComputer

@dataclass
class TnsPersonalComputerWithIpGuarantee(TnsPersonalComputer, Parsable):
    """
    Describes a pc or server with infos (ip address, guarantee)
    """
    # Information of the guarantee or warranty of a device
    guarantee: Optional[TnsGuarantee] = None
    # The ips property
    ips: Optional[list[TnsIpMacWithServiceAssignments]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsPersonalComputerWithIpGuarantee:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsPersonalComputerWithIpGuarantee
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsPersonalComputerWithIpGuarantee()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .tns_guarantee import TnsGuarantee
        from .tns_ip_mac_with_service_assignments import TnsIpMacWithServiceAssignments
        from .tns_personal_computer import TnsPersonalComputer

        from .tns_guarantee import TnsGuarantee
        from .tns_ip_mac_with_service_assignments import TnsIpMacWithServiceAssignments
        from .tns_personal_computer import TnsPersonalComputer

        fields: dict[str, Callable[[Any], None]] = {
            "guarantee": lambda n : setattr(self, 'guarantee', n.get_object_value(TnsGuarantee)),
            "ips": lambda n : setattr(self, 'ips', n.get_collection_of_object_values(TnsIpMacWithServiceAssignments)),
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
        writer.write_object_value("guarantee", self.guarantee)
        writer.write_collection_of_object_values("ips", self.ips)
    

