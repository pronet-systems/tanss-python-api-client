from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class TnsCustomerNotification(AdditionalDataHolder, Parsable):
    """
    Benachrichtigung im Kundenportal inkl. Firmen-/Firmentyp-Zuordnungen.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Aktiv
    active: Optional[bool] = None
    # IDs der zugeordneten Firmen
    companies: Optional[list[int]] = None
    # IDs der zugeordneten Firmentypen
    company_types: Optional[list[int]] = None
    # Inhalt
    content: Optional[str] = None
    # Gültig ab (Unix-Sekunden; 0 = unbegrenzt)
    date_from: Optional[int] = None
    # Gültig bis (Unix-Sekunden; 0 = unbegrenzt)
    date_to: Optional[int] = None
    # ID der Benachrichtigung
    id: Optional[int] = None
    # Priorität
    priority: Optional[int] = None
    # Titel
    title: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsCustomerNotification:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsCustomerNotification
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsCustomerNotification()
    
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
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
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
        writer.write_int_value("id", self.id)
        writer.write_int_value("priority", self.priority)
        writer.write_str_value("title", self.title)
        writer.write_additional_data_value(self.additional_data)
    

