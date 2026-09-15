from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class TnsTokenLog(AdditionalDataHolder, Parsable):
    """
    Protokolleintrag eines erstellten API-Tokens (TnsTokenLog).
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The createdByEmployeeId property
    created_by_employee_id: Optional[int] = None
    # The creationDate property
    creation_date: Optional[int] = None
    # The expirationDate property
    expiration_date: Optional[int] = None
    # Externes Programm (Enum TnsExtPrograms).
    ext_program: Optional[str] = None
    # The id property
    id: Optional[int] = None
    # The info property
    info: Optional[str] = None
    # Maskiertes Token.
    token: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsTokenLog:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsTokenLog
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsTokenLog()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "createdByEmployeeId": lambda n : setattr(self, 'created_by_employee_id', n.get_int_value()),
            "creationDate": lambda n : setattr(self, 'creation_date', n.get_int_value()),
            "expirationDate": lambda n : setattr(self, 'expiration_date', n.get_int_value()),
            "extProgram": lambda n : setattr(self, 'ext_program', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "info": lambda n : setattr(self, 'info', n.get_str_value()),
            "token": lambda n : setattr(self, 'token', n.get_str_value()),
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
        writer.write_int_value("createdByEmployeeId", self.created_by_employee_id)
        writer.write_int_value("creationDate", self.creation_date)
        writer.write_int_value("expirationDate", self.expiration_date)
        writer.write_str_value("extProgram", self.ext_program)
        writer.write_int_value("id", self.id)
        writer.write_str_value("info", self.info)
        writer.write_str_value("token", self.token)
        writer.write_additional_data_value(self.additional_data)
    

