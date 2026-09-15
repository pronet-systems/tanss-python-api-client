from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tns_link_type import TnsLinkType

@dataclass
class TnsTanssEventRuleConfiguration(AdditionalDataHolder, Parsable):
    """
    defines the filter for the event rule list
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # ids of the assignment to be filtered
    link_ids: Optional[list[int]] = None
    # Enum representing the "link type" of an assignment. The id is given in the field "linkId"
    link_type: Optional[TnsLinkType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsTanssEventRuleConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsTanssEventRuleConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsTanssEventRuleConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .tns_link_type import TnsLinkType

        from .tns_link_type import TnsLinkType

        fields: dict[str, Callable[[Any], None]] = {
            "linkIds": lambda n : setattr(self, 'link_ids', n.get_collection_of_primitive_values(int)),
            "linkType": lambda n : setattr(self, 'link_type', n.get_enum_value(TnsLinkType)),
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
        writer.write_collection_of_primitive_values("linkIds", self.link_ids)
        writer.write_enum_value("linkType", self.link_type)
        writer.write_additional_data_value(self.additional_data)
    

