from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tns_offer_erp_selection import TnsOfferErpSelection
    from .tns_offer_template import TnsOfferTemplate

from .tns_offer_template import TnsOfferTemplate

@dataclass
class TnsOfferTemplateDetails(TnsOfferTemplate, Parsable):
    """
    Describes an offer template, including attached erp selections
    """
    # The erpSelections property
    erp_selections: Optional[list[TnsOfferErpSelection]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsOfferTemplateDetails:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsOfferTemplateDetails
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsOfferTemplateDetails()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .tns_offer_erp_selection import TnsOfferErpSelection
        from .tns_offer_template import TnsOfferTemplate

        from .tns_offer_erp_selection import TnsOfferErpSelection
        from .tns_offer_template import TnsOfferTemplate

        fields: dict[str, Callable[[Any], None]] = {
            "erpSelections": lambda n : setattr(self, 'erp_selections', n.get_collection_of_object_values(TnsOfferErpSelection)),
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
        writer.write_collection_of_object_values("erpSelections", self.erp_selections)
    

