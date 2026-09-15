from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class GetPutResponse_content(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The achieved property
    achieved: Optional[float] = None
    # The employeeId property
    employee_id: Optional[int] = None
    # The percent property
    percent: Optional[float] = None
    # The target property
    target: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> GetPutResponse_content:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: GetPutResponse_content
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return GetPutResponse_content()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "achieved": lambda n : setattr(self, 'achieved', n.get_float_value()),
            "employeeId": lambda n : setattr(self, 'employee_id', n.get_int_value()),
            "percent": lambda n : setattr(self, 'percent', n.get_float_value()),
            "target": lambda n : setattr(self, 'target', n.get_float_value()),
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
        writer.write_float_value("achieved", self.achieved)
        writer.write_int_value("employeeId", self.employee_id)
        writer.write_float_value("percent", self.percent)
        writer.write_float_value("target", self.target)
        writer.write_additional_data_value(self.additional_data)
    

