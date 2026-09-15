from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tns_pdf_mail_receivers import TnsPdfMailReceivers
    from .tns_personal_computer_configuration import TnsPersonalComputerConfiguration
    from .tns_personal_computer_pdf_configuration_sort_field import TnsPersonalComputerPdfConfiguration_sortField
    from .tns_personal_computer_pdf_configuration_sort_order import TnsPersonalComputerPdfConfiguration_sortOrder

from .tns_personal_computer_configuration import TnsPersonalComputerConfiguration

@dataclass
class TnsPersonalComputerPdfConfiguration(TnsPersonalComputerConfiguration, Parsable):
    """
    Listenkonfiguration für die PDF-Erzeugung der PC/Server-Liste
    """
    # anzuzeigende Spalten (Enum-Werte nicht ermittelt)
    columns: Optional[list[str]] = None
    # The itemsPerPage property
    items_per_page: Optional[int] = None
    # The loadVhosts property
    load_vhosts: Optional[bool] = None
    # Empfänger für den Mailversand eines erzeugten PDFs
    mail: Optional[TnsPdfMailReceivers] = None
    # The omitTotalCount property
    omit_total_count: Optional[bool] = None
    # The page property
    page: Optional[int] = None
    # The searchText property
    search_text: Optional[str] = None
    # The sortField property
    sort_field: Optional[TnsPersonalComputerPdfConfiguration_sortField] = None
    # The sortOrder property
    sort_order: Optional[TnsPersonalComputerPdfConfiguration_sortOrder] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsPersonalComputerPdfConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsPersonalComputerPdfConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsPersonalComputerPdfConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .tns_pdf_mail_receivers import TnsPdfMailReceivers
        from .tns_personal_computer_configuration import TnsPersonalComputerConfiguration
        from .tns_personal_computer_pdf_configuration_sort_field import TnsPersonalComputerPdfConfiguration_sortField
        from .tns_personal_computer_pdf_configuration_sort_order import TnsPersonalComputerPdfConfiguration_sortOrder

        from .tns_pdf_mail_receivers import TnsPdfMailReceivers
        from .tns_personal_computer_configuration import TnsPersonalComputerConfiguration
        from .tns_personal_computer_pdf_configuration_sort_field import TnsPersonalComputerPdfConfiguration_sortField
        from .tns_personal_computer_pdf_configuration_sort_order import TnsPersonalComputerPdfConfiguration_sortOrder

        fields: dict[str, Callable[[Any], None]] = {
            "columns": lambda n : setattr(self, 'columns', n.get_collection_of_primitive_values(str)),
            "itemsPerPage": lambda n : setattr(self, 'items_per_page', n.get_int_value()),
            "loadVhosts": lambda n : setattr(self, 'load_vhosts', n.get_bool_value()),
            "mail": lambda n : setattr(self, 'mail', n.get_object_value(TnsPdfMailReceivers)),
            "omitTotalCount": lambda n : setattr(self, 'omit_total_count', n.get_bool_value()),
            "page": lambda n : setattr(self, 'page', n.get_int_value()),
            "searchText": lambda n : setattr(self, 'search_text', n.get_str_value()),
            "sortField": lambda n : setattr(self, 'sort_field', n.get_enum_value(TnsPersonalComputerPdfConfiguration_sortField)),
            "sortOrder": lambda n : setattr(self, 'sort_order', n.get_enum_value(TnsPersonalComputerPdfConfiguration_sortOrder)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_collection_of_primitive_values("columns", self.columns)
        writer.write_int_value("itemsPerPage", self.items_per_page)
        writer.write_bool_value("loadVhosts", self.load_vhosts)
        writer.write_object_value("mail", self.mail)
        writer.write_bool_value("omitTotalCount", self.omit_total_count)
        writer.write_int_value("page", self.page)
        writer.write_str_value("searchText", self.search_text)
        writer.write_enum_value("sortField", self.sort_field)
        writer.write_enum_value("sortOrder", self.sort_order)
    

