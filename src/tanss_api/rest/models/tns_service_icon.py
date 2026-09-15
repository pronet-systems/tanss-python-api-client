from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tns_service_icon_type import TnsServiceIconType

@dataclass
class TnsServiceIcon(AdditionalDataHolder, Parsable):
    """
    Service icon which is shown when listing pcs or server.They are used to establish a connection to the device.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # address which is used to establish the connection (mostly the ip address)
    address: Optional[str] = None
    # if the service has a special "call" (command line or url), the command is given
    command: Optional[str] = None
    # name of the service
    name: Optional[str] = None
    # if the service has an "own" icon, here the name of the image is given
    symbol: Optional[str] = None
    # Defines the "type" of the service icon
    type: Optional[TnsServiceIconType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsServiceIcon:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsServiceIcon
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsServiceIcon()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .tns_service_icon_type import TnsServiceIconType

        from .tns_service_icon_type import TnsServiceIconType

        fields: dict[str, Callable[[Any], None]] = {
            "address": lambda n : setattr(self, 'address', n.get_str_value()),
            "command": lambda n : setattr(self, 'command', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "symbol": lambda n : setattr(self, 'symbol', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(TnsServiceIconType)),
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
        writer.write_str_value("address", self.address)
        writer.write_str_value("command", self.command)
        writer.write_str_value("name", self.name)
        writer.write_str_value("symbol", self.symbol)
        writer.write_enum_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    

