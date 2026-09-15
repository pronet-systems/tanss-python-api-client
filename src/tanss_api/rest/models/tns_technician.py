from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .employee_short import EmployeeShort

from .employee_short import EmployeeShort

@dataclass
class TnsTechnician(EmployeeShort, Parsable):
    """
    Reduzierter Mitarbeiter (Techniker) mit E-Mail und Namensfeldern.
    """
    # The emailAddress property
    email_address: Optional[str] = None
    # The firstName property
    first_name: Optional[str] = None
    # The lastName property
    last_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsTechnician:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsTechnician
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsTechnician()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .employee_short import EmployeeShort

        from .employee_short import EmployeeShort

        fields: dict[str, Callable[[Any], None]] = {
            "emailAddress": lambda n : setattr(self, 'email_address', n.get_str_value()),
            "firstName": lambda n : setattr(self, 'first_name', n.get_str_value()),
            "lastName": lambda n : setattr(self, 'last_name', n.get_str_value()),
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
        writer.write_str_value("emailAddress", self.email_address)
        writer.write_str_value("firstName", self.first_name)
        writer.write_str_value("lastName", self.last_name)
    

