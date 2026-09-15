from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .next_post_request_body_daily_type import NextPostRequestBody_dailyType
    from .next_post_request_body_monthly_type import NextPostRequestBody_monthlyType
    from .next_post_request_body_series_type import NextPostRequestBody_seriesType
    from .next_post_request_body_yearly_type import NextPostRequestBody_yearlyType

@dataclass
class NextPostRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Sub-pattern used for daily recurrences
    daily_type: Optional[NextPostRequestBody_dailyType] = None
    # Date after which the series stops recurring as a unix timestamp
    expire_date: Optional[int] = None
    # Date of the first execution as a unix timestamp
    first_execution_date: Optional[int] = None
    # Identifier of the linked entity
    link_id: Optional[int] = None
    # Type identifier of the linked entity
    link_type_id: Optional[int] = None
    # Sub-pattern used for monthly recurrences
    monthly_type: Optional[NextPostRequestBody_monthlyType] = None
    # Date of the next scheduled execution as a unix timestamp
    next_execution_date: Optional[int] = None
    # Overall recurrence pattern of the series
    series_type: Optional[NextPostRequestBody_seriesType] = None
    # Identifier of the associated support entry
    support_id: Optional[int] = None
    # Identifier of the task this recurrence series belongs to
    task_id: Optional[int] = None
    # Sub-pattern used for yearly recurrences
    yearly_type: Optional[NextPostRequestBody_yearlyType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> NextPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: NextPostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return NextPostRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .next_post_request_body_daily_type import NextPostRequestBody_dailyType
        from .next_post_request_body_monthly_type import NextPostRequestBody_monthlyType
        from .next_post_request_body_series_type import NextPostRequestBody_seriesType
        from .next_post_request_body_yearly_type import NextPostRequestBody_yearlyType

        from .next_post_request_body_daily_type import NextPostRequestBody_dailyType
        from .next_post_request_body_monthly_type import NextPostRequestBody_monthlyType
        from .next_post_request_body_series_type import NextPostRequestBody_seriesType
        from .next_post_request_body_yearly_type import NextPostRequestBody_yearlyType

        fields: dict[str, Callable[[Any], None]] = {
            "dailyType": lambda n : setattr(self, 'daily_type', n.get_enum_value(NextPostRequestBody_dailyType)),
            "expireDate": lambda n : setattr(self, 'expire_date', n.get_int_value()),
            "firstExecutionDate": lambda n : setattr(self, 'first_execution_date', n.get_int_value()),
            "linkId": lambda n : setattr(self, 'link_id', n.get_int_value()),
            "linkTypeId": lambda n : setattr(self, 'link_type_id', n.get_int_value()),
            "monthlyType": lambda n : setattr(self, 'monthly_type', n.get_enum_value(NextPostRequestBody_monthlyType)),
            "nextExecutionDate": lambda n : setattr(self, 'next_execution_date', n.get_int_value()),
            "seriesType": lambda n : setattr(self, 'series_type', n.get_enum_value(NextPostRequestBody_seriesType)),
            "supportId": lambda n : setattr(self, 'support_id', n.get_int_value()),
            "taskId": lambda n : setattr(self, 'task_id', n.get_int_value()),
            "yearlyType": lambda n : setattr(self, 'yearly_type', n.get_enum_value(NextPostRequestBody_yearlyType)),
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
        writer.write_enum_value("dailyType", self.daily_type)
        writer.write_int_value("expireDate", self.expire_date)
        writer.write_int_value("firstExecutionDate", self.first_execution_date)
        writer.write_int_value("linkId", self.link_id)
        writer.write_int_value("linkTypeId", self.link_type_id)
        writer.write_enum_value("monthlyType", self.monthly_type)
        writer.write_int_value("nextExecutionDate", self.next_execution_date)
        writer.write_enum_value("seriesType", self.series_type)
        writer.write_int_value("supportId", self.support_id)
        writer.write_int_value("taskId", self.task_id)
        writer.write_enum_value("yearlyType", self.yearly_type)
        writer.write_additional_data_value(self.additional_data)
    

