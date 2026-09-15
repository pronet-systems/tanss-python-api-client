from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tns_search_area import TnsSearchArea
    from .tns_search_area_configuration import TnsSearchAreaConfiguration

@dataclass
class TnsSearchConfiguration(AdditionalDataHolder, Parsable):
    """
    object representing a definition for searching in misc. areas
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # describes in which areas to search
    areas: Optional[list[TnsSearchArea]] = None
    # here, some specific search parameters can be overridden
    configs: Optional[TnsSearchAreaConfiguration] = None
    # the query string
    query: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsSearchConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsSearchConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsSearchConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .tns_search_area import TnsSearchArea
        from .tns_search_area_configuration import TnsSearchAreaConfiguration

        from .tns_search_area import TnsSearchArea
        from .tns_search_area_configuration import TnsSearchAreaConfiguration

        fields: dict[str, Callable[[Any], None]] = {
            "areas": lambda n : setattr(self, 'areas', n.get_collection_of_enum_values(TnsSearchArea)),
            "configs": lambda n : setattr(self, 'configs', n.get_object_value(TnsSearchAreaConfiguration)),
            "query": lambda n : setattr(self, 'query', n.get_str_value()),
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
        writer.write_collection_of_enum_values("areas", self.areas)
        writer.write_object_value("configs", self.configs)
        writer.write_str_value("query", self.query)
        writer.write_additional_data_value(self.additional_data)
    

