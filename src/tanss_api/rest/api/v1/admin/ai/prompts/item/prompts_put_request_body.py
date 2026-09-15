from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .......models.tns_text_module_type import TnsTextModuleType

@dataclass
class PromptsPutRequestBody(AdditionalDataHolder, Parsable):
    """
    Zu ändernde Felder des Prompts (JSON-Merge)
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Relative Rang-Verschiebung innerhalb der Kategorie (z.B. -1/+1)
    adjust_rank: Optional[int] = None
    # ID der Prompt-Kategorie (0/null = ohne Kategorie)
    category_id: Optional[int] = None
    # ID der LLM-Konfiguration
    config_id: Optional[int] = None
    # Zugeordnete Abteilungs-IDs
    employee_departments: Optional[list[int]] = None
    # Zugeordnete Mitarbeiter-IDs
    employees: Optional[list[int]] = None
    # Prompt-Text; darf den Platzhalter {text} enthalten
    instruction: Optional[str] = None
    # The name property
    name: Optional[str] = None
    # Zugeordnete Textbaustein-Typen
    text_module_types: Optional[list[TnsTextModuleType]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PromptsPutRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PromptsPutRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PromptsPutRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .......models.tns_text_module_type import TnsTextModuleType

        from .......models.tns_text_module_type import TnsTextModuleType

        fields: dict[str, Callable[[Any], None]] = {
            "adjustRank": lambda n : setattr(self, 'adjust_rank', n.get_int_value()),
            "categoryId": lambda n : setattr(self, 'category_id', n.get_int_value()),
            "configId": lambda n : setattr(self, 'config_id', n.get_int_value()),
            "employeeDepartments": lambda n : setattr(self, 'employee_departments', n.get_collection_of_primitive_values(int)),
            "employees": lambda n : setattr(self, 'employees', n.get_collection_of_primitive_values(int)),
            "instruction": lambda n : setattr(self, 'instruction', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "textModuleTypes": lambda n : setattr(self, 'text_module_types', n.get_collection_of_enum_values(TnsTextModuleType)),
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
        writer.write_int_value("adjustRank", self.adjust_rank)
        writer.write_int_value("categoryId", self.category_id)
        writer.write_int_value("configId", self.config_id)
        writer.write_collection_of_primitive_values("employeeDepartments", self.employee_departments)
        writer.write_collection_of_primitive_values("employees", self.employees)
        writer.write_str_value("instruction", self.instruction)
        writer.write_str_value("name", self.name)
        writer.write_collection_of_enum_values("textModuleTypes", self.text_module_types)
        writer.write_additional_data_value(self.additional_data)
    

