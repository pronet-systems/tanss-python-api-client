from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .timeline_put_request_body_custom_type_ids import TimelinePutRequestBody_customTypeIds
    from .timeline_put_request_body_entity import TimelinePutRequestBody_entity
    from .timeline_put_request_body_fetch_types import TimelinePutRequestBody_fetchTypes
    from .timeline_put_request_body_ids import TimelinePutRequestBody_ids
    from .timeline_put_request_body_planning_types import TimelinePutRequestBody_planningTypes
    from .timeline_put_request_body_timeframe import TimelinePutRequestBody_timeframe

@dataclass
class TimelinePutRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Identifiers of custom entry types to include.
    custom_type_ids: Optional[list[TimelinePutRequestBody_customTypeIds]] = None
    # The entity type whose timeline is requested.
    entity: Optional[TimelinePutRequestBody_entity] = None
    # The kinds of timeline entries to fetch (supports, tickets, phone calls, and similar).
    fetch_types: Optional[list[TimelinePutRequestBody_fetchTypes]] = None
    # Identifiers of the entities to include in the timeline.
    ids: Optional[list[TimelinePutRequestBody_ids]] = None
    # Planning types to include in the timeline.
    planning_types: Optional[list[TimelinePutRequestBody_planningTypes]] = None
    # Whether frontend-oriented values should be used in the response.
    show_frontend_values: Optional[bool] = None
    # Whether internal phone calls should be shown.
    show_internal_calls: Optional[bool] = None
    # Whether the real duration of support entries should be shown.
    show_real_duration: Optional[bool] = None
    # Time range (from/to) to load timeline data for.
    timeframe: Optional[TimelinePutRequestBody_timeframe] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TimelinePutRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TimelinePutRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TimelinePutRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .timeline_put_request_body_custom_type_ids import TimelinePutRequestBody_customTypeIds
        from .timeline_put_request_body_entity import TimelinePutRequestBody_entity
        from .timeline_put_request_body_fetch_types import TimelinePutRequestBody_fetchTypes
        from .timeline_put_request_body_ids import TimelinePutRequestBody_ids
        from .timeline_put_request_body_planning_types import TimelinePutRequestBody_planningTypes
        from .timeline_put_request_body_timeframe import TimelinePutRequestBody_timeframe

        from .timeline_put_request_body_custom_type_ids import TimelinePutRequestBody_customTypeIds
        from .timeline_put_request_body_entity import TimelinePutRequestBody_entity
        from .timeline_put_request_body_fetch_types import TimelinePutRequestBody_fetchTypes
        from .timeline_put_request_body_ids import TimelinePutRequestBody_ids
        from .timeline_put_request_body_planning_types import TimelinePutRequestBody_planningTypes
        from .timeline_put_request_body_timeframe import TimelinePutRequestBody_timeframe

        fields: dict[str, Callable[[Any], None]] = {
            "customTypeIds": lambda n : setattr(self, 'custom_type_ids', n.get_collection_of_object_values(TimelinePutRequestBody_customTypeIds)),
            "entity": lambda n : setattr(self, 'entity', n.get_enum_value(TimelinePutRequestBody_entity)),
            "fetchTypes": lambda n : setattr(self, 'fetch_types', n.get_collection_of_object_values(TimelinePutRequestBody_fetchTypes)),
            "ids": lambda n : setattr(self, 'ids', n.get_collection_of_object_values(TimelinePutRequestBody_ids)),
            "planningTypes": lambda n : setattr(self, 'planning_types', n.get_collection_of_object_values(TimelinePutRequestBody_planningTypes)),
            "showFrontendValues": lambda n : setattr(self, 'show_frontend_values', n.get_bool_value()),
            "showInternalCalls": lambda n : setattr(self, 'show_internal_calls', n.get_bool_value()),
            "showRealDuration": lambda n : setattr(self, 'show_real_duration', n.get_bool_value()),
            "timeframe": lambda n : setattr(self, 'timeframe', n.get_object_value(TimelinePutRequestBody_timeframe)),
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
        writer.write_collection_of_object_values("customTypeIds", self.custom_type_ids)
        writer.write_enum_value("entity", self.entity)
        writer.write_collection_of_object_values("fetchTypes", self.fetch_types)
        writer.write_collection_of_object_values("ids", self.ids)
        writer.write_collection_of_object_values("planningTypes", self.planning_types)
        writer.write_bool_value("showFrontendValues", self.show_frontend_values)
        writer.write_bool_value("showInternalCalls", self.show_internal_calls)
        writer.write_bool_value("showRealDuration", self.show_real_duration)
        writer.write_object_value("timeframe", self.timeframe)
        writer.write_additional_data_value(self.additional_data)
    

