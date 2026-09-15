from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .with_link_type_put_request_body_employee_ids import WithLinkTypePutRequestBody_employeeIds
    from .with_link_type_put_request_body_link_ids import WithLinkTypePutRequestBody_linkIds
    from .with_link_type_put_request_body_log_file_type_ids import WithLinkTypePutRequestBody_logFileTypeIds
    from .with_link_type_put_request_body_timeframe import WithLinkTypePutRequestBody_timeframe

@dataclass
class WithLinkTypePutRequestBody(AdditionalDataHolder, Parsable):
    """
    See the matching schema for the field shape.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Identifiers of employees whose log entries to include.
    employee_ids: Optional[list[WithLinkTypePutRequestBody_employeeIds]] = None
    # Identifiers of linked entities to filter the log list by.
    link_ids: Optional[list[WithLinkTypePutRequestBody_linkIds]] = None
    # Identifiers of log entry types to include.
    log_file_type_ids: Optional[list[WithLinkTypePutRequestBody_logFileTypeIds]] = None
    # Whether to sort results with the newest entries first.
    newest_first: Optional[bool] = None
    # Free-text search term applied to log entries.
    search_text: Optional[str] = None
    # Identifier of a support entry to restrict the log list to.
    support_id: Optional[int] = None
    # Identifier of a ticket to restrict the log list to.
    ticket_id: Optional[int] = None
    # Time range used to filter log entries by date.
    timeframe: Optional[WithLinkTypePutRequestBody_timeframe] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WithLinkTypePutRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WithLinkTypePutRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WithLinkTypePutRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .with_link_type_put_request_body_employee_ids import WithLinkTypePutRequestBody_employeeIds
        from .with_link_type_put_request_body_link_ids import WithLinkTypePutRequestBody_linkIds
        from .with_link_type_put_request_body_log_file_type_ids import WithLinkTypePutRequestBody_logFileTypeIds
        from .with_link_type_put_request_body_timeframe import WithLinkTypePutRequestBody_timeframe

        from .with_link_type_put_request_body_employee_ids import WithLinkTypePutRequestBody_employeeIds
        from .with_link_type_put_request_body_link_ids import WithLinkTypePutRequestBody_linkIds
        from .with_link_type_put_request_body_log_file_type_ids import WithLinkTypePutRequestBody_logFileTypeIds
        from .with_link_type_put_request_body_timeframe import WithLinkTypePutRequestBody_timeframe

        fields: dict[str, Callable[[Any], None]] = {
            "employeeIds": lambda n : setattr(self, 'employee_ids', n.get_collection_of_object_values(WithLinkTypePutRequestBody_employeeIds)),
            "linkIds": lambda n : setattr(self, 'link_ids', n.get_collection_of_object_values(WithLinkTypePutRequestBody_linkIds)),
            "logFileTypeIds": lambda n : setattr(self, 'log_file_type_ids', n.get_collection_of_object_values(WithLinkTypePutRequestBody_logFileTypeIds)),
            "newestFirst": lambda n : setattr(self, 'newest_first', n.get_bool_value()),
            "searchText": lambda n : setattr(self, 'search_text', n.get_str_value()),
            "supportId": lambda n : setattr(self, 'support_id', n.get_int_value()),
            "ticketId": lambda n : setattr(self, 'ticket_id', n.get_int_value()),
            "timeframe": lambda n : setattr(self, 'timeframe', n.get_object_value(WithLinkTypePutRequestBody_timeframe)),
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
        writer.write_collection_of_object_values("linkIds", self.link_ids)
        writer.write_collection_of_object_values("logFileTypeIds", self.log_file_type_ids)
        writer.write_bool_value("newestFirst", self.newest_first)
        writer.write_str_value("searchText", self.search_text)
        writer.write_int_value("supportId", self.support_id)
        writer.write_int_value("ticketId", self.ticket_id)
        writer.write_object_value("timeframe", self.timeframe)
        writer.write_additional_data_value(self.additional_data)
    

