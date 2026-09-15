from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class FilesAndLinksUrlPostRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Identifier of the object this link is assigned to.
    assigned_id: Optional[int] = None
    # Creation timestamp (epoch seconds). Set server-side - a value sent here is overwritten.
    created_at: Optional[int] = None
    # Identifier of the employee who created the entry. Set server-side - a value sent here is overwritten.
    created_by: Optional[int] = None
    # Unique identifier of the file/link entry. Generated server-side.
    id: Optional[int] = None
    # Last modification timestamp (epoch seconds). Set server-side - a value sent here is overwritten.
    modified_at: Optional[int] = None
    # Identifier of the employee who last modified the entry. Set server-side - a value sent here is overwritten.
    modified_by: Optional[int] = None
    # Display title of the link.
    title: Optional[str] = None
    # The stored URL.
    url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> FilesAndLinksUrlPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: FilesAndLinksUrlPostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return FilesAndLinksUrlPostRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "assignedId": lambda n : setattr(self, 'assigned_id', n.get_int_value()),
            "createdAt": lambda n : setattr(self, 'created_at', n.get_int_value()),
            "createdBy": lambda n : setattr(self, 'created_by', n.get_int_value()),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "modifiedAt": lambda n : setattr(self, 'modified_at', n.get_int_value()),
            "modifiedBy": lambda n : setattr(self, 'modified_by', n.get_int_value()),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
            "url": lambda n : setattr(self, 'url', n.get_str_value()),
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
        writer.write_int_value("assignedId", self.assigned_id)
        writer.write_str_value("title", self.title)
        writer.write_str_value("url", self.url)
        writer.write_additional_data_value(self.additional_data)
    

