from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tns_checklist import TnsChecklist
    from .tns_checklist_assignment import TnsChecklistAssignment

from .tns_checklist import TnsChecklist

@dataclass
class TnsChecklistWithAssignmentInfos(TnsChecklist, Parsable):
    """
    model used to render tickets in lists
    """
    # infos regarding as assignment between a checklist and i.e. a ticket
    assignment_infos: Optional[TnsChecklistAssignment] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsChecklistWithAssignmentInfos:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsChecklistWithAssignmentInfos
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsChecklistWithAssignmentInfos()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .tns_checklist import TnsChecklist
        from .tns_checklist_assignment import TnsChecklistAssignment

        from .tns_checklist import TnsChecklist
        from .tns_checklist_assignment import TnsChecklistAssignment

        fields: dict[str, Callable[[Any], None]] = {
            "assignmentInfos": lambda n : setattr(self, 'assignment_infos', n.get_object_value(TnsChecklistAssignment)),
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
        writer.write_object_value("assignmentInfos", self.assignment_infos)
    

