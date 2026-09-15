from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .timestamp_day_closing import TimestampDayClosing
    from .timestamp_day_closing_till_date_error import TimestampDayClosingTillDateError

@dataclass
class TimestampDayClosingTillDateResult(AdditionalDataHolder, Parsable):
    """
    response given when creating day closings till a given date
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # a list of created day closing objects
    created_day_closings: Optional[list[TimestampDayClosing]] = None
    # a list of errors that occured while creating the day closings
    errors: Optional[list[TimestampDayClosingTillDateError]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TimestampDayClosingTillDateResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TimestampDayClosingTillDateResult
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TimestampDayClosingTillDateResult()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .timestamp_day_closing import TimestampDayClosing
        from .timestamp_day_closing_till_date_error import TimestampDayClosingTillDateError

        from .timestamp_day_closing import TimestampDayClosing
        from .timestamp_day_closing_till_date_error import TimestampDayClosingTillDateError

        fields: dict[str, Callable[[Any], None]] = {
            "createdDayClosings": lambda n : setattr(self, 'created_day_closings', n.get_collection_of_object_values(TimestampDayClosing)),
            "errors": lambda n : setattr(self, 'errors', n.get_collection_of_object_values(TimestampDayClosingTillDateError)),
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
        writer.write_collection_of_object_values("createdDayClosings", self.created_day_closings)
        writer.write_collection_of_object_values("errors", self.errors)
        writer.write_additional_data_value(self.additional_data)
    

