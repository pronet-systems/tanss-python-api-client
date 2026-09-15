from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .support_rules_put_request_body_active import SupportRulesPutRequestBody_active
    from .support_rules_put_request_body_sort_field import SupportRulesPutRequestBody_sortField
    from .support_rules_put_request_body_sort_order import SupportRulesPutRequestBody_sortOrder

@dataclass
class SupportRulesPutRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Whether to include active, inactive or both kinds of rules
    active: Optional[SupportRulesPutRequestBody_active] = None
    # Number of items returned per page
    items_per_page: Optional[int] = None
    # Skip calculating the total result count for faster paging
    omit_total_count: Optional[bool] = None
    # One-based page number to retrieve
    page: Optional[int] = None
    # Free-text search term used to filter support rules
    search_text: Optional[str] = None
    # Field the result list is sorted by
    sort_field: Optional[SupportRulesPutRequestBody_sortField] = None
    # Sort direction for the result list
    sort_order: Optional[SupportRulesPutRequestBody_sortOrder] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SupportRulesPutRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SupportRulesPutRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SupportRulesPutRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .support_rules_put_request_body_active import SupportRulesPutRequestBody_active
        from .support_rules_put_request_body_sort_field import SupportRulesPutRequestBody_sortField
        from .support_rules_put_request_body_sort_order import SupportRulesPutRequestBody_sortOrder

        from .support_rules_put_request_body_active import SupportRulesPutRequestBody_active
        from .support_rules_put_request_body_sort_field import SupportRulesPutRequestBody_sortField
        from .support_rules_put_request_body_sort_order import SupportRulesPutRequestBody_sortOrder

        fields: dict[str, Callable[[Any], None]] = {
            "active": lambda n : setattr(self, 'active', n.get_enum_value(SupportRulesPutRequestBody_active)),
            "itemsPerPage": lambda n : setattr(self, 'items_per_page', n.get_int_value()),
            "omitTotalCount": lambda n : setattr(self, 'omit_total_count', n.get_bool_value()),
            "page": lambda n : setattr(self, 'page', n.get_int_value()),
            "searchText": lambda n : setattr(self, 'search_text', n.get_str_value()),
            "sortField": lambda n : setattr(self, 'sort_field', n.get_enum_value(SupportRulesPutRequestBody_sortField)),
            "sortOrder": lambda n : setattr(self, 'sort_order', n.get_enum_value(SupportRulesPutRequestBody_sortOrder)),
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
        writer.write_enum_value("sortField", self.sort_field)
        writer.write_enum_value("sortOrder", self.sort_order)
        writer.write_additional_data_value(self.additional_data)
    

