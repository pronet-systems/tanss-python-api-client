from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tns_offer_erp_selection_material_source import TnsOfferErpSelectionMaterialSource
    from .tns_offer_erp_selection_material_type import TnsOfferErpSelectionMaterialType

@dataclass
class TnsOfferErpSelectionMaterial(AdditionalDataHolder, Parsable):
    """
    This object represents a single source of material, which is used in erp selections
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # determines the "id" of the material.* if the source TANSS is used, this represents the id of the TANSS material* if the source MENTION is used, this represents the id of the MENTION material
    article_id: Optional[str] = None
    # id of the associated erp selection
    erp_selection_id: Optional[int] = None
    # id of the erp selection material
    id: Optional[int] = None
    # position of this material.
    pos: Optional[int] = None
    # determines the "source" for this material selection (either TANSS or MENTION)."articleId" determines the id of the material
    source: Optional[TnsOfferErpSelectionMaterialSource] = None
    # (not implemented yet, but a type can be used to determined the "type" of a material)
    type: Optional[TnsOfferErpSelectionMaterialType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsOfferErpSelectionMaterial:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsOfferErpSelectionMaterial
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsOfferErpSelectionMaterial()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .tns_offer_erp_selection_material_source import TnsOfferErpSelectionMaterialSource
        from .tns_offer_erp_selection_material_type import TnsOfferErpSelectionMaterialType

        from .tns_offer_erp_selection_material_source import TnsOfferErpSelectionMaterialSource
        from .tns_offer_erp_selection_material_type import TnsOfferErpSelectionMaterialType

        fields: dict[str, Callable[[Any], None]] = {
            "articleId": lambda n : setattr(self, 'article_id', n.get_str_value()),
            "erpSelectionId": lambda n : setattr(self, 'erp_selection_id', n.get_int_value()),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "pos": lambda n : setattr(self, 'pos', n.get_int_value()),
            "source": lambda n : setattr(self, 'source', n.get_enum_value(TnsOfferErpSelectionMaterialSource)),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(TnsOfferErpSelectionMaterialType)),
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
        writer.write_str_value("articleId", self.article_id)
        writer.write_int_value("erpSelectionId", self.erp_selection_id)
        writer.write_int_value("id", self.id)
        writer.write_int_value("pos", self.pos)
        writer.write_enum_value("source", self.source)
        writer.write_enum_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    

