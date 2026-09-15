from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .checklist_put_request_body_position import ChecklistPutRequestBody_position
    from .checklist_put_request_body_type import ChecklistPutRequestBody_type

@dataclass
class ChecklistPutRequestBody(AdditionalDataHolder, Parsable):
    """
    Request body.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Whether the checklist is currently active
    active: Optional[bool] = None
    # Whether the checklist has been completed
    completed: Optional[bool] = None
    # Identifier of the employee who created the checklist
    creator_id: Optional[int] = None
    # Description of the checklist
    description: Optional[str] = None
    # Unique identifier of the checklist
    id: Optional[int] = None
    # Name of the checklist
    name: Optional[str] = None
    # Display position of the checklist
    position: Optional[ChecklistPutRequestBody_position] = None
    # Kind of checklist
    type: Optional[ChecklistPutRequestBody_type] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ChecklistPutRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ChecklistPutRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ChecklistPutRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .checklist_put_request_body_position import ChecklistPutRequestBody_position
        from .checklist_put_request_body_type import ChecklistPutRequestBody_type

        from .checklist_put_request_body_position import ChecklistPutRequestBody_position
        from .checklist_put_request_body_type import ChecklistPutRequestBody_type

        fields: dict[str, Callable[[Any], None]] = {
            "active": lambda n : setattr(self, 'active', n.get_bool_value()),
            "completed": lambda n : setattr(self, 'completed', n.get_bool_value()),
            "creatorId": lambda n : setattr(self, 'creator_id', n.get_int_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "position": lambda n : setattr(self, 'position', n.get_enum_value(ChecklistPutRequestBody_position)),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(ChecklistPutRequestBody_type)),
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
        writer.write_bool_value("completed", self.completed)
        writer.write_int_value("creatorId", self.creator_id)
        writer.write_str_value("description", self.description)
        writer.write_str_value("name", self.name)
        writer.write_enum_value("position", self.position)
        writer.write_enum_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    

