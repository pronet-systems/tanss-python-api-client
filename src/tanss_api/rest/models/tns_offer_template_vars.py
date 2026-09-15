from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tns_checklist_item_var import TnsChecklistItemVar
    from .tns_offer_template_details import TnsOfferTemplateDetails

from .tns_offer_template_details import TnsOfferTemplateDetails

@dataclass
class TnsOfferTemplateVars(TnsOfferTemplateDetails, Parsable):
    """
    Describes an offer template, including attached erp selections and processed vars
    """
    # The vars property
    vars: Optional[list[TnsChecklistItemVar]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsOfferTemplateVars:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsOfferTemplateVars
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsOfferTemplateVars()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .tns_checklist_item_var import TnsChecklistItemVar
        from .tns_offer_template_details import TnsOfferTemplateDetails

        from .tns_checklist_item_var import TnsChecklistItemVar
        from .tns_offer_template_details import TnsOfferTemplateDetails

        fields: dict[str, Callable[[Any], None]] = {
            "vars": lambda n : setattr(self, 'vars', n.get_collection_of_object_values(TnsChecklistItemVar)),
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
        writer.write_collection_of_object_values("vars", self.vars)
    

