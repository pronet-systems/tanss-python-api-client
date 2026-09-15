from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tns_checklist_small import TnsChecklistSmall
    from .tns_checklist_type import TnsChecklistType

from .tns_checklist_small import TnsChecklistSmall

@dataclass
class TnsChecklist(TnsChecklistSmall, Parsable):
    """
    describes a checklist
    """
    # is checklist active?
    active: Optional[bool] = None
    # id of the employee who created this checklist
    creator_id: Optional[int] = None
    # describes the checklist, i.e. a short info
    description: Optional[str] = None
    # id of the checklist
    id: Optional[int] = None
    # name of the checklist
    name: Optional[str] = None
    # id of the the previous version of the checklist
    predecessor_id: Optional[int] = None
    # defines the type of a checklist
    type: Optional[TnsChecklistType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsChecklist:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsChecklist
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsChecklist()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .tns_checklist_small import TnsChecklistSmall
        from .tns_checklist_type import TnsChecklistType

        from .tns_checklist_small import TnsChecklistSmall
        from .tns_checklist_type import TnsChecklistType

        fields: dict[str, Callable[[Any], None]] = {
            "active": lambda n : setattr(self, 'active', n.get_bool_value()),
            "creatorId": lambda n : setattr(self, 'creator_id', n.get_int_value()),
            "predecessorId": lambda n : setattr(self, 'predecessor_id', n.get_int_value()),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(TnsChecklistType)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_bool_value("active", self.active)
        writer.write_int_value("creatorId", self.creator_id)
        writer.write_int_value("predecessorId", self.predecessor_id)
        writer.write_enum_value("type", self.type)
    

