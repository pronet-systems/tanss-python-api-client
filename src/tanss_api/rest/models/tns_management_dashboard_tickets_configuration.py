from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .logic_operator_type import LogicOperatorType

@dataclass
class TnsManagementDashboardTicketsConfiguration(AdditionalDataHolder, Parsable):
    """
    Tag-Kombination, für die Tickets des Dashboards geladen werden
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Tag-IDs
    tags: Optional[list[int]] = None
    # Enum representing the logic linking of certain ids (AND / NOT / OR)
    type: Optional[LogicOperatorType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsManagementDashboardTicketsConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsManagementDashboardTicketsConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsManagementDashboardTicketsConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .logic_operator_type import LogicOperatorType

        from .logic_operator_type import LogicOperatorType

        fields: dict[str, Callable[[Any], None]] = {
            "tags": lambda n : setattr(self, 'tags', n.get_collection_of_primitive_values(int)),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(LogicOperatorType)),
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
        writer.write_collection_of_primitive_values("tags", self.tags)
        writer.write_enum_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    

