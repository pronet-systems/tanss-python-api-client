from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tns_material import TnsMaterial
    from .tns_offer_erp_selection_material_source import TnsOfferErpSelectionMaterialSource

from .tns_material import TnsMaterial

@dataclass
class TnsMaterialWithSource(TnsMaterial, Parsable):
    """
    This object represents a TANSS material entry, including the "source" of the material (TANSS / MENTION)
    """
    # determines the "source" for this material selection (either TANSS or MENTION)."articleId" determines the id of the material
    source: Optional[TnsOfferErpSelectionMaterialSource] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsMaterialWithSource:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsMaterialWithSource
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsMaterialWithSource()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .tns_material import TnsMaterial
        from .tns_offer_erp_selection_material_source import TnsOfferErpSelectionMaterialSource

        from .tns_material import TnsMaterial
        from .tns_offer_erp_selection_material_source import TnsOfferErpSelectionMaterialSource

        fields: dict[str, Callable[[Any], None]] = {
            "source": lambda n : setattr(self, 'source', n.get_enum_value(TnsOfferErpSelectionMaterialSource)),
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
        writer.write_enum_value("source", self.source)
    

