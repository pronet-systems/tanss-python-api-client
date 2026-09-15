from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tns_tanss_event_rule_action_params import TnsTanssEventRuleActionParams
    from .tns_tanss_event_rule_action_type import TnsTanssEventRuleActionType

@dataclass
class TnsTanssEventRuleAction(AdditionalDataHolder, Parsable):
    """
    Defines an assignment from a TANSS event rule to an assignment (i.e. Ticket Board Panel)
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # defines which action shall be executed
    action_type: Optional[TnsTanssEventRuleActionType] = None
    # defines the parameters for the action
    params: Optional[TnsTanssEventRuleActionParams] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsTanssEventRuleAction:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsTanssEventRuleAction
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsTanssEventRuleAction()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .tns_tanss_event_rule_action_params import TnsTanssEventRuleActionParams
        from .tns_tanss_event_rule_action_type import TnsTanssEventRuleActionType

        from .tns_tanss_event_rule_action_params import TnsTanssEventRuleActionParams
        from .tns_tanss_event_rule_action_type import TnsTanssEventRuleActionType

        fields: dict[str, Callable[[Any], None]] = {
            "actionType": lambda n : setattr(self, 'action_type', n.get_enum_value(TnsTanssEventRuleActionType)),
            "params": lambda n : setattr(self, 'params', n.get_object_value(TnsTanssEventRuleActionParams)),
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
        writer.write_enum_value("actionType", self.action_type)
        writer.write_object_value("params", self.params)
        writer.write_additional_data_value(self.additional_data)
    

