from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tns_offer import TnsOffer
    from .tns_offer_material import TnsOfferMaterial
    from .tns_offer_variable import TnsOfferVariable

from .tns_offer import TnsOffer

@dataclass
class TnsOfferDetails(TnsOffer, Parsable):
    """
    Describes an offer, including variables and material
    """
    # The mats property
    mats: Optional[list[TnsOfferMaterial]] = None
    # The vars property
    vars: Optional[list[TnsOfferVariable]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsOfferDetails:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsOfferDetails
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsOfferDetails()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .tns_offer import TnsOffer
        from .tns_offer_material import TnsOfferMaterial
        from .tns_offer_variable import TnsOfferVariable

        from .tns_offer import TnsOffer
        from .tns_offer_material import TnsOfferMaterial
        from .tns_offer_variable import TnsOfferVariable

        fields: dict[str, Callable[[Any], None]] = {
            "mats": lambda n : setattr(self, 'mats', n.get_collection_of_object_values(TnsOfferMaterial)),
            "vars": lambda n : setattr(self, 'vars', n.get_collection_of_object_values(TnsOfferVariable)),
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
        writer.write_collection_of_object_values("mats", self.mats)
        writer.write_collection_of_object_values("vars", self.vars)
    

