from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tns_l_l_m_model import TnsLLMModel
    from .tns_l_l_m_provider import TnsLLMProvider

@dataclass
class TnsLLMConfiguration(AdditionalDataHolder, Parsable):
    """
    KI-/LLM-Konfiguration (apiKey wird in Antworten ausgeblendet)
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # API-Key des Providers (nur beim Anlegen/Ändern; wird verschlüsselt gespeichert)
    api_key: Optional[str] = None
    # Zeitpunkt der Bestätigung (Timestamp)
    confirmed: Optional[int] = None
    # true, wenn ein API-Key hinterlegt ist
    has_key: Optional[bool] = None
    # The id property
    id: Optional[int] = None
    # LLM-Provider
    llm_provider: Optional[TnsLLMProvider] = None
    # The name property
    name: Optional[str] = None
    # Bevorzugtes LLM-Modell
    pref_model: Optional[TnsLLMModel] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsLLMConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsLLMConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsLLMConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .tns_l_l_m_model import TnsLLMModel
        from .tns_l_l_m_provider import TnsLLMProvider

        from .tns_l_l_m_model import TnsLLMModel
        from .tns_l_l_m_provider import TnsLLMProvider

        fields: dict[str, Callable[[Any], None]] = {
            "apiKey": lambda n : setattr(self, 'api_key', n.get_str_value()),
            "confirmed": lambda n : setattr(self, 'confirmed', n.get_int_value()),
            "hasKey": lambda n : setattr(self, 'has_key', n.get_bool_value()),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "llmProvider": lambda n : setattr(self, 'llm_provider', n.get_enum_value(TnsLLMProvider)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "prefModel": lambda n : setattr(self, 'pref_model', n.get_enum_value(TnsLLMModel)),
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
        writer.write_str_value("apiKey", self.api_key)
        writer.write_int_value("confirmed", self.confirmed)
        writer.write_enum_value("llmProvider", self.llm_provider)
        writer.write_str_value("name", self.name)
        writer.write_enum_value("prefModel", self.pref_model)
        writer.write_additional_data_value(self.additional_data)
    

