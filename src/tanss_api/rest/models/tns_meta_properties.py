from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tns_meta_properties_extras import TnsMetaProperties_extras
    from .tns_meta_properties_fields import TnsMetaProperties_fields

@dataclass
class TnsMetaProperties(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The editable property
    editable: Optional[bool] = None
    # The extras property
    extras: Optional[TnsMetaProperties_extras] = None
    # The fields property
    fields: Optional[TnsMetaProperties_fields] = None
    # The message property
    message: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsMetaProperties:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsMetaProperties
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsMetaProperties()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .tns_meta_properties_extras import TnsMetaProperties_extras
        from .tns_meta_properties_fields import TnsMetaProperties_fields

        from .tns_meta_properties_extras import TnsMetaProperties_extras
        from .tns_meta_properties_fields import TnsMetaProperties_fields

        fields: dict[str, Callable[[Any], None]] = {
            "editable": lambda n : setattr(self, 'editable', n.get_bool_value()),
            "extras": lambda n : setattr(self, 'extras', n.get_object_value(TnsMetaProperties_extras)),
            "fields": lambda n : setattr(self, 'fields', n.get_object_value(TnsMetaProperties_fields)),
            "message": lambda n : setattr(self, 'message', n.get_str_value()),
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
        writer.write_bool_value("editable", self.editable)
        writer.write_object_value("extras", self.extras)
        writer.write_object_value("fields", self.fields)
        writer.write_str_value("message", self.message)
        writer.write_additional_data_value(self.additional_data)
    

