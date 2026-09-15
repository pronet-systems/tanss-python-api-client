from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tns_phone_number_found_type import TnsPhoneNumberFoundType

@dataclass
class TnsPhoneNumberFoundItem(AdditionalDataHolder, Parsable):
    """
    Determines a source of a phone number which could be retrieved from a company or an employee
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # describes if the company or employee is still active
    active: Optional[bool] = None
    # Describes how many chars were left out while doing the search.This could have been the case when searching for companies. In this case, some chars will be left out so thatnumber extensions can be searched as well. Example:* A company has the phone number 06154/6006-0* You search for a number 06154/6006-123* The system will try to replace the last 3 chars of the company, so that the number could be found as well,  because 06154/6006-123 is an extension to 06154/6006-0
    chars_left_out: Optional[int] = None
    # When searching for employees, the "main" company id of the employee will be returned as well
    company_id: Optional[int] = None
    # id of the company or employee which was found (based on the "type")
    id: Optional[int] = None
    # a string containing the name of the company or employee
    name: Optional[str] = None
    # Determines how a phone number could be matched
    type: Optional[TnsPhoneNumberFoundType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsPhoneNumberFoundItem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsPhoneNumberFoundItem
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsPhoneNumberFoundItem()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .tns_phone_number_found_type import TnsPhoneNumberFoundType

        from .tns_phone_number_found_type import TnsPhoneNumberFoundType

        fields: dict[str, Callable[[Any], None]] = {
            "active": lambda n : setattr(self, 'active', n.get_bool_value()),
            "charsLeftOut": lambda n : setattr(self, 'chars_left_out', n.get_int_value()),
            "companyId": lambda n : setattr(self, 'company_id', n.get_int_value()),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(TnsPhoneNumberFoundType)),
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
        writer.write_int_value("charsLeftOut", self.chars_left_out)
        writer.write_int_value("companyId", self.company_id)
        writer.write_int_value("id", self.id)
        writer.write_str_value("name", self.name)
        writer.write_enum_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    

