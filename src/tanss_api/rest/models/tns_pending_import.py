from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tns_object_template_type import TnsObjectTemplateType

@dataclass
class TnsPendingImport(AdditionalDataHolder, Parsable):
    """
    Ausstehender Vorlagen-Import aus einem anderen TANSS-System.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Serialisierte Vorlage.
    content: Optional[str] = None
    # The createdTemplateId property
    created_template_id: Optional[int] = None
    # The creator property
    creator: Optional[str] = None
    # The creatorEmail property
    creator_email: Optional[str] = None
    # Anlagedatum (serverseitig gesetzt).
    date: Optional[int] = None
    # The id property
    id: Optional[int] = None
    # 0 solange nicht importiert.
    import_date: Optional[int] = None
    # The importEmployeeId property
    import_employee_id: Optional[int] = None
    # The name property
    name: Optional[str] = None
    # The tucId property
    tuc_id: Optional[str] = None
    # Typ einer Objektvorlage.
    type: Optional[TnsObjectTemplateType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsPendingImport:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsPendingImport
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsPendingImport()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .tns_object_template_type import TnsObjectTemplateType

        from .tns_object_template_type import TnsObjectTemplateType

        fields: dict[str, Callable[[Any], None]] = {
            "content": lambda n : setattr(self, 'content', n.get_str_value()),
            "createdTemplateId": lambda n : setattr(self, 'created_template_id', n.get_int_value()),
            "creator": lambda n : setattr(self, 'creator', n.get_str_value()),
            "creatorEmail": lambda n : setattr(self, 'creator_email', n.get_str_value()),
            "date": lambda n : setattr(self, 'date', n.get_int_value()),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "importDate": lambda n : setattr(self, 'import_date', n.get_int_value()),
            "importEmployeeId": lambda n : setattr(self, 'import_employee_id', n.get_int_value()),
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
        writer.write_str_value("content", self.content)
        writer.write_int_value("createdTemplateId", self.created_template_id)
        writer.write_str_value("creator", self.creator)
        writer.write_str_value("creatorEmail", self.creator_email)
        writer.write_int_value("date", self.date)
        writer.write_int_value("id", self.id)
        writer.write_int_value("importDate", self.import_date)
        writer.write_int_value("importEmployeeId", self.import_employee_id)
        writer.write_str_value("name", self.name)
        writer.write_str_value("tucId", self.tuc_id)
        writer.write_enum_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    

