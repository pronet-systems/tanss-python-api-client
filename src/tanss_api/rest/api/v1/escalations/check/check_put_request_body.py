from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .check_put_request_body_check_mode import CheckPutRequestBody_checkMode

@dataclass
class CheckPutRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Mode determining how the escalation check acts
    check_mode: Optional[CheckPutRequestBody_checkMode] = None
    # Origin from which the check was started
    check_started_from: Optional[str] = None
    # Whether the activation of the check itself should be logged
    log_activated_check: Optional[bool] = None
    # Whether check results should be logged when possible
    logging_if_possible: Optional[bool] = None
    # Whether rules with a reset event should be reset
    reset_rules_if_possble: Optional[bool] = None
    # Restrict processing to a single escalation rule
    rule_id: Optional[int] = None
    # Restrict processing to a single ticket
    ticket_id: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CheckPutRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CheckPutRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CheckPutRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .check_put_request_body_check_mode import CheckPutRequestBody_checkMode

        from .check_put_request_body_check_mode import CheckPutRequestBody_checkMode

        fields: dict[str, Callable[[Any], None]] = {
            "checkMode": lambda n : setattr(self, 'check_mode', n.get_enum_value(CheckPutRequestBody_checkMode)),
            "checkStartedFrom": lambda n : setattr(self, 'check_started_from', n.get_str_value()),
            "logActivatedCheck": lambda n : setattr(self, 'log_activated_check', n.get_bool_value()),
            "loggingIfPossible": lambda n : setattr(self, 'logging_if_possible', n.get_bool_value()),
            "resetRulesIfPossble": lambda n : setattr(self, 'reset_rules_if_possble', n.get_bool_value()),
            "ruleId": lambda n : setattr(self, 'rule_id', n.get_int_value()),
            "ticketId": lambda n : setattr(self, 'ticket_id', n.get_int_value()),
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
        writer.write_enum_value("checkMode", self.check_mode)
        writer.write_str_value("checkStartedFrom", self.check_started_from)
        writer.write_bool_value("logActivatedCheck", self.log_activated_check)
        writer.write_bool_value("loggingIfPossible", self.logging_if_possible)
        writer.write_bool_value("resetRulesIfPossble", self.reset_rules_if_possble)
        writer.write_int_value("ruleId", self.rule_id)
        writer.write_int_value("ticketId", self.ticket_id)
        writer.write_additional_data_value(self.additional_data)
    

