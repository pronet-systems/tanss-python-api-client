from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class MultiSelectOptionsPutRequestBody(AdditionalDataHolder, Parsable):
    """
    Request body.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Identifier of the checklist item this option belongs to
    checklist_item_id: Optional[int] = None
    # Descriptive text for the option
    description: Optional[str] = None
    # Unique identifier of the multi-select option
    multi_select_id: Optional[int] = None
    # Display name of the option
    name: Optional[str] = None
    # Ordering rank of the option within its item
    rank: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MultiSelectOptionsPutRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MultiSelectOptionsPutRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MultiSelectOptionsPutRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "checklistItemId": lambda n : setattr(self, 'checklist_item_id', n.get_int_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "multiSelectId": lambda n : setattr(self, 'multi_select_id', n.get_int_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "rank": lambda n : setattr(self, 'rank', n.get_int_value()),
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
        writer.write_int_value("checklistItemId", self.checklist_item_id)
        writer.write_str_value("description", self.description)
        writer.write_int_value("multiSelectId", self.multi_select_id)
        writer.write_str_value("name", self.name)
        writer.write_int_value("rank", self.rank)
        writer.write_additional_data_value(self.additional_data)
    

