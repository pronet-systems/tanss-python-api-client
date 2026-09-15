from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class CustomerEmployee_preferred_customer(AdditionalDataHolder, Parsable):
    """
    Preferred company of the employee. Only present when the request was sent without`preferredCustomers=false`. `id` is `0` and `customer_number` empty when no preferredcompany is set; `external_id` is only filled when one is.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The customer_number property
    customer_number: Optional[str] = None
    # The external_id property
    external_id: Optional[str] = None
    # The id property
    id: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CustomerEmployee_preferred_customer:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CustomerEmployee_preferred_customer
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CustomerEmployee_preferred_customer()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "customer_number": lambda n : setattr(self, 'customer_number', n.get_str_value()),
            "external_id": lambda n : setattr(self, 'external_id', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
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
        writer.write_str_value("customer_number", self.customer_number)
        writer.write_str_value("external_id", self.external_id)
        writer.write_int_value("id", self.id)
        writer.write_additional_data_value(self.additional_data)
    

