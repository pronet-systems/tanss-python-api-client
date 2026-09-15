from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .conditions_post_request_body_priorities import ConditionsPostRequestBody_priorities
    from .conditions_post_request_body_ticket_types import ConditionsPostRequestBody_ticketTypes

@dataclass
class ConditionsPostRequestBody(AdditionalDataHolder, Parsable):
    """
    Request body.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Deadline time in hours
    deadline_hours: Optional[int] = None
    # Additional deadline time in minutes
    deadline_minutes: Optional[int] = None
    # Unique identifier of the SLA condition. Generated server-side.
    id: Optional[int] = None
    # List of ticket priority identifiers this condition applies to
    priorities: Optional[list[ConditionsPostRequestBody_priorities]] = None
    # Reaction time in hours
    reaction_time: Optional[int] = None
    # Additional reaction time in minutes
    reaction_time_minutes: Optional[int] = None
    # Identifier of the SLA this condition belongs to. Taken from the path parameter.
    sla_id: Optional[int] = None
    # Position used to order conditions within the SLA
    sort_order: Optional[int] = None
    # List of ticket type identifiers this condition applies to
    ticket_types: Optional[list[ConditionsPostRequestBody_ticketTypes]] = None
    # Identifier of the working time model used to calculate deadlines
    working_time_model: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ConditionsPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ConditionsPostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ConditionsPostRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .conditions_post_request_body_priorities import ConditionsPostRequestBody_priorities
        from .conditions_post_request_body_ticket_types import ConditionsPostRequestBody_ticketTypes

        from .conditions_post_request_body_priorities import ConditionsPostRequestBody_priorities
        from .conditions_post_request_body_ticket_types import ConditionsPostRequestBody_ticketTypes

        fields: dict[str, Callable[[Any], None]] = {
            "deadlineHours": lambda n : setattr(self, 'deadline_hours', n.get_int_value()),
            "deadlineMinutes": lambda n : setattr(self, 'deadline_minutes', n.get_int_value()),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "priorities": lambda n : setattr(self, 'priorities', n.get_collection_of_object_values(ConditionsPostRequestBody_priorities)),
            "reactionTime": lambda n : setattr(self, 'reaction_time', n.get_int_value()),
            "reactionTimeMinutes": lambda n : setattr(self, 'reaction_time_minutes', n.get_int_value()),
            "slaId": lambda n : setattr(self, 'sla_id', n.get_int_value()),
            "sortOrder": lambda n : setattr(self, 'sort_order', n.get_int_value()),
            "ticketTypes": lambda n : setattr(self, 'ticket_types', n.get_collection_of_object_values(ConditionsPostRequestBody_ticketTypes)),
            "workingTimeModel": lambda n : setattr(self, 'working_time_model', n.get_int_value()),
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
        writer.write_int_value("deadlineHours", self.deadline_hours)
        writer.write_int_value("deadlineMinutes", self.deadline_minutes)
        writer.write_collection_of_object_values("priorities", self.priorities)
        writer.write_int_value("reactionTime", self.reaction_time)
        writer.write_int_value("reactionTimeMinutes", self.reaction_time_minutes)
        writer.write_int_value("sortOrder", self.sort_order)
        writer.write_collection_of_object_values("ticketTypes", self.ticket_types)
        writer.write_int_value("workingTimeModel", self.working_time_model)
        writer.write_additional_data_value(self.additional_data)
    

