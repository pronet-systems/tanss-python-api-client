from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class TimestampPauseConfig(AdditionalDataHolder, Parsable):
    """
    Defines a configuration for automatical pause subtraction.This is needed because longer working periods must contain certain pauses.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Describes the amount of minutes needed to require a minimum pause (defined in "minimumPause")
    from_minutes: Optional[int] = None
    # The id property
    id: Optional[int] = None
    # A working period must contain at least a pause of x minutes
    minimum_pause: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TimestampPauseConfig:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TimestampPauseConfig
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TimestampPauseConfig()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "fromMinutes": lambda n : setattr(self, 'from_minutes', n.get_int_value()),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "minimumPause": lambda n : setattr(self, 'minimum_pause', n.get_int_value()),
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
        writer.write_int_value("fromMinutes", self.from_minutes)
        writer.write_int_value("minimumPause", self.minimum_pause)
        writer.write_additional_data_value(self.additional_data)
    

