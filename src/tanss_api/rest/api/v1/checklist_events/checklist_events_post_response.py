from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ....models.checklist_event import ChecklistEvent
    from ....models.tns_meta_message import TnsMetaMessage

@dataclass
class ChecklistEventsPostResponse(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # An automated action attached to a checklist item, a multi-select option or — inside the ITportal wizard — to a card, widget or option.
    content: Optional[ChecklistEvent] = None
    # The meta property
    meta: Optional[TnsMetaMessage] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ChecklistEventsPostResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ChecklistEventsPostResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ChecklistEventsPostResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ....models.checklist_event import ChecklistEvent
        from ....models.tns_meta_message import TnsMetaMessage

        from ....models.checklist_event import ChecklistEvent
        from ....models.tns_meta_message import TnsMetaMessage

        fields: dict[str, Callable[[Any], None]] = {
            "content": lambda n : setattr(self, 'content', n.get_object_value(ChecklistEvent)),
            "meta": lambda n : setattr(self, 'meta', n.get_object_value(TnsMetaMessage)),
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
        writer.write_object_value("content", self.content)
        writer.write_object_value("meta", self.meta)
        writer.write_additional_data_value(self.additional_data)
    

