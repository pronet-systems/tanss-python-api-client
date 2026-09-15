from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tns_identify_item_result_object import TnsIdentifyItemResult_object
    from .tns_identify_search_section import TnsIdentifySearchSection
    from .tns_link_type_for_search import TnsLinkTypeForSearch

@dataclass
class TnsIdentifyItemResult(AdditionalDataHolder, Parsable):
    """
    Describes a single result for a "query item"
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # retrieved "id" of the entity which was found
    link_id: Optional[int] = None
    # Enum representing the "link type" of an entity to be identifed
    link_type: Optional[TnsLinkTypeForSearch] = None
    # name of the entity which was found
    name: Optional[str] = None
    # object of the target entity (containing the actual found entity, i.e. company, cpu type, manufacturer...)
    object: Optional[TnsIdentifyItemResult_object] = None
    # (optional) if not mathcin 100%, will return a certain percentage
    percent: Optional[int] = None
    # in which "sections" shall be searched
    search_section: Optional[TnsIdentifySearchSection] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsIdentifyItemResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsIdentifyItemResult
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsIdentifyItemResult()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .tns_identify_item_result_object import TnsIdentifyItemResult_object
        from .tns_identify_search_section import TnsIdentifySearchSection
        from .tns_link_type_for_search import TnsLinkTypeForSearch

        from .tns_identify_item_result_object import TnsIdentifyItemResult_object
        from .tns_identify_search_section import TnsIdentifySearchSection
        from .tns_link_type_for_search import TnsLinkTypeForSearch

        fields: dict[str, Callable[[Any], None]] = {
            "linkId": lambda n : setattr(self, 'link_id', n.get_int_value()),
            "linkType": lambda n : setattr(self, 'link_type', n.get_enum_value(TnsLinkTypeForSearch)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "object": lambda n : setattr(self, 'object', n.get_object_value(TnsIdentifyItemResult_object)),
            "percent": lambda n : setattr(self, 'percent', n.get_int_value()),
            "searchSection": lambda n : setattr(self, 'search_section', n.get_enum_value(TnsIdentifySearchSection)),
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
        writer.write_int_value("linkId", self.link_id)
        writer.write_enum_value("linkType", self.link_type)
        writer.write_str_value("name", self.name)
        writer.write_object_value("object", self.object)
        writer.write_int_value("percent", self.percent)
        writer.write_enum_value("searchSection", self.search_section)
        writer.write_additional_data_value(self.additional_data)
    

