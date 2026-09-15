from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tns_l_l_m_provider import TnsLLMProvider

@dataclass
class TnsLLMProviderContent(AdditionalDataHolder, Parsable):
    """
    LLM-Provider mit seinen aktiven Modellen
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Aktive Modelle des Providers (Modell-Enum-Namen)
    models: Optional[list[str]] = None
    # LLM-Provider
    provider: Optional[TnsLLMProvider] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsLLMProviderContent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsLLMProviderContent
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsLLMProviderContent()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .tns_l_l_m_provider import TnsLLMProvider

        from .tns_l_l_m_provider import TnsLLMProvider

        fields: dict[str, Callable[[Any], None]] = {
            "models": lambda n : setattr(self, 'models', n.get_collection_of_primitive_values(str)),
            "provider": lambda n : setattr(self, 'provider', n.get_enum_value(TnsLLMProvider)),
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
        writer.write_collection_of_primitive_values("models", self.models)
        writer.write_enum_value("provider", self.provider)
        writer.write_additional_data_value(self.additional_data)
    

