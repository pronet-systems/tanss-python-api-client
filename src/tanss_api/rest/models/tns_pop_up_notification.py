from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class TnsPopUpNotification(AdditionalDataHolder, Parsable):
    """
    PopUp-Benachrichtigung (Felder aus den Beispielen der Basis-Spec zu /api/v1/popUpNotifications abgeleitet).
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The confirmedDate property
    confirmed_date: Optional[int] = None
    # The employeeId property
    employee_id: Optional[int] = None
    # The linkId property
    link_id: Optional[int] = None
    # The linkTypeId property
    link_type_id: Optional[int] = None
    # The notifyAfter property
    notify_after: Optional[int] = None
    # The title property
    title: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsPopUpNotification:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsPopUpNotification
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsPopUpNotification()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "confirmedDate": lambda n : setattr(self, 'confirmed_date', n.get_int_value()),
            "employeeId": lambda n : setattr(self, 'employee_id', n.get_int_value()),
            "linkId": lambda n : setattr(self, 'link_id', n.get_int_value()),
            "linkTypeId": lambda n : setattr(self, 'link_type_id', n.get_int_value()),
            "notifyAfter": lambda n : setattr(self, 'notify_after', n.get_int_value()),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
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
        writer.write_int_value("confirmedDate", self.confirmed_date)
        writer.write_int_value("employeeId", self.employee_id)
        writer.write_int_value("linkId", self.link_id)
        writer.write_int_value("linkTypeId", self.link_type_id)
        writer.write_int_value("notifyAfter", self.notify_after)
        writer.write_str_value("title", self.title)
        writer.write_additional_data_value(self.additional_data)
    

