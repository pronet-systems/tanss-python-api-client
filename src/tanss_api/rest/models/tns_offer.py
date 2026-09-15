from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class TnsOffer(AdditionalDataHolder, Parsable):
    """
    Describes an offer
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # id othe employee who has created this offer
    created_by_employee_id: Optional[int] = None
    # creation date of this offer
    date: Optional[int] = None
    # id of the offer
    id: Optional[int] = None
    # id of the offer assignment
    link_id: Optional[int] = None
    # link type of the offer assignment
    link_type_id: Optional[int] = None
    # name of the offer
    name: Optional[str] = None
    # date which the offer expires
    valid_till: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsOffer:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsOffer
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsOffer()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "createdByEmployeeId": lambda n : setattr(self, 'created_by_employee_id', n.get_int_value()),
            "date": lambda n : setattr(self, 'date', n.get_int_value()),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "linkId": lambda n : setattr(self, 'link_id', n.get_int_value()),
            "linkTypeId": lambda n : setattr(self, 'link_type_id', n.get_int_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "validTill": lambda n : setattr(self, 'valid_till', n.get_int_value()),
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
        writer.write_int_value("createdByEmployeeId", self.created_by_employee_id)
        writer.write_int_value("date", self.date)
        writer.write_int_value("linkId", self.link_id)
        writer.write_int_value("linkTypeId", self.link_type_id)
        writer.write_str_value("name", self.name)
        writer.write_int_value("validTill", self.valid_till)
        writer.write_additional_data_value(self.additional_data)
    

