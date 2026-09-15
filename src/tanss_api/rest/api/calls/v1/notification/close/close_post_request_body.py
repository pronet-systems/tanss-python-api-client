from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class ClosePostRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Employee whose notification is closed.
    employee_id: Optional[int] = None
    # The idString property
    id_string: Optional[str] = None
    # The mail property
    mail: Optional[str] = None
    # Id of the phone call the notification belongs to.
    phone_call_id: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ClosePostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ClosePostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ClosePostRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "employeeId": lambda n : setattr(self, 'employee_id', n.get_int_value()),
            "idString": lambda n : setattr(self, 'id_string', n.get_str_value()),
            "mail": lambda n : setattr(self, 'mail', n.get_str_value()),
            "phoneCallId": lambda n : setattr(self, 'phone_call_id', n.get_int_value()),
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
        writer.write_str_value("idString", self.id_string)
        writer.write_str_value("mail", self.mail)
        writer.write_int_value("phoneCallId", self.phone_call_id)
        writer.write_additional_data_value(self.additional_data)
    

