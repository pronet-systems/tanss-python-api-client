from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .escalations_post_request_body_conditions import EscalationsPostRequestBody_conditions
    from .escalations_post_request_body_events import EscalationsPostRequestBody_events
    from .escalations_post_request_body_triggers import EscalationsPostRequestBody_triggers
    from .escalations_post_request_body_trigger_logic_operator import EscalationsPostRequestBody_triggerLogicOperator

@dataclass
class EscalationsPostRequestBody(AdditionalDataHolder, Parsable):
    """
    Request body.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Whether the rule is currently active
    active: Optional[bool] = None
    # Identifier of the escalation category the rule belongs to
    category_id: Optional[int] = None
    # Conditions that must be met for the rule to apply
    conditions: Optional[list[EscalationsPostRequestBody_conditions]] = None
    # Descriptive text explaining the rule
    description: Optional[str] = None
    # Actions executed when the rule triggers
    events: Optional[list[EscalationsPostRequestBody_events]] = None
    # Unique identifier of the escalation rule
    id: Optional[int] = None
    # Name of the escalation rule
    name: Optional[str] = None
    # Logical operator combining the rule triggers
    trigger_logic_operator: Optional[EscalationsPostRequestBody_triggerLogicOperator] = None
    # Triggers that cause the rule to fire
    triggers: Optional[list[EscalationsPostRequestBody_triggers]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EscalationsPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EscalationsPostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return EscalationsPostRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .escalations_post_request_body_conditions import EscalationsPostRequestBody_conditions
        from .escalations_post_request_body_events import EscalationsPostRequestBody_events
        from .escalations_post_request_body_triggers import EscalationsPostRequestBody_triggers
        from .escalations_post_request_body_trigger_logic_operator import EscalationsPostRequestBody_triggerLogicOperator

        from .escalations_post_request_body_conditions import EscalationsPostRequestBody_conditions
        from .escalations_post_request_body_events import EscalationsPostRequestBody_events
        from .escalations_post_request_body_triggers import EscalationsPostRequestBody_triggers
        from .escalations_post_request_body_trigger_logic_operator import EscalationsPostRequestBody_triggerLogicOperator

        fields: dict[str, Callable[[Any], None]] = {
            "active": lambda n : setattr(self, 'active', n.get_bool_value()),
            "categoryId": lambda n : setattr(self, 'category_id', n.get_int_value()),
            "conditions": lambda n : setattr(self, 'conditions', n.get_collection_of_object_values(EscalationsPostRequestBody_conditions)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "events": lambda n : setattr(self, 'events', n.get_collection_of_object_values(EscalationsPostRequestBody_events)),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "triggerLogicOperator": lambda n : setattr(self, 'trigger_logic_operator', n.get_enum_value(EscalationsPostRequestBody_triggerLogicOperator)),
            "triggers": lambda n : setattr(self, 'triggers', n.get_collection_of_object_values(EscalationsPostRequestBody_triggers)),
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
        writer.write_bool_value("active", self.active)
        writer.write_int_value("categoryId", self.category_id)
        writer.write_collection_of_object_values("conditions", self.conditions)
        writer.write_str_value("description", self.description)
        writer.write_collection_of_object_values("events", self.events)
        writer.write_str_value("name", self.name)
        writer.write_enum_value("triggerLogicOperator", self.trigger_logic_operator)
        writer.write_collection_of_object_values("triggers", self.triggers)
        writer.write_additional_data_value(self.additional_data)
    

