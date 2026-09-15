from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tns_error_code import TnsErrorCode

@dataclass
class TnsException(AdditionalDataHolder, Parsable):
    """
    describes an error that occurs in TANSS
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # localized error message (currently only in english)
    localized_text: Optional[str] = None
    # Stable error code (see object). For example `CANT_CHECK_ITEM_TWICE`.Use this (not `localizedText`) for programmatic error handling.
    text: Optional[TnsErrorCode] = None
    # detailled message of a general java exception
    thrown_exception_message: Optional[str] = None
    # name of the TANSS exception
    type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsException:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsException
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsException()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .tns_error_code import TnsErrorCode

        from .tns_error_code import TnsErrorCode

        fields: dict[str, Callable[[Any], None]] = {
            "localizedText": lambda n : setattr(self, 'localized_text', n.get_str_value()),
            "text": lambda n : setattr(self, 'text', n.get_enum_value(TnsErrorCode)),
            "thrownExceptionMessage": lambda n : setattr(self, 'thrown_exception_message', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_str_value()),
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
        writer.write_str_value("localizedText", self.localized_text)
        writer.write_enum_value("text", self.text)
        writer.write_str_value("thrownExceptionMessage", self.thrown_exception_message)
        writer.write_str_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    

