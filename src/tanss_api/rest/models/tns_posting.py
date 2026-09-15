from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class TnsPosting(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # actual content / text
    content: Optional[str] = None
    # date when the posting was created (is filled automatically with the current date by the API when creating items)
    date: Optional[int] = None
    # id of the author of this posting (is filled automatically with the current logged in user by the API when creating items)
    employee_id: Optional[int] = None
    # id of the posting
    id: Optional[int] = None
    # wether the posting is internal or not
    internal: Optional[bool] = None
    # the title of the posting
    title: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsPosting:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsPosting
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsPosting()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "content": lambda n : setattr(self, 'content', n.get_str_value()),
            "date": lambda n : setattr(self, 'date', n.get_int_value()),
            "employeeId": lambda n : setattr(self, 'employee_id', n.get_int_value()),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "internal": lambda n : setattr(self, 'internal', n.get_bool_value()),
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
        writer.write_str_value("content", self.content)
        writer.write_int_value("date", self.date)
        writer.write_int_value("employeeId", self.employee_id)
        writer.write_bool_value("internal", self.internal)
        writer.write_str_value("title", self.title)
        writer.write_additional_data_value(self.additional_data)
    

