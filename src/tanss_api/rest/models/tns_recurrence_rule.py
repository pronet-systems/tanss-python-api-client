from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tns_recurrence_assignment import TnsRecurrenceAssignment
    from .tns_recurrence_exclude import TnsRecurrenceExclude
    from .tns_recurrence_rule_calculated import TnsRecurrenceRule_calculated
    from .tns_recurrence_rule_master_support import TnsRecurrenceRule_masterSupport

@dataclass
class TnsRecurrenceRule(AdditionalDataHolder, Parsable):
    """
    Wiederholungsregel (RRULE)
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The assignments property
    assignments: Optional[list[TnsRecurrenceAssignment]] = None
    # Berechnete Termine der Serie (Struktur unbekannt)
    calculated: Optional[list[TnsRecurrenceRule_calculated]] = None
    # The employeeIds property
    employee_ids: Optional[list[int]] = None
    # The endDate property
    end_date: Optional[int] = None
    # The excludeDelta property
    exclude_delta: Optional[int] = None
    # The excluded property
    excluded: Optional[list[TnsRecurrenceExclude]] = None
    # The id property
    id: Optional[int] = None
    # The linkId property
    link_id: Optional[int] = None
    # The linkTypeId property
    link_type_id: Optional[int] = None
    # Master-Termin der Serie (Struktur unbekannt, vermutlich TnsSupport)
    master_support: Optional[TnsRecurrenceRule_masterSupport] = None
    # The rrule property
    rrule: Optional[str] = None
    # The startDate property
    start_date: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsRecurrenceRule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsRecurrenceRule
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsRecurrenceRule()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .tns_recurrence_assignment import TnsRecurrenceAssignment
        from .tns_recurrence_exclude import TnsRecurrenceExclude
        from .tns_recurrence_rule_calculated import TnsRecurrenceRule_calculated
        from .tns_recurrence_rule_master_support import TnsRecurrenceRule_masterSupport

        from .tns_recurrence_assignment import TnsRecurrenceAssignment
        from .tns_recurrence_exclude import TnsRecurrenceExclude
        from .tns_recurrence_rule_calculated import TnsRecurrenceRule_calculated
        from .tns_recurrence_rule_master_support import TnsRecurrenceRule_masterSupport

        fields: dict[str, Callable[[Any], None]] = {
            "assignments": lambda n : setattr(self, 'assignments', n.get_collection_of_object_values(TnsRecurrenceAssignment)),
            "calculated": lambda n : setattr(self, 'calculated', n.get_collection_of_object_values(TnsRecurrenceRule_calculated)),
            "employeeIds": lambda n : setattr(self, 'employee_ids', n.get_collection_of_primitive_values(int)),
            "endDate": lambda n : setattr(self, 'end_date', n.get_int_value()),
            "excludeDelta": lambda n : setattr(self, 'exclude_delta', n.get_int_value()),
            "excluded": lambda n : setattr(self, 'excluded', n.get_collection_of_object_values(TnsRecurrenceExclude)),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "linkId": lambda n : setattr(self, 'link_id', n.get_int_value()),
            "linkTypeId": lambda n : setattr(self, 'link_type_id', n.get_int_value()),
            "masterSupport": lambda n : setattr(self, 'master_support', n.get_object_value(TnsRecurrenceRule_masterSupport)),
            "rrule": lambda n : setattr(self, 'rrule', n.get_str_value()),
            "startDate": lambda n : setattr(self, 'start_date', n.get_int_value()),
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
        writer.write_collection_of_object_values("calculated", self.calculated)
        writer.write_collection_of_primitive_values("employeeIds", self.employee_ids)
        writer.write_int_value("endDate", self.end_date)
        writer.write_int_value("excludeDelta", self.exclude_delta)
        writer.write_collection_of_object_values("excluded", self.excluded)
        writer.write_int_value("id", self.id)
        writer.write_int_value("linkId", self.link_id)
        writer.write_int_value("linkTypeId", self.link_type_id)
        writer.write_object_value("masterSupport", self.master_support)
        writer.write_str_value("rrule", self.rrule)
        writer.write_int_value("startDate", self.start_date)
        writer.write_additional_data_value(self.additional_data)
    

