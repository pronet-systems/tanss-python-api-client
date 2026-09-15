from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tns_company_type import TnsCompanyType

@dataclass
class CompanyDetail(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # city
    city: Optional[str] = None
    # country
    country: Optional[str] = None
    # This is the "displayed id" (=Kundennummer) of the company. The id must be unique, a customer nr. could be used multiple times
    display_id: Optional[str] = None
    # e-Mail
    email: Optional[str] = None
    # if this company is a subsidiary, then here the id of the "central" / "headquerter" company is given
    headquarter_id: Optional[int] = None
    # id of the company
    id: Optional[int] = None
    # If true, the company is inactive
    inactive: Optional[bool] = None
    # if true, this company is locked
    lockout: Optional[bool] = None
    # if company is locked, a reason can be given here
    lockout_reason: Optional[str] = None
    # matchcode (used for searching)
    matchcode: Optional[str] = None
    # name of the company
    name: Optional[str] = None
    # a note for this company
    note: Optional[str] = None
    # postal code
    postcode: Optional[str] = None
    # street
    street: Optional[str] = None
    # a support info (internal remark) can be used here
    support_info: Optional[str] = None
    # telefax number
    telefax: Optional[str] = None
    # phone number
    telephone: Optional[str] = None
    # The types property
    types: Optional[list[TnsCompanyType]] = None
    # website
    website: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CompanyDetail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CompanyDetail
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CompanyDetail()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .tns_company_type import TnsCompanyType

        from .tns_company_type import TnsCompanyType

        fields: dict[str, Callable[[Any], None]] = {
            "city": lambda n : setattr(self, 'city', n.get_str_value()),
            "country": lambda n : setattr(self, 'country', n.get_str_value()),
            "displayId": lambda n : setattr(self, 'display_id', n.get_str_value()),
            "email": lambda n : setattr(self, 'email', n.get_str_value()),
            "headquarterId": lambda n : setattr(self, 'headquarter_id', n.get_int_value()),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "inactive": lambda n : setattr(self, 'inactive', n.get_bool_value()),
            "lockout": lambda n : setattr(self, 'lockout', n.get_bool_value()),
            "lockoutReason": lambda n : setattr(self, 'lockout_reason', n.get_str_value()),
            "matchcode": lambda n : setattr(self, 'matchcode', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "note": lambda n : setattr(self, 'note', n.get_str_value()),
            "postcode": lambda n : setattr(self, 'postcode', n.get_str_value()),
            "street": lambda n : setattr(self, 'street', n.get_str_value()),
            "supportInfo": lambda n : setattr(self, 'support_info', n.get_str_value()),
            "telefax": lambda n : setattr(self, 'telefax', n.get_str_value()),
            "telephone": lambda n : setattr(self, 'telephone', n.get_str_value()),
            "types": lambda n : setattr(self, 'types', n.get_collection_of_object_values(TnsCompanyType)),
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
        writer.write_int_value("headquarterId", self.headquarter_id)
        writer.write_bool_value("inactive", self.inactive)
        writer.write_bool_value("lockout", self.lockout)
        writer.write_str_value("lockoutReason", self.lockout_reason)
        writer.write_str_value("matchcode", self.matchcode)
        writer.write_str_value("name", self.name)
        writer.write_str_value("note", self.note)
        writer.write_str_value("postcode", self.postcode)
        writer.write_str_value("street", self.street)
        writer.write_str_value("supportInfo", self.support_info)
        writer.write_str_value("telefax", self.telefax)
        writer.write_str_value("telephone", self.telephone)
        writer.write_collection_of_object_values("types", self.types)
        writer.write_str_value("website", self.website)
        writer.write_additional_data_value(self.additional_data)
    

