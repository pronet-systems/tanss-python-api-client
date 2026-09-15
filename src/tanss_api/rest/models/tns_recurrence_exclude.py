from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tns_recurrence_assignment import TnsRecurrenceAssignment

@dataclass
class TnsRecurrenceExclude(AdditionalDataHolder, Parsable):
    """
    Ausnahme zu einer Wiederholungsregel
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The assignments property
    assignments: Optional[list[TnsRecurrenceAssignment]] = None
    # The employeeId property
    employee_id: Optional[int] = None
    # The id property
    id: Optional[int] = None
    # The indexed property
    indexed: Optional[int] = None
    # The isoDateString property
    iso_date_string: Optional[str] = None
    # The ruleId property
    rule_id: Optional[int] = None
    # The ruleLinkId property
    rule_link_id: Optional[int] = None
    # The ruleLinkTypeId property
    rule_link_type_id: Optional[int] = None
    # The sequenceId property
    sequence_id: Optional[int] = None
    # The timestamp property
    timestamp: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsRecurrenceExclude:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsRecurrenceExclude
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsRecurrenceExclude()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .tns_recurrence_assignment import TnsRecurrenceAssignment

        from .tns_recurrence_assignment import TnsRecurrenceAssignment

        fields: dict[str, Callable[[Any], None]] = {
            "assignments": lambda n : setattr(self, 'assignments', n.get_collection_of_object_values(TnsRecurrenceAssignment)),
            "employeeId": lambda n : setattr(self, 'employee_id', n.get_int_value()),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "indexed": lambda n : setattr(self, 'indexed', n.get_int_value()),
            "isoDateString": lambda n : setattr(self, 'iso_date_string', n.get_str_value()),
            "ruleId": lambda n : setattr(self, 'rule_id', n.get_int_value()),
            "ruleLinkId": lambda n : setattr(self, 'rule_link_id', n.get_int_value()),
            "ruleLinkTypeId": lambda n : setattr(self, 'rule_link_type_id', n.get_int_value()),
            "sequenceId": lambda n : setattr(self, 'sequence_id', n.get_int_value()),
            "timestamp": lambda n : setattr(self, 'timestamp', n.get_int_value()),
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
        writer.write_collection_of_object_values("assignments", self.assignments)
        writer.write_int_value("employeeId", self.employee_id)
        writer.write_int_value("id", self.id)
        writer.write_int_value("indexed", self.indexed)
        writer.write_str_value("isoDateString", self.iso_date_string)
        writer.write_int_value("ruleId", self.rule_id)
        writer.write_int_value("ruleLinkId", self.rule_link_id)
        writer.write_int_value("ruleLinkTypeId", self.rule_link_type_id)
        writer.write_int_value("sequenceId", self.sequence_id)
        writer.write_int_value("timestamp", self.timestamp)
        writer.write_additional_data_value(self.additional_data)
    

