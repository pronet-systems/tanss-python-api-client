from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class TnsExternal(AdditionalDataHolder, Parsable):
    """
    Zuordnung einer externen ID (z.B. TANSS_TUCID) zu einem TANSS-Objekt
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Externe ID
    ext_id: Optional[str] = None
    # ID des verknuepften Objekts
    link_id: Optional[int] = None
    # Verknuepfungstyp (2 = Firma)
    link_type_id: Optional[int] = None
    # Externes Programm/Quelle (z.B. TANSS_TUCID)
    prog: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsExternal:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsExternal
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsExternal()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "extId": lambda n : setattr(self, 'ext_id', n.get_str_value()),
            "linkId": lambda n : setattr(self, 'link_id', n.get_int_value()),
            "linkTypeId": lambda n : setattr(self, 'link_type_id', n.get_int_value()),
            "prog": lambda n : setattr(self, 'prog', n.get_str_value()),
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
        writer.write_str_value("extId", self.ext_id)
        writer.write_int_value("linkId", self.link_id)
        writer.write_int_value("linkTypeId", self.link_type_id)
        writer.write_str_value("prog", self.prog)
        writer.write_additional_data_value(self.additional_data)
    

