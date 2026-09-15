from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tns_price_commons import TnsPriceCommons

from .tns_price_commons import TnsPriceCommons

@dataclass
class TnsAccountingTypePrice(TnsPriceCommons, Parsable):
    """
    This object represents a special accountig type price
    """
    # id of the counting type
    accounting_type_id: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsAccountingTypePrice:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsAccountingTypePrice
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsAccountingTypePrice()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .tns_price_commons import TnsPriceCommons

        from .tns_price_commons import TnsPriceCommons

        fields: dict[str, Callable[[Any], None]] = {
            "accountingTypeId": lambda n : setattr(self, 'accounting_type_id', n.get_int_value()),
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
        writer.write_int_value("accountingTypeId", self.accounting_type_id)
    

