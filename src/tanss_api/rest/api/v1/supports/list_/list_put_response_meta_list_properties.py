from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .list_put_response_meta_list_properties_supports import ListPutResponse_meta_listProperties_supports

@dataclass
class ListPutResponse_meta_listProperties(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # per-support computed extras, keyed by support id
    supports: Optional[ListPutResponse_meta_listProperties_supports] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ListPutResponse_meta_listProperties:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ListPutResponse_meta_listProperties
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ListPutResponse_meta_listProperties()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .list_put_response_meta_list_properties_supports import ListPutResponse_meta_listProperties_supports

        from .list_put_response_meta_list_properties_supports import ListPutResponse_meta_listProperties_supports

        fields: dict[str, Callable[[Any], None]] = {
            "supports": lambda n : setattr(self, 'supports', n.get_object_value(ListPutResponse_meta_listProperties_supports)),
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
        writer.write_object_value("supports", self.supports)
        writer.write_additional_data_value(self.additional_data)
    

