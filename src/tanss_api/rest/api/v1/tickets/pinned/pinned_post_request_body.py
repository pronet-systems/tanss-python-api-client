from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .pinned_post_request_body_type import PinnedPostRequestBody_type

@dataclass
class PinnedPostRequestBody(AdditionalDataHolder, Parsable):
    """
    Request body.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Unique identifier of the pinned entry
    id: Optional[int] = None
    # Identifier of the linked item that is pinned
    link_id: Optional[int] = None
    # Identifier of the ticket the entry is pinned to
    ticket_id: Optional[int] = None
    # Type of the pinned item
    type: Optional[PinnedPostRequestBody_type] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PinnedPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PinnedPostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PinnedPostRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .pinned_post_request_body_type import PinnedPostRequestBody_type

        from .pinned_post_request_body_type import PinnedPostRequestBody_type

        fields: dict[str, Callable[[Any], None]] = {
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "linkId": lambda n : setattr(self, 'link_id', n.get_int_value()),
            "ticketId": lambda n : setattr(self, 'ticket_id', n.get_int_value()),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(PinnedPostRequestBody_type)),
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
        writer.write_int_value("linkId", self.link_id)
        writer.write_int_value("ticketId", self.ticket_id)
        writer.write_enum_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    

