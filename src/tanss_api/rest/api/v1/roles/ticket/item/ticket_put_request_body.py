from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .ticket_put_request_body_kind_of_inheritance import TicketPutRequestBody_kindOfInheritance

@dataclass
class TicketPutRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Identifier of the department scope for role selection.
    department_id: Optional[int] = None
    # Identifier of the employee whose roles are being picked.
    employee_id: Optional[int] = None
    # How the role assignment is inherited or overridden.
    kind_of_inheritance: Optional[TicketPutRequestBody_kindOfInheritance] = None
    # Identifier of the role being selected.
    role_id: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TicketPutRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TicketPutRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TicketPutRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .ticket_put_request_body_kind_of_inheritance import TicketPutRequestBody_kindOfInheritance

        from .ticket_put_request_body_kind_of_inheritance import TicketPutRequestBody_kindOfInheritance

        fields: dict[str, Callable[[Any], None]] = {
            "departmentId": lambda n : setattr(self, 'department_id', n.get_int_value()),
            "employeeId": lambda n : setattr(self, 'employee_id', n.get_int_value()),
            "kindOfInheritance": lambda n : setattr(self, 'kind_of_inheritance', n.get_enum_value(TicketPutRequestBody_kindOfInheritance)),
            "roleId": lambda n : setattr(self, 'role_id', n.get_int_value()),
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
        writer.write_int_value("departmentId", self.department_id)
        writer.write_int_value("employeeId", self.employee_id)
        writer.write_enum_value("kindOfInheritance", self.kind_of_inheritance)
        writer.write_int_value("roleId", self.role_id)
        writer.write_additional_data_value(self.additional_data)
    

