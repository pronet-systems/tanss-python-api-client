from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .properties_post_response_content_fields import PropertiesPostResponse_content_fields
    from .properties_post_response_content_permissions import PropertiesPostResponse_content_permissions

@dataclass
class PropertiesPostResponse_content(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The editable property
    editable: Optional[bool] = None
    # The fields property
    fields: Optional[PropertiesPostResponse_content_fields] = None
    # The permissions property
    permissions: Optional[PropertiesPostResponse_content_permissions] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PropertiesPostResponse_content:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PropertiesPostResponse_content
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PropertiesPostResponse_content()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .properties_post_response_content_fields import PropertiesPostResponse_content_fields
        from .properties_post_response_content_permissions import PropertiesPostResponse_content_permissions

        from .properties_post_response_content_fields import PropertiesPostResponse_content_fields
        from .properties_post_response_content_permissions import PropertiesPostResponse_content_permissions

        fields: dict[str, Callable[[Any], None]] = {
            "editable": lambda n : setattr(self, 'editable', n.get_bool_value()),
            "fields": lambda n : setattr(self, 'fields', n.get_object_value(PropertiesPostResponse_content_fields)),
            "permissions": lambda n : setattr(self, 'permissions', n.get_object_value(PropertiesPostResponse_content_permissions)),
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
        writer.write_bool_value("editable", self.editable)
        writer.write_object_value("fields", self.fields)
        writer.write_object_value("permissions", self.permissions)
        writer.write_additional_data_value(self.additional_data)
    

