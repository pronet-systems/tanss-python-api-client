from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class UpdateRelevantInfosPutRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Hash value used to identify or deduplicate the update run
    hash: Optional[str] = None
    # Whether the update should be logged when possible
    logging_if_possible: Optional[bool] = None
    # Restrict the update to a single escalation rule
    rule_id: Optional[int] = None
    # Start timestamp of the update run
    start_date: Optional[int] = None
    # Restrict the update to a single ticket
    ticket_id: Optional[int] = None
    # Origin from which the update was started
    update_started_from: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UpdateRelevantInfosPutRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UpdateRelevantInfosPutRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UpdateRelevantInfosPutRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "hash": lambda n : setattr(self, 'hash', n.get_str_value()),
            "loggingIfPossible": lambda n : setattr(self, 'logging_if_possible', n.get_bool_value()),
            "ruleId": lambda n : setattr(self, 'rule_id', n.get_int_value()),
            "startDate": lambda n : setattr(self, 'start_date', n.get_int_value()),
            "ticketId": lambda n : setattr(self, 'ticket_id', n.get_int_value()),
            "updateStartedFrom": lambda n : setattr(self, 'update_started_from', n.get_str_value()),
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
        writer.write_str_value("hash", self.hash)
        writer.write_bool_value("loggingIfPossible", self.logging_if_possible)
        writer.write_int_value("ruleId", self.rule_id)
        writer.write_int_value("startDate", self.start_date)
        writer.write_int_value("ticketId", self.ticket_id)
        writer.write_str_value("updateStartedFrom", self.update_started_from)
        writer.write_additional_data_value(self.additional_data)
    

