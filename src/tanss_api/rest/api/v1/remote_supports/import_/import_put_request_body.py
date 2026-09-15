from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .import_put_request_body_remote_maintenance_type import ImportPutRequestBody_remoteMaintenanceType

@dataclass
class ImportPutRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Number of past days to include in the fetch.
    number_of_days: Optional[int] = None
    # Remote maintenance provider whose sessions should be fetched.
    remote_maintenance_type: Optional[ImportPutRequestBody_remoteMaintenanceType] = None
    # Identifier of the user whose remote support sessions should be fetched.
    user_id: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ImportPutRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ImportPutRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ImportPutRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .import_put_request_body_remote_maintenance_type import ImportPutRequestBody_remoteMaintenanceType

        from .import_put_request_body_remote_maintenance_type import ImportPutRequestBody_remoteMaintenanceType

        fields: dict[str, Callable[[Any], None]] = {
            "numberOfDays": lambda n : setattr(self, 'number_of_days', n.get_int_value()),
            "remoteMaintenanceType": lambda n : setattr(self, 'remote_maintenance_type', n.get_enum_value(ImportPutRequestBody_remoteMaintenanceType)),
            "userId": lambda n : setattr(self, 'user_id', n.get_int_value()),
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
        writer.write_int_value("numberOfDays", self.number_of_days)
        writer.write_enum_value("remoteMaintenanceType", self.remote_maintenance_type)
        writer.write_int_value("userId", self.user_id)
        writer.write_additional_data_value(self.additional_data)
    

