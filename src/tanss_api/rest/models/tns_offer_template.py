from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class TnsOfferTemplate(AdditionalDataHolder, Parsable):
    """
    Describes an offer template
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # id of the employee who has created this offer template
    created_by_employee_id: Optional[int] = None
    # timestamp of the creation of this offer template
    creation_date: Optional[int] = None
    # id of the offer template
    id: Optional[int] = None
    # name of the offer template
    name: Optional[str] = None
    # if the offer template is a "newer" version of another template, the old template (pervious id) goes here
    previous_id: Optional[int] = None
    # you can define here how long (in days) a generated offer will be valid
    valid_in_days: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsOfferTemplate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsOfferTemplate
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsOfferTemplate()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "createdByEmployeeId": lambda n : setattr(self, 'created_by_employee_id', n.get_int_value()),
            "creationDate": lambda n : setattr(self, 'creation_date', n.get_int_value()),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "previousId": lambda n : setattr(self, 'previous_id', n.get_int_value()),
            "validInDays": lambda n : setattr(self, 'valid_in_days', n.get_int_value()),
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
        writer.write_int_value("creationDate", self.creation_date)
        writer.write_str_value("name", self.name)
        writer.write_int_value("previousId", self.previous_id)
        writer.write_int_value("validInDays", self.valid_in_days)
        writer.write_additional_data_value(self.additional_data)
    

