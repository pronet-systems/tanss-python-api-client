from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .department import Department

from .department import Department

@dataclass
class TnsEmployeeDepartment(Department, Parsable):
    """
    Abteilung (TnsEmployeeDepartment) mit Zusatzfeldern; Basis ist das offizielle Department-Schema.
    """
    # IDs der zugeordneten Mitarbeiter (in den Systemhaus-One-Routen nicht befüllt).
    employee_ids: Optional[list[int]] = None
    # Zugeordnetes Projekt (Mention/SAP).
    mention_project: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsEmployeeDepartment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsEmployeeDepartment
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsEmployeeDepartment()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .department import Department

        from .department import Department

        fields: dict[str, Callable[[Any], None]] = {
            "employeeIds": lambda n : setattr(self, 'employee_ids', n.get_collection_of_primitive_values(int)),
            "mentionProject": lambda n : setattr(self, 'mention_project', n.get_str_value()),
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
        writer.write_collection_of_primitive_values("employeeIds", self.employee_ids)
        writer.write_str_value("mentionProject", self.mention_project)
    

