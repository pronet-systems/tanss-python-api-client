from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class CompaniesPutRequestBody(AdditionalDataHolder, Parsable):
    """
    Request body.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # City of the company address
    city: Optional[str] = None
    # Country of the company address
    country: Optional[str] = None
    # Human-readable display identifier of the company
    display_id: Optional[str] = None
    # Primary email address of the company
    email: Optional[str] = None
    # Unique identifier of the company
    id: Optional[int] = None
    # Whether the company is marked inactive
    inactive: Optional[bool] = None
    # Short matchcode used for searching the company
    matchcode: Optional[str] = None
    # Name of the company
    name: Optional[str] = None
    # Postal code of the company address
    postcode: Optional[str] = None
    # Street address of the company
    street: Optional[str] = None
    # Identifier of the company type
    type_id: Optional[int] = None
    # Website URL of the company
    website: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CompaniesPutRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CompaniesPutRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CompaniesPutRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "city": lambda n : setattr(self, 'city', n.get_str_value()),
            "country": lambda n : setattr(self, 'country', n.get_str_value()),
            "displayId": lambda n : setattr(self, 'display_id', n.get_str_value()),
            "email": lambda n : setattr(self, 'email', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "inactive": lambda n : setattr(self, 'inactive', n.get_bool_value()),
            "matchcode": lambda n : setattr(self, 'matchcode', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "postcode": lambda n : setattr(self, 'postcode', n.get_str_value()),
            "street": lambda n : setattr(self, 'street', n.get_str_value()),
            "typeId": lambda n : setattr(self, 'type_id', n.get_int_value()),
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
        writer.write_str_value("city", self.city)
        writer.write_str_value("country", self.country)
        writer.write_str_value("displayId", self.display_id)
        writer.write_str_value("email", self.email)
        writer.write_bool_value("inactive", self.inactive)
        writer.write_str_value("matchcode", self.matchcode)
        writer.write_str_value("name", self.name)
        writer.write_str_value("postcode", self.postcode)
        writer.write_str_value("street", self.street)
        writer.write_int_value("typeId", self.type_id)
        writer.write_str_value("website", self.website)
        writer.write_additional_data_value(self.additional_data)
    

