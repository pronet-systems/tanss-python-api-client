from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .pdf_export_post_request_body_file_name_type import PdfExportPostRequestBody_fileNameType

@dataclass
class PdfExportPostRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Whether the export should actually be performed
    execute: Optional[bool] = None
    # Naming scheme applied to the exported files
    file_name_type: Optional[PdfExportPostRequestBody_fileNameType] = None
    # Start date of the export range
    from_date: Optional[str] = None
    # Lower bound order identifier for the export range
    from_order_id: Optional[int] = None
    # End date of the export range
    to_date: Optional[str] = None
    # Upper bound order identifier for the export range
    to_order_id: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PdfExportPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PdfExportPostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PdfExportPostRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .pdf_export_post_request_body_file_name_type import PdfExportPostRequestBody_fileNameType

        from .pdf_export_post_request_body_file_name_type import PdfExportPostRequestBody_fileNameType

        fields: dict[str, Callable[[Any], None]] = {
            "execute": lambda n : setattr(self, 'execute', n.get_bool_value()),
            "fileNameType": lambda n : setattr(self, 'file_name_type', n.get_enum_value(PdfExportPostRequestBody_fileNameType)),
            "fromDate": lambda n : setattr(self, 'from_date', n.get_str_value()),
            "fromOrderId": lambda n : setattr(self, 'from_order_id', n.get_int_value()),
            "toDate": lambda n : setattr(self, 'to_date', n.get_str_value()),
            "toOrderId": lambda n : setattr(self, 'to_order_id', n.get_int_value()),
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
        writer.write_bool_value("execute", self.execute)
        writer.write_enum_value("fileNameType", self.file_name_type)
        writer.write_str_value("fromDate", self.from_date)
        writer.write_int_value("fromOrderId", self.from_order_id)
        writer.write_str_value("toDate", self.to_date)
        writer.write_int_value("toOrderId", self.to_order_id)
        writer.write_additional_data_value(self.additional_data)
    

