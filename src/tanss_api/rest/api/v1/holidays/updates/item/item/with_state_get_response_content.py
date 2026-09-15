from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class WithStateGetResponse_content(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The date property
    date: Optional[datetime.date] = None
    # The fixed property
    fixed: Optional[bool] = None
    # The holiday property
    holiday: Optional[str] = None
    # The name property
    name: Optional[str] = None
    # The states property
    states: Optional[list[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WithStateGetResponse_content:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WithStateGetResponse_content
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WithStateGetResponse_content()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "date": lambda n : setattr(self, 'date', n.get_date_value()),
            "fixed": lambda n : setattr(self, 'fixed', n.get_bool_value()),
            "holiday": lambda n : setattr(self, 'holiday', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "states": lambda n : setattr(self, 'states', n.get_collection_of_primitive_values(str)),
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
        writer.write_date_value("date", self.date)
        writer.write_bool_value("fixed", self.fixed)
        writer.write_str_value("holiday", self.holiday)
        writer.write_str_value("name", self.name)
        writer.write_collection_of_primitive_values("states", self.states)
        writer.write_additional_data_value(self.additional_data)
    

