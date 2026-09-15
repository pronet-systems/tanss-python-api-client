from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class WithCompanyDeleteRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The customerLinkId property
    customer_link_id: Optional[int] = None
    # The customerLinkTypeId property
    customer_link_type_id: Optional[int] = None
    # The delivererLinkId property
    deliverer_link_id: Optional[int] = None
    # The delivererLinkTypeId property
    deliverer_link_type_id: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WithCompanyDeleteRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WithCompanyDeleteRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WithCompanyDeleteRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "customerLinkId": lambda n : setattr(self, 'customer_link_id', n.get_int_value()),
            "customerLinkTypeId": lambda n : setattr(self, 'customer_link_type_id', n.get_int_value()),
            "delivererLinkId": lambda n : setattr(self, 'deliverer_link_id', n.get_int_value()),
            "delivererLinkTypeId": lambda n : setattr(self, 'deliverer_link_type_id', n.get_int_value()),
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
        writer.write_int_value("customerLinkId", self.customer_link_id)
        writer.write_int_value("customerLinkTypeId", self.customer_link_type_id)
        writer.write_int_value("delivererLinkId", self.deliverer_link_id)
        writer.write_int_value("delivererLinkTypeId", self.deliverer_link_type_id)
        writer.write_additional_data_value(self.additional_data)
    

