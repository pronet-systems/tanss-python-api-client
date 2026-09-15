from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tns_tag_assignment import TnsTagAssignment

@dataclass
class TnsTagWithoutGroupTag(AdditionalDataHolder, Parsable):
    """
    represents a tag
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # background color of the tag (in hex, for example FF0000 - max. 6 chars!)
    background_color: Optional[str] = None
    # description of the tag (optional)
    description: Optional[str] = None
    # font color of the tag (in hex, for example FF0000 - max. 6 chars!)
    font_color: Optional[str] = None
    # id of the group tag
    group_tag_id: Optional[int] = None
    # inherit visibilities from group tag
    group_tag_inheritance: Optional[bool] = None
    # The id property
    id: Optional[int] = None
    # name of image (optional)
    image: Optional[str] = None
    # is the tag a parent for other tags
    is_group_parent: Optional[bool] = None
    # name of the tag
    name: Optional[str] = None
    # visibility assignments (departments, employees, company categories, ticket types)
    visibilities: Optional[list[TnsTagAssignment]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsTagWithoutGroupTag:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsTagWithoutGroupTag
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsTagWithoutGroupTag()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .tns_tag_assignment import TnsTagAssignment

        from .tns_tag_assignment import TnsTagAssignment

        fields: dict[str, Callable[[Any], None]] = {
            "backgroundColor": lambda n : setattr(self, 'background_color', n.get_str_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "fontColor": lambda n : setattr(self, 'font_color', n.get_str_value()),
            "groupTagId": lambda n : setattr(self, 'group_tag_id', n.get_int_value()),
            "groupTagInheritance": lambda n : setattr(self, 'group_tag_inheritance', n.get_bool_value()),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "image": lambda n : setattr(self, 'image', n.get_str_value()),
            "isGroupParent": lambda n : setattr(self, 'is_group_parent', n.get_bool_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "visibilities": lambda n : setattr(self, 'visibilities', n.get_collection_of_object_values(TnsTagAssignment)),
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
        writer.write_str_value("backgroundColor", self.background_color)
        writer.write_str_value("description", self.description)
        writer.write_str_value("fontColor", self.font_color)
        writer.write_int_value("groupTagId", self.group_tag_id)
        writer.write_bool_value("groupTagInheritance", self.group_tag_inheritance)
        writer.write_str_value("image", self.image)
        writer.write_bool_value("isGroupParent", self.is_group_parent)
        writer.write_str_value("name", self.name)
        writer.write_collection_of_object_values("visibilities", self.visibilities)
        writer.write_additional_data_value(self.additional_data)
    

