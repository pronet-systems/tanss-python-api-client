from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class TimerFragment(AdditionalDataHolder, Parsable):
    """
    Timers can have multiple fragments, meaning a start/stop timeframe.Each fragment can have a note.A timer is running if the last fragment has no stop time.If the last fragment has a stop time, the timer is stopped.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # a note for this fragment.You could for example make notes of things which are done in this fragment which should help generating the support for this timer
    note: Optional[str] = None
    # starting time of the fragment
    start_time: Optional[int] = None
    # end time of the fragment (if 0 means that the timer is still running)
    stop_time: Optional[int] = None
    # id of the timer id for this fragment
    timer_id: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TimerFragment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TimerFragment
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TimerFragment()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "note": lambda n : setattr(self, 'note', n.get_str_value()),
            "startTime": lambda n : setattr(self, 'start_time', n.get_int_value()),
            "stopTime": lambda n : setattr(self, 'stop_time', n.get_int_value()),
            "timerId": lambda n : setattr(self, 'timer_id', n.get_int_value()),
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
        writer.write_str_value("note", self.note)
        writer.write_int_value("startTime", self.start_time)
        writer.write_int_value("stopTime", self.stop_time)
        writer.write_int_value("timerId", self.timer_id)
        writer.write_additional_data_value(self.additional_data)
    

