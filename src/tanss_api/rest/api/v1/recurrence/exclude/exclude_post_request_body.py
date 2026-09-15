from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class ExcludePostRequestBody(AdditionalDataHolder, Parsable):
    """
    Request body.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Identifier of the employee who created the exclusion.
    employee_id: Optional[int] = None
    # Unique identifier of the recurrence exclusion.
    id: Optional[int] = None
    # Timestamp indicating when the exclusion was indexed.
    indexed: Optional[int] = None
    # Excluded occurrence date in ISO date format.
    iso_date_string: Optional[str] = None
    # Identifier of the recurrence rule this exclusion applies to.
    rule_id: Optional[int] = None
    # Unix timestamp of the excluded occurrence.
    timestamp: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ExcludePostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ExcludePostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ExcludePostRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "employeeId": lambda n : setattr(self, 'employee_id', n.get_int_value()),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "indexed": lambda n : setattr(self, 'indexed', n.get_int_value()),
            "isoDateString": lambda n : setattr(self, 'iso_date_string', n.get_str_value()),
            "ruleId": lambda n : setattr(self, 'rule_id', n.get_int_value()),
            "timestamp": lambda n : setattr(self, 'timestamp', n.get_int_value()),
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
        writer.write_int_value("employeeId", self.employee_id)
        writer.write_int_value("indexed", self.indexed)
        writer.write_str_value("isoDateString", self.iso_date_string)
        writer.write_int_value("ruleId", self.rule_id)
        writer.write_int_value("timestamp", self.timestamp)
        writer.write_additional_data_value(self.additional_data)
    

