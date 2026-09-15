from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import ComposedTypeWrapper, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ......models.tns_file_pass_response import TnsFilePassResponse
    from ......models.tns_pdf_mail_send_result import TnsPdfMailSendResult

@dataclass
class PdfPutResponse_content(ComposedTypeWrapper, Parsable):
    """
    Composed type wrapper for classes TnsFilePassResponse, TnsPdfMailSendResult
    """
    # Composed type representation for type TnsFilePassResponse
    tns_file_pass_response: Optional[TnsFilePassResponse] = None
    # Composed type representation for type TnsPdfMailSendResult
    tns_pdf_mail_send_result: Optional[TnsPdfMailSendResult] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PdfPutResponse_content:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PdfPutResponse_content
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        result = PdfPutResponse_content()
        if mapping_value and mapping_value.casefold() == "TnsFilePassResponse".casefold():
            from ......models.tns_file_pass_response import TnsFilePassResponse

            result.tns_file_pass_response = TnsFilePassResponse()
        elif mapping_value and mapping_value.casefold() == "TnsPdfMailSendResult".casefold():
            from ......models.tns_pdf_mail_send_result import TnsPdfMailSendResult

            result.tns_pdf_mail_send_result = TnsPdfMailSendResult()
        return result
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ......models.tns_file_pass_response import TnsFilePassResponse
        from ......models.tns_pdf_mail_send_result import TnsPdfMailSendResult

        if self.tns_file_pass_response:
            return self.tns_file_pass_response.get_field_deserializers()
        if self.tns_pdf_mail_send_result:
            return self.tns_pdf_mail_send_result.get_field_deserializers()
        return {}
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        if self.tns_file_pass_response:
            writer.write_object_value(None, self.tns_file_pass_response)
        elif self.tns_pdf_mail_send_result:
            writer.write_object_value(None, self.tns_pdf_mail_send_result)
    

