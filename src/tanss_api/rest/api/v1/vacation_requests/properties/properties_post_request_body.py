from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .properties_post_request_body_planning_type import PropertiesPostRequestBody_planningType
    from .properties_post_request_body_status import PropertiesPostRequestBody_status

@dataclass
class PropertiesPostRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # End of the requested absence as a Unix timestamp
    end_date: Optional[int] = None
    # Unique identifier of the vacation request
    id: Optional[int] = None
    # Additional absence sub-type identifier, used only for absence entries
    planning_additional_id: Optional[int] = None
    # Type of planning entry this request represents
    planning_type: Optional[PropertiesPostRequestBody_planningType] = None
    # Identifier of the approval process the request runs through
    process_id: Optional[int] = None
    # Identifier of the current approval process step
    process_step_id: Optional[int] = None
    # When the request was submitted, as a Unix timestamp
    request_date: Optional[int] = None
    # Reason text provided by the requester
    request_reason: Optional[str] = None
    # Identifier of the employee who filed the request
    requester_id: Optional[int] = None
    # Start of the requested absence as a Unix timestamp
    start_date: Optional[int] = None
    # Approval status of the request
    status: Optional[PropertiesPostRequestBody_status] = None
    # Identifier of the supervisor handling the request
    supervisor_id: Optional[int] = None
    # Reason or comment provided by the supervisor
    supervisor_reason: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PropertiesPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PropertiesPostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PropertiesPostRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .properties_post_request_body_planning_type import PropertiesPostRequestBody_planningType
        from .properties_post_request_body_status import PropertiesPostRequestBody_status

        from .properties_post_request_body_planning_type import PropertiesPostRequestBody_planningType
        from .properties_post_request_body_status import PropertiesPostRequestBody_status

        fields: dict[str, Callable[[Any], None]] = {
            "endDate": lambda n : setattr(self, 'end_date', n.get_int_value()),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "planningAdditionalId": lambda n : setattr(self, 'planning_additional_id', n.get_int_value()),
            "planningType": lambda n : setattr(self, 'planning_type', n.get_enum_value(PropertiesPostRequestBody_planningType)),
            "processId": lambda n : setattr(self, 'process_id', n.get_int_value()),
            "processStepId": lambda n : setattr(self, 'process_step_id', n.get_int_value()),
            "requestDate": lambda n : setattr(self, 'request_date', n.get_int_value()),
            "requestReason": lambda n : setattr(self, 'request_reason', n.get_str_value()),
            "requesterId": lambda n : setattr(self, 'requester_id', n.get_int_value()),
            "startDate": lambda n : setattr(self, 'start_date', n.get_int_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(PropertiesPostRequestBody_status)),
            "supervisorId": lambda n : setattr(self, 'supervisor_id', n.get_int_value()),
            "supervisorReason": lambda n : setattr(self, 'supervisor_reason', n.get_str_value()),
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
        writer.write_int_value("endDate", self.end_date)
        writer.write_int_value("id", self.id)
        writer.write_int_value("planningAdditionalId", self.planning_additional_id)
        writer.write_enum_value("planningType", self.planning_type)
        writer.write_int_value("processId", self.process_id)
        writer.write_int_value("processStepId", self.process_step_id)
        writer.write_int_value("requestDate", self.request_date)
        writer.write_str_value("requestReason", self.request_reason)
        writer.write_int_value("requesterId", self.requester_id)
        writer.write_int_value("startDate", self.start_date)
        writer.write_enum_value("status", self.status)
        writer.write_int_value("supervisorId", self.supervisor_id)
        writer.write_str_value("supervisorReason", self.supervisor_reason)
        writer.write_additional_data_value(self.additional_data)
    

