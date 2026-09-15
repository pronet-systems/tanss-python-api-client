from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class ActionPutRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Identifier of the checklist the action belongs to
    checklist_id: Optional[int] = None
    # Identifier of the checklist item the action refers to
    checklist_item_id: Optional[int] = None
    # Identifier of the top-level checklist
    checklist_main_id: Optional[int] = None
    # Timestamp when the action was performed
    date: Optional[int] = None
    # Whether the action is hidden
    hidden: Optional[bool] = None
    # Identifier of the linked entity the checklist is attached to
    link_id: Optional[int] = None
    # Type of the linked entity the checklist is attached to
    link_type_id: Optional[int] = None
    # Identifier of the related support ticket
    support_id: Optional[int] = None
    # Identifier of the employee who performed the action
    user_id: Optional[int] = None
    # Recorded value for the action; a positive value marks the item as checked
    value: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ActionPutRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ActionPutRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ActionPutRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "checklistId": lambda n : setattr(self, 'checklist_id', n.get_int_value()),
            "checklistItemId": lambda n : setattr(self, 'checklist_item_id', n.get_int_value()),
            "checklistMainId": lambda n : setattr(self, 'checklist_main_id', n.get_int_value()),
            "date": lambda n : setattr(self, 'date', n.get_int_value()),
            "hidden": lambda n : setattr(self, 'hidden', n.get_bool_value()),
            "linkId": lambda n : setattr(self, 'link_id', n.get_int_value()),
            "linkTypeId": lambda n : setattr(self, 'link_type_id', n.get_int_value()),
            "supportId": lambda n : setattr(self, 'support_id', n.get_int_value()),
            "userId": lambda n : setattr(self, 'user_id', n.get_int_value()),
            "value": lambda n : setattr(self, 'value', n.get_int_value()),
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
        writer.write_int_value("checklistId", self.checklist_id)
        writer.write_int_value("checklistItemId", self.checklist_item_id)
        writer.write_int_value("checklistMainId", self.checklist_main_id)
        writer.write_int_value("date", self.date)
        writer.write_bool_value("hidden", self.hidden)
        writer.write_int_value("linkId", self.link_id)
        writer.write_int_value("linkTypeId", self.link_type_id)
        writer.write_int_value("supportId", self.support_id)
        writer.write_int_value("userId", self.user_id)
        writer.write_int_value("value", self.value)
        writer.write_additional_data_value(self.additional_data)
    

