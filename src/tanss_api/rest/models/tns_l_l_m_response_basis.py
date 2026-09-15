from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tns_l_l_m_choice import TnsLLMChoice

@dataclass
class TnsLLMResponseBasis(AdditionalDataHolder, Parsable):
    """
    Antwort des LLM-Providers (TnsLLMResponseBasis).
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The choices property
    choices: Optional[list[TnsLLMChoice]] = None
    # The created property
    created: Optional[int] = None
    # The id property
    id: Optional[str] = None
    # The model property
    model: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsLLMResponseBasis:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsLLMResponseBasis
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsLLMResponseBasis()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .tns_l_l_m_choice import TnsLLMChoice

        from .tns_l_l_m_choice import TnsLLMChoice

        fields: dict[str, Callable[[Any], None]] = {
            "choices": lambda n : setattr(self, 'choices', n.get_collection_of_object_values(TnsLLMChoice)),
            "created": lambda n : setattr(self, 'created', n.get_int_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "model": lambda n : setattr(self, 'model', n.get_str_value()),
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
        writer.write_collection_of_object_values("choices", self.choices)
        writer.write_int_value("created", self.created)
        writer.write_str_value("id", self.id)
        writer.write_str_value("model", self.model)
        writer.write_additional_data_value(self.additional_data)
    

