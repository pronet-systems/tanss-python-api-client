from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tns_comment import TnsComment
    from .tns_ticket_comment_media import TnsTicketComment_media
    from .tns_ticket_comment_path import TnsTicketComment_path

from .tns_comment import TnsComment

@dataclass
class TnsTicketComment(TnsComment, Parsable):
    """
    Ticket-Kommentar (TnsPosting) mit den zusätzlichen Feldern der tanss.x-Route.
    """
    # The categoryId property
    category_id: Optional[int] = None
    # The completedDate property
    completed_date: Optional[int] = None
    # The media property
    media: Optional[list[TnsTicketComment_media]] = None
    # The path property
    path: Optional[list[TnsTicketComment_path]] = None
    # The pinned property
    pinned: Optional[bool] = None
    # The productId property
    product_id: Optional[int] = None
    # Unterdrückt die Benachrichtigung.
    silent: Optional[bool] = None
    # The toEmployeeId property
    to_employee_id: Optional[int] = None
    # Posting-Typ, serverseitig TICKET_COMMENT.
    type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsTicketComment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsTicketComment
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsTicketComment()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .tns_comment import TnsComment
        from .tns_ticket_comment_media import TnsTicketComment_media
        from .tns_ticket_comment_path import TnsTicketComment_path

        from .tns_comment import TnsComment
        from .tns_ticket_comment_media import TnsTicketComment_media
        from .tns_ticket_comment_path import TnsTicketComment_path

        fields: dict[str, Callable[[Any], None]] = {
            "categoryId": lambda n : setattr(self, 'category_id', n.get_int_value()),
            "completedDate": lambda n : setattr(self, 'completed_date', n.get_int_value()),
            "media": lambda n : setattr(self, 'media', n.get_collection_of_object_values(TnsTicketComment_media)),
            "path": lambda n : setattr(self, 'path', n.get_collection_of_object_values(TnsTicketComment_path)),
            "pinned": lambda n : setattr(self, 'pinned', n.get_bool_value()),
            "productId": lambda n : setattr(self, 'product_id', n.get_int_value()),
            "silent": lambda n : setattr(self, 'silent', n.get_bool_value()),
            "toEmployeeId": lambda n : setattr(self, 'to_employee_id', n.get_int_value()),
            "type": lambda n : setattr(self, 'type', n.get_str_value()),
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
        writer.write_int_value("categoryId", self.category_id)
        writer.write_int_value("completedDate", self.completed_date)
        writer.write_collection_of_object_values("media", self.media)
        writer.write_collection_of_object_values("path", self.path)
        writer.write_bool_value("pinned", self.pinned)
        writer.write_int_value("productId", self.product_id)
        writer.write_bool_value("silent", self.silent)
        writer.write_int_value("toEmployeeId", self.to_employee_id)
        writer.write_str_value("type", self.type)
    

