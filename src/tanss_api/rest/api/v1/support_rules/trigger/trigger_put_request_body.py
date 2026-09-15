from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .trigger_put_request_body_check_mode import TriggerPutRequestBody_checkMode
    from .trigger_put_request_body_support_ids import TriggerPutRequestBody_supportIds

@dataclass
class TriggerPutRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # How the rule is evaluated: preview only, simulate, or actually escalate
    check_mode: Optional[TriggerPutRequestBody_checkMode] = None
    # Re-process support entries that were already handled by the rule
    process_already_processed_supports: Optional[bool] = None
    # Identifier of the support rule to evaluate
    rule_id: Optional[int] = None
    # Send a notification email if errors occur during evaluation
    send_mail_on_errors: Optional[bool] = None
    # Identifiers of the support entries the rule should be applied to
    support_ids: Optional[list[TriggerPutRequestBody_supportIds]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TriggerPutRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TriggerPutRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TriggerPutRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .trigger_put_request_body_check_mode import TriggerPutRequestBody_checkMode
        from .trigger_put_request_body_support_ids import TriggerPutRequestBody_supportIds

        from .trigger_put_request_body_check_mode import TriggerPutRequestBody_checkMode
        from .trigger_put_request_body_support_ids import TriggerPutRequestBody_supportIds

        fields: dict[str, Callable[[Any], None]] = {
            "checkMode": lambda n : setattr(self, 'check_mode', n.get_enum_value(TriggerPutRequestBody_checkMode)),
            "processAlreadyProcessedSupports": lambda n : setattr(self, 'process_already_processed_supports', n.get_bool_value()),
            "ruleId": lambda n : setattr(self, 'rule_id', n.get_int_value()),
            "sendMailOnErrors": lambda n : setattr(self, 'send_mail_on_errors', n.get_bool_value()),
            "supportIds": lambda n : setattr(self, 'support_ids', n.get_collection_of_object_values(TriggerPutRequestBody_supportIds)),
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
        writer.write_bool_value("processAlreadyProcessedSupports", self.process_already_processed_supports)
        writer.write_int_value("ruleId", self.rule_id)
        writer.write_bool_value("sendMailOnErrors", self.send_mail_on_errors)
        writer.write_collection_of_object_values("supportIds", self.support_ids)
        writer.write_additional_data_value(self.additional_data)
    

