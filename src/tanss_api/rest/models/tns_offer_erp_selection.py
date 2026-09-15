from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tns_offer_erp_selection_material_with_material import TnsOfferErpSelectionMaterialWithMaterial

@dataclass
class TnsOfferErpSelection(AdditionalDataHolder, Parsable):
    """
    This object represents an "erp selection" profile to be used in offer templates
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # id of the erp selection
    id: Optional[int] = None
    # The mats property
    mats: Optional[list[TnsOfferErpSelectionMaterialWithMaterial]] = None
    # This prompt will be shown when a user shall specify some material within an offer.
    prompt: Optional[str] = None
    # variable name of the erp selection.This name is used in the offer template within the {ERP:...} syntax
    variable_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsOfferErpSelection:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsOfferErpSelection
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsOfferErpSelection()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .tns_offer_erp_selection_material_with_material import TnsOfferErpSelectionMaterialWithMaterial

        from .tns_offer_erp_selection_material_with_material import TnsOfferErpSelectionMaterialWithMaterial

        fields: dict[str, Callable[[Any], None]] = {
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "mats": lambda n : setattr(self, 'mats', n.get_collection_of_object_values(TnsOfferErpSelectionMaterialWithMaterial)),
            "prompt": lambda n : setattr(self, 'prompt', n.get_str_value()),
            "variableName": lambda n : setattr(self, 'variable_name', n.get_str_value()),
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
        writer.write_collection_of_object_values("mats", self.mats)
        writer.write_str_value("prompt", self.prompt)
        writer.write_str_value("variableName", self.variable_name)
        writer.write_additional_data_value(self.additional_data)
    

