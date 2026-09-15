from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class FilesAndLinksPostRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Timestamp when the entry was created. Set server-side - a value sent here is overwritten.
    created_at: Optional[int] = None
    # ID of the user who created the entry. Set server-side - a value sent here is overwritten.
    created_by: Optional[int] = None
    # Icon representing the entry
    icon: Optional[str] = None
    # Unique identifier of the file or link entry. Generated server-side.
    id: Optional[int] = None
    # Timestamp when the entry was last modified. Set server-side - a value sent here is overwritten.
    modified_at: Optional[int] = None
    # ID of the user who last modified the entry. Set server-side - a value sent here is overwritten.
    modified_by: Optional[int] = None
    # ID of the parent entry this item is nested under
    parent_id: Optional[int] = None
    # Display title of the file or link entry
    title: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> FilesAndLinksPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: FilesAndLinksPostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return FilesAndLinksPostRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "createdAt": lambda n : setattr(self, 'created_at', n.get_int_value()),
            "createdBy": lambda n : setattr(self, 'created_by', n.get_int_value()),
            "icon": lambda n : setattr(self, 'icon', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "modifiedAt": lambda n : setattr(self, 'modified_at', n.get_int_value()),
            "modifiedBy": lambda n : setattr(self, 'modified_by', n.get_int_value()),
            "parentId": lambda n : setattr(self, 'parent_id', n.get_int_value()),
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
        writer.write_str_value("icon", self.icon)
        writer.write_int_value("parentId", self.parent_id)
        writer.write_str_value("title", self.title)
        writer.write_additional_data_value(self.additional_data)
    

