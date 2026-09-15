from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .ticket_delete_request_body_kind_of_inheritance import TicketDeleteRequestBody_kindOfInheritance

@dataclass
class TicketDeleteRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Id of the department the assignment applies to (optional; used for department-level roles).
    department_id: Optional[int] = None
    # Id of the employee whose role assignment is removed.
    employee_id: Optional[int] = None
    # How the assignment relates to inheritance across projects and sub-tickets.
    kind_of_inheritance: Optional[TicketDeleteRequestBody_kindOfInheritance] = None
    # Id of the role to revoke.
    role_id: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TicketDeleteRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TicketDeleteRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TicketDeleteRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .ticket_delete_request_body_kind_of_inheritance import TicketDeleteRequestBody_kindOfInheritance

        from .ticket_delete_request_body_kind_of_inheritance import TicketDeleteRequestBody_kindOfInheritance

        fields: dict[str, Callable[[Any], None]] = {
            "departmentId": lambda n : setattr(self, 'department_id', n.get_int_value()),
            "employeeId": lambda n : setattr(self, 'employee_id', n.get_int_value()),
            "kindOfInheritance": lambda n : setattr(self, 'kind_of_inheritance', n.get_enum_value(TicketDeleteRequestBody_kindOfInheritance)),
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
    

