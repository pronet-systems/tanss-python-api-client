from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tns_cloud_upload_receiver_employee import TnsCloudUploadReceiverEmployee

@dataclass
class TnsCloudUploadReceivers(AdditionalDataHolder, Parsable):
    """
    Mögliche Empfänger eines CloudUpload-Tokens, gruppiert.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The contactpersons property
    contactpersons: Optional[list[TnsCloudUploadReceiverEmployee]] = None
    # The employees property
    employees: Optional[list[TnsCloudUploadReceiverEmployee]] = None
    # The relations property
    relations: Optional[list[TnsCloudUploadReceiverEmployee]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsCloudUploadReceivers:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsCloudUploadReceivers
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsCloudUploadReceivers()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .tns_cloud_upload_receiver_employee import TnsCloudUploadReceiverEmployee

        from .tns_cloud_upload_receiver_employee import TnsCloudUploadReceiverEmployee

        fields: dict[str, Callable[[Any], None]] = {
            "contactpersons": lambda n : setattr(self, 'contactpersons', n.get_collection_of_object_values(TnsCloudUploadReceiverEmployee)),
            "employees": lambda n : setattr(self, 'employees', n.get_collection_of_object_values(TnsCloudUploadReceiverEmployee)),
            "relations": lambda n : setattr(self, 'relations', n.get_collection_of_object_values(TnsCloudUploadReceiverEmployee)),
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
        writer.write_collection_of_object_values("contactpersons", self.contactpersons)
        writer.write_collection_of_object_values("employees", self.employees)
        writer.write_collection_of_object_values("relations", self.relations)
        writer.write_additional_data_value(self.additional_data)
    

