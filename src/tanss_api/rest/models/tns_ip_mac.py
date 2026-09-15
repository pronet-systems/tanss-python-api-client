from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tns_ip_mac_assignment_type import TnsIpMacAssignmentType
    from .tns_ip_mac_minimum import TnsIpMacMinimum

from .tns_ip_mac_minimum import TnsIpMacMinimum

@dataclass
class TnsIpMac(TnsIpMacMinimum, Parsable):
    # id of the assignment, which this entry is assigned to (i.e. id of the pc)
    assignment_id: Optional[int] = None
    # determines, which "id" is meant by "assignmentId"
    assignment_type: Optional[TnsIpMacAssignmentType] = None
    # id of this network interface entry
    id: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsIpMac:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsIpMac
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsIpMac()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .tns_ip_mac_assignment_type import TnsIpMacAssignmentType
        from .tns_ip_mac_minimum import TnsIpMacMinimum

        from .tns_ip_mac_assignment_type import TnsIpMacAssignmentType
        from .tns_ip_mac_minimum import TnsIpMacMinimum

        fields: dict[str, Callable[[Any], None]] = {
            "assignmentId": lambda n : setattr(self, 'assignment_id', n.get_int_value()),
            "assignmentType": lambda n : setattr(self, 'assignment_type', n.get_enum_value(TnsIpMacAssignmentType)),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
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
        writer.write_int_value("assignmentId", self.assignment_id)
        writer.write_enum_value("assignmentType", self.assignment_type)
        writer.write_int_value("id", self.id)
    

