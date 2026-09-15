from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .query_put_request_body_employee_ids import QueryPutRequestBody_employeeIds
    from .query_put_request_body_rule_ids import QueryPutRequestBody_ruleIds
    from .query_put_request_body_timeframe import QueryPutRequestBody_timeframe

@dataclass
class QueryPutRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # If true, also checks which employees are assigned to the recurrence rule's master and linked employees.
    check_employees_in_support: Optional[bool] = None
    # Identifiers of the employees to restrict the query to.
    employee_ids: Optional[list[QueryPutRequestBody_employeeIds]] = None
    # Identifiers of the recurrence rules to query.
    rule_ids: Optional[list[QueryPutRequestBody_ruleIds]] = None
    # Time window (from/to timestamps) within which recurrences are calculated.
    timeframe: Optional[QueryPutRequestBody_timeframe] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> QueryPutRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: QueryPutRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return QueryPutRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .query_put_request_body_employee_ids import QueryPutRequestBody_employeeIds
        from .query_put_request_body_rule_ids import QueryPutRequestBody_ruleIds
        from .query_put_request_body_timeframe import QueryPutRequestBody_timeframe

        from .query_put_request_body_employee_ids import QueryPutRequestBody_employeeIds
        from .query_put_request_body_rule_ids import QueryPutRequestBody_ruleIds
        from .query_put_request_body_timeframe import QueryPutRequestBody_timeframe

        fields: dict[str, Callable[[Any], None]] = {
            "checkEmployeesInSupport": lambda n : setattr(self, 'check_employees_in_support', n.get_bool_value()),
            "employeeIds": lambda n : setattr(self, 'employee_ids', n.get_collection_of_object_values(QueryPutRequestBody_employeeIds)),
            "ruleIds": lambda n : setattr(self, 'rule_ids', n.get_collection_of_object_values(QueryPutRequestBody_ruleIds)),
            "timeframe": lambda n : setattr(self, 'timeframe', n.get_object_value(QueryPutRequestBody_timeframe)),
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
        writer.write_bool_value("checkEmployeesInSupport", self.check_employees_in_support)
        writer.write_collection_of_object_values("employeeIds", self.employee_ids)
        writer.write_collection_of_object_values("ruleIds", self.rule_ids)
        writer.write_object_value("timeframe", self.timeframe)
        writer.write_additional_data_value(self.additional_data)
    

