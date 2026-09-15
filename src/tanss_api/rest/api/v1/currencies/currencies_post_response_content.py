from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class CurrenciesPostResponse_content(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The factor property
    factor: Optional[float] = None
    # The id property
    id: Optional[int] = None
    # The name property
    name: Optional[str] = None
    # The symbol property
    symbol: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CurrenciesPostResponse_content:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CurrenciesPostResponse_content
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CurrenciesPostResponse_content()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "factor": lambda n : setattr(self, 'factor', n.get_float_value()),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "symbol": lambda n : setattr(self, 'symbol', n.get_str_value()),
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
        writer.write_float_value("factor", self.factor)
        writer.write_int_value("id", self.id)
        writer.write_str_value("name", self.name)
        writer.write_str_value("symbol", self.symbol)
        writer.write_additional_data_value(self.additional_data)
    

