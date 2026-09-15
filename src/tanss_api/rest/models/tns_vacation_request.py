from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tns_planning_type import TnsPlanningType
    from .tns_vacation_request_day import TnsVacationRequestDay
    from .tns_vacation_request_status import TnsVacationRequestStatus

@dataclass
class TnsVacationRequest(AdditionalDataHolder, Parsable):
    """
    vacation request (or illness, absence, custom type, overtime, standBy, custom). If a custom type shall be stored, use the planningAdditionalId property to specify the custom type
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The days property
    days: Optional[list[TnsVacationRequestDay]] = None
    # start for this vacation request
    end_date: Optional[int] = None
    # id of the vacation request
    id: Optional[int] = None
    # only if planningType is ABSENCE or CUSTOM / used for additional specification (Sonderurlaub, Kur, etc.)
    planning_additional_id: Optional[int] = None
    # The planning type defines if a support is actually a support, appointment (or some other type)
    planning_type: Optional[TnsPlanningType] = None
    # if a approval process is used for this vacation request - specifies the id of the process
    process_id: Optional[int] = None
    # if a approval process is used for this vacation request - specifies the id of the current process step
    process_step_id: Optional[int] = None
    # timestamp when this vacation request was initially created
    request_date: Optional[int] = None
    # reason for this vacation request (optional)
    request_reason: Optional[str] = None
    # id of the requester (employee)
    requester_id: Optional[int] = None
    # start for this vacation request
    start_date: Optional[int] = None
    # Specifies the status of a vacation request
    status: Optional[TnsVacationRequestStatus] = None
    # timestamp when this vacation request was accepted or declined
    supervisor_date: Optional[int] = None
    # id of the supervisor (employee who has accepted/declined this request)
    supervisor_id: Optional[int] = None
    # reason for accepting/declining this request (optional)
    supervisor_reason: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsVacationRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsVacationRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsVacationRequest()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .tns_planning_type import TnsPlanningType
        from .tns_vacation_request_day import TnsVacationRequestDay
        from .tns_vacation_request_status import TnsVacationRequestStatus

        from .tns_planning_type import TnsPlanningType
        from .tns_vacation_request_day import TnsVacationRequestDay
        from .tns_vacation_request_status import TnsVacationRequestStatus

        fields: dict[str, Callable[[Any], None]] = {
            "days": lambda n : setattr(self, 'days', n.get_collection_of_object_values(TnsVacationRequestDay)),
            "endDate": lambda n : setattr(self, 'end_date', n.get_int_value()),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "planningAdditionalId": lambda n : setattr(self, 'planning_additional_id', n.get_int_value()),
            "planningType": lambda n : setattr(self, 'planning_type', n.get_enum_value(TnsPlanningType)),
            "processId": lambda n : setattr(self, 'process_id', n.get_int_value()),
            "processStepId": lambda n : setattr(self, 'process_step_id', n.get_int_value()),
            "requestDate": lambda n : setattr(self, 'request_date', n.get_int_value()),
            "requestReason": lambda n : setattr(self, 'request_reason', n.get_str_value()),
            "requesterId": lambda n : setattr(self, 'requester_id', n.get_int_value()),
            "startDate": lambda n : setattr(self, 'start_date', n.get_int_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(TnsVacationRequestStatus)),
            "supervisorDate": lambda n : setattr(self, 'supervisor_date', n.get_int_value()),
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
        writer.write_collection_of_object_values("days", self.days)
        writer.write_int_value("endDate", self.end_date)
        writer.write_int_value("planningAdditionalId", self.planning_additional_id)
        writer.write_enum_value("planningType", self.planning_type)
        writer.write_int_value("processId", self.process_id)
        writer.write_int_value("processStepId", self.process_step_id)
        writer.write_int_value("requestDate", self.request_date)
        writer.write_str_value("requestReason", self.request_reason)
        writer.write_int_value("requesterId", self.requester_id)
        writer.write_int_value("startDate", self.start_date)
        writer.write_enum_value("status", self.status)
        writer.write_int_value("supervisorDate", self.supervisor_date)
        writer.write_int_value("supervisorId", self.supervisor_id)
        writer.write_str_value("supervisorReason", self.supervisor_reason)
        writer.write_additional_data_value(self.additional_data)
    

