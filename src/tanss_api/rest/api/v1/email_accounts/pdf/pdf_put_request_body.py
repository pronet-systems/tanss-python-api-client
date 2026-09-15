from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .pdf_put_request_body_active import PdfPutRequestBody_active
    from .pdf_put_request_body_branches import PdfPutRequestBody_branches
    from .pdf_put_request_body_mail import PdfPutRequestBody_mail
    from .pdf_put_request_body_sort_field import PdfPutRequestBody_sortField
    from .pdf_put_request_body_sort_order import PdfPutRequestBody_sortOrder

@dataclass
class PdfPutRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The active property
    active: Optional[PdfPutRequestBody_active] = None
    # How branch companies are treated.
    branches: Optional[PdfPutRequestBody_branches] = None
    # Columns to render in the PDF. Empty means the default set.
    columns: Optional[list[str]] = None
    # Restrict the list to this company (0 = no company filter).
    company_id: Optional[int] = None
    # The itemsPerPage property
    items_per_page: Optional[int] = None
    # Receivers, used when the PDF is requested as an email instead of a download.
    mail: Optional[PdfPutRequestBody_mail] = None
    # The page property
    page: Optional[int] = None
    # The searchText property
    search_text: Optional[str] = None
    # The sortField property
    sort_field: Optional[PdfPutRequestBody_sortField] = None
    # The sortOrder property
    sort_order: Optional[PdfPutRequestBody_sortOrder] = None
    
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
        from .pdf_put_request_body_active import PdfPutRequestBody_active
        from .pdf_put_request_body_branches import PdfPutRequestBody_branches
        from .pdf_put_request_body_mail import PdfPutRequestBody_mail
        from .pdf_put_request_body_sort_field import PdfPutRequestBody_sortField
        from .pdf_put_request_body_sort_order import PdfPutRequestBody_sortOrder

        from .pdf_put_request_body_active import PdfPutRequestBody_active
        from .pdf_put_request_body_branches import PdfPutRequestBody_branches
        from .pdf_put_request_body_mail import PdfPutRequestBody_mail
        from .pdf_put_request_body_sort_field import PdfPutRequestBody_sortField
        from .pdf_put_request_body_sort_order import PdfPutRequestBody_sortOrder

        fields: dict[str, Callable[[Any], None]] = {
            "active": lambda n : setattr(self, 'active', n.get_enum_value(PdfPutRequestBody_active)),
            "branches": lambda n : setattr(self, 'branches', n.get_enum_value(PdfPutRequestBody_branches)),
            "columns": lambda n : setattr(self, 'columns', n.get_collection_of_primitive_values(str)),
            "companyId": lambda n : setattr(self, 'company_id', n.get_int_value()),
            "itemsPerPage": lambda n : setattr(self, 'items_per_page', n.get_int_value()),
            "mail": lambda n : setattr(self, 'mail', n.get_object_value(PdfPutRequestBody_mail)),
            "page": lambda n : setattr(self, 'page', n.get_int_value()),
            "searchText": lambda n : setattr(self, 'search_text', n.get_str_value()),
            "sortField": lambda n : setattr(self, 'sort_field', n.get_enum_value(PdfPutRequestBody_sortField)),
            "sortOrder": lambda n : setattr(self, 'sort_order', n.get_enum_value(PdfPutRequestBody_sortOrder)),
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
        writer.write_enum_value("active", self.active)
        writer.write_enum_value("branches", self.branches)
        writer.write_collection_of_primitive_values("columns", self.columns)
        writer.write_int_value("companyId", self.company_id)
        writer.write_int_value("itemsPerPage", self.items_per_page)
        writer.write_object_value("mail", self.mail)
        writer.write_int_value("page", self.page)
        writer.write_str_value("searchText", self.search_text)
        writer.write_enum_value("sortField", self.sort_field)
        writer.write_enum_value("sortOrder", self.sort_order)
        writer.write_additional_data_value(self.additional_data)
    

