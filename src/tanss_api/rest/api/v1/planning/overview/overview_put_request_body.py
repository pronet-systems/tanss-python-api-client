from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .overview_put_request_body_employee_ids import OverviewPutRequestBody_employeeIds
    from .overview_put_request_body_timeframe import OverviewPutRequestBody_timeframe

@dataclass
class OverviewPutRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Identifiers of the employees to include in the overview
    employee_ids: Optional[list[OverviewPutRequestBody_employeeIds]] = None
    # Time range (from/to) the planning overview covers
    timeframe: Optional[OverviewPutRequestBody_timeframe] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OverviewPutRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OverviewPutRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return OverviewPutRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .overview_put_request_body_employee_ids import OverviewPutRequestBody_employeeIds
        from .overview_put_request_body_timeframe import OverviewPutRequestBody_timeframe

        from .overview_put_request_body_employee_ids import OverviewPutRequestBody_employeeIds
        from .overview_put_request_body_timeframe import OverviewPutRequestBody_timeframe

        fields: dict[str, Callable[[Any], None]] = {
            "employeeIds": lambda n : setattr(self, 'employee_ids', n.get_collection_of_object_values(OverviewPutRequestBody_employeeIds)),
            "timeframe": lambda n : setattr(self, 'timeframe', n.get_object_value(OverviewPutRequestBody_timeframe)),
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
        writer.write_collection_of_object_values("employeeIds", self.employee_ids)
        writer.write_object_value("timeframe", self.timeframe)
        writer.write_additional_data_value(self.additional_data)
    

