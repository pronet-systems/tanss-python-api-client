from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class TnsOfferMaterial(AdditionalDataHolder, Parsable):
    """
    Describes a material which is used in an offer
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # amount for this material
    amount: Optional[float] = None
    # article number (optional)
    article_nr: Optional[str] = None
    # discount for this material (optional)
    discount: Optional[float] = None
    # id of the corresponding erp selection for this material
    erp_selection_id: Optional[int] = None
    # id of the corresponding erp selection material for this material
    erp_selection_material_id: Optional[int] = None
    # id of the offer material
    id: Optional[int] = None
    # label / name for this material
    label: Optional[str] = None
    # id of the associated offer
    offer_id: Optional[int] = None
    # position of the material in the offer
    pos: Optional[int] = None
    # single price for this material
    price: Optional[float] = None
    # remark for this material (optional text)
    remark: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsOfferMaterial:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsOfferMaterial
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsOfferMaterial()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "amount": lambda n : setattr(self, 'amount', n.get_float_value()),
            "articleNr": lambda n : setattr(self, 'article_nr', n.get_str_value()),
            "discount": lambda n : setattr(self, 'discount', n.get_float_value()),
            "erpSelectionId": lambda n : setattr(self, 'erp_selection_id', n.get_int_value()),
            "erpSelectionMaterialId": lambda n : setattr(self, 'erp_selection_material_id', n.get_int_value()),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "label": lambda n : setattr(self, 'label', n.get_str_value()),
            "offerId": lambda n : setattr(self, 'offer_id', n.get_int_value()),
            "pos": lambda n : setattr(self, 'pos', n.get_int_value()),
            "price": lambda n : setattr(self, 'price', n.get_float_value()),
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
        writer.write_float_value("amount", self.amount)
        writer.write_str_value("articleNr", self.article_nr)
        writer.write_float_value("discount", self.discount)
        writer.write_int_value("erpSelectionId", self.erp_selection_id)
        writer.write_int_value("erpSelectionMaterialId", self.erp_selection_material_id)
        writer.write_int_value("id", self.id)
        writer.write_str_value("label", self.label)
        writer.write_int_value("offerId", self.offer_id)
        writer.write_int_value("pos", self.pos)
        writer.write_float_value("price", self.price)
        writer.write_str_value("remark", self.remark)
        writer.write_additional_data_value(self.additional_data)
    

