from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tns_material import TnsMaterial
    from .tns_offer_erp_selection_material import TnsOfferErpSelectionMaterial

from .tns_offer_erp_selection_material import TnsOfferErpSelectionMaterial

@dataclass
class TnsOfferErpSelectionMaterialWithMaterial(TnsOfferErpSelectionMaterial, Parsable):
    """
    This object represents a single source of material, which is used in erp selections (inlcuding attached material infos)
    """
    # This object represents a TANSS material entry
    material: Optional[TnsMaterial] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsOfferErpSelectionMaterialWithMaterial:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsOfferErpSelectionMaterialWithMaterial
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsOfferErpSelectionMaterialWithMaterial()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .tns_material import TnsMaterial
        from .tns_offer_erp_selection_material import TnsOfferErpSelectionMaterial

        from .tns_material import TnsMaterial
        from .tns_offer_erp_selection_material import TnsOfferErpSelectionMaterial

        fields: dict[str, Callable[[Any], None]] = {
            "material": lambda n : setattr(self, 'material', n.get_object_value(TnsMaterial)),
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
        writer.write_object_value("material", self.material)
    

