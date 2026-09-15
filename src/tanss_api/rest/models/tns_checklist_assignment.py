from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class TnsChecklistAssignment(AdditionalDataHolder, Parsable):
    """
    infos regarding as assignment between a checklist and i.e. a ticket
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # if checklist was completed by a process, id of the employee who has completed the checklist is given here
    completed_by_employee_id: Optional[int] = None
    # if checklist was completed by a process, defines the date (timestamp)
    completed_on_date: Optional[int] = None
    # if checklist was completed by a process, a reason (text) could be given in the process event
    completed_reason: Optional[str] = None
    # rank (position) of the checklist
    rank: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsChecklistAssignment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsChecklistAssignment
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsChecklistAssignment()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "completedByEmployeeId": lambda n : setattr(self, 'completed_by_employee_id', n.get_int_value()),
            "completedOnDate": lambda n : setattr(self, 'completed_on_date', n.get_int_value()),
            "completedReason": lambda n : setattr(self, 'completed_reason', n.get_str_value()),
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
        writer.write_int_value("completedByEmployeeId", self.completed_by_employee_id)
        writer.write_int_value("completedOnDate", self.completed_on_date)
        writer.write_str_value("completedReason", self.completed_reason)
        writer.write_int_value("rank", self.rank)
        writer.write_additional_data_value(self.additional_data)
    

