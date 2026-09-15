from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class TnsGuarantee(AdditionalDataHolder, Parsable):
    """
    Information of the guarantee or warranty of a device
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # date when the guarantee expires
    guarantee_expire: Optional[int] = None
    # number of months (device guarantee)
    guarantee_month: Optional[int] = None
    # link id of the assignment
    link_id: Optional[int] = None
    # link type id of the assignment
    link_type_id: Optional[int] = None
    # date when this device was purchased
    purchase_date: Optional[int] = None
    # Misc. remarks regarding the guarantee / warranty
    remark: Optional[str] = None
    # date when the warranty expires
    warranty_expire: Optional[int] = None
    # number of months (device warranty)
    warranty_month: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsGuarantee:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsGuarantee
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsGuarantee()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "guaranteeExpire": lambda n : setattr(self, 'guarantee_expire', n.get_int_value()),
            "guaranteeMonth": lambda n : setattr(self, 'guarantee_month', n.get_int_value()),
            "linkId": lambda n : setattr(self, 'link_id', n.get_int_value()),
            "linkTypeId": lambda n : setattr(self, 'link_type_id', n.get_int_value()),
            "purchaseDate": lambda n : setattr(self, 'purchase_date', n.get_int_value()),
            "remark": lambda n : setattr(self, 'remark', n.get_str_value()),
            "warrantyExpire": lambda n : setattr(self, 'warranty_expire', n.get_int_value()),
            "warrantyMonth": lambda n : setattr(self, 'warranty_month', n.get_int_value()),
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
        writer.write_int_value("guaranteeExpire", self.guarantee_expire)
        writer.write_int_value("guaranteeMonth", self.guarantee_month)
        writer.write_int_value("linkId", self.link_id)
        writer.write_int_value("linkTypeId", self.link_type_id)
        writer.write_int_value("purchaseDate", self.purchase_date)
        writer.write_str_value("remark", self.remark)
        writer.write_int_value("warrantyExpire", self.warranty_expire)
        writer.write_int_value("warrantyMonth", self.warranty_month)
        writer.write_additional_data_value(self.additional_data)
    

