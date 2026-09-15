from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class CustomerNotificationsPutRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The active property
    active: Optional[bool] = None
    # The companies property
    companies: Optional[list[int]] = None
    # The companyTypes property
    company_types: Optional[list[int]] = None
    # The content property
    content: Optional[str] = None
    # The dateFrom property
    date_from: Optional[int] = None
    # The dateTo property
    date_to: Optional[int] = None
    # The priority property
    priority: Optional[int] = None
    # The title property
    title: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CustomerNotificationsPutRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CustomerNotificationsPutRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CustomerNotificationsPutRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "active": lambda n : setattr(self, 'active', n.get_bool_value()),
            "companies": lambda n : setattr(self, 'companies', n.get_collection_of_primitive_values(int)),
            "companyTypes": lambda n : setattr(self, 'company_types', n.get_collection_of_primitive_values(int)),
            "content": lambda n : setattr(self, 'content', n.get_str_value()),
            "dateFrom": lambda n : setattr(self, 'date_from', n.get_int_value()),
            "dateTo": lambda n : setattr(self, 'date_to', n.get_int_value()),
            "priority": lambda n : setattr(self, 'priority', n.get_int_value()),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
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
        writer.write_bool_value("active", self.active)
        writer.write_collection_of_primitive_values("companies", self.companies)
        writer.write_collection_of_primitive_values("companyTypes", self.company_types)
        writer.write_str_value("content", self.content)
        writer.write_int_value("dateFrom", self.date_from)
        writer.write_int_value("dateTo", self.date_to)
        writer.write_int_value("priority", self.priority)
        writer.write_str_value("title", self.title)
        writer.write_additional_data_value(self.additional_data)
    

