from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class TnsRemoteMaintenanceEmployeeAssignmentId(AdditionalDataHolder, Parsable):
    """
    Identifies a "translation" of a userId based on a remote support "type" to a TANSS employee / technician.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # UserId which is transferred in a remote support object
    user_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsRemoteMaintenanceEmployeeAssignmentId:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsRemoteMaintenanceEmployeeAssignmentId
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsRemoteMaintenanceEmployeeAssignmentId()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "userId": lambda n : setattr(self, 'user_id', n.get_str_value()),
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
        writer.write_str_value("userId", self.user_id)
        writer.write_additional_data_value(self.additional_data)
    

