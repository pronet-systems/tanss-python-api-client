from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class TnsAvailabilityInfo_endInfos(AdditionalDataHolder, Parsable):
    """
    specific informations about absences, when they will end.They key ist the id of the absence, the value is an info object regarding infos
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsAvailabilityInfo_endInfos:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsAvailabilityInfo_endInfos
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsAvailabilityInfo_endInfos()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
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
        writer.write_additional_data_value(self.additional_data)
    

