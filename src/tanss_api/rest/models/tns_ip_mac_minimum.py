from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class TnsIpMacMinimum(AdditionalDataHolder, Parsable):
    """
    Information of network interface options (such as ip or mac address)
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # is this entry a dhcp assigned ip address?
    dhcp: Optional[bool] = None
    # ip address
    ip: Optional[str] = None
    # mac address
    mac: Optional[str] = None
    # remarks
    remark: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsIpMacMinimum:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsIpMacMinimum
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsIpMacMinimum()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "dhcp": lambda n : setattr(self, 'dhcp', n.get_bool_value()),
            "ip": lambda n : setattr(self, 'ip', n.get_str_value()),
            "mac": lambda n : setattr(self, 'mac', n.get_str_value()),
            "remark": lambda n : setattr(self, 'remark', n.get_str_value()),
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
        writer.write_str_value("ip", self.ip)
        writer.write_str_value("mac", self.mac)
        writer.write_str_value("remark", self.remark)
        writer.write_additional_data_value(self.additional_data)
    

