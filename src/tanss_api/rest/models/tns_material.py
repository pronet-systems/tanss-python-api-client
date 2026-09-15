from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class TnsMaterial(AdditionalDataHolder, Parsable):
    """
    This object represents a TANSS material entry
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # article number of this material
    article_number: Optional[str] = None
    # id of this material
    id: Optional[int] = None
    # laben / name of this material
    label: Optional[str] = None
    # price for this material
    price: Optional[float] = None
    # addition text / remark for this material
    remark: Optional[str] = None
    # serial number
    serial_number: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsMaterial:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsMaterial
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsMaterial()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "articleNumber": lambda n : setattr(self, 'article_number', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "label": lambda n : setattr(self, 'label', n.get_str_value()),
            "price": lambda n : setattr(self, 'price', n.get_float_value()),
            "remark": lambda n : setattr(self, 'remark', n.get_str_value()),
            "serialNumber": lambda n : setattr(self, 'serial_number', n.get_str_value()),
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
        writer.write_str_value("articleNumber", self.article_number)
        writer.write_int_value("id", self.id)
        writer.write_str_value("label", self.label)
        writer.write_float_value("price", self.price)
        writer.write_str_value("remark", self.remark)
        writer.write_str_value("serialNumber", self.serial_number)
        writer.write_additional_data_value(self.additional_data)
    

