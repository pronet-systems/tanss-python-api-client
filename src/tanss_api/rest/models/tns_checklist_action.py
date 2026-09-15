from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class TnsChecklistAction(AdditionalDataHolder, Parsable):
    """
    describes the "state" of a checklist item, i.e. if it's checked
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # date, when the action took place
    date: Optional[int] = None
    # if a support was created, while this item was check, the id is given here (which contains the sevice text for this item)
    support_id: Optional[int] = None
    # id of the user who checked this field
    user_id: Optional[int] = None
    # 1 = checked / 0 = not checked
    value: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsChecklistAction:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsChecklistAction
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsChecklistAction()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "date": lambda n : setattr(self, 'date', n.get_int_value()),
            "supportId": lambda n : setattr(self, 'support_id', n.get_int_value()),
            "userId": lambda n : setattr(self, 'user_id', n.get_int_value()),
            "value": lambda n : setattr(self, 'value', n.get_int_value()),
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
        writer.write_int_value("date", self.date)
        writer.write_int_value("supportId", self.support_id)
        writer.write_int_value("userId", self.user_id)
        writer.write_int_value("value", self.value)
        writer.write_additional_data_value(self.additional_data)
    

