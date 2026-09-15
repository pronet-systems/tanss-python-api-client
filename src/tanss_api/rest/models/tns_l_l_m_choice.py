from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tns_l_l_m_finish_reason import TnsLLMFinishReason
    from .tns_l_l_m_message import TnsLLMMessage

@dataclass
class TnsLLMChoice(AdditionalDataHolder, Parsable):
    """
    Antwortalternative einer LLM-Antwort.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Abschlussgrund einer LLM-Antwort.
    finish_reason: Optional[TnsLLMFinishReason] = None
    # Nachricht einer LLM-Antwort.
    message: Optional[TnsLLMMessage] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsLLMChoice:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsLLMChoice
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsLLMChoice()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .tns_l_l_m_finish_reason import TnsLLMFinishReason
        from .tns_l_l_m_message import TnsLLMMessage

        from .tns_l_l_m_finish_reason import TnsLLMFinishReason
        from .tns_l_l_m_message import TnsLLMMessage

        fields: dict[str, Callable[[Any], None]] = {
            "finishReason": lambda n : setattr(self, 'finish_reason', n.get_enum_value(TnsLLMFinishReason)),
            "message": lambda n : setattr(self, 'message', n.get_object_value(TnsLLMMessage)),
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
        writer.write_enum_value("finishReason", self.finish_reason)
        writer.write_object_value("message", self.message)
        writer.write_additional_data_value(self.additional_data)
    

