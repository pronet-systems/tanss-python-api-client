from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class TnsTanssEventPostingObject(AdditionalDataHolder, Parsable):
    """
    if the tanss ticket object contains infos about a comment, then the infos are given here
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # content of the comment
    content: Optional[str] = None
    # id of the author / employee
    employee_id: Optional[int] = None
    # name of the author / employee
    employee_name: Optional[str] = None
    # id of the comment
    id: Optional[int] = None
    # true if it's an internal comment
    internal: Optional[bool] = None
    # title of the comment
    title: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsTanssEventPostingObject:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsTanssEventPostingObject
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsTanssEventPostingObject()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "content": lambda n : setattr(self, 'content', n.get_str_value()),
            "employeeId": lambda n : setattr(self, 'employee_id', n.get_int_value()),
            "employeeName": lambda n : setattr(self, 'employee_name', n.get_str_value()),
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
        writer.write_int_value("employeeId", self.employee_id)
        writer.write_str_value("employeeName", self.employee_name)
        writer.write_int_value("id", self.id)
        writer.write_bool_value("internal", self.internal)
        writer.write_str_value("title", self.title)
        writer.write_additional_data_value(self.additional_data)
    

