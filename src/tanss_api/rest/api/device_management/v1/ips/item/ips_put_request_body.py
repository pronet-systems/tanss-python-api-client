from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ......models.tns_ip_mac_service_assignment_only_service_id import TnsIpMacServiceAssignmentOnlyServiceId

@dataclass
class IpsPutRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The dhcp property
    dhcp: Optional[bool] = None
    # The hidden property
    hidden: Optional[bool] = None
    # The ip property
    ip: Optional[str] = None
    # The mac property
    mac: Optional[str] = None
    # The remark property
    remark: Optional[str] = None
    # The serviceAssignments property
    service_assignments: Optional[list[TnsIpMacServiceAssignmentOnlyServiceId]] = None
    # The showServices property
    show_services: Optional[bool] = None
    # The sort property
    sort: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> IpsPutRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: IpsPutRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return IpsPutRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ......models.tns_ip_mac_service_assignment_only_service_id import TnsIpMacServiceAssignmentOnlyServiceId

        from ......models.tns_ip_mac_service_assignment_only_service_id import TnsIpMacServiceAssignmentOnlyServiceId

        fields: dict[str, Callable[[Any], None]] = {
            "dhcp": lambda n : setattr(self, 'dhcp', n.get_bool_value()),
            "hidden": lambda n : setattr(self, 'hidden', n.get_bool_value()),
            "ip": lambda n : setattr(self, 'ip', n.get_str_value()),
            "mac": lambda n : setattr(self, 'mac', n.get_str_value()),
            "remark": lambda n : setattr(self, 'remark', n.get_str_value()),
            "serviceAssignments": lambda n : setattr(self, 'service_assignments', n.get_collection_of_object_values(TnsIpMacServiceAssignmentOnlyServiceId)),
            "showServices": lambda n : setattr(self, 'show_services', n.get_bool_value()),
            "sort": lambda n : setattr(self, 'sort', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_bool_value("dhcp", self.dhcp)
        writer.write_bool_value("hidden", self.hidden)
        writer.write_str_value("ip", self.ip)
        writer.write_str_value("mac", self.mac)
        writer.write_str_value("remark", self.remark)
        writer.write_collection_of_object_values("serviceAssignments", self.service_assignments)
        writer.write_bool_value("showServices", self.show_services)
        writer.write_str_value("sort", self.sort)
        writer.write_additional_data_value(self.additional_data)
    

