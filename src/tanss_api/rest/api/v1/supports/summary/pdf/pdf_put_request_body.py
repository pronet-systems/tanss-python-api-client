from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .pdf_put_request_body_configuration import PdfPutRequestBody_configuration
    from .pdf_put_request_body_grouping import PdfPutRequestBody_grouping
    from .pdf_put_request_body_print_options import PdfPutRequestBody_printOptions
    from .pdf_put_request_body_supplement_sheet import PdfPutRequestBody_supplementSheet

@dataclass
class PdfPutRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Support list configuration selecting which entries the summary covers
    configuration: Optional[PdfPutRequestBody_configuration] = None
    # Reference date of the summary as a unix timestamp
    date: Optional[int] = None
    # How summary entries are grouped in the output
    grouping: Optional[PdfPutRequestBody_grouping] = None
    # Include price information in the summary
    include_pricing: Optional[bool] = None
    # Invoice number associated with the summary
    invoice_number: Optional[int] = None
    # Print only the supplement sheet without the main summary
    only_supplement_sheet: Optional[bool] = None
    # Which document variant is generated
    print_options: Optional[PdfPutRequestBody_printOptions] = None
    # Type of supplement sheet to include in the printout
    supplement_sheet: Optional[PdfPutRequestBody_supplementSheet] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PdfPutRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PdfPutRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PdfPutRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .pdf_put_request_body_configuration import PdfPutRequestBody_configuration
        from .pdf_put_request_body_grouping import PdfPutRequestBody_grouping
        from .pdf_put_request_body_print_options import PdfPutRequestBody_printOptions
        from .pdf_put_request_body_supplement_sheet import PdfPutRequestBody_supplementSheet

        from .pdf_put_request_body_configuration import PdfPutRequestBody_configuration
        from .pdf_put_request_body_grouping import PdfPutRequestBody_grouping
        from .pdf_put_request_body_print_options import PdfPutRequestBody_printOptions
        from .pdf_put_request_body_supplement_sheet import PdfPutRequestBody_supplementSheet

        fields: dict[str, Callable[[Any], None]] = {
            "configuration": lambda n : setattr(self, 'configuration', n.get_object_value(PdfPutRequestBody_configuration)),
            "date": lambda n : setattr(self, 'date', n.get_int_value()),
            "grouping": lambda n : setattr(self, 'grouping', n.get_enum_value(PdfPutRequestBody_grouping)),
            "includePricing": lambda n : setattr(self, 'include_pricing', n.get_bool_value()),
            "invoiceNumber": lambda n : setattr(self, 'invoice_number', n.get_int_value()),
            "onlySupplementSheet": lambda n : setattr(self, 'only_supplement_sheet', n.get_bool_value()),
            "printOptions": lambda n : setattr(self, 'print_options', n.get_enum_value(PdfPutRequestBody_printOptions)),
            "supplementSheet": lambda n : setattr(self, 'supplement_sheet', n.get_enum_value(PdfPutRequestBody_supplementSheet)),
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
        writer.write_object_value("configuration", self.configuration)
        writer.write_int_value("date", self.date)
        writer.write_enum_value("grouping", self.grouping)
        writer.write_bool_value("includePricing", self.include_pricing)
        writer.write_int_value("invoiceNumber", self.invoice_number)
        writer.write_bool_value("onlySupplementSheet", self.only_supplement_sheet)
        writer.write_enum_value("printOptions", self.print_options)
        writer.write_enum_value("supplementSheet", self.supplement_sheet)
        writer.write_additional_data_value(self.additional_data)
    

