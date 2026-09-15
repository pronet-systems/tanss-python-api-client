from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tns_ip_mac import TnsIpMac
    from .tns_ip_mac_service_assignment_only_service_id import TnsIpMacServiceAssignmentOnlyServiceId

from .tns_ip_mac import TnsIpMac

@dataclass
class TnsIpMacWithServiceAssignments(TnsIpMac, Parsable):
    # if you define ip addresses, you can also give a list of service assignments which shall be assigned to this ip address
    service_assignments: Optional[list[TnsIpMacServiceAssignmentOnlyServiceId]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsIpMacWithServiceAssignments:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsIpMacWithServiceAssignments
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsIpMacWithServiceAssignments()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .tns_ip_mac import TnsIpMac
        from .tns_ip_mac_service_assignment_only_service_id import TnsIpMacServiceAssignmentOnlyServiceId

        from .tns_ip_mac import TnsIpMac
        from .tns_ip_mac_service_assignment_only_service_id import TnsIpMacServiceAssignmentOnlyServiceId

        fields: dict[str, Callable[[Any], None]] = {
            "serviceAssignments": lambda n : setattr(self, 'service_assignments', n.get_collection_of_object_values(TnsIpMacServiceAssignmentOnlyServiceId)),
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
        writer.write_collection_of_object_values("serviceAssignments", self.service_assignments)
    

