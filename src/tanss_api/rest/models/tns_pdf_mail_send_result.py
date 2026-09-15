from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class TnsPdfMailSendResult(AdditionalDataHolder, Parsable):
    """
    Ergebnis des PDF-Mailversands
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # aufgetretene Fehler
    exceptions: Optional[list[str]] = None
    # Empfänger mit Versandfehler
    sent_error: Optional[list[str]] = None
    # erfolgreich versendete Empfänger
    sent_succesfully: Optional[list[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsPdfMailSendResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsPdfMailSendResult
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsPdfMailSendResult()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "exceptions": lambda n : setattr(self, 'exceptions', n.get_collection_of_primitive_values(str)),
            "sentError": lambda n : setattr(self, 'sent_error', n.get_collection_of_primitive_values(str)),
            "sentSuccesfully": lambda n : setattr(self, 'sent_succesfully', n.get_collection_of_primitive_values(str)),
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
        writer.write_collection_of_primitive_values("exceptions", self.exceptions)
        writer.write_collection_of_primitive_values("sentError", self.sent_error)
        writer.write_collection_of_primitive_values("sentSuccesfully", self.sent_succesfully)
        writer.write_additional_data_value(self.additional_data)
    

