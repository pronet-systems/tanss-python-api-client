from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class TnsPhoneCallIdentify(AdditionalDataHolder, Parsable):
    """
    Minimal phone call object containing only from/to phone numbers
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Phone number of the caller (= "from" number)
    from_phone_number: Optional[str] = None
    # Phone number of the called (= "to" number)
    to_phone_number: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsPhoneCallIdentify:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsPhoneCallIdentify
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsPhoneCallIdentify()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "fromPhoneNumber": lambda n : setattr(self, 'from_phone_number', n.get_str_value()),
            "toPhoneNumber": lambda n : setattr(self, 'to_phone_number', n.get_str_value()),
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
        writer.write_str_value("fromPhoneNumber", self.from_phone_number)
        writer.write_str_value("toPhoneNumber", self.to_phone_number)
        writer.write_additional_data_value(self.additional_data)
    

