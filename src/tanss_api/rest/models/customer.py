from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .category import Category

@dataclass
class Customer(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Indicates if the company is an active or inactive customer
    active: Optional[bool] = None
    # The categories property
    categories: Optional[list[Category]] = None
    # City where the company is located
    city: Optional[str] = None
    # Country where the company is located
    country: Optional[str] = None
    # Represent the Id in the ERP-System
    customer_number: Optional[str] = None
    # General email address of the company
    email: Optional[str] = None
    # Fax number of the company
    fax_number: Optional[str] = None
    # Headquarters of the company
    headquarters: Optional[str] = None
    # Id of the company in tanss
    id: Optional[int] = None
    # Matchcode is a additional field with a unique key
    matchcode: Optional[str] = None
    # Unix timestamp of the last change to the company. Matched against the `modified` request parameter.
    modified: Optional[int] = None
    # Name of the company
    name: Optional[str] = None
    # First telephone number of the company
    phone_number: Optional[str] = None
    # Postalcode of the location
    postal_code: Optional[str] = None
    # Indicates if the company is a private customer
    private: Optional[bool] = None
    # Street where the company is located
    street: Optional[str] = None
    # Web address of the company
    website: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Customer:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Customer
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Customer()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .category import Category

        from .category import Category

        fields: dict[str, Callable[[Any], None]] = {
            "active": lambda n : setattr(self, 'active', n.get_bool_value()),
            "categories": lambda n : setattr(self, 'categories', n.get_collection_of_object_values(Category)),
            "city": lambda n : setattr(self, 'city', n.get_str_value()),
            "country": lambda n : setattr(self, 'country', n.get_str_value()),
            "customer_number": lambda n : setattr(self, 'customer_number', n.get_str_value()),
            "email": lambda n : setattr(self, 'email', n.get_str_value()),
            "fax_number": lambda n : setattr(self, 'fax_number', n.get_str_value()),
            "headquarters": lambda n : setattr(self, 'headquarters', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "matchcode": lambda n : setattr(self, 'matchcode', n.get_str_value()),
            "modified": lambda n : setattr(self, 'modified', n.get_int_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "phone_number": lambda n : setattr(self, 'phone_number', n.get_str_value()),
            "postal_code": lambda n : setattr(self, 'postal_code', n.get_str_value()),
            "private": lambda n : setattr(self, 'private', n.get_bool_value()),
            "street": lambda n : setattr(self, 'street', n.get_str_value()),
            "website": lambda n : setattr(self, 'website', n.get_str_value()),
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
        writer.write_collection_of_object_values("categories", self.categories)
        writer.write_str_value("city", self.city)
        writer.write_str_value("country", self.country)
        writer.write_str_value("customer_number", self.customer_number)
        writer.write_str_value("email", self.email)
        writer.write_str_value("fax_number", self.fax_number)
        writer.write_str_value("headquarters", self.headquarters)
        writer.write_int_value("id", self.id)
        writer.write_str_value("matchcode", self.matchcode)
        writer.write_int_value("modified", self.modified)
        writer.write_str_value("name", self.name)
        writer.write_str_value("phone_number", self.phone_number)
        writer.write_str_value("postal_code", self.postal_code)
        writer.write_bool_value("private", self.private)
        writer.write_str_value("street", self.street)
        writer.write_str_value("website", self.website)
        writer.write_additional_data_value(self.additional_data)
    

