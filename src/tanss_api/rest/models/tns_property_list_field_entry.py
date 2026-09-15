from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tns_property_list_field_entry_data import TnsPropertyListFieldEntry_data

@dataclass
class TnsPropertyListFieldEntry(AdditionalDataHolder, Parsable):
    """
    Eintrag einer Auswahlliste
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Zusatzdaten, z.B. selected=true bei Vorauswahl; sonst null
    data: Optional[TnsPropertyListFieldEntry_data] = None
    # Schluessel (z.B. TICKET, CALLBACK, SUPPORT, ABSENCE, BIRTHDAY, CHAT, SERVEREYE, OUTLOOK, EMAIL)
    key: Optional[str] = None
    # Uebersetzter Anzeigetext
    text: Optional[str] = None
    # The value property
    value: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsPropertyListFieldEntry:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsPropertyListFieldEntry
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsPropertyListFieldEntry()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .tns_property_list_field_entry_data import TnsPropertyListFieldEntry_data

        from .tns_property_list_field_entry_data import TnsPropertyListFieldEntry_data

        fields: dict[str, Callable[[Any], None]] = {
            "data": lambda n : setattr(self, 'data', n.get_object_value(TnsPropertyListFieldEntry_data)),
            "key": lambda n : setattr(self, 'key', n.get_str_value()),
            "text": lambda n : setattr(self, 'text', n.get_str_value()),
            "value": lambda n : setattr(self, 'value', n.get_int_value()),
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
        writer.write_object_value("data", self.data)
        writer.write_str_value("key", self.key)
        writer.write_str_value("text", self.text)
        writer.write_int_value("value", self.value)
        writer.write_additional_data_value(self.additional_data)
    

