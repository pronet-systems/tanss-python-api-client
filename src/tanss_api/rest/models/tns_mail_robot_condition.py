from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tns_mail_robot_condition_type import TnsMailRobotCondition_type

@dataclass
class TnsMailRobotCondition(AdditionalDataHolder, Parsable):
    """
    Bedingung einer Mailroboter-Regel
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Verknüpfung der Bedingung (AND, OR, ...)
    linked: Optional[str] = None
    # The number property
    number: Optional[int] = None
    # The ruleId property
    rule_id: Optional[int] = None
    # The type property
    type: Optional[TnsMailRobotCondition_type] = None
    # The value property
    value: Optional[str] = None
    # The variableName property
    variable_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsMailRobotCondition:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsMailRobotCondition
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsMailRobotCondition()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .tns_mail_robot_condition_type import TnsMailRobotCondition_type

        from .tns_mail_robot_condition_type import TnsMailRobotCondition_type

        fields: dict[str, Callable[[Any], None]] = {
            "linked": lambda n : setattr(self, 'linked', n.get_str_value()),
            "number": lambda n : setattr(self, 'number', n.get_int_value()),
            "ruleId": lambda n : setattr(self, 'rule_id', n.get_int_value()),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(TnsMailRobotCondition_type)),
            "value": lambda n : setattr(self, 'value', n.get_str_value()),
            "variableName": lambda n : setattr(self, 'variable_name', n.get_str_value()),
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
        writer.write_str_value("linked", self.linked)
        writer.write_int_value("number", self.number)
        writer.write_int_value("ruleId", self.rule_id)
        writer.write_enum_value("type", self.type)
        writer.write_str_value("value", self.value)
        writer.write_str_value("variableName", self.variable_name)
        writer.write_additional_data_value(self.additional_data)
    

