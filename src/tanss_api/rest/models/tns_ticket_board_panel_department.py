from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class TnsTicketBoardPanelDepartment(AdditionalDataHolder, Parsable):
    """
    Panel department
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Department id
    department_id: Optional[int] = None
    # Panel id
    panel_id: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsTicketBoardPanelDepartment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsTicketBoardPanelDepartment
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsTicketBoardPanelDepartment()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "departmentId": lambda n : setattr(self, 'department_id', n.get_int_value()),
            "panelId": lambda n : setattr(self, 'panel_id', n.get_int_value()),
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
        writer.write_int_value("departmentId", self.department_id)
        writer.write_int_value("panelId", self.panel_id)
        writer.write_additional_data_value(self.additional_data)
    

