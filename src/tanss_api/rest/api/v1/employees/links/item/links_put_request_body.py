from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class LinksPutRequestBody(AdditionalDataHolder, Parsable):
    """
    Request body.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Identifier of the employee this link belongs to. Set server-side from the authenticated user - a value sent here is ignored.
    employee_id: Optional[int] = None
    # Unique identifier of the employee link entry
    id: Optional[int] = None
    # The URL the entry points to
    link: Optional[str] = None
    # Link target behavior, e.g. how the link opens
    target: Optional[str] = None
    # Display heading shown for the link
    title: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LinksPutRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LinksPutRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return LinksPutRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "employeeId": lambda n : setattr(self, 'employee_id', n.get_int_value()),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "link": lambda n : setattr(self, 'link', n.get_str_value()),
            "target": lambda n : setattr(self, 'target', n.get_str_value()),
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
        writer.write_str_value("link", self.link)
        writer.write_str_value("target", self.target)
        writer.write_str_value("title", self.title)
        writer.write_additional_data_value(self.additional_data)
    

