from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class TnsPeripheryFieldInfo(AdditionalDataHolder, Parsable):
    """
    infos regarding "additional" fields in a periphery
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # id of the additional field
    additional_field_id: Optional[int] = None
    # title name for the field
    title: Optional[str] = None
    # value for this additional field
    value: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsPeripheryFieldInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsPeripheryFieldInfo
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsPeripheryFieldInfo()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "additionalFieldId": lambda n : setattr(self, 'additional_field_id', n.get_int_value()),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
            "value": lambda n : setattr(self, 'value', n.get_str_value()),
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
        writer.write_int_value("additionalFieldId", self.additional_field_id)
        writer.write_str_value("title", self.title)
        writer.write_str_value("value", self.value)
        writer.write_additional_data_value(self.additional_data)
    

