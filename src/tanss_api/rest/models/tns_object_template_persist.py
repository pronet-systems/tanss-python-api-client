from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tns_object_template_persist_content import TnsObjectTemplatePersist_content
    from .tns_object_template_type import TnsObjectTemplateType

@dataclass
class TnsObjectTemplatePersist(AdditionalDataHolder, Parsable):
    """
    Persistierte Objektvorlage (TnsObjectTemplatePersist).
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The active property
    active: Optional[bool] = None
    # Template-Inhalt (JsonElement).
    content: Optional[TnsObjectTemplatePersist_content] = None
    # The createdByEmployeeId property
    created_by_employee_id: Optional[int] = None
    # The creationDate property
    creation_date: Optional[int] = None
    # The description property
    description: Optional[str] = None
    # The fields property
    fields: Optional[str] = None
    # The id property
    id: Optional[int] = None
    # The isFavorite property
    is_favorite: Optional[bool] = None
    # The name property
    name: Optional[str] = None
    # Serialisiertes Template.
    template: Optional[str] = None
    # Typ einer Objektvorlage.
    type: Optional[TnsObjectTemplateType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsObjectTemplatePersist:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsObjectTemplatePersist
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsObjectTemplatePersist()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .tns_object_template_persist_content import TnsObjectTemplatePersist_content
        from .tns_object_template_type import TnsObjectTemplateType

        from .tns_object_template_persist_content import TnsObjectTemplatePersist_content
        from .tns_object_template_type import TnsObjectTemplateType

        fields: dict[str, Callable[[Any], None]] = {
            "active": lambda n : setattr(self, 'active', n.get_bool_value()),
            "content": lambda n : setattr(self, 'content', n.get_object_value(TnsObjectTemplatePersist_content)),
            "createdByEmployeeId": lambda n : setattr(self, 'created_by_employee_id', n.get_int_value()),
            "creationDate": lambda n : setattr(self, 'creation_date', n.get_int_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "fields": lambda n : setattr(self, 'fields', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "isFavorite": lambda n : setattr(self, 'is_favorite', n.get_bool_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "template": lambda n : setattr(self, 'template', n.get_str_value()),
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
        writer.write_object_value("content", self.content)
        writer.write_int_value("createdByEmployeeId", self.created_by_employee_id)
        writer.write_int_value("creationDate", self.creation_date)
        writer.write_str_value("description", self.description)
        writer.write_str_value("fields", self.fields)
        writer.write_int_value("id", self.id)
        writer.write_bool_value("isFavorite", self.is_favorite)
        writer.write_str_value("name", self.name)
        writer.write_str_value("template", self.template)
        writer.write_enum_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    

