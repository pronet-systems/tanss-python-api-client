from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tns_service_call_type import TnsServiceCallType

@dataclass
class TnsService(AdditionalDataHolder, Parsable):
    """
    represents a service (which can be assigned to an ip address on a pc/periphery)
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # is service active or not
    active: Optional[bool] = None
    # defines how a service will be executed
    call_type: Optional[TnsServiceCallType] = None
    # command which shall be executed (via batch file)%1% is the placeholder which contains the ip address
    command: Optional[str] = None
    # id of the service
    id: Optional[int] = None
    # filename of the image representing the service
    symbol: Optional[str] = None
    # name of the service
    text: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsService:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsService
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsService()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .tns_service_call_type import TnsServiceCallType

        from .tns_service_call_type import TnsServiceCallType

        fields: dict[str, Callable[[Any], None]] = {
            "active": lambda n : setattr(self, 'active', n.get_bool_value()),
            "callType": lambda n : setattr(self, 'call_type', n.get_enum_value(TnsServiceCallType)),
            "command": lambda n : setattr(self, 'command', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "symbol": lambda n : setattr(self, 'symbol', n.get_str_value()),
            "text": lambda n : setattr(self, 'text', n.get_str_value()),
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
        writer.write_bool_value("active", self.active)
        writer.write_enum_value("callType", self.call_type)
        writer.write_str_value("command", self.command)
        writer.write_str_value("symbol", self.symbol)
        writer.write_str_value("text", self.text)
        writer.write_additional_data_value(self.additional_data)
    

