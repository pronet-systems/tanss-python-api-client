from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .checklist_items_put_request_body_type import ChecklistItemsPutRequestBody_type

@dataclass
class ChecklistItemsPutRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Identifier of the checklist this item belongs to. Can only be set when creating the item - on update a value sent here is ignored.
    checklist_id: Optional[int] = None
    # Descriptive text for the item
    description: Optional[str] = None
    # Whether this item is the starting point of the checklist
    entry_point: Optional[bool] = None
    # Title or heading shown for the item
    heading: Optional[str] = None
    # Whether the item is currently hidden
    hidden: Optional[bool] = None
    # Unique identifier of the checklist item. Taken from the path parameter - a value sent here is ignored.
    id: Optional[int] = None
    # Identifier of the item that follows this one in the sequence
    next_item_id: Optional[int] = None
    # Service text associated with the item for billing purposes
    service_text: Optional[str] = None
    # The kind of checklist item (field, multi-select, included checklist, etc.)
    type: Optional[ChecklistItemsPutRequestBody_type] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ChecklistItemsPutRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ChecklistItemsPutRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ChecklistItemsPutRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .checklist_items_put_request_body_type import ChecklistItemsPutRequestBody_type

        from .checklist_items_put_request_body_type import ChecklistItemsPutRequestBody_type

        fields: dict[str, Callable[[Any], None]] = {
            "checklistId": lambda n : setattr(self, 'checklist_id', n.get_int_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "entryPoint": lambda n : setattr(self, 'entry_point', n.get_bool_value()),
            "heading": lambda n : setattr(self, 'heading', n.get_str_value()),
            "hidden": lambda n : setattr(self, 'hidden', n.get_bool_value()),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "nextItemId": lambda n : setattr(self, 'next_item_id', n.get_int_value()),
            "serviceText": lambda n : setattr(self, 'service_text', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(ChecklistItemsPutRequestBody_type)),
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
        writer.write_str_value("description", self.description)
        writer.write_bool_value("entryPoint", self.entry_point)
        writer.write_str_value("heading", self.heading)
        writer.write_bool_value("hidden", self.hidden)
        writer.write_int_value("nextItemId", self.next_item_id)
        writer.write_str_value("serviceText", self.service_text)
        writer.write_enum_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    

