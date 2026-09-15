from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tns_pop_up_notification import TnsPopUpNotification

@dataclass
class TnsTodoItem(AdditionalDataHolder, Parsable):
    """
    Eintrag einer ToDo-Liste.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The createdAt property
    created_at: Optional[int] = None
    # The doneAt property
    done_at: Optional[int] = None
    # The id property
    id: Optional[int] = None
    # The notification property
    notification: Optional[TnsPopUpNotification] = None
    # The position property
    position: Optional[int] = None
    # The rememberTime property
    remember_time: Optional[int] = None
    # The text property
    text: Optional[str] = None
    # The todoListId property
    todo_list_id: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsTodoItem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsTodoItem
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsTodoItem()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .tns_pop_up_notification import TnsPopUpNotification

        from .tns_pop_up_notification import TnsPopUpNotification

        fields: dict[str, Callable[[Any], None]] = {
            "createdAt": lambda n : setattr(self, 'created_at', n.get_int_value()),
            "doneAt": lambda n : setattr(self, 'done_at', n.get_int_value()),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "notification": lambda n : setattr(self, 'notification', n.get_object_value(TnsPopUpNotification)),
            "position": lambda n : setattr(self, 'position', n.get_int_value()),
            "rememberTime": lambda n : setattr(self, 'remember_time', n.get_int_value()),
            "text": lambda n : setattr(self, 'text', n.get_str_value()),
            "todoListId": lambda n : setattr(self, 'todo_list_id', n.get_int_value()),
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
        writer.write_int_value("createdAt", self.created_at)
        writer.write_int_value("doneAt", self.done_at)
        writer.write_int_value("id", self.id)
        writer.write_object_value("notification", self.notification)
        writer.write_int_value("position", self.position)
        writer.write_int_value("rememberTime", self.remember_time)
        writer.write_str_value("text", self.text)
        writer.write_int_value("todoListId", self.todo_list_id)
        writer.write_additional_data_value(self.additional_data)
    

