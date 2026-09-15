from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .escalations_put_request_body_active import EscalationsPutRequestBody_active
    from .escalations_put_request_body_sort_field import EscalationsPutRequestBody_sortField
    from .escalations_put_request_body_sort_order import EscalationsPutRequestBody_sortOrder

@dataclass
class EscalationsPutRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Filter for active, inactive, or all rules
    active: Optional[EscalationsPutRequestBody_active] = None
    # Restrict results to a specific escalation category
    category_id: Optional[int] = None
    # Restrict results to a specific escalation rule identifier
    id: Optional[int] = None
    # Whether related entities should be loaded with the results
    load_attached_entities: Optional[bool] = None
    # Free-text search term used to filter escalation rules
    search_text: Optional[str] = None
    # Field the result list is sorted by
    sort_field: Optional[EscalationsPutRequestBody_sortField] = None
    # Sort direction of the result list
    sort_order: Optional[EscalationsPutRequestBody_sortOrder] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EscalationsPutRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EscalationsPutRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return EscalationsPutRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .escalations_put_request_body_active import EscalationsPutRequestBody_active
        from .escalations_put_request_body_sort_field import EscalationsPutRequestBody_sortField
        from .escalations_put_request_body_sort_order import EscalationsPutRequestBody_sortOrder

        from .escalations_put_request_body_active import EscalationsPutRequestBody_active
        from .escalations_put_request_body_sort_field import EscalationsPutRequestBody_sortField
        from .escalations_put_request_body_sort_order import EscalationsPutRequestBody_sortOrder

        fields: dict[str, Callable[[Any], None]] = {
            "active": lambda n : setattr(self, 'active', n.get_enum_value(EscalationsPutRequestBody_active)),
            "categoryId": lambda n : setattr(self, 'category_id', n.get_int_value()),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "loadAttachedEntities": lambda n : setattr(self, 'load_attached_entities', n.get_bool_value()),
            "searchText": lambda n : setattr(self, 'search_text', n.get_str_value()),
            "sortField": lambda n : setattr(self, 'sort_field', n.get_enum_value(EscalationsPutRequestBody_sortField)),
            "sortOrder": lambda n : setattr(self, 'sort_order', n.get_enum_value(EscalationsPutRequestBody_sortOrder)),
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
        writer.write_int_value("categoryId", self.category_id)
        writer.write_int_value("id", self.id)
        writer.write_bool_value("loadAttachedEntities", self.load_attached_entities)
        writer.write_str_value("searchText", self.search_text)
        writer.write_enum_value("sortField", self.sort_field)
        writer.write_enum_value("sortOrder", self.sort_order)
        writer.write_additional_data_value(self.additional_data)
    

