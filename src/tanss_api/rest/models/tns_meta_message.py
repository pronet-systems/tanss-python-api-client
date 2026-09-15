from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tns_meta_message_linked_entities import TnsMetaMessage_linkedEntities
    from .tns_meta_message_list_properties import TnsMetaMessage_listProperties
    from .tns_meta_properties import TnsMetaProperties

@dataclass
class TnsMetaMessage(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The linkedEntities property
    linked_entities: Optional[TnsMetaMessage_linkedEntities] = None
    # The listProperties property
    list_properties: Optional[TnsMetaMessage_listProperties] = None
    # The properties property
    properties: Optional[TnsMetaProperties] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsMetaMessage:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsMetaMessage
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsMetaMessage()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .tns_meta_message_linked_entities import TnsMetaMessage_linkedEntities
        from .tns_meta_message_list_properties import TnsMetaMessage_listProperties
        from .tns_meta_properties import TnsMetaProperties

        from .tns_meta_message_linked_entities import TnsMetaMessage_linkedEntities
        from .tns_meta_message_list_properties import TnsMetaMessage_listProperties
        from .tns_meta_properties import TnsMetaProperties

        fields: dict[str, Callable[[Any], None]] = {
            "linkedEntities": lambda n : setattr(self, 'linked_entities', n.get_object_value(TnsMetaMessage_linkedEntities)),
            "listProperties": lambda n : setattr(self, 'list_properties', n.get_object_value(TnsMetaMessage_listProperties)),
            "properties": lambda n : setattr(self, 'properties', n.get_object_value(TnsMetaProperties)),
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
        writer.write_object_value("linkedEntities", self.linked_entities)
        writer.write_object_value("listProperties", self.list_properties)
        writer.write_object_value("properties", self.properties)
        writer.write_additional_data_value(self.additional_data)
    

