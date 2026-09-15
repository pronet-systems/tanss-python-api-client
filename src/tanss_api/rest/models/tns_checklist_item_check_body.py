from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tns_checklist_item_check_body_vars import TnsChecklistItemCheckBody_vars

@dataclass
class TnsChecklistItemCheckBody(AdditionalDataHolder, Parsable):
    """
    infos required for checking an item in a checklist
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # id of the checklist which this item is in
    checklist_id: Optional[int] = None
    # id of the checlist item that will be checked
    item_id: Optional[int] = None
    # link id of the assignment (if assigned to a ticket then the ticket id goes here)
    link_id: Optional[int] = None
    # linktype of the assignment (i.e. 11 for ticket)
    link_type_id: Optional[int] = None
    # if the item is part of an "included" checklist, you must specify the "main" checklist as well
    main_checklist_id: Optional[int] = None
    # if an multiselect option is checked, give the multiselect option id here
    multi_select_id: Optional[int] = None
    # 1 = check / 0 = uncheck
    value: Optional[int] = None
    # if vars are needed for checking this field, then give these here
    vars: Optional[TnsChecklistItemCheckBody_vars] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsChecklistItemCheckBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsChecklistItemCheckBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsChecklistItemCheckBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .tns_checklist_item_check_body_vars import TnsChecklistItemCheckBody_vars

        from .tns_checklist_item_check_body_vars import TnsChecklistItemCheckBody_vars

        fields: dict[str, Callable[[Any], None]] = {
            "checklistId": lambda n : setattr(self, 'checklist_id', n.get_int_value()),
            "itemId": lambda n : setattr(self, 'item_id', n.get_int_value()),
            "linkId": lambda n : setattr(self, 'link_id', n.get_int_value()),
            "linkTypeId": lambda n : setattr(self, 'link_type_id', n.get_int_value()),
            "mainChecklistId": lambda n : setattr(self, 'main_checklist_id', n.get_int_value()),
            "multiSelectId": lambda n : setattr(self, 'multi_select_id', n.get_int_value()),
            "value": lambda n : setattr(self, 'value', n.get_int_value()),
            "vars": lambda n : setattr(self, 'vars', n.get_object_value(TnsChecklistItemCheckBody_vars)),
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
        writer.write_int_value("itemId", self.item_id)
        writer.write_int_value("linkId", self.link_id)
        writer.write_int_value("linkTypeId", self.link_type_id)
        writer.write_int_value("mainChecklistId", self.main_checklist_id)
        writer.write_int_value("multiSelectId", self.multi_select_id)
        writer.write_int_value("value", self.value)
        writer.write_object_value("vars", self.vars)
        writer.write_additional_data_value(self.additional_data)
    

