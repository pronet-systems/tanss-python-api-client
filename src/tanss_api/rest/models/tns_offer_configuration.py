from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tns_offer_configuration_validity import TnsOfferConfiguration_validity

@dataclass
class TnsOfferConfiguration(AdditionalDataHolder, Parsable):
    """
    Filter, which offers shall be loaded
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # if only offers from one company shall be fetched, give the company id here
    company_id: Optional[int] = None
    # only returns offers from this template
    template_id: Optional[int] = None
    # filters by the "validTill" date — VALID returns only offers still valid, EXPIRED only expired ones, NONE does not filter
    validity: Optional[TnsOfferConfiguration_validity] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsOfferConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsOfferConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsOfferConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .tns_offer_configuration_validity import TnsOfferConfiguration_validity

        from .tns_offer_configuration_validity import TnsOfferConfiguration_validity

        fields: dict[str, Callable[[Any], None]] = {
            "companyId": lambda n : setattr(self, 'company_id', n.get_int_value()),
            "templateId": lambda n : setattr(self, 'template_id', n.get_int_value()),
            "validity": lambda n : setattr(self, 'validity', n.get_enum_value(TnsOfferConfiguration_validity)),
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
        writer.write_int_value("companyId", self.company_id)
        writer.write_int_value("templateId", self.template_id)
        writer.write_enum_value("validity", self.validity)
        writer.write_additional_data_value(self.additional_data)
    

