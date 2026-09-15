from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .....models.tns_support_create import TnsSupportCreate

from .....models.tns_support_create import TnsSupportCreate

@dataclass
class SupportsPostRequestBody(TnsSupportCreate, Parsable):
    # Serienumwandlung, Master-Support-Id
    recurrence_master_link_id: Optional[int] = None
    # Serienumwandlung, Sequenz-Id des Termins
    recurrence_rule_sequence_id: Optional[int] = None
    # Serienumwandlung, Zeitstempel des Termins
    recurrence_rule_sequence_timestamp: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SupportsPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SupportsPostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SupportsPostRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .....models.tns_support_create import TnsSupportCreate

        from .....models.tns_support_create import TnsSupportCreate

        fields: dict[str, Callable[[Any], None]] = {
            "recurrenceMasterLinkId": lambda n : setattr(self, 'recurrence_master_link_id', n.get_int_value()),
            "recurrenceRuleSequenceId": lambda n : setattr(self, 'recurrence_rule_sequence_id', n.get_int_value()),
            "recurrenceRuleSequenceTimestamp": lambda n : setattr(self, 'recurrence_rule_sequence_timestamp', n.get_int_value()),
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
        writer.write_int_value("recurrenceMasterLinkId", self.recurrence_master_link_id)
        writer.write_int_value("recurrenceRuleSequenceId", self.recurrence_rule_sequence_id)
        writer.write_int_value("recurrenceRuleSequenceTimestamp", self.recurrence_rule_sequence_timestamp)
    

