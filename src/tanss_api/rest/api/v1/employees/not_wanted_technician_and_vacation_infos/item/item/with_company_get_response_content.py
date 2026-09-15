from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class WithCompanyGetResponse_content(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The notWantedTechnician property
    not_wanted_technician: Optional[bool] = None
    # The onVacation property
    on_vacation: Optional[bool] = None
    # unix timestamp when the vacation ends (0 if not on vacation)
    vacation_until: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WithCompanyGetResponse_content:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WithCompanyGetResponse_content
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WithCompanyGetResponse_content()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "notWantedTechnician": lambda n : setattr(self, 'not_wanted_technician', n.get_bool_value()),
            "onVacation": lambda n : setattr(self, 'on_vacation', n.get_bool_value()),
            "vacationUntil": lambda n : setattr(self, 'vacation_until', n.get_int_value()),
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
        writer.write_bool_value("notWantedTechnician", self.not_wanted_technician)
        writer.write_bool_value("onVacation", self.on_vacation)
        writer.write_int_value("vacationUntil", self.vacation_until)
        writer.write_additional_data_value(self.additional_data)
    

