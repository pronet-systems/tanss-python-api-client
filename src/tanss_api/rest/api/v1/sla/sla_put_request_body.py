from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .sla_put_request_body_active import SlaPutRequestBody_active

@dataclass
class SlaPutRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Filter for active, inactive, or both kinds of SLAs
    active: Optional[SlaPutRequestBody_active] = None
    # Maximum number of items returned per page
    items_per_page: Optional[int] = None
    # Whether to skip calculating the total result count for performance
    omit_total_count: Optional[bool] = None
    # Page number of the paginated result, starting at 1
    page: Optional[int] = None
    # Free-text search term matched against SLA name and description
    search_text: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SlaPutRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SlaPutRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SlaPutRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .sla_put_request_body_active import SlaPutRequestBody_active

        from .sla_put_request_body_active import SlaPutRequestBody_active

        fields: dict[str, Callable[[Any], None]] = {
            "active": lambda n : setattr(self, 'active', n.get_enum_value(SlaPutRequestBody_active)),
            "itemsPerPage": lambda n : setattr(self, 'items_per_page', n.get_int_value()),
            "omitTotalCount": lambda n : setattr(self, 'omit_total_count', n.get_bool_value()),
            "page": lambda n : setattr(self, 'page', n.get_int_value()),
            "searchText": lambda n : setattr(self, 'search_text', n.get_str_value()),
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
        writer.write_int_value("itemsPerPage", self.items_per_page)
        writer.write_bool_value("omitTotalCount", self.omit_total_count)
        writer.write_int_value("page", self.page)
        writer.write_str_value("searchText", self.search_text)
        writer.write_additional_data_value(self.additional_data)
    

