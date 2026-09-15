from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class TnsEmployeeAvatar(AdditionalDataHolder, Parsable):
    """
    Avatar-Bild eines Mitarbeiters
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Bilddaten (Base64)
    avatar: Optional[bytes] = None
    # The employeeId property
    employee_id: Optional[int] = None
    # The mimeType property
    mime_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsEmployeeAvatar:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsEmployeeAvatar
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsEmployeeAvatar()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "avatar": lambda n : setattr(self, 'avatar', n.get_bytes_value()),
            "employeeId": lambda n : setattr(self, 'employee_id', n.get_int_value()),
            "mimeType": lambda n : setattr(self, 'mime_type', n.get_str_value()),
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
        writer.write_bytes_value("avatar", self.avatar)
        writer.write_int_value("employeeId", self.employee_id)
        writer.write_str_value("mimeType", self.mime_type)
        writer.write_additional_data_value(self.additional_data)
    

