from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class TnsRemoteMaintenanceDeviceAssignment(AdditionalDataHolder, Parsable):
    """
    Object containing the "translation" of a deviceId based on a remote support "type" to a TANSS company. Optionally,a linkTypeId / linkId (assignment) can be given as well, so the system knows exactly to which device the deviceId refers.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Company which this deviceId refers to
    company_id: Optional[int] = None
    # DeviceId which is transferred in a remote support object
    device_id: Optional[str] = None
    # LinkId of the assignment which this deviceId refers to
    link_id: Optional[int] = None
    # LinkTypeId of the assignment which this deviceId refers to
    link_type_id: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsRemoteMaintenanceDeviceAssignment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsRemoteMaintenanceDeviceAssignment
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsRemoteMaintenanceDeviceAssignment()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "companyId": lambda n : setattr(self, 'company_id', n.get_int_value()),
            "deviceId": lambda n : setattr(self, 'device_id', n.get_str_value()),
            "linkId": lambda n : setattr(self, 'link_id', n.get_int_value()),
            "linkTypeId": lambda n : setattr(self, 'link_type_id', n.get_int_value()),
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
        writer.write_int_value("companyId", self.company_id)
        writer.write_str_value("deviceId", self.device_id)
        writer.write_int_value("linkId", self.link_id)
        writer.write_int_value("linkTypeId", self.link_type_id)
        writer.write_additional_data_value(self.additional_data)
    

