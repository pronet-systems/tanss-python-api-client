from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tns_mail_robot_action import TnsMailRobotAction
    from .tns_mail_robot_condition import TnsMailRobotCondition
    from .tns_mail_robot_rule_mode import TnsMailRobotRule_mode

@dataclass
class TnsMailRobotRule(AdditionalDataHolder, Parsable):
    """
    Mailroboter-Regel mit Aktionen und Bedingungen. Feldnamen aus der Entity TnsMailRobotRule abgeleitet (DTO im Build obfuskiert, JSON-Schlüssel unsicher).
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The actions property
    actions: Optional[list[TnsMailRobotAction]] = None
    # The apiImport property
    api_import: Optional[bool] = None
    # The companyId property
    company_id: Optional[int] = None
    # The conditions property
    conditions: Optional[list[TnsMailRobotCondition]] = None
    # The id property
    id: Optional[int] = None
    # The inactive property
    inactive: Optional[bool] = None
    # The linkId property
    link_id: Optional[int] = None
    # The linkTypeId property
    link_type_id: Optional[int] = None
    # The mode property
    mode: Optional[TnsMailRobotRule_mode] = None
    # The name property
    name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsMailRobotRule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsMailRobotRule
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsMailRobotRule()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .tns_mail_robot_action import TnsMailRobotAction
        from .tns_mail_robot_condition import TnsMailRobotCondition
        from .tns_mail_robot_rule_mode import TnsMailRobotRule_mode

        from .tns_mail_robot_action import TnsMailRobotAction
        from .tns_mail_robot_condition import TnsMailRobotCondition
        from .tns_mail_robot_rule_mode import TnsMailRobotRule_mode

        fields: dict[str, Callable[[Any], None]] = {
            "actions": lambda n : setattr(self, 'actions', n.get_collection_of_object_values(TnsMailRobotAction)),
            "apiImport": lambda n : setattr(self, 'api_import', n.get_bool_value()),
            "companyId": lambda n : setattr(self, 'company_id', n.get_int_value()),
            "conditions": lambda n : setattr(self, 'conditions', n.get_collection_of_object_values(TnsMailRobotCondition)),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "inactive": lambda n : setattr(self, 'inactive', n.get_bool_value()),
            "linkId": lambda n : setattr(self, 'link_id', n.get_int_value()),
            "linkTypeId": lambda n : setattr(self, 'link_type_id', n.get_int_value()),
            "mode": lambda n : setattr(self, 'mode', n.get_enum_value(TnsMailRobotRule_mode)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
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
        writer.write_bool_value("apiImport", self.api_import)
        writer.write_int_value("companyId", self.company_id)
        writer.write_collection_of_object_values("conditions", self.conditions)
        writer.write_int_value("id", self.id)
        writer.write_bool_value("inactive", self.inactive)
        writer.write_int_value("linkId", self.link_id)
        writer.write_int_value("linkTypeId", self.link_type_id)
        writer.write_enum_value("mode", self.mode)
        writer.write_str_value("name", self.name)
        writer.write_additional_data_value(self.additional_data)
    

