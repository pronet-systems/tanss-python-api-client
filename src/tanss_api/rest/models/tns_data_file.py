from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tns_data_file_enum import TnsDataFileEnum

@dataclass
class TnsDataFile(AdditionalDataHolder, Parsable):
    """
    An object describing an upload file result
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # MIME type of the uploaded file
    mime_type: Optional[str] = None
    # filename of the uploaded file
    name: Optional[str] = None
    # filesize of the uploaded file
    size: Optional[int] = None
    # info representing the upload state
    status: Optional[TnsDataFileEnum] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsDataFile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsDataFile
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsDataFile()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .tns_data_file_enum import TnsDataFileEnum

        from .tns_data_file_enum import TnsDataFileEnum

        fields: dict[str, Callable[[Any], None]] = {
            "mimeType": lambda n : setattr(self, 'mime_type', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "size": lambda n : setattr(self, 'size', n.get_int_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(TnsDataFileEnum)),
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
        writer.write_str_value("mimeType", self.mime_type)
        writer.write_str_value("name", self.name)
        writer.write_int_value("size", self.size)
        writer.write_enum_value("status", self.status)
        writer.write_additional_data_value(self.additional_data)
    

