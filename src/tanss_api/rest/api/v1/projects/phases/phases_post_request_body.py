from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .phases_post_request_body_billing_type import PhasesPostRequestBody_billingType
    from .phases_post_request_body_clearance_mode import PhasesPostRequestBody_clearanceMode

@dataclass
class PhasesPostRequestBody(AdditionalDataHolder, Parsable):
    """
    Request body.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Billing mode governing how work in the phase is invoiced.
    billing_type: Optional[PhasesPostRequestBody_billingType] = None
    # Clearance mode controlling whether tickets in the phase may be cleared.
    clearance_mode: Optional[PhasesPostRequestBody_clearanceMode] = None
    # Whether all preceding phases must be closed before this one can start.
    closed_pre_phases_required: Optional[bool] = None
    # End date of the phase as a Unix timestamp.
    end_date: Optional[int] = None
    # Unique identifier of the project phase.
    id: Optional[int] = None
    # Display name of the project phase.
    name: Optional[str] = None
    # Identifier of the project this phase belongs to.
    project_id: Optional[int] = None
    # Ordering rank of the phase within the project.
    rank: Optional[int] = None
    # Start date of the phase as a Unix timestamp.
    start_date: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PhasesPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PhasesPostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PhasesPostRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .phases_post_request_body_billing_type import PhasesPostRequestBody_billingType
        from .phases_post_request_body_clearance_mode import PhasesPostRequestBody_clearanceMode

        from .phases_post_request_body_billing_type import PhasesPostRequestBody_billingType
        from .phases_post_request_body_clearance_mode import PhasesPostRequestBody_clearanceMode

        fields: dict[str, Callable[[Any], None]] = {
            "billingType": lambda n : setattr(self, 'billing_type', n.get_enum_value(PhasesPostRequestBody_billingType)),
            "clearanceMode": lambda n : setattr(self, 'clearance_mode', n.get_enum_value(PhasesPostRequestBody_clearanceMode)),
            "closedPrePhasesRequired": lambda n : setattr(self, 'closed_pre_phases_required', n.get_bool_value()),
            "endDate": lambda n : setattr(self, 'end_date', n.get_int_value()),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "projectId": lambda n : setattr(self, 'project_id', n.get_int_value()),
            "rank": lambda n : setattr(self, 'rank', n.get_int_value()),
            "startDate": lambda n : setattr(self, 'start_date', n.get_int_value()),
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
        writer.write_enum_value("billingType", self.billing_type)
        writer.write_enum_value("clearanceMode", self.clearance_mode)
        writer.write_bool_value("closedPrePhasesRequired", self.closed_pre_phases_required)
        writer.write_int_value("endDate", self.end_date)
        writer.write_str_value("name", self.name)
        writer.write_int_value("projectId", self.project_id)
        writer.write_int_value("rank", self.rank)
        writer.write_int_value("startDate", self.start_date)
        writer.write_additional_data_value(self.additional_data)
    

