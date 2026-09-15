from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tns_meta_properties import TnsMetaProperties
    from .tns_support import TnsSupport

@dataclass
class TnsSupportObjectProperties(AdditionalDataHolder, Parsable):
    """
    Taetigkeit mit berechneten Meta-Properties (TnsObjectProperties<TnsSupport>)
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # describes a support entry (same for appointment)
    data: Optional[TnsSupport] = None
    # The properties property
    properties: Optional[TnsMetaProperties] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsSupportObjectProperties:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsSupportObjectProperties
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsSupportObjectProperties()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .tns_meta_properties import TnsMetaProperties
        from .tns_support import TnsSupport

        from .tns_meta_properties import TnsMetaProperties
        from .tns_support import TnsSupport

        fields: dict[str, Callable[[Any], None]] = {
            "data": lambda n : setattr(self, 'data', n.get_object_value(TnsSupport)),
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
        writer.write_object_value("data", self.data)
        writer.write_object_value("properties", self.properties)
        writer.write_additional_data_value(self.additional_data)
    

