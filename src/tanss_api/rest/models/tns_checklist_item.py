from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tns_checklist_action import TnsChecklistAction
    from .tns_checklist_item_type import TnsChecklistItemType
    from .tns_checklist_item_var import TnsChecklistItemVar

@dataclass
class TnsChecklistItem(AdditionalDataHolder, Parsable):
    """
    represents an item in a checklist
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # describes the "state" of a checklist item, i.e. if it's checked
    action: Optional[TnsChecklistAction] = None
    # id of the checklist, which the item is contained in
    checklist_id: Optional[int] = None
    # description / text of the checklist item
    description: Optional[str] = None
    # true if this is the first item of a checklist
    entry_point: Optional[bool] = None
    # headinh / title of the checklist item
    heading: Optional[str] = None
    # true if thes field is hidden
    hidden: Optional[bool] = None
    # id of the item
    id: Optional[int] = None
    # id of the "next" field in the process chain
    next_item_id: Optional[int] = None
    # text which is used when creating a support
    service_text: Optional[str] = None
    # defines the type of a checklist item
    type: Optional[TnsChecklistItemType] = None
    # if vars were used in teh text, these must be given in the "check" body to fill in the correct values / infos for checking the item
    vars: Optional[list[TnsChecklistItemVar]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsChecklistItem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsChecklistItem
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsChecklistItem()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .tns_checklist_action import TnsChecklistAction
        from .tns_checklist_item_type import TnsChecklistItemType
        from .tns_checklist_item_var import TnsChecklistItemVar

        from .tns_checklist_action import TnsChecklistAction
        from .tns_checklist_item_type import TnsChecklistItemType
        from .tns_checklist_item_var import TnsChecklistItemVar

        fields: dict[str, Callable[[Any], None]] = {
            "action": lambda n : setattr(self, 'action', n.get_object_value(TnsChecklistAction)),
            "checklistId": lambda n : setattr(self, 'checklist_id', n.get_int_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "entryPoint": lambda n : setattr(self, 'entry_point', n.get_bool_value()),
            "heading": lambda n : setattr(self, 'heading', n.get_str_value()),
            "hidden": lambda n : setattr(self, 'hidden', n.get_bool_value()),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "nextItemId": lambda n : setattr(self, 'next_item_id', n.get_int_value()),
            "serviceText": lambda n : setattr(self, 'service_text', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(TnsChecklistItemType)),
            "vars": lambda n : setattr(self, 'vars', n.get_collection_of_object_values(TnsChecklistItemVar)),
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
        writer.write_object_value("action", self.action)
        writer.write_int_value("checklistId", self.checklist_id)
        writer.write_str_value("description", self.description)
        writer.write_bool_value("entryPoint", self.entry_point)
        writer.write_str_value("heading", self.heading)
        writer.write_bool_value("hidden", self.hidden)
        writer.write_int_value("id", self.id)
        writer.write_int_value("nextItemId", self.next_item_id)
        writer.write_str_value("serviceText", self.service_text)
        writer.write_enum_value("type", self.type)
        writer.write_collection_of_object_values("vars", self.vars)
        writer.write_additional_data_value(self.additional_data)
    

