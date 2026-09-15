from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tns_posting import TnsPosting

from .tns_posting import TnsPosting

@dataclass
class TnsComment(TnsPosting, Parsable):
    """
    Defines a ticket comment
    """
    # the id of the ticket is given here
    comment_of_id: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsComment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsComment
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsComment()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .tns_posting import TnsPosting

        from .tns_posting import TnsPosting

        fields: dict[str, Callable[[Any], None]] = {
            "commentOfId": lambda n : setattr(self, 'comment_of_id', n.get_int_value()),
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
        writer.write_int_value("commentOfId", self.comment_of_id)
    

