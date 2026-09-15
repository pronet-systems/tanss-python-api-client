from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .timestamp import Timestamp
    from .timestamp_day_closing import TimestampDayClosing
    from .timestamp_edit_mode import TimestampEditMode
    from .timestamp_history import TimestampHistory
    from .timestamp_info import TimestampInfo

from .timestamp_info import TimestampInfo

@dataclass
class TimestampInfoWithHistory(TimestampInfo, Parsable):
    """
    Object containing informations about timestamps grouped by employee and days:* a list of timestamp objects* infos about the single "periods" of timestamps* the working time model of the employee for the given day* history of timestamp changes* requested changes
    """
    # if any change requests are present for this user / day, they are given here
    changes_requested: Optional[list[Timestamp]] = None
    # Describes a day closing of a timestamp statistic. Here, all values are persisted into the database with infosabout working time, vacation, documented supports and the balance for this day.
    day_closing: Optional[TimestampDayClosing] = None
    # describes how a timestamp was (or may be) edited* NONE = may not be edited* MAY_REQUEST = user may only request changes* DIRECT_ACCESS = timestamps may be modified directly
    edit_mode: Optional[TimestampEditMode] = None
    # history of all timestamp changes of this employee / day
    history: Optional[list[TimestampHistory]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TimestampInfoWithHistory:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TimestampInfoWithHistory
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TimestampInfoWithHistory()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .timestamp import Timestamp
        from .timestamp_day_closing import TimestampDayClosing
        from .timestamp_edit_mode import TimestampEditMode
        from .timestamp_history import TimestampHistory
        from .timestamp_info import TimestampInfo

        from .timestamp import Timestamp
        from .timestamp_day_closing import TimestampDayClosing
        from .timestamp_edit_mode import TimestampEditMode
        from .timestamp_history import TimestampHistory
        from .timestamp_info import TimestampInfo

        fields: dict[str, Callable[[Any], None]] = {
            "changesRequested": lambda n : setattr(self, 'changes_requested', n.get_collection_of_object_values(Timestamp)),
            "dayClosing": lambda n : setattr(self, 'day_closing', n.get_object_value(TimestampDayClosing)),
            "editMode": lambda n : setattr(self, 'edit_mode', n.get_enum_value(TimestampEditMode)),
            "history": lambda n : setattr(self, 'history', n.get_collection_of_object_values(TimestampHistory)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_collection_of_object_values("changesRequested", self.changes_requested)
        writer.write_object_value("dayClosing", self.day_closing)
        writer.write_enum_value("editMode", self.edit_mode)
    

