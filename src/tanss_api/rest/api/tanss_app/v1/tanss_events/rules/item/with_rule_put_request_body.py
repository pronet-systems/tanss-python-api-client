from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .......models.tns_tanss_event_rule_action import TnsTanssEventRuleAction
    from .......models.tns_tanss_event_rule_assignment import TnsTanssEventRuleAssignment
    from .with_rule_put_request_body_employees import WithRulePutRequestBody_employees
    from .with_rule_put_request_body_trigger_types import WithRulePutRequestBody_triggerTypes

@dataclass
class WithRulePutRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The actions property
    actions: Optional[list[TnsTanssEventRuleAction]] = None
    # The active property
    active: Optional[bool] = None
    # The assignments property
    assignments: Optional[list[TnsTanssEventRuleAssignment]] = None
    # TnsTanssEventRuleEmployeeAssignment (Felder unbekannt)
    employees: Optional[list[WithRulePutRequestBody_employees]] = None
    # The name property
    name: Optional[str] = None
    # TnsTanssEventRuleTriggerAssignment (Felder unbekannt)
    trigger_types: Optional[list[WithRulePutRequestBody_triggerTypes]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WithRulePutRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WithRulePutRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WithRulePutRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .......models.tns_tanss_event_rule_action import TnsTanssEventRuleAction
        from .......models.tns_tanss_event_rule_assignment import TnsTanssEventRuleAssignment
        from .with_rule_put_request_body_employees import WithRulePutRequestBody_employees
        from .with_rule_put_request_body_trigger_types import WithRulePutRequestBody_triggerTypes

        from .......models.tns_tanss_event_rule_action import TnsTanssEventRuleAction
        from .......models.tns_tanss_event_rule_assignment import TnsTanssEventRuleAssignment
        from .with_rule_put_request_body_employees import WithRulePutRequestBody_employees
        from .with_rule_put_request_body_trigger_types import WithRulePutRequestBody_triggerTypes

        fields: dict[str, Callable[[Any], None]] = {
            "actions": lambda n : setattr(self, 'actions', n.get_collection_of_object_values(TnsTanssEventRuleAction)),
            "active": lambda n : setattr(self, 'active', n.get_bool_value()),
            "assignments": lambda n : setattr(self, 'assignments', n.get_collection_of_object_values(TnsTanssEventRuleAssignment)),
            "employees": lambda n : setattr(self, 'employees', n.get_collection_of_object_values(WithRulePutRequestBody_employees)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "triggerTypes": lambda n : setattr(self, 'trigger_types', n.get_collection_of_object_values(WithRulePutRequestBody_triggerTypes)),
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
        writer.write_collection_of_object_values("actions", self.actions)
        writer.write_bool_value("active", self.active)
        writer.write_collection_of_object_values("assignments", self.assignments)
        writer.write_collection_of_object_values("employees", self.employees)
        writer.write_str_value("name", self.name)
        writer.write_collection_of_object_values("triggerTypes", self.trigger_types)
        writer.write_additional_data_value(self.additional_data)
    

