from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tns_object_template_assignments import TnsObjectTemplate_assignments
    from .tns_object_template_linked_entities import TnsObjectTemplate_linkedEntities
    from .tns_object_template_type import TnsObjectTemplateType

@dataclass
class TnsObjectTemplate(AdditionalDataHolder, Parsable):
    """
    Exportierte Objektvorlage (ITnsObjectTemplate); Inhalt ist typabhängig, weitere Felder möglich.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The active property
    active: Optional[bool] = None
    # TnsObjectTemplateAssignmentInfos (Struktur nicht verifiziert).
    assignments: Optional[TnsObjectTemplate_assignments] = None
    # The description property
    description: Optional[str] = None
    # The fields property
    fields: Optional[list[str]] = None
    # The id property
    id: Optional[int] = None
    # The linkedEntities property
    linked_entities: Optional[TnsObjectTemplate_linkedEntities] = None
    # The name property
    name: Optional[str] = None
    # The tucId property
    tuc_id: Optional[str] = None
    # Typ einer Objektvorlage.
    type: Optional[TnsObjectTemplateType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsObjectTemplate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsObjectTemplate
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsObjectTemplate()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .tns_object_template_assignments import TnsObjectTemplate_assignments
        from .tns_object_template_linked_entities import TnsObjectTemplate_linkedEntities
        from .tns_object_template_type import TnsObjectTemplateType

        from .tns_object_template_assignments import TnsObjectTemplate_assignments
        from .tns_object_template_linked_entities import TnsObjectTemplate_linkedEntities
        from .tns_object_template_type import TnsObjectTemplateType

        fields: dict[str, Callable[[Any], None]] = {
            "active": lambda n : setattr(self, 'active', n.get_bool_value()),
            "assignments": lambda n : setattr(self, 'assignments', n.get_object_value(TnsObjectTemplate_assignments)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "fields": lambda n : setattr(self, 'fields', n.get_collection_of_primitive_values(str)),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "linkedEntities": lambda n : setattr(self, 'linked_entities', n.get_object_value(TnsObjectTemplate_linkedEntities)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "tucId": lambda n : setattr(self, 'tuc_id', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(TnsObjectTemplateType)),
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
        writer.write_bool_value("active", self.active)
        writer.write_object_value("assignments", self.assignments)
        writer.write_str_value("description", self.description)
        writer.write_collection_of_primitive_values("fields", self.fields)
        writer.write_int_value("id", self.id)
        writer.write_object_value("linkedEntities", self.linked_entities)
        writer.write_str_value("name", self.name)
        writer.write_str_value("tucId", self.tuc_id)
        writer.write_enum_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    

