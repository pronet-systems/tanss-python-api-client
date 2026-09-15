from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class TnsAnticipatedCallbackSearchResult(AdditionalDataHolder, Parsable):
    """
    gives infos about anticipated callbacks in company search results
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # date when the anticipated callback was entered
    date: Optional[int] = None
    # id of the employee who waits for this callback
    from_employee_id: Optional[int] = None
    # phone number of this callback
    phone_number: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsAnticipatedCallbackSearchResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsAnticipatedCallbackSearchResult
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsAnticipatedCallbackSearchResult()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "date": lambda n : setattr(self, 'date', n.get_int_value()),
            "fromEmployeeId": lambda n : setattr(self, 'from_employee_id', n.get_int_value()),
            "phoneNumber": lambda n : setattr(self, 'phone_number', n.get_str_value()),
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
        writer.write_int_value("date", self.date)
        writer.write_int_value("fromEmployeeId", self.from_employee_id)
        writer.write_str_value("phoneNumber", self.phone_number)
        writer.write_additional_data_value(self.additional_data)
    

