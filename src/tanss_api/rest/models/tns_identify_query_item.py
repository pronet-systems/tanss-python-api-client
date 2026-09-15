from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tns_identify_search_section import TnsIdentifySearchSection
    from .tns_link_type_for_search import TnsLinkTypeForSearch

@dataclass
class TnsIdentifyQueryItem(AdditionalDataHolder, Parsable):
    """
    Describes a item which is to be "identifed" by the API (i.e. get an id by name)
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # identifier (or name) of the entity. This will be used to search the entity id.
    identifier: Optional[str] = None
    # Enum representing the "link type" of an entity to be identifed
    link_type: Optional[TnsLinkTypeForSearch] = None
    # The searchSections property
    search_sections: Optional[list[TnsIdentifySearchSection]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsIdentifyQueryItem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsIdentifyQueryItem
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsIdentifyQueryItem()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .tns_identify_search_section import TnsIdentifySearchSection
        from .tns_link_type_for_search import TnsLinkTypeForSearch

        from .tns_identify_search_section import TnsIdentifySearchSection
        from .tns_link_type_for_search import TnsLinkTypeForSearch

        fields: dict[str, Callable[[Any], None]] = {
            "identifier": lambda n : setattr(self, 'identifier', n.get_str_value()),
            "linkType": lambda n : setattr(self, 'link_type', n.get_enum_value(TnsLinkTypeForSearch)),
            "searchSections": lambda n : setattr(self, 'search_sections', n.get_collection_of_enum_values(TnsIdentifySearchSection)),
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
        writer.write_str_value("identifier", self.identifier)
        writer.write_enum_value("linkType", self.link_type)
        writer.write_collection_of_enum_values("searchSections", self.search_sections)
        writer.write_additional_data_value(self.additional_data)
    

